"""Scan employees_v02.csv for two data-integrity issues surfaced by the grader review:

  (A) Orphan sub-unit rows — a Unit code like `WK-PD-10` (section-prefix + numeric
      suffix) but a BLANK Section/Department. These leak into a literal grep for the
      section code, so "size of <section>" counted by grep ≠ counted by exact Section.
  (B) Count-gold grep sensitivity — for every exact_count item, extract the org code(s)
      from the question and compare the GOLD count to a literal-substring (grep) count
      and to exact Section/Unit/Department counts. Flags items where grep would mislead
      and items whose cohort is touched by orphan rows.

Read-only. Writes analysis/review/kb-integrity-scan.md + prints a summary.
  python scan_kb_integrity.py
"""
from __future__ import annotations

import csv, io, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
BENCH = HERE.parents[2] / "the source exam" / _REPO_ROOT
KB = BENCH / "knowledge_base" / "employees_v02.csv"
Q = BENCH / "questions" / "questions_v02.json"
OUT = HERE / "review" / "kb-integrity-scan.md"

CODE = re.compile(r"\b[A-Z0-9]{2,}(?:-[A-Z0-9]+)+\b")     # WK-PD, B2B-SUP, MKT-EVT, RET-OFF…
SUBUNIT = re.compile(r"^(.*)-\d+$")                        # WK-PD-10 -> prefix WK-PD


def main():
    rows = list(csv.DictReader(KB.open(encoding="utf-8")))
    n = len(rows)
    def g(r, c): return (r.get(c) or "").strip()
    sections = {g(r, "Section") for r in rows if g(r, "Section")}
    depts = {g(r, "Department") for r in rows if g(r, "Department")}
    units = {g(r, "Unit") for r in rows if g(r, "Unit")}

    L = [f"# KB integrity scan — employees_v02.csv ({n} rows)", ""]

    # ---- blank-field audit ----
    blank = {c: sum(1 for r in rows if not g(r, c)) for c in ("Department", "Section", "Unit")}
    L += ["## Blank-field counts", "", "| field | blank rows |", "|---|---|"]
    L += [f"| {c} | {blank[c]} |" for c in blank]

    # ---- (A) orphan sub-units: Unit present, Section blank ----
    unit_no_sec = [r for r in rows if g(r, "Unit") and not g(r, "Section")]
    by_prefix = defaultdict(list)
    for r in unit_no_sec:
        m = SUBUNIT.match(g(r, "Unit"))
        by_prefix[m.group(1) if m else g(r, "Unit")].append(r)
    L += ["", f"## (A) Rows with a Unit but BLANK Section — {len(unit_no_sec)}", ""]
    if unit_no_sec:
        L += ["Grouped by unit prefix; **prefix-is-section** = that prefix is a real Section "
              "elsewhere (so these rows arguably belong to it but are uncounted by an exact "
              "Section query, and over-counted by a substring grep):", "",
              "| unit prefix | orphan rows | prefix is a real Section? | that Section's exact size |",
              "|---|---|---|---|"]
        for p, rs in sorted(by_prefix.items(), key=lambda x: -len(x[1])):
            exact = sum(1 for r in rows if g(r, "Section") == p)
            L.append(f"| `{p}` | {len(rs)} | {'YES' if p in sections else 'no'} | "
                     f"{exact if p in sections else '—'} |")
        L += ["", "Sample orphan rows:", ""]
        for r in unit_no_sec[:12]:
            L.append(f"- id `{r['Employee ID']}`  Dept=`{g(r,'Department')}`  Section=`` "
                     f"Unit=`{g(r,'Unit')}`  Pos=`{g(r,'Position in English')}`")

    # also: Unit present, Department blank
    unit_no_dept = [r for r in rows if g(r, "Unit") and not g(r, "Department")]
    L += ["", f"_Rows with a Unit but blank Department: {len(unit_no_dept)}_"]

    # ---- section grep-sensitivity: substring overcount vs exact ----
    sens = []
    for s in sections:
        exact = sum(1 for r in rows if g(r, "Section") == s)
        sub = sum(1 for r in rows if any(s in (r.get(c) or "") for c in r))
        if sub != exact:
            sens.append((s, exact, sub, sub - exact))
    L += ["", f"## Sections where a literal grep over-counts (substring ≠ exact) — {len(sens)}", ""]
    if sens:
        L += ["| Section | exact size | grep (substring) | delta |", "|---|---|---|---|"]
        for s, e, sub, d in sorted(sens, key=lambda x: -x[3]):
            L.append(f"| `{s}` | {e} | {sub} | +{d} |")

    # ---- (B) count-gold grep sensitivity ----
    items = json.loads(Q.read_text(encoding="utf-8"))
    items = items.get("questions") or items.get("items")
    counts = [it for it in items if it["expected_answer"].get("exact_count") is not None]
    grep_traps, gt_mismatch = [], []
    for it in counts:
        gold = it["expected_answer"]["exact_count"]
        gtn = len(it.get("ground_truth_row_ids") or [])
        if gtn != gold:
            gt_mismatch.append((it["id"], gold, gtn))
        codes = CODE.findall(it["question"])
        for code in codes:
            sub = sum(1 for r in rows if any(code in (r.get(c) or "") for c in r))
            sec = sum(1 for r in rows if g(r, "Section") == code)
            uni = sum(1 for r in rows if g(r, "Unit") == code)
            dep = sum(1 for r in rows if g(r, "Department") == code)
            if sub != gold and gold in (sec, uni, dep):
                field = "Section" if gold == sec else ("Unit" if gold == uni else "Department")
                grep_traps.append((it["id"], it.get("language"), code, gold, sub, field))
    L += ["", f"## (B) Count items where grep over/under-counts vs the gold — {len(grep_traps)}", "",
          "_Gold matches an **exact field** count but a literal grep on the code gives a different "
          "number → a model that greps the code (instead of an exact field query) is led to the wrong "
          "count. This is a real model/tool-use failure the benchmark should reward, **not** a grader bug._", ""]
    if grep_traps:
        L += ["| id | lang | code | gold (exact) | grep count | exact field |", "|---|---|---|---|---|---|"]
        for iid, lang, code, gold, sub, field in grep_traps:
            L.append(f"| {iid} | {lang} | `{code}` | {gold} | {sub} | {field} |")
    if gt_mismatch:
        L += ["", f"### ⚠ count items where gold ≠ len(ground_truth_row_ids) — {len(gt_mismatch)}", "",
              "| id | gold | #gt_ids |", "|---|---|---|"]
        L += [f"| {iid} | {gold} | {gtn} |" for iid, gold, gtn in gt_mismatch]

    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"rows={n}  blank-Section={blank['Section']}  blank-Dept={blank['Department']}")
    print(f"(A) Unit-but-blank-Section rows: {len(unit_no_sec)}  across {len(by_prefix)} unit prefixes")
    realsec = [p for p in by_prefix if p in sections]
    print(f"    of which prefix-is-a-real-Section: {sum(len(by_prefix[p]) for p in realsec)} rows "
          f"in prefixes {sorted(realsec)}")
    print(f"sections grep over-counts: {len(sens)}  -> {sorted(s for s,_,_,_ in sens)}")
    print(f"(B) count-gold grep-trap items: {len(grep_traps)}  ·  gold≠#gt_ids: {len(gt_mismatch)}")
    print(f"wrote {OUT.relative_to(HERE)}")


if __name__ == "__main__":
    main()
