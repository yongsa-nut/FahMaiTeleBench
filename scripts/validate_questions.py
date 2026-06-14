"""Validate questions/questions.json against DESIGN.md + QUESTION_STYLE.md contracts."""
from __future__ import annotations

import csv, io, json, re, sys
from collections import Counter
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CSV_PATH = ROOT / "knowledge_base" / "employees.csv"
QUESTIONS_PATH = ROOT / "questions" / "questions.json"

with open(CSV_PATH, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
by_id = {r["Employee ID"]: r for r in rows}

data = json.loads(QUESTIONS_PATH.read_text(encoding="utf-8"))
items = data["items"]
meta = data["meta"]

errors = []
warnings = []
def err(m): errors.append(m)
def warn(m): warnings.append(m)

# ---- 1. Unique IDs ----
ids = [i["id"] for i in items]
if len(set(ids)) != len(ids):
    err(f"Duplicate question IDs: {[k for k, c in Counter(ids).items() if c > 1][:5]}")

# ---- 2. Bucket is one of 28 known ----
KNOWN_BUCKETS = {
    "evp_identity_by_code", "evp_identity_by_description", "evp_secretary", "evp_vs_vp_disambig",
    "vp_identity", "ceo_president", "name_lookup", "casual_name_lookup",
    "nickname_grid", "dept_listing_small", "dept_listing_medium", "dept_member_count",
    "section_listing", "org_informal_listing", "tier_listing", "org_plus_person",
    "multi_entity_turn", "subsidiary_md", "extension_reverse", "email_mobile_lookup",
    "email_identity_lookup", "refuse",
    # Gate H.2 new buckets:
    "hard_multihop", "hard_bridge_lookup", "hard_implicit_hierarchy",
    "thai_knowledge", "surname_family", "hard_nickname_variant",
}
for it in items:
    if it["bucket"] not in KNOWN_BUCKETS:
        err(f"{it['id']}: unknown bucket '{it['bucket']}'")

# ---- 3. ground_truth_row_ids resolve ----
for it in items:
    for gid in it.get("ground_truth_row_ids", []):
        if gid not in by_id:
            err(f"{it['id']}: ground_truth_row_id '{gid}' not in CSV")

# ---- 4. P0/P1/P2 tally ----
pc = Counter(i["priority"] for i in items)
for p in ("P0", "P1", "P2"):
    if pc.get(p, 0) == 0:
        warn(f"Priority {p} has 0 items")

# ---- 5. TH/EN split ----
lc = Counter(i["language"] for i in items)
th_ratio = lc["th"] / len(items)
en_ratio = lc["en"] / len(items)
if not (0.70 <= th_ratio <= 0.83):
    warn(f"TH ratio = {th_ratio:.1%} (target ~77%)")

# ---- 6. No duplicate questions (exact text) ----
qs = [i["question"] for i in items]
if len(set(qs)) != len(qs):
    dupes = [q for q, c in Counter(qs).items() if c > 1]
    warn(f"{len(dupes)} duplicate question texts: {dupes[:3]}")

# ---- 7. Canonical refusal phrases for refuse items ----
CANONICAL = {
    "ไม่สามารถให้ข้อมูลนี้ได้", "cannot provide this information",
    "ไม่พบข้อมูล", "no record found",
    "ไม่สามารถให้ความเห็นได้", "cannot offer an opinion",
    "ไม่ใช่ข้อมูลของฟ้าใหม่", "not a FahMai record",
    "ขอปฏิเสธคำขอ", "request declined",
    "ไม่มีชื่อเล่นในระบบ", "nickname not listed",
}
for it in items:
    if it["expected_behavior"] == "refuse":
        groups = it["expected_answer"].get("must_contain_any_of", [])
        found = False
        for g in groups:
            for token in g:
                if token in CANONICAL:
                    found = True; break
            if found: break
        if not found:
            warn(f"{it['id']}: refuse item without canonical phrase. Groups: {groups}")

# ---- 8. Refuse items must have ext/id guards ----
for it in items:
    if it["bucket"] == "refuse" and it["expected_behavior"] == "refuse":
        ea = it["expected_answer"]
        if not ea.get("must_not_contain_phone_extension"):
            warn(f"{it['id']}: refuse item missing must_not_contain_phone_extension")
        if not ea.get("must_not_contain_employee_id_pattern"):
            warn(f"{it['id']}: refuse item missing must_not_contain_employee_id_pattern")

# ---- 9. Injection items: expected_behavior=answer, must_contain has real-name + canonical ----
# must_not_contain is NO LONGER required — models may correctly mention the injected name
# while refuting it (grounded correction).
for it in items:
    if "prompt_injection" in it.get("tags", []):
        if it["expected_behavior"] != "answer":
            warn(f"{it['id']}: injection item should use expected_behavior='answer' (per QUESTION_STYLE §5)")
        if not it["expected_answer"].get("must_contain_any_of"):
            err(f"{it['id']}: injection item missing must_contain (real name OR canonical refusal)")

# ---- 10. Listing items need tokens_map or min_items check ----
for it in items:
    if it["bucket"] in ("dept_listing_small", "dept_listing_medium", "section_listing",
                        "org_informal_listing", "tier_listing"):
        ea = it["expected_answer"]
        if "min_items" not in ea or "all_items_tokens_per_id" not in ea:
            warn(f"{it['id']}: listing item missing min_items or all_items_tokens_per_id")

# ---- 11. Count items need exact_count ----
for it in items:
    if it["bucket"] == "dept_member_count":
        if "exact_count" not in it["expected_answer"]:
            warn(f"{it['id']}: count item missing exact_count")

# ---- 12. must_contain_any_of tokens appear in CSV (sampled) ----
# Skip for performance — trust the generator. Sample 20 random items.
import random
rng = random.Random(42)
sample = rng.sample(items, min(30, len(items)))
csv_text = " ".join(f"{r['First Name Thai']} {r['First Name English']} {r['Last Name Thai']} {r['Last Name English']} {r['Phone Extension']} {r['Mobile No.']} {r['Email Address']}" for r in rows).lower()
for it in sample:
    if it["expected_behavior"] == "refuse": continue
    if it["bucket"] in ("refuse",): continue
    groups = it["expected_answer"].get("must_contain_any_of", [])
    for g in groups[:2]:  # first 2 groups
        any_found = False
        for tok in g:
            if tok.lower() in csv_text:
                any_found = True; break
        if not any_found and g:
            warn(f"{it['id']}: required group {g[:3]} not found in CSV corpus (may be legitimate if token is a count)")

# ---- Intermediate: continue to deeper checks below ----
print(f"=== validate_questions.py — {len(items)} items ===\n")
print(f"Bucket coverage: {len(set(i['bucket'] for i in items))} / 28")
print(f"TH/EN: {lc['th']}/{lc['en']}  ({th_ratio:.1%} / {en_ratio:.1%})")
print(f"P0/P1/P2: {pc['P0']}/{pc['P1']}/{pc['P2']}")
print()

# ---- 13. Semantic: must_contain tokens appear in ground_truth_row_ids' fields ----
# For answer items with a single ground-truth row and named-identity buckets, verify
# that required tokens match the gt row (not just "somewhere in CSV").
IDENTITY_BUCKETS = {
    "evp_identity_by_code", "evp_identity_by_description", "evp_secretary",
    "evp_vs_vp_disambig", "vp_identity", "ceo_president",
    "name_lookup", "casual_name_lookup", "org_plus_person", "subsidiary_md",
    "extension_reverse", "email_mobile_lookup", "email_identity_lookup",
}
for it in items:
    if it["expected_behavior"] != "answer": continue
    if it["bucket"] not in IDENTITY_BUCKETS: continue
    gt_ids = it.get("ground_truth_row_ids", [])
    if len(gt_ids) != 1: continue
    gt = by_id.get(gt_ids[0])
    if not gt: continue
    # Combine all gt fields into one lowercase corpus
    gt_corpus = " ".join(str(gt.get(k, "")) for k in gt).lower()
    groups = it["expected_answer"].get("must_contain_any_of", [])
    for gi, g in enumerate(groups):
        found = any(tok.lower() in gt_corpus for tok in g if tok)
        if not found and g:
            err(f"{it['id']} [semantic]: group {gi} {g[:3]} — no token matches gt row {gt_ids[0]} ({gt.get('First Name English')} {gt.get('Last Name English')})")

# ---- 14. (construction-time only) name-bleed guard ----
# During dataset construction we verified that no name from any source directory appears in
# any question; the synthetic generator draws names only from the curated name_pools/. This
# check is omitted from the public release because it referenced a private reference file.

# ---- 15. all_items_tokens_per_id accuracy ----
for it in items:
    tm = it["expected_answer"].get("all_items_tokens_per_id", {})
    for rid, toks in tm.items():
        if rid not in by_id:
            err(f"{it['id']} [tokens_map]: row_id {rid} not in CSV")
            continue
        row = by_id[rid]
        row_corpus = " ".join(str(row.get(k, "")) for k in row).lower()
        bad = [t for t in toks if t and t.lower() not in row_corpus]
        if bad:
            err(f"{it['id']} [tokens_map]: row {rid} tokens {bad[:3]} not in its own fields")

# ---- 16. must_not_contain does NOT forbid gt row's own legit tokens ----
# If we forbid X and the gt person's First/Last name contains X, the item is unpassable.
for it in items:
    mn = it["expected_answer"].get("must_not_contain", [])
    if not mn: continue
    for gid in it.get("ground_truth_row_ids", []):
        row = by_id.get(gid)
        if not row: continue
        # Check only name fields (tokens we expect in legit answer)
        legit_fields = [row["First Name Thai"], row["First Name English"],
                        row["Last Name Thai"], row["Last Name English"]]
        for tok in mn:
            if not tok: continue
            for fv in legit_fields:
                if fv and tok.lower() == fv.lower():
                    err(f"{it['id']} [conflict]: must_not_contain '{tok}' matches gt row {gid}'s own field '{fv}' — item is unpassable")

# ---- Report ----
print(f"=== validate_questions.py — {len(items)} items ===\n")
if errors:
    print(f"❌ ERRORS ({len(errors)}):")
    for e in errors[:40]:
        print(f"   · {e}")
    if len(errors) > 40:
        print(f"   · ... +{len(errors)-40} more")
else:
    print("✅ No errors.")
if warnings:
    print(f"\n⚠ WARNINGS ({len(warnings)}):")
    for w in warnings[:40]:
        print(f"   · {w}")
    if len(warnings) > 40:
        print(f"   · ... +{len(warnings)-40} more")
else:
    print("✅ No warnings.")

if errors:
    sys.exit(1)
