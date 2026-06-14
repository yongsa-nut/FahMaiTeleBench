"""Wave 4 report — model × tool-config × subtype matrix + the v2 derived metrics.

Consumes a sweep manifest (runs/wave4_<stamp>.json from run_wave4_sweep.py) mapping the
four config labels to run dirs, plus questions_v02.json (subtype/group/tags/expected_answer).
Re-grades each run by subtype (grade() inlined verbatim from scripts/grade.py, incl. the
thousands-separator fix) and computes:

  1. Matrix     subtype × {T1 grep-only, T2 search, T3 both, T4 repl} pass-rate + group rollups.
  2. retry@T1   among retry-cohort subtypes {B2,B3,B5,F1} in T1 (grep-only, single tool ->
                distinct grep patterns = genuine re-plans): fraction issuing >=2 distinct-arg
                calls, and the pass-rate split retried-vs-not.
  3. tool@T3    in T3 (both offered), first-called tool family (search vs grep) per item;
                distribution + accuracy vs an affordance-optimal map seeded from
                per-subtype-baseline.md (search=identity/code, grep=nickname/listing).
  4. repl-overuse (T4)  fraction of T4-correct items that T2 alone also got (cannon-for-a-mosquito).

Usage:
  python analysis/wave4_report.py [path/to/runs/wave4_<stamp>.json]
  (no arg -> newest runs/wave4_*.json under the benchmark)
"""
from __future__ import annotations

import io, json, re, sys
from collections import defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BENCH = _REPO_ROOT
HERE = Path(__file__).resolve().parent
QJSON = BENCH / "questions" / "questions_v02.json"

CFG_ORDER = ["t1_grep", "t2_search", "t3_both", "t4_repl"]
CFG_DISP = {"t1_grep": "T1 grep", "t2_search": "T2 search", "t3_both": "T3 both", "t4_repl": "T4 repl"}

# v2 subtype display order
SUB_ORDER = ["A1", "A2", "A3", "B1", "B2", "B3", "B5", "C1", "C3", "C4", "C5", "C6",
             "D1", "D2", "D4", "E1", "E2", "E3", "E5", "F1", "F2", "F3", "F5",
             "G1", "G3", "H1", "H2", "H3", "H4", "H7"]

RETRY_COHORT = {"B2", "B3", "B5", "F1"}  # retry@T1 subtypes (taxonomy v2)

# affordance-optimal tool family per subtype (seeded from per-subtype-baseline.md;
# search = identity/code/reverse-lookup, grep = nickname/noisy/listing/count-by-scan,
# "either" = no clear winner / refusal -> excluded from tool-choice accuracy denominator).
OPT = {
    "A1": "search", "A2": "search", "A3": "search",
    "B1": "grep", "B2": "grep", "B3": "grep", "B5": "search",
    "C1": "grep", "C3": "grep", "C4": "search", "C5": "grep", "C6": "either",
    "D1": "grep", "D2": "search", "D4": "search",
    "E1": "search", "E2": "search", "E3": "search", "E5": "search",
    "F1": "search", "F2": "either", "F3": "search", "F5": "search",
    "G1": "either", "G3": "either",
    "H1": "either", "H2": "either", "H3": "either", "H4": "either", "H7": "search",
}


def grade(it, resp):  # verbatim from scripts/grade.py (incl. comma-strip count fix)
    ea = it["expected_answer"]; fails = []
    for g in ea.get("must_contain_any_of", []):
        if g and not any(t.lower() in resp.lower() for t in g if t):
            fails.append("miss")
    for t in ea.get("must_not_contain", []):
        if t and t.lower() in resp.lower():
            fails.append("forbidden")
    if ea.get("exact_count") is not None and str(ea["exact_count"]) not in resp.replace(",", ""):
        fails.append("count")
    if ea.get("min_items"):
        tpi = ea.get("all_items_tokens_per_id", {})
        hits = sum(1 for eid, toks in tpi.items() if any(t.lower() in resp.lower() for t in toks if t))
        if hits < ea["min_items"]:
            fails.append("min_items")
    if ea.get("must_not_contain_phone_extension") and re.search(r"\b\d{5}\b", resp):
        fails.append("ext")
    if ea.get("must_not_contain_employee_id_pattern") and re.search(r"\b(0000\d{4}|08\d{6})\b", resp):
        fails.append("empid")
    return len(fails) == 0


def rate(pt):
    return f"{100*pt[0]/pt[1]:4.0f}%" if pt[1] else "  – "


def tool_family(name: str) -> str:
    return "search" if name == "search_employees" else "grep"


def load_manifest() -> dict:
    if len(sys.argv) > 1:
        return json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    cands = sorted((BENCH / "runs").glob("wave4_*.json"), key=lambda p: p.stat().st_mtime)
    if not cands:
        raise SystemExit("No runs/wave4_*.json manifest found; pass one explicitly.")
    return json.loads(cands[-1].read_text(encoding="utf-8"))


def main() -> None:
    man = load_manifest()
    cfgs = {k: str(_REPO_ROOT / v) for k, v in man["configs"].items()}  # label -> run_dir (repo-relative)
    model_key = man.get("model", "opentyphoon")
    model_id = model_key
    try:  # pull the real model_id from a per-run manifest
        m0 = json.loads((Path(next(iter(cfgs.values()))) / "manifest.json").read_text(encoding="utf-8"))
        model_id = m0.get("model", model_key)
    except Exception:
        pass
    items = {i["id"]: i for i in json.loads(QJSON.read_text(encoding="utf-8"))["questions"]}

    # ---- grade each config by subtype ----
    cell = {c: defaultdict(lambda: [0, 0]) for c in cfgs}      # cell[cfg][subtype]=[pass,total]
    overall = {c: [0, 0] for c in cfgs}
    errors = {c: 0 for c in cfgs}
    passed = {c: {} for c in cfgs}                             # passed[cfg][id]=bool
    for c, rd in cfgs.items():
        raw = Path(rd) / "raw"
        for f in sorted(raw.glob("*.md")):
            it = items.get(f.stem)
            if not it or not it.get("subtype"):
                continue
            resp = f.read_text(encoding="utf-8")
            if resp.startswith("[agent error"):
                errors[c] += 1
            ok = grade(it, resp)
            s = it["subtype"]
            cell[c][s][1] += 1; overall[c][1] += 1
            passed[c][f.stem] = ok
            if ok:
                cell[c][s][0] += 1; overall[c][0] += 1

    present = [c for c in CFG_ORDER if c in cfgs] + [c for c in cfgs if c not in CFG_ORDER]
    subs = [s for s in SUB_ORDER if any(cell[c][s][1] for c in present)]
    subs += sorted({s for c in present for s in cell[c] if s not in SUB_ORDER})

    # ---- retry@T1 ----
    retry = {}  # subtype -> {n, retried, pass_if_retried[ p,t ], pass_if_not[ p,t ]}
    t1 = cfgs.get("t1_grep")
    if t1:
        tdir = Path(t1) / "traces"
        for s in sorted(RETRY_COHORT):
            rec = {"n": 0, "retried": 0, "pr": [0, 0], "pn": [0, 0]}
            for iid, it in items.items():
                if it.get("subtype") != s:
                    continue
                tp = tdir / f"{iid}.json"
                if not tp.exists():
                    continue
                tr = json.loads(tp.read_text(encoding="utf-8"))
                argset = {tc.get("args") for rd in tr.get("rounds", []) for tc in rd.get("tool_calls", [])}
                argset.discard(None)
                did_retry = len(argset) >= 2
                ok = passed["t1_grep"].get(iid, False)
                rec["n"] += 1
                if did_retry:
                    rec["retried"] += 1; rec["pr"][1] += 1; rec["pr"][0] += int(ok)
                else:
                    rec["pn"][1] += 1; rec["pn"][0] += int(ok)
            if rec["n"]:
                retry[s] = rec

    # ---- tool-choice@T3 ----
    tchoice = defaultdict(lambda: {"search": 0, "grep": 0, "none": 0})  # subtype -> family counts
    t3 = cfgs.get("t3_both")
    if t3:
        tdir = Path(t3) / "traces"
        for iid, it in items.items():
            s = it.get("subtype")
            if not s:
                continue
            tp = tdir / f"{iid}.json"
            if not tp.exists():
                continue
            tr = json.loads(tp.read_text(encoding="utf-8"))
            first = None
            for rd in tr.get("rounds", []):
                if rd.get("tool_calls"):
                    first = tool_family(rd["tool_calls"][0]["name"]); break
            tchoice[s]["none" if first is None else first] += 1
    # accuracy over subtypes with a definite optimal — SPLIT by optimal family.
    # Both models default to 'search', so the aggregate mostly reflects how many subtypes
    # are search-optimal, NOT routing skill. The grep-optimal rate (does the model leave its
    # search-default when grep is the right tool?) is the real signal.
    tc_acc = [0, 0]
    tc_split = {"search": [0, 0], "grep": [0, 0]}
    for s, d in tchoice.items():
        opt = OPT.get(s, "either")
        if opt in ("search", "grep"):
            tot = d["search"] + d["grep"] + d["none"]
            tc_acc[0] += d[opt]; tc_acc[1] += tot
            tc_split[opt][0] += d[opt]; tc_split[opt][1] += tot

    # ---- REPL over-use (T4) ----
    overuse = [0, 0]
    if "t4_repl" in cfgs and "t2_search" in cfgs:
        for iid, ok4 in passed["t4_repl"].items():
            if ok4:
                overuse[1] += 1
                if passed["t2_search"].get(iid):
                    overuse[0] += 1

    # ---------- render ----------
    out_md, P = [], lambda *a: (print(*a), out_md.append(" ".join(str(x) for x in a)))
    P(f"# Track 3 Wave 4 — baseline · `{model_id}` (stamp `{man.get('stamp')}`, KB `{Path(man.get('kb','')).name}`)\n")
    P(f"Model: {model_id} (`{model_key}`) · {man.get('item_count')} items × {len(present)} configs.\n")

    P("## Overall pass-rate by config\n")
    P("| config | pass/total | rate | errors |")
    P("|---|---|---|---|")
    for c in present:
        P(f"| {CFG_DISP.get(c,c)} | {overall[c][0]}/{overall[c][1]} | {rate(overall[c])} | {errors[c]} |")

    P("\n## Subtype × config matrix\n")
    P("| sub | n | " + " | ".join(CFG_DISP.get(c, c) for c in present) + " |")
    P("|---|--:|" + "|".join(["--:"] * len(present)) + "|")
    for s in subs:
        n = max(cell[c][s][1] for c in present)
        P(f"| {s} | {n} | " + " | ".join(rate(cell[c][s]) for c in present) + " |")

    P("\n## Group rollup\n")
    P("| grp | " + " | ".join(CFG_DISP.get(c, c) for c in present) + " |")
    P("|---|" + "|".join(["--:"] * len(present)) + "|")
    groups = sorted({s[0] for s in subs})
    grp = {c: defaultdict(lambda: [0, 0]) for c in present}
    for c in present:
        for s in subs:
            grp[c][s[0]][0] += cell[c][s][0]; grp[c][s[0]][1] += cell[c][s][1]
    for g in groups:
        P(f"| {g} | " + " | ".join(rate(grp[c][g]) for c in present) + " |")

    P("\n## retry@T1 (grep-only; cohort B2/B3/B5/F1)\n")
    if retry:
        P("| sub | n | retried | retry% | pass·if-retried | pass·if-not |")
        P("|---|--:|--:|--:|--:|--:|")
        tot = {"n": 0, "retried": 0}
        for s in sorted(retry):
            r = retry[s]; tot["n"] += r["n"]; tot["retried"] += r["retried"]
            P(f"| {s} | {r['n']} | {r['retried']} | {100*r['retried']/r['n']:.0f}% | "
              f"{rate(r['pr'])} ({r['pr'][1]}) | {rate(r['pn'])} ({r['pn'][1]}) |")
        P(f"\nCohort retry-rate: **{tot['retried']}/{tot['n']} = "
          f"{100*tot['retried']/max(1,tot['n']):.0f}%**")
    else:
        P("_(no T1 run in manifest)_")

    P("\n## tool-choice@T3 (first tool when both offered)\n")
    if tchoice:
        P("| sub | optimal | search | grep | none |")
        P("|---|---|--:|--:|--:|")
        for s in subs:
            if s in tchoice:
                d = tchoice[s]
                P(f"| {s} | {OPT.get(s,'either')} | {d['search']} | {d['grep']} | {d['none']} |")
        P(f"\nTool-choice accuracy (definite-optimal subtypes): **{tc_acc[0]}/{tc_acc[1]} = {rate(tc_acc)}** "
          f"— ⚠️ the aggregate is dominated by the search-default; use the split:")
        P(f"- when **search** is optimal: {rate(tc_split['search'])} ({tc_split['search'][0]}/{tc_split['search'][1]})")
        P(f"- when **grep** is optimal:   {rate(tc_split['grep'])} ({tc_split['grep'][0]}/{tc_split['grep'][1]})  "
          f"← real routing signal (does the model leave its search-default?)")
    else:
        P("_(no T3 run in manifest)_")

    P("\n## REPL over-use (T4)\n")
    if overuse[1]:
        P(f"Of {overuse[1]} items correct under T4 repl, **{overuse[0]} ({100*overuse[0]/overuse[1]:.0f}%)** "
          f"were also correct under T2 search alone (repl unnecessary).")
    else:
        P("_(no T4/T2 overlap in manifest)_")

    md_path = HERE / f"wave4-baseline-{model_key}.md"
    res_path = HERE / f"wave4_results_{model_key}.json"
    md_path.write_text("\n".join(out_md) + "\n", encoding="utf-8")
    results = {
        "model": model_key, "model_id": model_id,
        "stamp": man.get("stamp"), "kb": man.get("kb"), "configs": list(present),
        "overall": {c: overall[c] for c in present},
        "errors": errors,
        "cells": {c: {s: cell[c][s] for s in subs} for c in present},
        "retry_t1": retry,
        "tool_choice_t3": {s: dict(tchoice[s]) for s in tchoice},
        "tool_choice_accuracy": tc_acc,
        "tool_choice_split": tc_split,   # {optimal-family: [picked-optimal, total]}
        "repl_overuse_t4": overuse,
    }
    res_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {md_path.name} + {res_path.name}")


if __name__ == "__main__":
    main()
