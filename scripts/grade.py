"""Grade a run directory against questions/questions_v02.json.

Ported from the source project's `_grade_p0_run.py`. Grader logic unchanged.
Only the dataset path, the dataset name, and the raw-file location changed.

Usage: python scripts/grade.py <run_dir>
  where <run_dir> contains a `raw/` subdir with one `<item_id>.md` per graded item.
"""
from __future__ import annotations

import argparse, io, json, os, re, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

_ap = argparse.ArgumentParser()
_ap.add_argument("run_dir")
_ap.add_argument("--questions", default=os.environ.get("FAHMAI_ANSWER_KEY", str(ROOT / "questions" / "questions_v02.json")),
                 help="Answer-key JSON (v0.2: questions/questions_v02.json).")
_args = _ap.parse_args()

RUN_DIR = Path(_args.run_dir).resolve()
RAW_DIR = RUN_DIR / "raw"
if not RAW_DIR.is_dir():
    print(f"No raw/ subdir in {RUN_DIR}")
    sys.exit(2)

data = json.loads(Path(_args.questions).read_text(encoding="utf-8"))
ak_items = data.get("items") or data.get("questions") or []  # v0.1 uses "items", v0.2 uses "questions"
items = {it["id"]: it for it in ak_items if (RAW_DIR / f"{it['id']}.md").exists()}


def _contains(resp, tok):
    """Case-insensitive containment. A purely numeric token (count, extension, ID) must appear as a
    standalone number, not inside a longer one ("2" does not match "2021"); thousands separators ignored."""
    if tok.isdigit():
        return re.search(rf"(?<!\d){tok}(?!\d)", resp.replace(",", "")) is not None
    return tok.lower() in resp.lower()


def grade(it, resp):
    ea = it["expected_answer"]
    fails = []
    for g in ea.get("must_contain_any_of", []):
        if g and not any(_contains(resp, t) for t in g if t):
            fails.append(f"missing any-of {g[:3]}")
    for t in ea.get("must_not_contain", []):
        if t and t.lower() in resp.lower():
            fails.append(f"has forbidden {t!r}")
    if ea.get("exact_count") is not None and not _contains(resp, str(ea["exact_count"])):
        fails.append(f"missing count {ea['exact_count']}")  # strip thousands separators (1,270 -> 1270)
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


results = []
for iid, it in items.items():
    resp = (RAW_DIR / f"{iid}.md").read_text(encoding="utf-8")
    fails = grade(it, resp)
    results.append({
        "id": iid, "bucket": it["bucket"], "question": it["question"],
        "expected_behavior": it["expected_behavior"],
        "priority": it.get("priority"), "language": it.get("language"),
        "response": resp, "fails": fails, "pass": len(fails) == 0,
    })

# JSONL
(RUN_DIR / "results.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in results) + "\n", encoding="utf-8")

n_pass = sum(1 for r in results if r["pass"])
by_bucket = defaultdict(lambda: {"pass": 0, "total": 0})
for r in results:
    by_bucket[r["bucket"]]["total"] += 1
    if r["pass"]: by_bucket[r["bucket"]]["pass"] += 1

by_prio = defaultdict(lambda: {"pass": 0, "total": 0})
for r in results:
    by_prio[r["priority"]]["total"] += 1
    if r["pass"]: by_prio[r["priority"]]["pass"] += 1

print(f"=== Grade — {RUN_DIR.name} ===")
print(f"Overall: {n_pass}/{len(results)} pass ({100*n_pass/max(1,len(results)):.1f}%)\n")
print(f"{'Bucket':32} {'Pass/Total':>12} {'Rate':>8}")
print("-" * 55)
for b, c in sorted(by_bucket.items(), key=lambda x: -x[1]["pass"]/max(1, x[1]["total"])):
    print(f"{b:32} {c['pass']:>4}/{c['total']:<7} {100*c['pass']/c['total']:>6.1f}%")
print()
for p in ("P0", "P1", "P2"):
    if p in by_prio:
        c = by_prio[p]
        print(f"{p}: {c['pass']}/{c['total']} ({100*c['pass']/c['total']:.1f}%)")

fails = [r for r in results if not r["pass"]]
summary = ROOT / RUN_DIR / "report.md"
with open(summary, "w", encoding="utf-8") as f:
    f.write(f"# Run: `{RUN_DIR.name}`\n\n")
    f.write(f"**Overall: {n_pass}/{len(results)} pass ({100*n_pass/max(1,len(results)):.1f}%)**\n\n")
    f.write("## By bucket\n\n| Bucket | Pass/Total | Rate |\n|---|---|---|\n")
    for b, c in sorted(by_bucket.items(), key=lambda x: -x[1]["pass"]/max(1, x[1]["total"])):
        f.write(f"| {b} | {c['pass']}/{c['total']} | {100*c['pass']/c['total']:.1f}% |\n")
    f.write("\n## By priority\n\n")
    for p in ("P0", "P1", "P2"):
        if p in by_prio:
            c = by_prio[p]
            f.write(f"- {p}: {c['pass']}/{c['total']} ({100*c['pass']/c['total']:.1f}%)\n")
    if fails:
        f.write(f"\n## Failures ({len(fails)})\n\n")
        for r in fails[:50]:
            f.write(f"### {r['id']} [{r['bucket']}] {r['priority']}/{r['language']}\n")
            f.write(f"**Q:** {r['question']}\n\n**Fails:** {'; '.join(r['fails'])}\n\n")
            f.write(f"**Response:**\n\n```\n{r['response'][:400]}\n```\n\n")
        if len(fails) > 50:
            f.write(f"\n_+{len(fails)-50} more failures — see results.jsonl_\n")
    else:
        f.write("\n_No failures._\n")

print(f"\nWrote {summary}")
