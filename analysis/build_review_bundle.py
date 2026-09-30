"""Build the Track-3 human-review bundle: pair every item with its gold, a slice
of the actual KB, and the model answers + grader verdicts — then bake per-rater
self-contained HTML files (clone of the Track-1 Phase-6 annotate.html pattern).

Track 3 grades by airtight *deterministic substring* matching (no LLM judge), so
the thing humans validate is the GRADER, not the outputs. This builds the data a
rater needs to do that in one view:
  • gold rendered human-readably + the raw expected_answer,
  • the KB rows the question is about (target rows from ground_truth_row_ids) plus
    near-miss homonyms (so uniqueness / "not-found" is checkable),
  • each (model, tool-config) answer with its tool-call trace and the grader verdict.

Model⊕grader disagreement is the triage signal. We emit:
  • triage_items.json  — high-signal slice (flagged), verdicts SHOWN (anchored bug-finding),
  • blind_sample.json  — fixed-seed stratified ~60, verdict HIDDEN in the HTML until the
                         rater records their own (anti-anchoring → unbiased grader error rate),
  • review_items.json  — all 625 records,
  • triage-summary.md   — flag counts + an upfront candidate-bug list.

Inputs are the Wave-4 sweep manifests (runs/wave4_*.json: {configs:{label:run_dir}}).
The Typhoon manifest (wave4_full.json) has no "model" key — we read it from each
run dir's manifest.json. Run Typhoon-only now; add the gpt-5.4 manifest when its sweep lands.

Usage:
  python build_review_bundle.py --manifests "<bench>/runs/wave4_full.json"
  python build_review_bundle.py --manifests <typhoon.json> <gpt54.json> --strong gpt54
  python build_review_bundle.py --manifests <...> --raters raterA raterB
  python build_review_bundle.py --manifests <...> --limit 20    # smoke
"""
from __future__ import annotations

import argparse, csv, io, json, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent                       # repo analysis/ directory
ROOT = HERE.parents[0]                                        # repo root
BENCH = ROOT / "the source exam" / _REPO_ROOT
TEMPLATE = HERE / "review.html"
OUT = HERE / "review"

CONFIG_ORDER = ["t1_grep", "t2_search", "t3_both", "t4_repl"]
BLIND_SEED = 20260524
BLIND_N = 40
PER_CATEGORY = 3                                             # extra coverage items per category
HARD_SUBTYPES = {"E1", "E2", "E3", "B3", "B4"}               # multi-hop + disambiguation (C4 = aggregation, not hard)

# triage flag -> weight (higher = more urgent to review)
FLAG_WEIGHT = {"strong_fail": 100, "weak_pass_risk": 80, "all_fail": 60,
               "disagree": 30, "short_token": 25, "refusal": 15, "listing": 10}
# always force-included regardless of per-category quota — the rare, must-not-miss bug class
# (weak_pass_risk count-golds are near-identical; the per-category quota samples enough of them)
PRIORITY_FLAGS = {"strong_fail"}

# bake placeholders — must match review.html exactly
ITEMS_PLACEHOLDER = "const BAKED_ITEMS = null; /* BAKED_ITEMS_PLACEHOLDER */"
NAME_PLACEHOLDER = "const BAKED_NAME  = null; /* BAKED_NAME_PLACEHOLDER */"


# ============================ grader (inlined from scripts/grade.py:37-57) ============================

def _contains(resp, tok):
    """Case-insensitive containment. A purely numeric token (count, extension, ID) must appear as a
    standalone number, not inside a longer one ("2" does not match "2021"); thousands separators ignored."""
    if tok.isdigit():
        return re.search(rf"(?<!\d){tok}(?!\d)", resp.replace(",", "")) is not None
    return tok.lower() in resp.lower()


def grade(it, resp):
    """Reason-rich fails, identical to scripts/grade.py — empty list == PASS."""
    ea = it["expected_answer"]
    fails = []
    for g in ea.get("must_contain_any_of", []):
        if g and not any(_contains(resp, t) for t in g if t):
            fails.append(f"missing any-of {g[:3]}")
    for t in ea.get("must_not_contain", []):
        if t and t.lower() in resp.lower():
            fails.append(f"has forbidden {t!r}")
    if ea.get("exact_count") is not None and not _contains(resp, str(ea["exact_count"])):
        fails.append(f"missing count {ea['exact_count']}")
    if ea.get("min_items"):
        tpi = ea.get("all_items_tokens_per_id", {})
        hits = sum(1 for eid, toks in tpi.items() if any(_contains(resp, t) for t in toks if t))
        if hits < ea["min_items"]:
            fails.append(f"min_items {ea['min_items']} not met ({hits})")
    if ea.get("must_not_contain_phone_extension") and re.search(r"\b\d{5}\b", resp):
        fails.append("has ext pattern")
    if ea.get("must_not_contain_employee_id_pattern") and re.search(r"\b(0000\d{4}|08\d{6})\b", resp):
        fails.append("has emp ID pattern")
    return fails


# ============================ KB ============================

# display fields: (label, CSV column)
KB_VIEW = [("id", "Employee ID"), ("name_en", None), ("name_th", None),
           ("nick_en", "Nickname English"), ("nick_th", "Nickname Thai"),
           ("position_en", "Position in English"), ("dept", "Department"),
           ("section", "Section"), ("unit", "Unit"),
           ("level", "Position Level"), ("ext", "Phone Extension"), ("mobile", "Mobile No.")]


def load_kb(path: Path):
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    index = {r["Employee ID"]: r for r in rows}
    return rows, index


def row_view(r: dict) -> dict:
    out = {}
    for label, col in KB_VIEW:
        if label == "name_en":
            out[label] = f"{r.get('First Name English','')} {r.get('Last Name English','')}".strip()
        elif label == "name_th":
            out[label] = f"{r.get('First Name Thai','')} {r.get('Last Name Thai','')}".strip()
        else:
            out[label] = (r.get(col) or "").strip()
    return out


def name_blob(r: dict) -> str:
    parts = [r.get(c, "") for c in ("First Name English", "Last Name English", "First Name Thai",
                                    "Last Name Thai", "Nickname English", "Nickname Thai")]
    return " ".join(p for p in parts if p).lower()


_TOK = re.compile(r"[A-Za-z฀-๿]{2,}")


def near_miss(question: str, gt_ids: set, rows: list, blobs: list, cap: int = 15) -> list:
    """KB rows (not in gt) whose name/nickname shares a token with the question — the
    homonyms / distractors a rater needs to judge uniqueness and 'not-found'."""
    toks = {t.lower() for t in _TOK.findall(question)}
    if not toks:
        return []
    scored = []
    for r, blob in zip(rows, blobs):
        if r["Employee ID"] in gt_ids:
            continue
        hits = sum(1 for t in toks if t in blob)
        if hits:
            scored.append((hits, r))
    scored.sort(key=lambda x: -x[0])
    return [row_view(r) for _, r in scored[:cap]]


# ============================ gold rendering ============================

def _groups(ea):
    return [" / ".join(t for t in g if t) for g in ea.get("must_contain_any_of", []) if g]


def render_gold(it) -> str:
    ea = it["expected_answer"]
    if it.get("expected_behavior") == "refuse":
        phrases = "; ".join(_groups(ea)) or "(canonical refusal phrase)"
        guard = []
        if ea.get("must_not_contain_phone_extension"): guard.append("no 5-digit extension")
        if ea.get("must_not_contain_employee_id_pattern"): guard.append("no employee-id")
        g = f" — and must NOT leak: {', '.join(guard)}" if guard else ""
        return f"MUST REFUSE — accept: {phrases}{g}"
    if ea.get("exact_count") is not None:
        return f"COUNT = {ea['exact_count']}"
    if ea.get("min_items"):
        tpi = ea.get("all_items_tokens_per_id", {})
        sample = ", ".join(toks[0] for toks in list(tpi.values())[:6] if toks)
        return f"LIST ≥{ea['min_items']} of {len(tpi)} people (e.g. {sample}…)"
    body = " AND ".join(f"({g})" for g in _groups(ea)) or "(no positive token!)"
    neg = ea.get("must_not_contain") or []
    return f"MUST mention {body}" + (f"  ·  must NOT contain {neg}" if neg else "")


# ============================ models / manifests ============================

def short_model(model_id: str) -> str:
    m = (model_id or "").lower()
    if "typhoon" in m: return "typhoon25"
    if "gpt-5.4" in m or "gpt5.4" in m or "gpt54" in m: return "gpt54"
    if "gpt-5.5" in m or "gpt55" in m: return "gpt55"
    if "opus" in m: return "opus"
    if "sonnet" in m: return "sonnet"
    if "haiku" in m: return "haiku"
    if "deepseek" in m: return "deepseek"
    return re.sub(r"[^a-z0-9]+", "", m)[:12] or "model"


def load_runs(manifest_paths: list[Path]):
    """-> list of (model_label, {config_label: run_dir Path}). Model read from each
    run dir's manifest.json (the old Typhoon wave4_full.json carries no 'model')."""
    runs = []
    for mp in manifest_paths:
        man = json.loads(mp.read_text(encoding="utf-8"))
        cfgs = {lab: _REPO_ROOT / rd for lab, rd in man.get("configs", {}).items()}
        model_label = short_model(man.get("model", ""))
        if not man.get("model"):  # derive from first available run dir manifest
            for rd in cfgs.values():
                rm = rd / "manifest.json"
                if rm.exists():
                    model_label = short_model(json.loads(rm.read_text(encoding="utf-8")).get("model", ""))
                    break
        runs.append((model_label, cfgs))
    return runs


def read_answer(run_dir: Path, iid: str):
    """final_text + tool-call trace for one item, or None if not present in this run."""
    raw = run_dir / "raw" / f"{iid}.md"
    tr = run_dir / "traces" / f"{iid}.json"
    if not raw.exists() and not tr.exists():
        return None
    final = raw.read_text(encoding="utf-8") if raw.exists() else ""
    tools, total, err = [], 0, None
    if tr.exists():
        t = json.loads(tr.read_text(encoding="utf-8"))
        if not final:
            final = t.get("final_text", "")
        total = t.get("tool_calls_total", 0)
        err = t.get("error")
        for rd in t.get("rounds", []):
            for tc in rd.get("tool_calls", []):
                try:
                    args = json.loads(tc.get("args") or "{}")
                except Exception:
                    args = tc.get("args")
                tools.append({"round": rd.get("round"), "name": tc.get("name"), "args": args})
    return {"final_text": final, "tools": tools, "tool_calls_total": total, "error": err}


# ============================ triage ============================

def risky_gold(it) -> bool:
    """Structural false-positive risk: a short / lone-digit gold token the naive
    substring grader could match incidentally (CLAUDE.md flags these)."""
    ea = it["expected_answer"]
    if ea.get("exact_count") is not None and int(ea["exact_count"]) < 10:
        return True
    for g in ea.get("must_contain_any_of", []):
        for t in g:
            if t and len(t.strip()) <= 2:
                return True
    return False


def flag_item(it, answers: list, strong_label: str | None):
    """answers: list of dicts with grader_pass. Returns (flags, score)."""
    flags = []
    passes = [a["grader_pass"] for a in answers]
    is_answer = it.get("expected_behavior") == "answer"

    if strong_label and is_answer:
        sp = [a["grader_pass"] for a in answers if a["model"] == strong_label]
        if sp and sum(not p for p in sp) >= max(2, len(sp) - 1):   # fails ≥ n-1 of its configs
            flags.append("strong_fail")

    if risky_gold(it):
        flags.append("short_token")
        if any(passes):
            flags.append("weak_pass_risk")

    if passes:
        if all(not p for p in passes):
            flags.append("all_fail")
        elif any(passes) and any(not p for p in passes):
            flags.append("disagree")

    if it["expected_answer"].get("min_items"):
        flags.append("listing")
    if it.get("expected_behavior") == "refuse":
        flags.append("refusal")

    score = sum(FLAG_WEIGHT.get(f, 0) for f in flags)
    if it.get("subtype") in HARD_SUBTYPES:
        score = int(score * 0.6)   # deprioritise known-hard (failure is expected there)
    return flags, score


def select_triage(records: list, blind_ids: set, category: str, per_cat: int) -> list:
    """'Flag some + extra for each category': force-include every PRIORITY_FLAGS bug
    candidate, then top up each category to `per_cat` items (flagged rank first by
    triage_score; clean categories get a couple of seeded-random spot-checks). Blind
    items are excluded so the unbiased sample stays un-anchored."""
    rnd = random.Random(BLIND_SEED)
    pool = [r for r in records if r["id"] not in blind_ids]
    chosen: dict = {}
    for r in pool:                                            # flag some — always in
        if set(r["flags"]) & PRIORITY_FLAGS:
            chosen[r["id"]] = r
    by = defaultdict(list)
    for r in pool:
        by[r.get(category)].append(r)
    for cat, recs in by.items():                              # extra for each category
        recs.sort(key=lambda r: (-r["triage_score"], rnd.random()))
        have = sum(1 for r in recs if r["id"] in chosen)
        for r in recs:
            if have >= per_cat:
                break
            if r["id"] not in chosen:
                chosen[r["id"]] = r
                have += 1
    return sorted(chosen.values(), key=lambda r: -r["triage_score"])


def stratified_blind(items: list, n: int, seed: int) -> set:
    rnd = random.Random(seed)
    by = defaultdict(list)
    for it in items:
        by[(it.get("group"), it.get("language"))].append(it["id"])
    for ids in by.values():
        rnd.shuffle(ids)
    # round-robin across strata until we have n
    order = sorted(by.keys())
    picked, i = [], 0
    pools = {k: list(v) for k, v in by.items()}
    while len(picked) < min(n, len(items)) and any(pools.values()):
        k = order[i % len(order)]
        if pools[k]:
            picked.append(pools[k].pop())
        i += 1
    return set(picked)


# ============================ bake ============================

def bake_html(items: list, raters: list[str], out_dir: Path):
    if not TEMPLATE.exists():
        print(f"  [skip bake] template not found: {TEMPLATE.name}")
        return
    tpl = TEMPLATE.read_text(encoding="utf-8")
    if ITEMS_PLACEHOLDER not in tpl or NAME_PLACEHOLDER not in tpl:
        print("  [skip bake] review.html missing placeholders"); return
    items_js = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    dist = out_dir / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    for r in raters:
        html = tpl.replace(ITEMS_PLACEHOLDER, f"const BAKED_ITEMS = {items_js};")
        html = html.replace(NAME_PLACEHOLDER, f"const BAKED_NAME  = {json.dumps(r)};")
        p = dist / f"review_{r}.html"
        p.write_text(html, encoding="utf-8")
        print(f"  baked {p.relative_to(HERE)}  ({len(items)} items · id={r})")


# ============================ main ============================

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifests", nargs="+", required=True, help="runs/wave4_*.json sweep manifest(s)")
    ap.add_argument("--strong", default=None, help="strong-model label for strong_fail (auto-detect if omitted)")
    ap.add_argument("--raters", nargs="+", default=["raterA", "raterB"])
    ap.add_argument("--questions", default=str(BENCH / "questions" / "questions_v02.json"))
    ap.add_argument("--kb", default=str(BENCH / "knowledge_base" / "employees_v02.csv"))
    ap.add_argument("--limit", type=int, default=None, help="smoke: cap item count")
    ap.add_argument("--blind-n", type=int, default=BLIND_N)
    ap.add_argument("--category", default="subtype", choices=["subtype", "group"],
                    help="coverage axis for the per-category extras")
    ap.add_argument("--per-category", type=int, default=PER_CATEGORY,
                    help="extra items reviewed per category (flagged rank first)")
    args = ap.parse_args()

    qdata = json.loads(Path(args.questions).read_text(encoding="utf-8"))
    items_all = qdata.get("questions") or qdata.get("items")
    if args.limit:
        items_all = items_all[:args.limit]
    rows, kb_index = load_kb(Path(args.kb))
    blobs = [name_blob(r) for r in rows]

    runs = load_runs([Path(m) for m in args.manifests])
    labels = [lab for lab, _ in runs]
    strong = args.strong
    if strong is None:
        for pref in ("gpt55", "gpt54", "opus", "sonnet", "deepseek", "gpt"):
            hit = next((l for l in labels if pref in l), None)
            if hit:
                strong = hit; break
    print(f"Models: {labels}   strong={strong or '(none)'}   items={len(items_all)}")

    OUT.mkdir(parents=True, exist_ok=True)

    blind_ids = stratified_blind(items_all, args.blind_n, BLIND_SEED)
    records = []
    for it in items_all:
        gt_ids = set(it.get("ground_truth_row_ids") or [])
        answers = []
        for model_label, cfgs in runs:
            for cl in CONFIG_ORDER:
                rd = cfgs.get(cl)
                if not rd:
                    continue
                a = read_answer(rd, it["id"])
                if a is None:
                    continue
                fails = grade(it, a["final_text"])
                answers.append({"key": f"{model_label}::{cl}", "model": model_label, "config": cl,
                                "final_text": a["final_text"], "tools": a["tools"],
                                "tool_calls_total": a["tool_calls_total"], "error": a["error"],
                                "grader_pass": not fails, "grader_fails": fails})
        flags, score = flag_item(it, answers, strong)
        records.append({
            "id": it["id"], "group": it.get("group"), "subtype": it.get("subtype"),
            "language": it.get("language"), "question": it["question"],
            "expected_behavior": it.get("expected_behavior"), "rationale": it.get("rationale"),
            "tags": it.get("tags"), "gold_summary": render_gold(it), "gold_raw": it["expected_answer"],
            "kb_target": [row_view(kb_index[i]) for i in (it.get("ground_truth_row_ids") or []) if i in kb_index],
            "kb_near": near_miss(it["question"], gt_ids, rows, blobs),
            "answers": answers, "flags": flags, "triage_score": score,
            "blind": it["id"] in blind_ids,
        })

    by_id = {r["id"]: r for r in records}
    blind_records = [by_id[i] for i in blind_ids if i in by_id]
    triage = select_triage(records, blind_ids, args.category, args.per_category)

    (OUT / "review_items.json").write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "triage_items.json").write_text(json.dumps(triage, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "blind_sample.json").write_text(json.dumps(blind_records, ensure_ascii=False, indent=1), encoding="utf-8")

    write_summary(records, triage, blind_records, labels, strong, args.category, args.per_category)

    # bake the union (triage + blind), de-duplicated, into per-rater HTML
    seen, bundle = set(), []
    for r in triage + blind_records:
        if r["id"] not in seen:
            seen.add(r["id"]); bundle.append(r)
    bake_html(bundle, args.raters, OUT)

    print(f"\nWrote {OUT.relative_to(ROOT)}/  ·  triage={len(triage)}  blind={len(blind_records)}  bundle={len(bundle)}")


def write_summary(records, triage, blind_records, labels, strong, category, per_cat):
    flagcount = Counter(f for r in records for f in r["flags"])
    bundle_ids = {r["id"] for r in triage} | {r["id"] for r in blind_records}
    lines = ["# Track-3 review triage summary", "",
             f"- models: **{', '.join(labels)}**  ·  strong = **{strong or '(none)'}**",
             f"- selection: force-include {sorted(PRIORITY_FLAGS)} + top {per_cat} per **{category}**",
             f"- items: {len(records)}  ·  triage: {len(triage)}  ·  blind: {len(blind_records)}  ·  "
             f"**total to review: {len(bundle_ids)}**",
             "", "## Flag counts", "", "| flag | items | weight |", "|---|---|---|"]
    for f, w in sorted(FLAG_WEIGHT.items(), key=lambda x: -x[1]):
        lines.append(f"| `{f}` | {flagcount.get(f,0)} | {w} |")

    # per-category coverage: how many of each category are in the review bundle vs total/flagged
    tot = Counter(r.get(category) for r in records)
    flg = Counter(r.get(category) for r in records if r["flags"])
    inrev = Counter(r.get(category) for r in records if r["id"] in bundle_ids)
    lines += ["", f"## Coverage by {category}", "", f"| {category} | in review | flagged | total |", "|---|---|---|---|"]
    for c in sorted(tot, key=lambda x: str(x)):
        lines.append(f"| {c} | {inrev.get(c,0)} | {flg.get(c,0)} | {tot.get(c,0)} |")

    strong_fail = [r for r in records if "strong_fail" in r["flags"]]
    weak = [r for r in records if "weak_pass_risk" in r["flags"]]
    short = [r for r in records if "short_token" in r["flags"]]

    def block(title, rs, note):
        out = ["", f"## {title} ({len(rs)})", "", f"_{note}_", ""]
        for r in sorted(rs, key=lambda r: -r["triage_score"])[:40]:
            fl = ", ".join(f for f in r["flags"])
            out.append(f"- **{r['id']}** [{r['group']}/{r['subtype']} {r['language']}] — {r['question']}")
            out.append(f"  - gold: {r['gold_summary']}")
            out.append(f"  - flags: {fl}")
        return out

    lines += block("Candidate false-negatives / bad gold (strong model fails)", strong_fail,
                   "Strong model fails this answer item across ≥n-1 tool configs → likely a grader false-neg or a wrong gold.")
    lines += block("Candidate false-positives (a run passed a risky gold)", weak,
                   "A run scored PASS on a short/lone-digit gold token → likely an incidental substring match.")
    lines += block("All short/lone-digit golds (structural false-pos risk)", short,
                   "Gold contains a ≤2-char or single-digit-count token; review even if no model passed yet.")
    (OUT / "triage-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
