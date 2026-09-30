"""Item-level bootstrap CIs for the Track 3 leaderboard (Table 1).

Locked methodology: a single greedy pass per cell (deterministic decoding removes the
across-run variance that the SEA-HELM 8-run protocol targets), so the reported uncertainty
is the *item-sampling* CI — resample the N graded items with replacement B times, recompute
accuracy, take the 2.5/97.5 percentiles. This is the right CI for "how much would the score
move on a different draw of items from the same distribution".

Reads every runs/wave4_<model>_full.json, grades per (model,config) with grade() verbatim from
scripts/grade.py, and emits a model × config accuracy ±95% CI table (+ a per-model overall over
the union of its items). Agent-error responses count as failures (they are real cell outcomes).

Usage: python analysis/bootstrap_ci.py [--boot 2000 --seed 0]
Outputs: analysis/leaderboard-ci.md + leaderboard-ci.json
"""
from __future__ import annotations

import argparse, io, json, random, re, sys
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BENCH = _REPO_ROOT
HERE = Path(__file__).resolve().parent
QJSON = BENCH / "questions" / "questions_v02.json"

CFG_ORDER = ["t1_grep", "t2_search", "t3_both", "t4_repl"]
CFG_DISP = {"t1_grep": "T1 grep", "t2_search": "T2 search", "t3_both": "T3 both", "t4_repl": "T4 repl"}
# The 12 model configurations reported in paper Table 3, in table order.
MODELS = [
    ("gpt54med", "gpt-5.4 (med)", "closed"), ("gpt55med", "gpt-5.5 (med)", "closed"),
    ("gpt55low", "gpt-5.5 (low)", "closed"), ("sonnet", "Claude Sonnet 4.6", "closed"),
    ("gemini30flash", "Gemini-3-Flash", "closed"),
    ("glm51", "GLM-5.1", "open"), ("deepseekv4pro", "DeepSeek-V4-Pro", "open"),
    ("deepseekv4flash", "DeepSeek-V4-Flash", "open"),
    ("gemma4", "Gemma-4-31B", "open"), ("minimax", "MiniMax-M2.7", "open"),
    ("opentyphoon", "Typhoon-2.5 (30B)", "thai"), ("typhoon8b", "Typhoon-S-8B", "thai"),
]
DISP = {k: d for k, d, _ in MODELS}
TIER = {k: t for k, _, t in MODELS}
TIER_ORDER = ["closed", "open", "thai"]
TIER_DISP = {"closed": "Closed source", "open": "Open weight", "thai": "Thai open weight"}


def _contains(resp, tok):
    """Case-insensitive containment. A purely numeric token (count, extension, ID) must appear as a
    standalone number, not inside a longer one ("2" does not match "2021"); thousands separators ignored."""
    if tok.isdigit():
        return re.search(rf"(?<!\d){tok}(?!\d)", resp.replace(",", "")) is not None
    return tok.lower() in resp.lower()


def grade(it, resp):  # verbatim from scripts/grade.py
    ea = it["expected_answer"]; fails = []
    for g in ea.get("must_contain_any_of", []):
        if g and not any(_contains(resp, t) for t in g if t):
            fails.append("miss")
    for t in ea.get("must_not_contain", []):
        if t and t.lower() in resp.lower():
            fails.append("forbidden")
    if ea.get("exact_count") is not None and not _contains(resp, str(ea["exact_count"])):
        fails.append("count")
    if ea.get("min_items"):
        tpi = ea.get("all_items_tokens_per_id", {})
        hits = sum(1 for eid, toks in tpi.items() if any(_contains(resp, t) for t in toks if t))
        if hits < ea["min_items"]:
            fails.append("min_items")
    if ea.get("must_not_contain_phone_extension") and re.search(r"\b\d{5}\b", resp):
        fails.append("ext")
    if ea.get("must_not_contain_employee_id_pattern") and re.search(r"\b(0000\d{4}|08\d{6})\b", resp):
        fails.append("empid")
    return len(fails) == 0


def boot_ci(vec, B, rng):
    """95% percentile CI of the mean of a 0/1 vector via item resampling."""
    n = len(vec)
    if n == 0:
        return (0.0, 0.0, 0.0)
    mean = 100 * sum(vec) / n
    means = []
    for _ in range(B):
        s = sum(vec[rng.randrange(n)] for _ in range(n))
        means.append(100 * s / n)
    means.sort()
    lo = means[int(0.025 * B)]
    hi = means[min(B - 1, int(0.975 * B))]
    return (mean, lo, hi)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    items = {i["id"]: i for i in json.loads(QJSON.read_text(encoding="utf-8"))["questions"]}

    # vec[model][cfg] = ordered list of 0/1 over the items present in that cell
    cell = {}      # (model,cfg) -> {id: ok}
    present = {}
    for key, _, _ in MODELS:
        man_p = BENCH / "runs" / f"wave4_{key}_full.json"
        if not man_p.exists():
            continue
        cfgs = {k: str(_REPO_ROOT / v) for k, v in json.loads(man_p.read_text(encoding="utf-8"))["configs"].items()}
        present[key] = [c for c in CFG_ORDER if c in cfgs]
        for c in present[key]:
            run_dir = Path(cfgs[c])
            d = {}
            # The committed artifact per run is results.jsonl (each record embeds the
            # model's final response verbatim); raw/*.md exists only after a local sweep.
            res_p = run_dir / "results.jsonl"
            if res_p.exists():
                for line in res_p.read_text(encoding="utf-8").splitlines():
                    if not line.strip():
                        continue
                    rec = json.loads(line)
                    if rec["id"] in items:
                        resp = rec.get("response", "")
                        d[rec["id"]] = int((not resp.startswith("[agent error")) and grade(items[rec["id"]], resp))
            else:
                for f in (run_dir / "raw").glob("*.md"):
                    if f.stem in items:
                        resp = f.read_text(encoding="utf-8")
                        d[f.stem] = int((not resp.startswith("[agent error")) and grade(items[f.stem], resp))
            cell[(key, c)] = d
    models = [k for k, _, _ in MODELS if k in present]

    results = {}
    out, P = [], lambda *a: (print(*a), out.append(" ".join(str(x) for x in a)))
    P("# Track 3 — leaderboard with item-level bootstrap 95% CIs\n")
    P(f"B = {args.boot} resamples, seed {args.seed}. Each cell = single greedy pass; CI is the "
      "item-sampling interval (resample items with replacement, recompute accuracy, 2.5/97.5 "
      "percentiles). Agent-errors count as failures.\n")
    P("| tier | model | " + " | ".join(CFG_DISP[c] for c in CFG_ORDER) + " |")
    P("|---|---|" + "|".join(["---"] * len(CFG_ORDER)) + "|")
    for tier in TIER_ORDER:
        for k in models:
            if TIER[k] != tier:
                continue
            results[k] = {}
            cells_disp = []
            for c in CFG_ORDER:
                if (k, c) not in cell:
                    cells_disp.append("—"); continue
                vec = list(cell[(k, c)].values())
                m, lo, hi = boot_ci(vec, args.boot, rng)
                results[k][c] = {"acc": m, "lo": lo, "hi": hi, "n": len(vec)}
                cells_disp.append(f"{m:.1f} [{lo:.1f}–{hi:.1f}]")
            P(f"| {TIER_DISP[tier]} | {DISP[k]} | " + " | ".join(cells_disp) + " |")

    md = HERE / "leaderboard-ci.md"
    md.write_text("\n".join(out) + "\n", encoding="utf-8")
    (HERE / "leaderboard-ci.json").write_text(
        json.dumps({"boot": args.boot, "seed": args.seed, "results": results},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {md.name} + leaderboard-ci.json")


if __name__ == "__main__":
    main()
