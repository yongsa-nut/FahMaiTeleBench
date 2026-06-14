"""Backfill Section/Department on the 99 orphan rows (Unit code present, Section/Dept
blank) and recompute the count golds that depend on them. Writes STAGING copies +
a change report; does NOT touch the canonical files (apply step is separate, after
the in-flight sweep finishes).

Section is derived from the Unit code: strip the trailing `-<n>`, then a trailing
`-LEAD` (a section's lead unit belongs to that section). Department = the dominant
Department already used by that Section.

Count golds (exact_count items) currently carry empty ground_truth_row_ids. For each,
we find the field+code whose OLD exact count equals the OLD gold (that's how the gold
was built), recompute it on the backfilled KB, and set exact_count + the
must_contain_any_of token + ground_truth_row_ids = the cohort. Items we can't map
confidently (e.g. C4 filtered counts) are reported and left untouched.

  python backfill_orphans.py            # write staging + report
  python backfill_orphans.py --apply    # copy staging over the canonical files (+ .bak)
"""
from __future__ import annotations

import argparse, csv, io, json, re, shutil, sys
from collections import Counter, defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
BENCH = HERE.parents[2] / "the source exam" / _REPO_ROOT
KB = BENCH / "knowledge_base" / "employees_v02.csv"
Q = BENCH / "questions" / "questions_v02.json"
KB_STAGE = KB.with_suffix(".backfilled.csv")
Q_STAGE = Q.with_suffix(".backfilled.json")
REPORT = HERE / "review" / "backfill-report.md"

CODE = re.compile(r"\b[A-Z0-9]{2,}(?:-[A-Z0-9]+)+\b")
FIELDS = ["Section", "Unit", "Department", "Branch"]


def section_of(unit: str) -> str:
    u = re.sub(r"-\d+$", "", unit.strip())   # WK-PD-10 -> WK-PD ; TEC-SEC-LEAD-2 -> TEC-SEC-LEAD
    u = re.sub(r"-LEAD$", "", u)              # TEC-SEC-LEAD -> TEC-SEC
    return u


def load_kb():
    with KB.open(encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="copy staging over canonical files (+ .bak)")
    args = ap.parse_args()

    if args.apply:
        for stage, dest in ((KB_STAGE, KB), (Q_STAGE, Q)):
            if not stage.exists():
                sys.exit(f"missing staging file {stage} — run without --apply first")
            bak = dest.with_suffix(dest.suffix + ".pre_backfill.bak")
            if not bak.exists():
                shutil.copy2(dest, bak)
            shutil.copy2(stage, dest)
            print(f"applied {stage.name} -> {dest.name}  (backup {bak.name})")
        return

    rows, fields = load_kb()
    g = lambda r, c: (r.get(c) or "").strip()
    sections = {g(r, "Section") for r in rows if g(r, "Section")}
    dept_of_section = {}
    for s in sections:
        c = Counter(g(r, "Department") for r in rows if g(r, "Section") == s and g(r, "Department"))
        if c:
            dept_of_section[s] = c.most_common(1)[0][0]

    # ---- backfill ----
    fixed, unresolved = [], []
    for r in rows:
        if g(r, "Unit") and not g(r, "Section"):
            sec = section_of(g(r, "Unit"))
            if sec in sections:
                r["Section"] = sec
                if not g(r, "Department"):
                    r["Department"] = dept_of_section.get(sec, "")
                fixed.append((r["Employee ID"], g(r, "Unit"), sec, r["Department"]))
            else:
                unresolved.append((r["Employee ID"], g(r, "Unit"), sec))

    KB_STAGE.write_text("", encoding="utf-8")
    with KB_STAGE.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

    # exact counts on the BACKFILLED rows, by field
    def count(field, code): return [r["Employee ID"] for r in rows if g(r, field) == code]
    # OLD counts (reload pristine to compare)
    old_rows, _ = load_kb()
    og = lambda r, c: (r.get(c) or "").strip()
    def old_count(field, code): return sum(1 for r in old_rows if og(r, field) == code)
    # distinct values per field, longest first (so WK-PD matches before dept WK)
    field_vals = {f: sorted({og(r, f) for r in old_rows if og(r, f)}, key=len, reverse=True)
                  for f in FIELDS}

    # ---- recompute count golds ----
    qdata = json.loads(Q.read_text(encoding="utf-8"))
    items = qdata.get("questions") or qdata.get("items")
    changed, unmapped = [], []
    for it in items:
        ea = it["expected_answer"]
        if ea.get("exact_count") is None:
            continue
        old_gold = ea["exact_count"]
        qlow = it["question"].lower()
        matched = None
        # find a Section/Unit/Department/Branch value that appears in the question AND whose
        # OLD exact count equals the OLD gold — that's the cohort the gold was built on.
        for fld in FIELDS:
            for v in field_vals[fld]:
                if v.lower() in qlow and old_count(fld, v) == old_gold:
                    matched = (v, fld); break
            if matched: break
        if not matched:
            unmapped.append((it["id"], old_gold, CODE.findall(it["question"]))); continue
        code, fld = matched
        ids = count(fld, code)
        new_gold = len(ids)
        if new_gold != old_gold or not it.get("ground_truth_row_ids"):
            ea["exact_count"] = new_gold
            ea["must_contain_any_of"] = [[str(new_gold)]]
            it["ground_truth_row_ids"] = ids
            it.setdefault("tags", []) if isinstance(it.get("tags"), list) else None
            changed.append((it["id"], it.get("language"), code, fld, old_gold, new_gold))

    Q_STAGE.write_text(json.dumps(qdata, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- report ----
    L = ["# Backfill report — orphan sections + count golds", "",
         f"- KB rows backfilled (Section+Dept set): **{len(fixed)}**" +
         (f"  ·  unresolved: {len(unresolved)}" if unresolved else "  ·  all resolved"),
         f"- count golds recomputed: **{len(changed)}**  ·  unmapped (left as-is): {len(unmapped)}",
         f"- staging: `{KB_STAGE.name}`, `{Q_STAGE.name}`  → apply with `--apply`", "",
         "## Count-gold changes", "", "| id | lang | code | field | old gold | new gold | Δ |",
         "|---|---|---|---|---|---|---|"]
    for iid, lang, code, fld, o, nn in sorted(changed):
        L.append(f"| {iid} | {lang} | `{code}` | {fld} | {o} | **{nn}** | {'+' if nn>=o else ''}{nn-o} |")
    if unmapped:
        L += ["", "## Count items NOT auto-mapped (review manually)", "",
              "| id | gold | codes in question |", "|---|---|---|"]
        for iid, gold, codes in unmapped:
            L.append(f"| {iid} | {gold} | {', '.join(codes) or '—'} |")
    if unresolved:
        L += ["", "## Orphan rows whose unit prefix is NOT a known Section", "",
              "| id | unit | derived section |", "|---|---|---|"]
        for eid, unit, sec in unresolved:
            L.append(f"| {eid} | `{unit}` | `{sec}` |")
    L += ["", "## Sample backfilled rows", "", "| id | unit | → Section | → Department |", "|---|---|---|---|"]
    for eid, unit, sec, dep in fixed[:20]:
        L.append(f"| {eid} | `{unit}` | `{sec}` | `{dep}` |")
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"backfilled {len(fixed)} rows (unresolved {len(unresolved)})")
    print(f"count golds changed: {len(changed)}  ·  unmapped: {len(unmapped)}")
    print(f"staging: {KB_STAGE.name}, {Q_STAGE.name}")
    print(f"report: {REPORT.relative_to(HERE)}")


if __name__ == "__main__":
    main()
