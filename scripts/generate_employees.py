"""Generate FahMai synthetic employee CSV.

Two modes:
  --mode sample  →  50-row curated sample hitting all adversarial patterns (Gate C)
  --mode full    →  ~2,000-row full directory (Gate D)

Both modes share the same row-construction logic. Determinism: single seed
baked at the top; same seed → byte-identical CSV.

The sample mode hard-codes ~50 specific rows to exercise every question bucket
at small scale (CEO, EA-twins-with-same-nickname, SFVP/SFDR adversarial pair,
branch variety, blank-rate illustration). The full mode generates organically
by allocating headcounts per department/level then filling.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
POOLS = ROOT / "name_pools"
KB = ROOT / "knowledge_base"
KB.mkdir(parents=True, exist_ok=True)

SEED = 20260419


# ============================================================================
# Column schema — canonical order matches DESIGN.md §3
# ============================================================================
COLS = [
    "Employee ID",
    "Department",
    "Section",
    "Unit",
    "Position in Thai",
    "Position in English",
    "First Name Thai",
    "Last Name Thai",
    "First Name English",
    "Last Name English",
    "Nickname Thai",
    "Nickname English",
    "Email Address",
    "Phone Extension",
    "Mobile No.",
    "Office Location",
    "Branch",
    "Start Year",
    "Position Level",
]


# ============================================================================
# Branch → extension prefix + office location defaults
# ============================================================================
BRANCH_META = {
    "BKK-R9":   {"ext_prefix": "7", "office_prefix": "FahMai Tower"},
    "BKK-SIAM": {"ext_prefix": "1", "office_prefix": "สาขาสยาม"},
    "BKK-LP":   {"ext_prefix": "2", "office_prefix": "สาขาลาดพร้าว"},
    "BKK-BNA":  {"ext_prefix": "3", "office_prefix": "สาขาบางนา"},
    "BKK-PKT":  {"ext_prefix": "4", "office_prefix": "คลังบางพลี"},
    "CNX":      {"ext_prefix": "5", "office_prefix": "สาขาเชียงใหม่"},
    "KKN":      {"ext_prefix": "6", "office_prefix": "สาขาขอนแก่น"},
    "NMA":      {"ext_prefix": "8", "office_prefix": "สาขาโคราช"},
    "CBI":      {"ext_prefix": "9", "office_prefix": "สาขาชลบุรี"},
    "HKT":      {"ext_prefix": "0", "office_prefix": "สาขาภูเก็ต"},
    "HDY":      {"ext_prefix": "5", "office_prefix": "สาขาหาดใหญ่"},
    "REMOTE":   {"ext_prefix": None, "office_prefix": "ทำงานทางไกล"},
}


# ============================================================================
# Load name pools
# ============================================================================
def load_pools():
    first = json.load(open(POOLS / "first_names_th.json", encoding="utf-8"))["items"]
    last = json.load(open(POOLS / "last_names_th.json", encoding="utf-8"))["items"]
    nicks = json.load(open(POOLS / "nicknames_th.json", encoding="utf-8"))["items"]
    variants = json.load(open(POOLS / "nickname_variants.json", encoding="utf-8"))["variants"]
    return first, last, nicks, variants


# ============================================================================
# Small helpers
# ============================================================================
def pick_first(rng, first_pool, gender=None):
    if gender:
        pool = [x for x in first_pool if x["gender"] in (gender, "u")]
    else:
        pool = first_pool
    return rng.choice(pool)


def pick_last(rng, last_pool):
    return rng.choice(last_pool)


# How commonly each nickname CATEGORY appears in real Thai offices.
# Weights are relative — classic & nature & soft are most common; weird /
# doubled / one-off brand names are rare (only a handful of employees).
NICK_CATEGORY_WEIGHTS = {
    "classic":   10,   # นัต, บี, ต้อม, ตูน, ปิ๊ง — traditional single-syllable
    "nature":     8,   # ฟ้า, ฝน, ดาว, น้ำ, พลอย, มุก — extremely common
    "soft":       7,   # อ้อม, ออม, นิว, แพร — common
    "modern":     6,   # Mint, Ice, Bank, Boss, Film, Golf, Beam — common English-loan
    "animal":     5,   # หมู, นก, ไก่ — real but less frequent than classic
    "food":       4,   # เค้ก, ส้ม, พีช — OK, not dominant
    "teen":       4,   # บูม, ซัน, เคน — OK
    "aesthetic":  2,   # Pimmada, Lalin — rarer
    "weird":      1,   # IBM, Porsche, Nestle — very rare
    "doubled":    1,   # ดีดี, กีกี, โอ้โอ้ — rare
}


def pick_nickname(rng, nicks_pool, blank_prob=0.55):
    if rng.random() < blank_prob:
        return None
    weights = [NICK_CATEGORY_WEIGHTS.get(n.get("category", ""), 3) for n in nicks_pool]
    return rng.choices(nicks_pool, weights=weights, k=1)[0]


def make_employee_id(rng, start_year: int, used: set) -> str:
    """Pre-2020: 0000####; 2020+: 08######."""
    while True:
        if start_year < 2020:
            eid = f"0000{rng.randint(1000, 9999):04d}"
        else:
            eid = f"08{rng.randint(100000, 999999):06d}"
        if eid not in used:
            used.add(eid)
            return eid


def make_email(first_en: str, last_en: str, used: set) -> str:
    """<FIRST>.<FIRSTLETTEROFLAST>@FAHMAI.CO.TH. Suffix digit on collision."""
    base = f"{first_en}.{last_en[:2]}@FAHMAI.CO.TH".upper()
    if base not in used:
        used.add(base)
        return base
    for i in range(2, 999):
        alt = f"{first_en}.{last_en[:2]}{i}@FAHMAI.CO.TH".upper()
        if alt not in used:
            used.add(alt)
            return alt
    raise RuntimeError("email collision overflow")


# ============================================================================
# Surname polish (Gate H.1) — extended pool + family clusters
# ============================================================================
#
# Real Thai surnames are typically 2–3 morpheme compounds, almost always
# unique to each family (per the 1913 Surname Act). The 147-item curated pool
# in `name_pools/last_names_th.json` is too small for a 2,000-row directory
# (natural re-use → ~7% uniqueness). We synthesise a ~2,000+ pool from
# Sanskrit/Pali morphemes so that 95–98% of employees can receive a unique
# surname; the remaining 2–5% are deliberate family clusters (shared surname
# → implicit sibling / spouse / parent-child relationship inside FahMai).
#
# Applied as a POST-PROCESSING pass after gen_full() so that Employee IDs,
# Units, branches, extensions stay byte-identical to the pre-polish CSV —
# only Last Name Thai/English and Email Address change.

SURNAME_PREFIXES = [
    ("เกียรติ", "Kiat"),   ("ศรี", "Sri"),        ("อภิ", "Aphi"),
    ("ธน", "Thana"),       ("จิร", "Chira"),       ("ราช", "Raj"),
    ("เทพ", "Thep"),       ("สัม", "Sam"),         ("วิศ", "Wis"),
    ("อัคร", "Akara"),      ("อนุ", "Anu"),         ("ประ", "Pra"),
    ("สุ", "Su"),           ("พิ", "Phi"),          ("มณี", "Mani"),
    ("ชัย", "Chai"),        ("มหา", "Maha"),        ("อธิ", "Athi"),
    ("ภัทร", "Phat"),       ("อมร", "Amon"),        ("รัตน", "Ratana"),
    ("วัชร", "Watchara"),   ("สุวรรณ", "Suwan"),    ("จันท", "Chan"),
    ("สม", "Som"),          ("พรหม", "Phrom"),      ("นรา", "Nara"),
    ("พง", "Phong"),        ("เกษม", "Kasem"),      ("บุญ", "Bun"),
]

SURNAME_SUFFIXES = [
    ("กุล", "kun"),         ("วงศ์", "wong"),        ("วงษ์", "wongs"),
    ("ศรี", "si"),          ("ทอง", "thong"),        ("ชัย", "chai"),
    ("สุข", "suk"),         ("ดี", "di"),            ("เจริญ", "charoen"),
    ("พัฒน์", "phat"),       ("รัตน์", "rat"),         ("สว่าง", "sawang"),
    ("มณี", "mani"),        ("งาม", "ngam"),         ("บุญ", "bun"),
    ("ใจ", "jai"),          ("นาม", "nam"),          ("พงศ์", "phong"),
    ("กำจร", "kamchon"),    ("เฉลิม", "chaloem"),    ("โชติ", "chot"),
    ("พิทักษ์", "phithak"),   ("ภิญโญ", "phinyo"),    ("เสริม", "soem"),
    ("ประเสริฐ", "prasert"), ("วัฒน์", "wat"),         ("สถิต", "sathit"),
    ("รักษา", "raksa"),     ("สินธุ์", "sin"),         ("ฟ้า", "fa"),
]


def build_extended_surname_pool(base_pool):
    """Return ~2,000+ unique synthetic Thai compound surnames.

    Strategy: seed with the 147 curated real-looking surnames, then compound
    morpheme prefixes × suffixes × base names to produce a deeper pool.
    Deduped by Thai form, capped at 14 Thai characters for readability.
    """
    pool = []
    seen = set()

    def add(th, en):
        if th in seen or len(th) > 14:
            return
        seen.add(th)
        pool.append({"th": th, "en": en.upper()})

    for item in base_pool:
        add(item["th"], item["en"])

    for p_th, p_en in SURNAME_PREFIXES:
        for s_th, s_en in SURNAME_SUFFIXES:
            add(p_th + s_th, p_en + s_en)

    for p_th, p_en in SURNAME_PREFIXES:
        for item in base_pool[:60]:
            add(p_th + item["th"], p_en + item["en"].lower())

    for item in base_pool[:60]:
        for s_th, s_en in SURNAME_SUFFIXES:
            add(item["th"] + s_th, item["en"] + s_en)

    return pool


def apply_surname_polish(rows, base_pool, seed=SEED + 1,
                         n_clusters=30,
                         cluster_size_weights=(0.70, 0.25, 0.05)):
    """Post-process: give each row a unique surname from the extended pool,
    then plant family clusters (2–4 rows sharing a surname).

    Mutates rows in place. Only modifies Last Name Thai/English + Email
    Address — Employee IDs, positions, branches, extensions stay byte-stable.

    Target: 95–98 % unique surnames. Default 30 clusters with 70/25/5
    pair/trio/quad mix → ~70 shared rows → ~96.5% unique on 1995 rows.
    """
    rng = random.Random(seed)
    pool = build_extended_surname_pool(base_pool)
    rng.shuffle(pool)

    n = len(rows)
    if len(pool) < n + 100:
        raise RuntimeError(
            f"Extended surname pool too small ({len(pool)}) for {n} rows"
        )

    # Phase 1 — every row gets a unique surname + regenerated email
    used_emails: set[str] = set()
    for i, r in enumerate(rows):
        sn = pool[i]
        r["Last Name Thai"] = sn["th"]
        r["Last Name English"] = sn["en"]
        r["Email Address"] = make_email(r["First Name English"], sn["en"], used_emails)

    # Phase 2 — plant family clusters (reassign siblings' surnames to match)
    # Candidates: mid-rank rows, not EAs or VP-secretaries (those are role-slotted,
    # not family rows). C-level and VP kept unique — no "CEO and CFO are siblings".
    candidate_idxs = [
        i for i, r in enumerate(rows)
        if r["Position Level"] in ("IC", "Lead", "Manager", "Director")
        and not r["Unit"].endswith("-EA")
        and not r["Unit"].endswith("-SEC")
    ]
    rng.shuffle(candidate_idxs)

    cumulative_weights = []
    acc = 0.0
    for w in cluster_size_weights:
        acc += w
        cumulative_weights.append(acc)

    def pick_cluster_size():
        r = rng.random()
        for size, cw in enumerate(cumulative_weights, start=2):
            if r < cw:
                return size
        return 2

    ci = 0
    planted = []
    for _ in range(n_clusters):
        size = pick_cluster_size()
        if ci + size > len(candidate_idxs):
            break
        anchor = candidate_idxs[ci]
        family_th = rows[anchor]["Last Name Thai"]
        family_en = rows[anchor]["Last Name English"]
        members = [anchor]
        for j in range(1, size):
            target = candidate_idxs[ci + j]
            rows[target]["Last Name Thai"] = family_th
            rows[target]["Last Name English"] = family_en
            rows[target]["Email Address"] = make_email(
                rows[target]["First Name English"], family_en, used_emails)
            members.append(target)
        planted.append((family_th, [rows[i]["Employee ID"] for i in members]))
        ci += size

    return planted


def make_extension(rng, branch: str, used: set) -> str | None:
    """5-digit, branch-prefixed. Blank for REMOTE and ~5% field staff."""
    if branch == "REMOTE":
        return None
    prefix = BRANCH_META[branch]["ext_prefix"]
    for _ in range(50):
        ext = prefix + f"{rng.randint(1000, 9999):04d}"
        if ext not in used:
            used.add(ext)
            return ext
    raise RuntimeError("extension collision")


def make_mobile(rng, blank_prob=0.55) -> str | None:
    if rng.random() < blank_prob:
        return None
    p = rng.choice(["08", "09", "06"])
    return f"{p}{rng.randint(10000000, 99999999)}".replace(
        f"{p}", f"{p}-", 1
    )  # ensure format 08X-XXXXXXX ...
    # simpler:


def make_mobile_clean(rng, blank_prob=0.55) -> str | None:
    if rng.random() < blank_prob:
        return None
    prefix = rng.choice(["081", "082", "083", "084", "085", "086", "087", "088", "089",
                         "091", "092", "093", "094", "095", "096", "097", "098", "099",
                         "061", "062", "063", "064", "065", "066", "067", "068"])
    mid = f"{rng.randint(0, 999):03d}"
    last = f"{rng.randint(0, 9999):04d}"
    return f"{prefix}-{mid}-{last}"


def start_year_for_level(rng, level: str) -> int:
    """Senior tiers hired earlier."""
    if level == "C-level":
        return rng.choice([2015, 2016, 2017, 2017, 2018, 2018, 2019])
    if level == "VP":
        return rng.choice([2015, 2016, 2017, 2018, 2018, 2019, 2019, 2020, 2020, 2021])
    if level == "Director":
        return rng.choice([2016, 2017, 2018, 2019, 2019, 2020, 2020, 2021, 2022, 2022])
    if level == "Manager":
        return rng.choice([2018, 2019, 2020, 2020, 2021, 2021, 2022, 2022, 2023, 2024])
    if level == "Lead":
        return rng.choice([2019, 2020, 2021, 2022, 2022, 2023, 2024, 2024, 2025])
    # IC
    return rng.choice([2020, 2021, 2022, 2022, 2023, 2023, 2024, 2024, 2025, 2025])


def senior_nickname_blank(level: str) -> float:
    """C-level / VP blank at higher rate than ICs."""
    return {"C-level": 0.75, "VP": 0.70, "Director": 0.60, "Manager": 0.55,
            "Lead": 0.52, "IC": 0.50}.get(level, 0.55)


# ============================================================================
# Sample (50-row curated) — hits every adversarial pattern
# Each spec: (unit, pos_th, pos_en, dept, section, branch, level,
#             gender_hint, nickname_override, first_override, start_year_override)
# None for fields means random.
# ============================================================================
SAMPLE_SPECS = [
    # --- CEO tier (3) ---
    ("CEO", "ประธานเจ้าหน้าที่บริหาร", "CHIEF EXECUTIVE OFFICER",
     "CEO", "CEO-OFF", "BKK-R9", "C-level", "m", None, None, 2016),
    ("CEO-EA", "เลขานุการของ CEO", "EXECUTIVE ASSISTANT TO CEO",
     "CEO", "CEO-OFF", "BKK-R9", "Manager", "f", None, None, None),
    ("CEO-CoS", "หัวหน้าสำนักงานประธาน", "CHIEF OF STAFF",
     "CEO", "CEO-OFF", "BKK-R9", "VP", "m", None, None, None),

    # --- C-suite + EA twins with SAME NICKNAME มิ้น (adversarial) ---
    ("CFO", "ประธานเจ้าหน้าที่การเงิน", "CHIEF FINANCIAL OFFICER",
     "FIN", "FIN-EXEC", "BKK-R9", "C-level", "f", None, None, None),
    ("FIN-EA", "เลขานุการของ CFO", "EXECUTIVE ASSISTANT TO CFO",
     "FIN", "FIN-EXEC", "BKK-R9", "Manager", "f", ("มิ้น", "MINT"), None, None),

    ("CTO", "ประธานเจ้าหน้าที่เทคโนโลยี", "CHIEF TECHNOLOGY OFFICER",
     "TEC", "TEC-EXEC", "BKK-R9", "C-level", "m", None, None, None),
    ("TEC-EA", "เลขานุการของ CTO", "EXECUTIVE ASSISTANT TO CTO",
     "TEC", "TEC-EXEC", "BKK-R9", "Manager", "f", ("มิ้น", "MINT"), None, None),  # ← SAME nickname as FIN-EA

    ("CMO", "ประธานเจ้าหน้าที่การตลาด", "CHIEF MARKETING OFFICER",
     "MKT", "MKT-EXEC", "BKK-R9", "C-level", "f", None, None, None),
    ("MKT-EA", "เลขานุการของ CMO", "EXECUTIVE ASSISTANT TO CMO",
     "MKT", "MKT-EXEC", "BKK-R9", "Manager", "f", None, None, None),

    ("CPO", "ประธานเจ้าหน้าที่ฝ่ายผลิตภัณฑ์", "CHIEF PRODUCT OFFICER",
     "SF", "SF-EXEC", "BKK-R9", "C-level", "m", None, None, None),

    # --- SaiFah division: SFVP vs SFDR adversarial pair ---
    ("SFVP", "รองประธานฝ่ายสายฟ้า", "VICE PRESIDENT OF SAIFAH",
     "SF", "SF-PD", "BKK-R9", "VP", "m", None, None, None),
    ("SFDR", "ผู้อำนวยการฝ่ายปฏิบัติการสายฟ้า", "DIRECTOR OF SAIFAH OPERATIONS",
     "SF", "SF-OPS", "BKK-R9", "Director", "f", None, None, None),
    ("SFVP-SEC", "เลขานุการของ SFVP", "SECRETARY OF SAIFAH VP",
     "SF", "SF-PD", "BKK-R9", "Manager", "f", None, None, None),
    ("SF-GM", "ผู้จัดการทั่วไปแบรนด์สายฟ้า", "GENERAL MANAGER OF SAIFAH",
     "SF", "SF-PD", "BKK-R9", "Director", "m", None, None, None),

    # --- Finance: FINVP vs FINFP + AP/AR managers ---
    ("FINVP", "รองประธานฝ่ายการเงิน", "VICE PRESIDENT FINANCE",
     "FIN", "FIN-FP", "BKK-R9", "VP", "m", None, None, None),
    ("FINFP", "ผู้อำนวยการฝ่ายการเงินและวางแผน", "DIRECTOR FINANCIAL PLANNING",
     "FIN", "FIN-FP", "BKK-R9", "Director", "f", None, None, None),
    ("FIN-AP-MGR", "ผู้จัดการฝ่ายบัญชีเจ้าหนี้", "ACCOUNTS PAYABLE MANAGER",
     "FIN", "FIN-AP", "BKK-R9", "Manager", "f", None, None, None),
    ("FIN-AR-MGR", "ผู้จัดการฝ่ายบัญชีลูกหนี้", "ACCOUNTS RECEIVABLE MANAGER",
     "FIN", "FIN-AR", "BKK-R9", "Manager", "m", None, None, None),

    # --- Thai-position-text near-miss pair (DESIGN.md) ---
    ("FIN-ACCDR", "ผู้อำนวยการฝ่ายบัญชี", "DIRECTOR ACCOUNTING",
     "FIN", "FIN-GL", "BKK-R9", "Director", "f", None, None, None),
    ("FIN-FINDR", "ผู้อำนวยการฝ่ายการเงิน", "DIRECTOR FINANCE",
     "FIN", "FIN-TR", "BKK-R9", "Director", "m", None, None, None),

    # --- HR (2) ---
    ("HRVP", "รองประธานฝ่ายทรัพยากรบุคคล", "VICE PRESIDENT HUMAN RESOURCES",
     "HR", "HR-OPS", "BKK-R9", "VP", "f", None, None, None),
    ("HR-TA-MGR", "ผู้จัดการฝ่ายสรรหาบุคลากร", "TALENT ACQUISITION MANAGER",
     "HR", "HR-TA", "BKK-R9", "Manager", "m", None, None, None),

    # --- Tech: TECVP vs TECPM + BE/MOB teams ---
    ("TECVP", "รองประธานฝ่ายเทคโนโลยี", "VICE PRESIDENT TECHNOLOGY",
     "TEC", "TEC-PLT", "BKK-R9", "VP", "m", None, None, None),
    ("TECPM", "รองประธานฝ่ายแพลตฟอร์ม", "VICE PRESIDENT PLATFORM",
     "TEC", "TEC-PLT", "BKK-R9", "VP", "m", None, None, None),
    ("TEC-BE-LEAD", "หัวหน้าทีมหลังบ้าน", "BACKEND ENGINEERING LEAD",
     "TEC", "TEC-BE", "BKK-R9", "Lead", "m", None, None, None),
    ("TEC-BE-1", "วิศวกรซอฟต์แวร์", "BACKEND SOFTWARE ENGINEER",
     "TEC", "TEC-BE", "BKK-R9", "IC", "m", None, None, None),
    ("TEC-BE-2", "วิศวกรซอฟต์แวร์", "BACKEND SOFTWARE ENGINEER",
     "TEC", "TEC-BE", "REMOTE", "IC", "f", None, None, None),
    ("TEC-MOB-LEAD", "หัวหน้าทีมโมบาย", "MOBILE ENGINEERING LEAD",
     "TEC", "TEC-MOB", "BKK-R9", "Lead", "f", None, None, None),
    ("TEC-MOB-1", "วิศวกรโมบาย", "MOBILE SOFTWARE ENGINEER",
     "TEC", "TEC-MOB", "BKK-R9", "IC", "m", None, None, None),

    # --- Marketing: MKTVP vs MKTBR (note: CMO above has same initial) ---
    ("MKTVP", "รองประธานฝ่ายการตลาด", "VICE PRESIDENT MARKETING",
     "MKT", "MKT-BR", "BKK-R9", "VP", "f", None, None, None),
    ("MKTBR", "ผู้อำนวยการฝ่ายแบรนด์", "DIRECTOR BRAND",
     "MKT", "MKT-BR", "BKK-R9", "Director", "f", None, None, None),
    ("MKT-DIG-MGR", "ผู้จัดการฝ่ายการตลาดดิจิทัล", "DIGITAL MARKETING MANAGER",
     "MKT", "MKT-DIG", "BKK-R9", "Manager", "m", None, None, None),
    ("MKT-DIG-1", "นักการตลาดดิจิทัล", "DIGITAL MARKETING SPECIALIST",
     "MKT", "MKT-DIG", "REMOTE", "IC", "f", None, None, None),

    # --- Support ---
    ("SUP-CHAT-LEAD", "หัวหน้าทีมแชทลูกค้า", "CHAT SUPPORT LEAD",
     "SUP", "SUP-CHAT", "BKK-R9", "Lead", "f", None, None, None),
    ("SUP-CHAT-1", "เจ้าหน้าที่แชทลูกค้า", "CHAT SUPPORT AGENT",
     "SUP", "SUP-CHAT", "BKK-R9", "IC", "f", None, None, None),
    ("SUP-CHAT-2", "เจ้าหน้าที่แชทลูกค้า", "CHAT SUPPORT AGENT",
     "SUP", "SUP-CHAT", "BKK-R9", "IC", "m", ("ไอซ์", "ICE"), None, None),

    # --- Retail: Siam branch manager + ICs ---
    ("RET-BKK-SIAM-MGR", "ผู้จัดการสาขาสยาม", "SIAM BRANCH MANAGER",
     "RET", "RET-BKK-SIAM", "BKK-SIAM", "Manager", "m", None, None, None),
    ("RET-BKK-SIAM-1", "พนักงานขาย", "RETAIL SALES ASSOCIATE",
     "RET", "RET-BKK-SIAM", "BKK-SIAM", "IC", "f", None, None, None),
    ("RET-BKK-SIAM-2", "ช่างซ่อม", "SERVICE TECHNICIAN",
     "RET", "RET-BKK-SIAM", "BKK-SIAM", "IC", "m", ("ไอซ์", "ICE"), None, None),

    # --- Retail: Chiang Mai branch ---
    ("RET-CNX-MGR", "ผู้จัดการสาขาเชียงใหม่", "CHIANG MAI BRANCH MANAGER",
     "RET", "RET-CNX", "CNX", "Manager", "f", None, None, None),
    ("RET-CNX-1", "พนักงานขาย", "RETAIL SALES ASSOCIATE",
     "RET", "RET-CNX", "CNX", "IC", "m", None, None, None),

    # --- B2B ---
    ("B2B-SLS-DR", "ผู้อำนวยการฝ่ายขายองค์กร", "B2B SALES DIRECTOR",
     "B2B", "B2B-SLS", "BKK-R9", "Director", "m", None, None, None),
    ("B2B-SLS-1", "ผู้แทนขายองค์กร", "B2B SALES REPRESENTATIVE",
     "B2B", "B2B-SLS", "BKK-R9", "IC", "f", None, None, None),

    # --- Logistics ---
    ("LOG-WH-LEAD", "หัวหน้าทีมคลังสินค้า", "WAREHOUSE LEAD",
     "LOG", "LOG-WH", "BKK-PKT", "Lead", "m", None, None, None),
    ("LOG-WH-1", "พนักงานคลังสินค้า", "WAREHOUSE ASSOCIATE",
     "LOG", "LOG-WH", "BKK-PKT", "IC", "m", None, None, None),
    ("LOG-WH-2", "พนักงานคลังสินค้า", "WAREHOUSE ASSOCIATE",
     "LOG", "LOG-WH", "BKK-PKT", "IC", "f", None, None, None),

    # --- Ops ---
    ("OPS-FAC-MGR", "ผู้จัดการฝ่ายอาคารสถานที่", "FACILITIES MANAGER",
     "OPS", "OPS-FAC", "BKK-R9", "Manager", "m", None, None, None),

    # --- Legal ---
    ("LEG-CNT-LEAD", "หัวหน้าทีมนิติกรรม", "CONTRACTS LEAD",
     "LEG", "LEG-CNT", "BKK-R9", "Lead", "f", None, None, None),

    # --- DaoNuea brand GM (subsidiary_md pattern) ---
    ("DN-GM", "ผู้จัดการทั่วไปแบรนด์ดาวเหนือ", "GENERAL MANAGER OF DAONUEA",
     "DN", "DN-PD", "BKK-R9", "Director", "m", None, None, None),

    # --- Extra IC (plain random — nickname+name-combo cases are generated at Gate F) ---
    ("TEC-DS-1", "นักวิทยาศาสตร์ข้อมูล", "DATA SCIENTIST",
     "TEC", "TEC-DS", "BKK-R9", "IC", "m", None, None, None),
]


# ============================================================================
# Row builder (shared by sample + full)
# ============================================================================
def build_row(rng, spec, first_pool, last_pool, nicks_pool,
              used_ids, used_emails, used_exts) -> dict:
    (unit, pos_th, pos_en, dept, section, branch, level,
     gender, nick_override, first_override, sy_override) = spec

    # name
    if first_override:
        first_th, first_en = first_override
    else:
        f = pick_first(rng, first_pool, gender)
        first_th, first_en = f["th"], f["en"]
    l = pick_last(rng, last_pool)
    last_th, last_en = l["th"], l["en"]

    # nickname
    if nick_override is not None:
        nick_th, nick_en = nick_override
    else:
        blank_p = senior_nickname_blank(level)
        n = pick_nickname(rng, nicks_pool, blank_prob=blank_p)
        if n is None:
            nick_th = nick_en = ""
        else:
            nick_th, nick_en = n["th"], n["en"]

    # start year + id
    sy = sy_override if sy_override else start_year_for_level(rng, level)
    eid = make_employee_id(rng, sy, used_ids)

    # email
    email = make_email(first_en, last_en, used_emails)

    # extension (blank for REMOTE + ~5% field staff)
    if branch == "REMOTE":
        ext = ""
    elif rng.random() < 0.05 and level == "IC":
        ext = ""
    else:
        ext = make_extension(rng, branch, used_exts) or ""

    # mobile (55% blank globally)
    mobile = make_mobile_clean(rng, blank_prob=0.55) or ""

    # office location
    office = BRANCH_META[branch]["office_prefix"]
    if branch == "BKK-R9":
        office = f"FahMai Tower {rng.randint(3, 28)}F"

    return {
        "Employee ID": eid,
        "Department": dept,
        "Section": section or "",
        "Unit": unit,
        "Position in Thai": pos_th,
        "Position in English": pos_en,
        "First Name Thai": first_th,
        "Last Name Thai": last_th,
        "First Name English": first_en,
        "Last Name English": last_en,
        "Nickname Thai": nick_th,
        "Nickname English": nick_en,
        "Email Address": email,
        "Phone Extension": ext,
        "Mobile No.": mobile,
        "Office Location": office,
        "Branch": branch,
        "Start Year": sy,
        "Position Level": level,
    }


# ============================================================================
# Mode: sample
# ============================================================================
def gen_sample():
    first_pool, last_pool, nicks_pool, variants = load_pools()
    rng = random.Random(SEED)

    used_ids, used_emails, used_exts = set(), set(), set()
    rows = []
    for spec in SAMPLE_SPECS:
        rows.append(build_row(rng, spec, first_pool, last_pool, nicks_pool,
                              used_ids, used_emails, used_exts))
    return rows


# ============================================================================
# Write + summarize
# ============================================================================
def write_csv(rows, path: Path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)


def summarize(rows):
    print(f"Rows: {len(rows)}\n")
    print("By Department:")
    for d, n in Counter(r["Department"] for r in rows).most_common():
        print(f"  {d:>6}  {n}")
    print("\nBy Position Level:")
    for l, n in Counter(r["Position Level"] for r in rows).most_common():
        print(f"  {l:<10}  {n}")
    print("\nBy Branch:")
    for b, n in Counter(r["Branch"] for r in rows).most_common():
        print(f"  {b:<10}  {n}")

    blank_nick = sum(1 for r in rows if not r["Nickname Thai"])
    blank_mob = sum(1 for r in rows if not r["Mobile No."])
    blank_ext = sum(1 for r in rows if not r["Phone Extension"])
    n = len(rows)
    print(f"\nBlank rates:")
    print(f"  Nickname:   {blank_nick}/{n} ({100*blank_nick/n:.0f}%)")
    print(f"  Mobile:     {blank_mob}/{n} ({100*blank_mob/n:.0f}%)")
    print(f"  Extension:  {blank_ext}/{n} ({100*blank_ext/n:.0f}%)")

    # Planted check: two EAs with nickname มิ้น
    mints = [r for r in rows if r["Nickname Thai"] == "มิ้น"]
    print(f"\nPlanted 'มิ้น' secretaries (the source project trap): {len(mints)}")
    for r in mints:
        print(f"  {r['Unit']:<12} {r['Position in English'][:40]:<40} {r['First Name English']} {r['Last Name English']}")

    # Planted: two with nickname ไอซ์ (ambiguous-nickname seed)
    ices = [r for r in rows if r["Nickname Thai"] == "ไอซ์"]
    print(f"\nPlanted 'ไอซ์' ambiguous seed: {len(ices)}")
    for r in ices:
        print(f"  {r['Unit']:<12} {r['First Name English']} {r['Last Name English']}  ({r['Department']})")

    # Surname uniqueness (Gate H.1)
    surnames = [r["Last Name Thai"] for r in rows]
    unique = len(set(surnames))
    shared = Counter(surnames)
    n_shared_rows = sum(v for v in shared.values() if v >= 2)
    n_clusters = sum(1 for v in shared.values() if v >= 2)
    print(f"\nSurname uniqueness:")
    print(f"  {unique} / {n} unique ({100*unique/n:.1f}%)")
    print(f"  Family clusters (2+ holders): {n_clusters} — {n_shared_rows} rows shared")
    top = shared.most_common(5)
    for k, v in top[:5]:
        if v >= 2:
            print(f"     {k}: {v}")


# ============================================================================
# Mode: full (Gate D)
# ============================================================================
# Per-department total headcount targets (sums to ~1,995, plus 8 exec = 2,003)
DEPT_TARGETS = {
    "TEC": 240, "SUP": 200, "RET": 380, "LOG": 180, "MKT": 110,
    "SF": 140, "DN": 130, "OPS": 120, "KS": 100, "FIN": 90,
    "WK": 80, "JC": 80, "B2B": 60, "HR": 50, "LEG": 25, "CEO": 10,
}

# Sections per department (full glossary from ORG_CHART.md)
DEPT_SECTIONS = {
    "CEO": ["CEO-OFF", "CEO-SEC", "CEO-STR"],
    "FIN": ["FIN-EXEC", "FIN-AP", "FIN-AR", "FIN-GL", "FIN-FP", "FIN-TR", "FIN-TAX"],
    "HR":  ["HR-EXEC", "HR-TA", "HR-LD", "HR-OPS", "HR-COMP", "HR-CUL"],
    "LEG": ["LEG-CNT", "LEG-IP", "LEG-COM"],
    "MKT": ["MKT-EXEC", "MKT-BR", "MKT-DIG", "MKT-CON", "MKT-PR", "MKT-CRM", "MKT-EVT"],
    "TEC": ["TEC-EXEC", "TEC-BE", "TEC-FE", "TEC-MOB", "TEC-DS", "TEC-SEC", "TEC-INF", "TEC-PLT", "TEC-QA", "TEC-DATA"],
    "OPS": ["OPS-EXEC", "OPS-FAC", "OPS-PROC", "OPS-PMO", "OPS-ADM", "OPS-TRV"],
    "LOG": ["LOG-WH", "LOG-SHP", "LOG-INV", "LOG-RET", "LOG-FLT"],
    "SUP": ["SUP-CHAT", "SUP-PHN", "SUP-EML", "SUP-TECH", "SUP-ESC", "SUP-TRN"],
    "RET": ["RET-HQ", "RET-BKK-SIAM", "RET-BKK-LP", "RET-BKK-BNA", "RET-CNX", "RET-KKN", "RET-NMA", "RET-CBI", "RET-HKT", "RET-HDY", "RET-TRN"],
    "B2B": ["B2B-SLS", "B2B-ACC", "B2B-SOL", "B2B-SUP"],
    "SF":  ["SF-EXEC", "SF-PD", "SF-ENG", "SF-OPS", "SF-MKT"],
    "DN":  ["DN-PD", "DN-ENG", "DN-OPS", "DN-MKT"],
    "KS":  ["KS-PD", "KS-ENG", "KS-OPS", "KS-MKT"],
    "WK":  ["WK-PD", "WK-ENG", "WK-OPS", "WK-MKT"],
    "JC":  ["JC-PD", "JC-ENG", "JC-OPS", "JC-MKT"],
}

# Branch weights per department (dict of branch → relative weight)
DEPT_BRANCH_WEIGHTS = {
    # Corporate → mostly HQ with some remote
    "CEO": {"BKK-R9": 100},
    "FIN": {"BKK-R9": 95, "REMOTE": 5},
    "HR":  {"BKK-R9": 95, "REMOTE": 5},
    "LEG": {"BKK-R9": 100},
    "MKT": {"BKK-R9": 75, "REMOTE": 20, "BKK-SIAM": 3, "BKK-LP": 2},
    "TEC": {"BKK-R9": 70, "REMOTE": 25, "CNX": 3, "BKK-BNA": 2},
    "OPS": {"BKK-R9": 90, "BKK-PKT": 8, "BKK-BNA": 2},
    "LOG": {"BKK-PKT": 65, "BKK-BNA": 15, "BKK-R9": 10, "CBI": 5, "CNX": 3, "HKT": 2},
    "SUP": {"BKK-R9": 90, "REMOTE": 8, "CNX": 2},
    "B2B": {"BKK-R9": 90, "CNX": 4, "HKT": 3, "CBI": 3},
    # Product divisions → mostly HQ
    "SF":  {"BKK-R9": 85, "REMOTE": 10, "CNX": 5},
    "DN":  {"BKK-R9": 85, "REMOTE": 10, "CNX": 5},
    "KS":  {"BKK-R9": 85, "REMOTE": 10, "HKT": 5},
    "WK":  {"BKK-R9": 85, "REMOTE": 10, "CNX": 5},
    "JC":  {"BKK-R9": 85, "REMOTE": 10, "BKK-BNA": 5},
    # Retail → spread across 10 non-HQ branches (no REMOTE, no HQ)
    "RET": {"BKK-SIAM": 15, "BKK-LP": 15, "BKK-BNA": 13, "CNX": 13,
            "HKT": 10, "CBI": 10, "KKN": 8, "NMA": 8, "HDY": 5, "BKK-R9": 3},
}

# Level mix per department — fraction of each level (sums to 1.0)
# Applied AFTER the foundation rows (exec+VPs+secretaries) are reserved
DEFAULT_LEVEL_MIX = {
    "Director": 0.03,   # ~3% directors among non-senior rows
    "Manager":  0.06,
    "Lead":     0.10,
    "IC":       0.81,
}


def weighted_choice(rng, weights: dict):
    items, w = zip(*weights.items())
    return rng.choices(items, weights=w, k=1)[0]


# ----------------------------------------------------------------------------
# Foundation rows: C-level + CoS + EAs + VPs + VP secretaries + brand GMs
# ----------------------------------------------------------------------------
def foundation_specs():
    """Return list of specs for the hard-coded leadership + secretaries + GMs."""
    specs = []

    # --- CEO tier ---
    specs += [
        ("CEO",     "ประธานเจ้าหน้าที่บริหาร", "CHIEF EXECUTIVE OFFICER",
         "CEO", "CEO-OFF", "BKK-R9", "C-level", "m", None, None, 2016),
        ("CEO-EA",  "เลขานุการของ CEO", "EXECUTIVE ASSISTANT TO CEO",
         "CEO", "CEO-OFF", "BKK-R9", "Manager", "f", None, None, None),
        ("CEO-CoS", "หัวหน้าสำนักงานประธาน", "CHIEF OF STAFF",
         "CEO", "CEO-OFF", "BKK-R9", "VP", "m", None, None, None),
    ]

    # --- C-suite + EAs (two EAs get the planted มิ้น nickname: CFO-EA + CTO-EA) ---
    csuite = [
        ("CFO",  "ประธานเจ้าหน้าที่การเงิน", "CHIEF FINANCIAL OFFICER",
         "FIN", "FIN-EXEC", "f", None),
        ("FIN-EA", "เลขานุการของ CFO", "EXECUTIVE ASSISTANT TO CFO",
         "FIN", "FIN-EXEC", "f", ("มิ้น", "MINT")),      # PLANTED
        ("CTO",  "ประธานเจ้าหน้าที่เทคโนโลยี", "CHIEF TECHNOLOGY OFFICER",
         "TEC", "TEC-EXEC", "m", None),
        ("TEC-EA", "เลขานุการของ CTO", "EXECUTIVE ASSISTANT TO CTO",
         "TEC", "TEC-EXEC", "f", ("มิ้น", "MINT")),      # PLANTED — twin
        ("COO",  "ประธานเจ้าหน้าที่ปฏิบัติการ", "CHIEF OPERATING OFFICER",
         "OPS", "OPS-EXEC", "m", None),
        ("OPS-EA", "เลขานุการของ COO", "EXECUTIVE ASSISTANT TO COO",
         "OPS", "OPS-EXEC", "f", None),
        ("CMO",  "ประธานเจ้าหน้าที่การตลาด", "CHIEF MARKETING OFFICER",
         "MKT", "MKT-EXEC", "f", None),
        ("MKT-EA", "เลขานุการของ CMO", "EXECUTIVE ASSISTANT TO CMO",
         "MKT", "MKT-EXEC", "f", None),
        ("CPO",  "ประธานเจ้าหน้าที่ฝ่ายผลิตภัณฑ์", "CHIEF PRODUCT OFFICER",
         "SF", "SF-EXEC", "m", None),
        ("CPO-EA", "เลขานุการของ CPO", "EXECUTIVE ASSISTANT TO CPO",
         "SF", "SF-EXEC", "f", None),
        ("CHRO", "ประธานเจ้าหน้าที่ฝ่ายทรัพยากรบุคคล", "CHIEF HUMAN RESOURCES OFFICER",
         "HR", "HR-EXEC", "f", None),
        ("HR-EA", "เลขานุการของ CHRO", "EXECUTIVE ASSISTANT TO CHRO",
         "HR", "HR-EXEC", "f", None),
    ]
    for (unit, p_th, p_en, dept, sec, gender, nick) in csuite:
        level = "C-level" if not unit.endswith("-EA") else "Manager"
        specs.append((unit, p_th, p_en, dept, sec, "BKK-R9", level, gender, nick, None, None))

    # --- VPs (one primary per dept + near-miss secondaries + product-division VPs) ---
    vps = [
        # Primary dept VPs (non-product)
        ("FINVP", "รองประธานฝ่ายการเงิน", "VICE PRESIDENT FINANCE",
         "FIN", "FIN-FP"),
        ("HRVP", "รองประธานฝ่ายทรัพยากรบุคคล", "VICE PRESIDENT HUMAN RESOURCES",
         "HR", "HR-OPS"),
        ("LEGVP", "รองประธานฝ่ายกฎหมาย", "VICE PRESIDENT LEGAL",
         "LEG", "LEG-COM"),
        ("MKTVP", "รองประธานฝ่ายการตลาด", "VICE PRESIDENT MARKETING",
         "MKT", "MKT-BR"),
        ("TECVP", "รองประธานฝ่ายเทคโนโลยี", "VICE PRESIDENT TECHNOLOGY",
         "TEC", "TEC-PLT"),
        ("OPSVP", "รองประธานฝ่ายปฏิบัติการ", "VICE PRESIDENT OPERATIONS",
         "OPS", "OPS-PMO"),
        ("LOGVP", "รองประธานฝ่ายโลจิสติกส์", "VICE PRESIDENT LOGISTICS",
         "LOG", "LOG-WH"),
        ("SUPVP", "รองประธานฝ่ายบริการลูกค้า", "VICE PRESIDENT CUSTOMER SUPPORT",
         "SUP", "SUP-TECH"),
        ("RETVP", "รองประธานฝ่ายเครือข่ายร้านค้า", "VICE PRESIDENT RETAIL NETWORK",
         "RET", "RET-HQ"),
        ("B2BVP", "รองประธานฝ่ายขายองค์กร", "VICE PRESIDENT B2B SALES",
         "B2B", "B2B-SLS"),
        # Product-division VPs (one per brand)
        ("SFVP", "รองประธานฝ่ายสายฟ้า", "VICE PRESIDENT OF SAIFAH",
         "SF", "SF-PD"),
        ("DNVP", "รองประธานฝ่ายดาวเหนือ", "VICE PRESIDENT OF DAONUEA",
         "DN", "DN-PD"),
        ("KSVP", "รองประธานฝ่ายคลื่นเสียง", "VICE PRESIDENT OF KLUENSIANG",
         "KS", "KS-PD"),
        ("WKVP", "รองประธานฝ่ายวงโคจร", "VICE PRESIDENT OF WONGKHOJON",
         "WK", "WK-PD"),
        ("JCVP", "รองประธานฝ่ายจุดเชื่อม", "VICE PRESIDENT OF JUDCHUEM",
         "JC", "JC-PD"),
        # Secondary VPs (near-miss + multi-VP depts)
        ("TECPM", "รองประธานฝ่ายแพลตฟอร์ม", "VICE PRESIDENT PLATFORM",
         "TEC", "TEC-PLT"),      # ← near-miss with TECVP
        ("MKTDG", "รองประธานฝ่ายการตลาดดิจิทัล", "VICE PRESIDENT DIGITAL MARKETING",
         "MKT", "MKT-DIG"),
        ("SUPCX", "รองประธานฝ่ายประสบการณ์ลูกค้า", "VICE PRESIDENT CUSTOMER EXPERIENCE",
         "SUP", "SUP-ESC"),
        ("LOGFL", "รองประธานฝ่ายขนส่ง", "VICE PRESIDENT FLEET",
         "LOG", "LOG-FLT"),
        ("OPSQA", "รองประธานฝ่ายคุณภาพ", "VICE PRESIDENT QUALITY",
         "OPS", "OPS-PMO"),
        ("RETBKK", "รองประธานสาขากรุงเทพ", "VICE PRESIDENT BANGKOK RETAIL",
         "RET", "RET-HQ"),
        ("RETUPC", "รองประธานสาขาต่างจังหวัด", "VICE PRESIDENT UPCOUNTRY RETAIL",
         "RET", "RET-HQ"),
        ("B2BACC", "รองประธานฝ่ายดูแลลูกค้าองค์กร", "VICE PRESIDENT B2B ACCOUNTS",
         "B2B", "B2B-ACC"),
        ("FINFP", "ผู้อำนวยการฝ่ายการเงินและวางแผน", "DIRECTOR FINANCIAL PLANNING",
         "FIN", "FIN-FP"),        # ← near-miss with FINVP (Director level, not VP)
        ("SFDR", "ผู้อำนวยการฝ่ายปฏิบัติการสายฟ้า", "DIRECTOR OF SAIFAH OPERATIONS",
         "SF", "SF-OPS"),         # ← near-miss with SFVP
        ("MKTBR", "ผู้อำนวยการฝ่ายแบรนด์", "DIRECTOR BRAND",
         "MKT", "MKT-BR"),        # ← near-miss with MKTVP
    ]
    for (unit, p_th, p_en, dept, sec) in vps:
        # FINFP, SFDR, MKTBR are directors (near-miss pairs); rest are VPs
        lvl = "Director" if unit in ("FINFP", "SFDR", "MKTBR") else "VP"
        specs.append((unit, p_th, p_en, dept, sec, "BKK-R9", lvl, None, None, None, None))

    # --- Per-VP secretaries (match Dept + Branch of boss) ---
    # Only for VP-level (not Directors)
    vp_units = [v[0] for v in vps if v[0] not in ("FINFP", "SFDR", "MKTBR")]
    for vu in vp_units:
        # find boss's dept/section
        boss = next(v for v in vps if v[0] == vu)
        _, _, _, dept, sec = boss
        specs.append((
            f"{vu}-SEC",
            f"เลขานุการของ {vu}",
            f"SECRETARY OF {vu}",
            dept, sec, "BKK-R9", "Manager",
            "f", None, None, None,
        ))

    # --- Thai-position near-miss pair (DESIGN.md) — both directors in FIN ---
    specs += [
        ("FIN-ACCDR", "ผู้อำนวยการฝ่ายบัญชี", "DIRECTOR ACCOUNTING",
         "FIN", "FIN-GL", "BKK-R9", "Director", "f", None, None, None),
        ("FIN-FINDR", "ผู้อำนวยการฝ่ายการเงิน", "DIRECTOR FINANCE",
         "FIN", "FIN-TR", "BKK-R9", "Director", "m", None, None, None),
    ]

    # --- 5 house-brand GMs (subsidiary_md pattern) — Director level ---
    brands_gm = [
        ("SF-GM", "ผู้จัดการทั่วไปแบรนด์สายฟ้า", "GENERAL MANAGER OF SAIFAH", "SF", "SF-PD"),
        ("DN-GM", "ผู้จัดการทั่วไปแบรนด์ดาวเหนือ", "GENERAL MANAGER OF DAONUEA", "DN", "DN-PD"),
        ("KS-GM", "ผู้จัดการทั่วไปแบรนด์คลื่นเสียง", "GENERAL MANAGER OF KLUENSIANG", "KS", "KS-PD"),
        ("WK-GM", "ผู้จัดการทั่วไปแบรนด์วงโคจร", "GENERAL MANAGER OF WONGKHOJON", "WK", "WK-PD"),
        ("JC-GM", "ผู้จัดการทั่วไปแบรนด์จุดเชื่อม", "GENERAL MANAGER OF JUDCHUEM", "JC", "JC-PD"),
    ]
    for (unit, p_th, p_en, dept, sec) in brands_gm:
        specs.append((unit, p_th, p_en, dept, sec, "BKK-R9", "Director", None, None, None, None))

    return specs


def gen_full():
    first_pool, last_pool, nicks_pool, variants = load_pools()
    rng = random.Random(SEED)

    used_ids, used_emails, used_exts = set(), set(), set()
    rows = []

    # --- foundation rows (leadership + secretaries + GMs) ---
    foundation = foundation_specs()
    for spec in foundation:
        rows.append(build_row(rng, spec, first_pool, last_pool, nicks_pool,
                              used_ids, used_emails, used_exts))

    # --- count foundation per dept so remaining headcount fills correctly ---
    foundation_per_dept = Counter(r["Department"] for r in rows)

    # --- random-fill each dept up to DEPT_TARGETS ---
    position_templates_by_dept = _position_templates()

    for dept, target in DEPT_TARGETS.items():
        remaining = target - foundation_per_dept.get(dept, 0)
        if remaining <= 0:
            continue
        sections = DEPT_SECTIONS[dept]
        # Reserve 1–2 extra directors for mid-size depts, more for big ones
        n_director = max(1, int(remaining * DEFAULT_LEVEL_MIX["Director"]))
        n_manager = max(2, int(remaining * DEFAULT_LEVEL_MIX["Manager"]))
        n_lead = max(3, int(remaining * DEFAULT_LEVEL_MIX["Lead"]))
        n_ic = remaining - n_director - n_manager - n_lead

        for _ in range(n_director):
            rows.append(_rand_row(rng, dept, sections, "Director", first_pool, last_pool,
                                  nicks_pool, used_ids, used_emails, used_exts,
                                  position_templates_by_dept))
        for _ in range(n_manager):
            rows.append(_rand_row(rng, dept, sections, "Manager", first_pool, last_pool,
                                  nicks_pool, used_ids, used_emails, used_exts,
                                  position_templates_by_dept))
        for _ in range(n_lead):
            rows.append(_rand_row(rng, dept, sections, "Lead", first_pool, last_pool,
                                  nicks_pool, used_ids, used_emails, used_exts,
                                  position_templates_by_dept))
        for _ in range(n_ic):
            rows.append(_rand_row(rng, dept, sections, "IC", first_pool, last_pool,
                                  nicks_pool, used_ids, used_emails, used_exts,
                                  position_templates_by_dept))

    # --- Planted adversarial seeds (post-foundation) ---
    # 3 employees with nickname ไอซ์ across different departments
    ice_targets_assigned = 0
    ice_depts_needed = {"SUP", "RET", "TEC"}
    ice_depts_done = set()
    for r in rows:
        if ice_targets_assigned >= 3:
            break
        if (r["Position Level"] == "IC" and r["Department"] in ice_depts_needed
                and r["Department"] not in ice_depts_done and r["Nickname Thai"]):
            r["Nickname Thai"] = "ไอซ์"
            r["Nickname English"] = "ICE"
            ice_depts_done.add(r["Department"])
            ice_targets_assigned += 1

    # Curated list of Thai nicknames that REAL offices commonly share across
    # multiple employees. Source: Ministry of Culture top-10 lists + Thai-
    # workplace forum lore. These are single-syllable traditional nicknames
    # plus the most-popular English-loan modern ones — NOT weird brand or
    # doubled forms (those stay rare via the random-nickname pool).
    COMMON_SHARED_NICKS = [
        # Traditional top-tier
        ("พลอย", "PLOY"), ("แพร", "PRAEW"), ("มุก", "MOOK"),
        ("ฝน", "FON"), ("ฟ้า", "FAH"), ("ดาว", "DAO"), ("น้ำ", "NAM"),
        ("บี", "BEE"), ("ออม", "AOM"), ("อ้อม", "OM"),
        ("นัต", "NUT"), ("ต้อม", "TUM"), ("ตูน", "TOON"), ("ปุ๊ก", "PUK"),
        ("ปิ๊ง", "PING"), ("แก้ว", "KAEW"), ("เปิ้ล", "PLE"),
        ("เอ", "AE"), ("โอ", "OH"),
        # Popular modern English-loan
        ("อาร์ม", "ARM"), ("บูม", "BOOM"), ("ฟิล์ม", "FILM"),
        ("เบียร์", "BEER"), ("นิว", "NEW"), ("กอล์ฟ", "GOLF"),
        ("แบงค์", "BANK"), ("บอส", "BOSS"), ("บีม", "BEAM"),
        ("เบนซ์", "BENZ"), ("มาร์ค", "MARK"), ("ซัน", "SUN"),
        # Food/color — realistically shared
        ("ส้ม", "SOM"), ("ชมพู", "CHOMPOO"), ("พีช", "PEACH"),
        ("เค้ก", "CAKE"), ("ไก่", "KAI"), ("นก", "NOK"),
    ]
    # Pick 20 of these for seeding ambiguity (deterministic via seeded rng).
    # Each gets force-assigned to 3 IC/Lead rows. ไอซ์ and มิ้น are already
    # seeded separately — exclude from this pool to avoid double-counting.
    pool_for_seed = [(th, en) for (th, en) in COMMON_SHARED_NICKS
                     if th not in ("ไอซ์", "มิ้น")]
    ambig_nicks_seeds = rng.sample(pool_for_seed, 20)
    ic_lead_rows = [r for r in rows if r["Position Level"] in ("IC", "Lead")]
    rng.shuffle(ic_lead_rows)
    idx = 0
    for (nth, nen) in ambig_nicks_seeds:
        for _ in range(3):
            if idx >= len(ic_lead_rows):
                break
            ic_lead_rows[idx]["Nickname Thai"] = nth
            ic_lead_rows[idx]["Nickname English"] = nen
            idx += 1

    # Ensure ~5% Department blank (secondment rows)
    n_secondment = int(len(rows) * 0.05)
    secondment_candidates = [r for r in rows if r["Position Level"] in ("IC", "Lead")
                             and r["Department"] not in ("CEO", "RET")]
    rng.shuffle(secondment_candidates)
    for r in secondment_candidates[:n_secondment]:
        r["Department"] = ""
        r["Section"] = ""  # full secondment → both blank

    # Gate H.1 — surname uniqueness polish. Post-process so Employee IDs,
    # units, branches, extensions stay byte-stable; only Last Name + Email
    # change. Plants ~30 family clusters (shared surname = same family).
    planted = apply_surname_polish(rows, last_pool)
    print(f"[polish] planted {len(planted)} family clusters "
          f"({sum(len(ids) for _, ids in planted)} rows)")

    return rows


def _position_templates():
    """Section → (pos_th_template, pos_en_template) for ICs and Leads."""
    T = {
        # FIN
        "FIN-AP": ("เจ้าหน้าที่บัญชีเจ้าหนี้", "ACCOUNTS PAYABLE OFFICER"),
        "FIN-AR": ("เจ้าหน้าที่บัญชีลูกหนี้", "ACCOUNTS RECEIVABLE OFFICER"),
        "FIN-GL": ("นักบัญชี", "ACCOUNTANT"),
        "FIN-FP": ("นักวิเคราะห์การเงิน", "FINANCIAL ANALYST"),
        "FIN-TR": ("เจ้าหน้าที่ฝ่ายคลัง", "TREASURY OFFICER"),
        "FIN-TAX": ("นักภาษีอากร", "TAX SPECIALIST"),
        # TEC
        "TEC-BE": ("วิศวกรซอฟต์แวร์", "BACKEND SOFTWARE ENGINEER"),
        "TEC-FE": ("วิศวกรฟรอนท์เอนด์", "FRONTEND SOFTWARE ENGINEER"),
        "TEC-MOB": ("วิศวกรโมบาย", "MOBILE SOFTWARE ENGINEER"),
        "TEC-DS": ("นักวิทยาศาสตร์ข้อมูล", "DATA SCIENTIST"),
        "TEC-SEC": ("วิศวกรความปลอดภัย", "SECURITY ENGINEER"),
        "TEC-INF": ("วิศวกรโครงสร้างพื้นฐาน", "INFRASTRUCTURE ENGINEER"),
        "TEC-PLT": ("วิศวกรแพลตฟอร์ม", "PLATFORM ENGINEER"),
        "TEC-QA": ("วิศวกรทดสอบคุณภาพ", "QA ENGINEER"),
        "TEC-DATA": ("วิศวกรข้อมูล", "DATA ENGINEER"),
        # MKT
        "MKT-BR": ("ผู้เชี่ยวชาญด้านแบรนด์", "BRAND SPECIALIST"),
        "MKT-DIG": ("นักการตลาดดิจิทัล", "DIGITAL MARKETING SPECIALIST"),
        "MKT-CON": ("ครีเอทีฟคอนเทนต์", "CONTENT CREATOR"),
        "MKT-PR": ("เจ้าหน้าที่ประชาสัมพันธ์", "PR OFFICER"),
        "MKT-CRM": ("นักการตลาด CRM", "CRM SPECIALIST"),
        "MKT-EVT": ("เจ้าหน้าที่จัดอีเวนต์", "EVENTS COORDINATOR"),
        # HR
        "HR-TA": ("เจ้าหน้าที่สรรหาบุคลากร", "TALENT ACQUISITION SPECIALIST"),
        "HR-LD": ("เจ้าหน้าที่พัฒนาบุคลากร", "LEARNING & DEVELOPMENT SPECIALIST"),
        "HR-OPS": ("เจ้าหน้าที่ฝ่ายทรัพยากรบุคคล", "HR OPERATIONS OFFICER"),
        "HR-COMP": ("เจ้าหน้าที่ฝ่ายผลตอบแทน", "COMPENSATION ANALYST"),
        "HR-CUL": ("เจ้าหน้าที่ฝ่ายวัฒนธรรมองค์กร", "CULTURE SPECIALIST"),
        # LEG
        "LEG-CNT": ("ทนายความฝ่ายสัญญา", "CONTRACTS COUNSEL"),
        "LEG-IP": ("ทนายความฝ่ายทรัพย์สินทางปัญญา", "IP COUNSEL"),
        "LEG-COM": ("เจ้าหน้าที่กำกับดูแล", "COMPLIANCE OFFICER"),
        # OPS
        "OPS-FAC": ("เจ้าหน้าที่ฝ่ายอาคารสถานที่", "FACILITIES OFFICER"),
        "OPS-PROC": ("เจ้าหน้าที่ฝ่ายจัดซื้อ", "PROCUREMENT OFFICER"),
        "OPS-PMO": ("ผู้จัดการโครงการ", "PROGRAM MANAGER"),
        "OPS-ADM": ("เจ้าหน้าที่ธุรการ", "ADMINISTRATOR"),
        "OPS-TRV": ("เจ้าหน้าที่ฝ่ายเดินทาง", "TRAVEL OFFICER"),
        # LOG
        "LOG-WH": ("พนักงานคลังสินค้า", "WAREHOUSE ASSOCIATE"),
        "LOG-SHP": ("เจ้าหน้าที่ฝ่ายขนส่ง", "SHIPPING COORDINATOR"),
        "LOG-INV": ("เจ้าหน้าที่ควบคุมสต็อก", "INVENTORY CONTROLLER"),
        "LOG-RET": ("เจ้าหน้าที่ฝ่ายคืนสินค้า", "RETURNS PROCESSOR"),
        "LOG-FLT": ("พนักงานขับรถ", "FLEET DRIVER"),
        # SUP
        "SUP-CHAT": ("เจ้าหน้าที่แชทลูกค้า", "CHAT SUPPORT AGENT"),
        "SUP-PHN": ("เจ้าหน้าที่บริการลูกค้าทางโทรศัพท์", "PHONE SUPPORT AGENT"),
        "SUP-EML": ("เจ้าหน้าที่บริการลูกค้าทางอีเมล", "EMAIL SUPPORT AGENT"),
        "SUP-TECH": ("เจ้าหน้าที่สนับสนุนทางเทคนิค", "TECHNICAL SUPPORT AGENT"),
        "SUP-ESC": ("เจ้าหน้าที่จัดการข้อร้องเรียน", "ESCALATIONS SPECIALIST"),
        "SUP-TRN": ("ผู้ฝึกอบรมทีมซัพพอร์ต", "SUPPORT TRAINER"),
        # RET
        "RET-HQ": ("เจ้าหน้าที่ปฏิบัติการรีเทล", "RETAIL OPERATIONS SPECIALIST"),
        "RET-BKK-SIAM": ("พนักงานขายสาขาสยาม", "SALES ASSOCIATE SIAM"),
        "RET-BKK-LP": ("พนักงานขายสาขาลาดพร้าว", "SALES ASSOCIATE LAD PHRAO"),
        "RET-BKK-BNA": ("พนักงานขายสาขาบางนา", "SALES ASSOCIATE BANGNA"),
        "RET-CNX": ("พนักงานขายสาขาเชียงใหม่", "SALES ASSOCIATE CHIANG MAI"),
        "RET-KKN": ("พนักงานขายสาขาขอนแก่น", "SALES ASSOCIATE KHON KAEN"),
        "RET-NMA": ("พนักงานขายสาขาโคราช", "SALES ASSOCIATE KORAT"),
        "RET-CBI": ("พนักงานขายสาขาชลบุรี", "SALES ASSOCIATE CHONBURI"),
        "RET-HKT": ("พนักงานขายสาขาภูเก็ต", "SALES ASSOCIATE PHUKET"),
        "RET-HDY": ("พนักงานขายสาขาหาดใหญ่", "SALES ASSOCIATE HAT YAI"),
        "RET-TRN": ("ผู้ฝึกอบรมพนักงานร้านค้า", "RETAIL TRAINER"),
        # B2B
        "B2B-SLS": ("ผู้แทนขายองค์กร", "B2B SALES REPRESENTATIVE"),
        "B2B-ACC": ("ผู้จัดการบัญชีลูกค้า", "ACCOUNT MANAGER"),
        "B2B-SOL": ("วิศวกรโซลูชันองค์กร", "SOLUTIONS ENGINEER"),
        "B2B-SUP": ("เจ้าหน้าที่บริการลูกค้าองค์กร", "B2B SUPPORT SPECIALIST"),
        # Product divisions
        "SF-PD": ("ผู้จัดการผลิตภัณฑ์สายฟ้า", "SAIFAH PRODUCT MANAGER"),
        "SF-ENG": ("วิศวกรผลิตภัณฑ์สายฟ้า", "SAIFAH PRODUCT ENGINEER"),
        "SF-OPS": ("เจ้าหน้าที่ปฏิบัติการแบรนด์", "SAIFAH BRAND OPERATIONS"),
        "SF-MKT": ("นักการตลาดแบรนด์สายฟ้า", "SAIFAH BRAND MARKETER"),
        "DN-PD": ("ผู้จัดการผลิตภัณฑ์ดาวเหนือ", "DAONUEA PRODUCT MANAGER"),
        "DN-ENG": ("วิศวกรผลิตภัณฑ์ดาวเหนือ", "DAONUEA PRODUCT ENGINEER"),
        "DN-OPS": ("เจ้าหน้าที่ปฏิบัติการแบรนด์ดาวเหนือ", "DAONUEA BRAND OPERATIONS"),
        "DN-MKT": ("นักการตลาดแบรนด์ดาวเหนือ", "DAONUEA BRAND MARKETER"),
        "KS-PD": ("ผู้จัดการผลิตภัณฑ์คลื่นเสียง", "KLUENSIANG PRODUCT MANAGER"),
        "KS-ENG": ("วิศวกรผลิตภัณฑ์คลื่นเสียง", "KLUENSIANG PRODUCT ENGINEER"),
        "KS-OPS": ("เจ้าหน้าที่ปฏิบัติการแบรนด์คลื่นเสียง", "KLUENSIANG BRAND OPERATIONS"),
        "KS-MKT": ("นักการตลาดแบรนด์คลื่นเสียง", "KLUENSIANG BRAND MARKETER"),
        "WK-PD": ("ผู้จัดการผลิตภัณฑ์วงโคจร", "WONGKHOJON PRODUCT MANAGER"),
        "WK-ENG": ("วิศวกรผลิตภัณฑ์วงโคจร", "WONGKHOJON PRODUCT ENGINEER"),
        "WK-OPS": ("เจ้าหน้าที่ปฏิบัติการแบรนด์วงโคจร", "WONGKHOJON BRAND OPERATIONS"),
        "WK-MKT": ("นักการตลาดแบรนด์วงโคจร", "WONGKHOJON BRAND MARKETER"),
        "JC-PD": ("ผู้จัดการผลิตภัณฑ์จุดเชื่อม", "JUDCHUEM PRODUCT MANAGER"),
        "JC-ENG": ("วิศวกรผลิตภัณฑ์จุดเชื่อม", "JUDCHUEM PRODUCT ENGINEER"),
        "JC-OPS": ("เจ้าหน้าที่ปฏิบัติการแบรนด์จุดเชื่อม", "JUDCHUEM BRAND OPERATIONS"),
        "JC-MKT": ("นักการตลาดแบรนด์จุดเชื่อม", "JUDCHUEM BRAND MARKETER"),
        # CEO
        "CEO-OFF": ("เจ้าหน้าที่สำนักงานประธาน", "CEO OFFICE SPECIALIST"),
        "CEO-SEC": ("เลขานุการ", "SECRETARIAT OFFICER"),
        "CEO-STR": ("นักกลยุทธ์องค์กร", "STRATEGY SPECIALIST"),
    }
    # Fallback generic
    return T


def _rand_row(rng, dept, sections, level, first_pool, last_pool, nicks_pool,
              used_ids, used_emails, used_exts, position_templates):
    # pick a section — avoid EXEC sections for non-senior rows
    candidate_sections = [s for s in sections if not s.endswith("-EXEC")]
    if not candidate_sections:
        candidate_sections = sections
    section = rng.choice(candidate_sections)

    # branch by dept weights
    branch = weighted_choice(rng, DEPT_BRANCH_WEIGHTS[dept])

    # Retail branch staff must sit at a section matching their branch
    if dept == "RET":
        branch_to_section = {
            "BKK-SIAM": "RET-BKK-SIAM", "BKK-LP": "RET-BKK-LP", "BKK-BNA": "RET-BKK-BNA",
            "CNX": "RET-CNX", "HKT": "RET-HKT", "CBI": "RET-CBI",
            "KKN": "RET-KKN", "NMA": "RET-NMA", "HDY": "RET-HDY",
            "BKK-R9": "RET-HQ",
        }
        section = branch_to_section.get(branch, "RET-HQ")

    # Position text from template
    p_th, p_en = position_templates.get(section, ("เจ้าหน้าที่", "SPECIALIST"))
    if level == "Director":
        p_th = "ผู้อำนวยการฝ่าย" + p_th
        p_en = "DIRECTOR " + p_en
    elif level == "Manager":
        p_th = "ผู้จัดการ" + p_th
        p_en = "MANAGER " + p_en
    elif level == "Lead":
        p_th = "หัวหน้าทีม" + p_th
        p_en = "LEAD " + p_en
    # IC: use template as-is

    # Unit code
    if level == "Director":
        unit = f"{section}-DR-{rng.randint(1, 9)}"
    elif level == "Manager":
        unit = f"{section}-MGR-{rng.randint(1, 9)}"
    elif level == "Lead":
        unit = f"{section}-LEAD-{rng.randint(1, 9)}"
    else:
        unit = f"{section}-{rng.randint(1, 99)}"

    spec = (unit, p_th, p_en, dept, section, branch, level, None, None, None, None)
    return build_row(rng, spec, first_pool, last_pool, nicks_pool,
                     used_ids, used_emails, used_exts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["sample", "full"], default="sample")
    args = ap.parse_args()

    if args.mode == "sample":
        rows = gen_sample()
        out = KB / "employees_sample.csv"
        write_csv(rows, out)
        print(f"Wrote {out}\n")
        summarize(rows)
    else:
        rows = gen_full()
        out = KB / "employees.csv"
        write_csv(rows, out)
        print(f"Wrote {out}\n")
        summarize(rows)


if __name__ == "__main__":
    main()
