"""Validate employees.csv against the contracts in DESIGN.md + ORG_CHART.md."""
from __future__ import annotations

import csv, io, re, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CSV_PATH = ROOT / "knowledge_base" / "employees.csv"

with open(CSV_PATH, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

n = len(rows)
errors: list[str] = []
warnings: list[str] = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


# ---- 1. Unique keys ----
ids = [r["Employee ID"] for r in rows]
if len(set(ids)) != n:
    dupes = [i for i, c in Counter(ids).items() if c > 1]
    err(f"Employee ID duplicates: {dupes[:5]}{'...' if len(dupes)>5 else ''}")

emails = [r["Email Address"] for r in rows]
if len(set(emails)) != n:
    dupes = [e for e, c in Counter(emails).items() if c > 1]
    err(f"Email duplicates: {dupes[:5]}{'...' if len(dupes)>5 else ''}")

# ---- 2. ID format ----
for r in rows:
    eid = r["Employee ID"]
    if not (re.fullmatch(r"0000\d{4}", eid) or re.fullmatch(r"08\d{6}", eid)):
        err(f"Bad Employee ID format: {eid} ({r['Unit']})")
        break  # report first

# ---- 3. Extension format ----
for r in rows:
    ext = r["Phone Extension"]
    if ext and not re.fullmatch(r"\d{5}", ext):
        err(f"Bad Phone Extension: '{ext}' ({r['Unit']})")
        break

# ---- 4. Email format ----
for r in rows:
    em = r["Email Address"]
    if not em.endswith("@FAHMAI.CO.TH"):
        err(f"Email not on fahmai.co.th: {em}")
        break

# ---- 5. Blank rate targets (DESIGN.md §3) ----
targets = {
    "Mobile No.": (0.55, 0.03),
    "Nickname Thai": (0.55, 0.05),       # slightly looser
    "Nickname English": (0.55, 0.05),
    "Phone Extension": (0.11, 0.03),
    "Department": (0.05, 0.03),
    "Section": (0.05, 0.03),             # secondment blanks both
}
for col, (target, tol) in targets.items():
    blank = sum(1 for r in rows if not r[col].strip())
    rate = blank / n
    if abs(rate - target) > tol:
        warn(f"Blank rate for '{col}' = {rate:.1%} (target {target:.0%} ± {tol:.0%})")

# ---- 6. Required foundation rows present ----
REQUIRED_UNITS = [
    "CEO", "CEO-EA", "CEO-CoS",
    "CFO", "FIN-EA", "CTO", "TEC-EA", "COO", "OPS-EA",
    "CMO", "MKT-EA", "CPO", "CPO-EA", "CHRO", "HR-EA",
    "FINVP", "TECVP", "MKTVP", "OPSVP", "HRVP", "LEGVP",
    "LOGVP", "SUPVP", "RETVP", "B2BVP",
    "SFVP", "DNVP", "KSVP", "WKVP", "JCVP",
    "TECPM", "MKTDG", "SFDR", "FINFP", "MKTBR",
    "FIN-ACCDR", "FIN-FINDR",
    "SF-GM", "DN-GM", "KS-GM", "WK-GM", "JC-GM",
]
present_units = {r["Unit"] for r in rows}
for u in REQUIRED_UNITS:
    if u not in present_units:
        err(f"Missing required Unit: {u}")

# ---- 7. VP secretaries: one per VP, matching Department ----
vp_units = [u for u in present_units if u in (
    "FINVP", "TECVP", "MKTVP", "OPSVP", "HRVP", "LEGVP",
    "LOGVP", "SUPVP", "RETVP", "B2BVP",
    "SFVP", "DNVP", "KSVP", "WKVP", "JCVP",
    "TECPM", "MKTDG", "SUPCX", "LOGFL", "OPSQA", "RETBKK", "RETUPC", "B2BACC",
    "CEO-CoS",
)]
for vu in vp_units:
    if vu == "CEO-CoS":
        continue  # CoS doesn't have their own secretary
    sec_unit = f"{vu}-SEC"
    if sec_unit not in present_units:
        warn(f"VP {vu} missing secretary row {sec_unit}")

# ---- 8. Planted the source project trap: CFO-EA + CTO-EA both nicknamed มิ้น ----
fin_ea = next((r for r in rows if r["Unit"] == "FIN-EA"), None)
tec_ea = next((r for r in rows if r["Unit"] == "TEC-EA"), None)
if not fin_ea or fin_ea["Nickname Thai"] != "มิ้น":
    err("Planted trap broken: FIN-EA (CFO's EA) does not have nickname มิ้น")
if not tec_ea or tec_ea["Nickname Thai"] != "มิ้น":
    err("Planted trap broken: TEC-EA (CTO's EA) does not have nickname มิ้น")

# ---- 9. Subsidiary-MD rows (5 GMs) ----
gm_rows = [r for r in rows if "GENERAL MANAGER OF" in r["Position in English"]]
if len(gm_rows) < 5:
    err(f"Expected ≥5 subsidiary-MD rows (one per brand), found {len(gm_rows)}")

# ---- 10. Every Unit/Section/Department should be populated (except secondment) ----
for r in rows:
    if not r["Unit"]:
        err(f"Blank Unit for employee {r['Employee ID']}")
        break

# ---- 11. Retail staff must be at non-HQ branches (almost all) ----
ret_at_hq = sum(1 for r in rows if r["Department"] == "RET" and r["Branch"] == "BKK-R9")
if ret_at_hq > 20:
    warn(f"{ret_at_hq} RET employees at BKK-R9 — should be mostly at branches")

# ---- 12. Surname uniqueness (Gate H.1 — 95-98% unique) ----
surnames = [r["Last Name Thai"] for r in rows]
unique_sn = len(set(surnames))
rate = unique_sn / n
if not (0.95 <= rate <= 0.98):
    err(f"Surname uniqueness = {rate:.3f} (target 0.95–0.98). "
        f"Unique: {unique_sn} / {n}")
shared = Counter(surnames)
family_clusters = sum(1 for v in shared.values() if v >= 2)
family_rows = sum(v for v in shared.values() if v >= 2)
oversized = [(k, v) for k, v in shared.items() if v > 4]
if oversized:
    warn(f"{len(oversized)} surname(s) held by > 4 people — family clusters "
         f"should stay 2–4 rows. Largest: {oversized[0]}")

# ---- Report ----
print(f"=== validate_csv.py — {n} rows ===\n")
if errors:
    print(f"❌ ERRORS ({len(errors)}):")
    for e in errors:
        print(f"   · {e}")
else:
    print("✅ No errors.")
if warnings:
    print(f"\n⚠ WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"   · {w}")
else:
    print("✅ No warnings.")

# Summary stats
print(f"\n--- Stats ---")
print(f"Unique Employee IDs: {len(set(ids))} / {n}")
print(f"Unique Emails:       {len(set(emails))} / {n}")
print(f"Unique Unit codes:   {len(present_units)}")
print(f"Unique Department codes: {len(set(r['Department'] for r in rows if r['Department']))}")
print(f"Unique Section codes:    {len(set(r['Section'] for r in rows if r['Section']))}")
print(f"Unique Surnames (TH):    {unique_sn} / {n}  ({100*unique_sn/n:.1f}%)")
print(f"Family clusters (2+):    {family_clusters}  ({family_rows} rows shared)")

if errors:
    sys.exit(1)
