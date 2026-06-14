"""Build B5 — informal enterprise shorthand (20), all airtight.

Shorthand pool (mirrors real Thai-enterprise conventions, to be documented in the
system prompt per taxonomy): branch province/airport codes (R9=Rama IX HQ, CNX=
Chiang Mai, HKT=Phuket, HDY=Hat Yai, KKN=Khon Kaen, NMA=Korat, CBI=Chonburi,
BNA=Bangna, LP=Lat Phrao, SIAM, REMOTE) + Thai informal dept (ฟินฯ=Finance) +
English dept acronyms (HR, MKT, TEC). The shorthand is the load-bearing expansion.

Three airtight forms:
  - branch-size COUNT (exact_count = true branch size; taxonomy's canonical B5).
  - branch-director IDENTITY (5 RET branches each have ONE sales director ->
    gold = first+last; fully airtight, immune to substring grader).
  - informal-dept-head IDENTITY (ฟินฯ/HR/MKT/TEC -> the unique C-level head).
All carry tag retry_t1 (B5 seeds the grep-only retry metric).
"""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
RANK = {'C-level': 5, 'VP': 4, 'Director': 3, 'Manager': 2, 'Lead': 1, 'IC': 0}
def fg(r): return sorted({r['First Name Thai'], r['First Name English'].title()})
def lg(r): return sorted({r['Last Name Thai'], r['Last Name English'].title()})
def nm(r): return f"{r['First Name Thai']} {r['Last Name Thai']}"

items, fails = [], []
def emit(lang, q, ea, gt, rat, tags, src):
    items.append({'bucket': 'enterprise_shorthand', 'subtype': 'B5', 'group': 'B',
        'v01_bucket': 'enterprise_shorthand', 'priority': 'P1', 'language': lang,
        'question': q, 'expected_behavior': 'answer', 'expected_answer': ea,
        'ground_truth_row_ids': gt, 'rationale': rat, 'tags': tags,
        'authored': '2026-05-24', 'src_id': src})

# ---- branch-size COUNT (11) ----
# code -> (Branch value, TH name, EN name)
BR = [('R9', 'BKK-R9', 'สาขาสำนักงานใหญ่ พระราม 9 (R9)', 'the Rama IX (R9) HQ'),
      ('CNX', 'CNX', 'สาขาเชียงใหม่ (CNX)', 'the Chiang Mai (CNX)'),
      ('HKT', 'HKT', 'สาขาภูเก็ต (HKT)', 'the Phuket (HKT)'),
      ('HDY', 'HDY', 'สาขาหาดใหญ่ (HDY)', 'the Hat Yai (HDY)'),
      ('KKN', 'KKN', 'สาขาขอนแก่น (KKN)', 'the Khon Kaen (KKN)'),
      ('NMA', 'NMA', 'สาขาโคราช (NMA)', 'the Korat (NMA)'),
      ('CBI', 'CBI', 'สาขาชลบุรี (CBI)', 'the Chonburi (CBI)'),
      ('BNA', 'BKK-BNA', 'สาขาบางนา (BNA)', 'the Bangna (BNA)'),
      ('LP', 'BKK-LP', 'สาขาลาดพร้าว (LP)', 'the Lat Phrao (LP)'),
      ('SIAM', 'BKK-SIAM', 'สาขาสยาม (SIAM)', 'the Siam (SIAM)'),
      ('REMOTE', 'REMOTE', 'ที่ทำงานทางไกล (REMOTE)', 'remote (REMOTE)')]
branch_count = Counter(r['Branch'] for r in R)
branch_ids = defaultdict(list)
for r in R: branch_ids[r['Branch']].append(r['Employee ID'])
for i, (code, val, th, en) in enumerate(BR):
    n = branch_count[val]
    if n == 0:
        fails.append(('B5-count', code, 'no rows')); continue
    lang = 'en' if i % 3 == 0 else 'th'
    q = (f'พนักงาน{th} มีกี่คน' if lang == 'th' else f'How many staff work at {en} branch?')
    ea = {'must_contain_any_of': [], 'must_not_contain': [], 'exact_count': n}
    emit(lang, q, ea, branch_ids[val],
         f'Enterprise shorthand: branch code {code} -> Branch={val}; exact_count={n}.',
         ['shorthand', 'branch', 'count', 'retry_t1'], f'B5-CNT-{code}')

# ---- RET branch-director IDENTITY (5) ----
sec = defaultdict(list)
for r in R: sec[r['Section']].append(r)
RET = [('RET-HKT', 'HKT', 'ภูเก็ต', 'Phuket'), ('RET-HDY', 'HDY', 'หาดใหญ่', 'Hat Yai'),
       ('RET-NMA', 'NMA', 'โคราช', 'Korat'), ('RET-BKK-SIAM', 'SIAM', 'สยาม', 'Siam'),
       ('RET-BKK-LP', 'LP', 'ลาดพร้าว', 'Lat Phrao')]
for i, (s, code, th, en) in enumerate(RET):
    rows = sec[s]
    mx = max(RANK[r['Position Level']] for r in rows)
    top = [r for r in rows if RANK[r['Position Level']] == mx]
    if len(top) != 1:
        fails.append(('B5-RET', s, 'non-unique top')); continue
    t = top[0]
    lang = 'th' if i % 2 == 0 else 'en'
    q = (f'ผู้อำนวยการทีมขายสาขา{th} ({code}) คือใคร' if lang == 'th'
         else f'Who is the sales director at the {en} ({code}) branch?')
    ea = {'must_contain_any_of': [fg(t), lg(t)], 'must_not_contain': []}
    emit(lang, q, ea, [t['Employee ID']],
         f'Shorthand {code}->{en} retail branch; unique sales director = {nm(t)} '
         f'({t["Position in English"]}).', ['shorthand', 'branch', 'identity', 'retry_t1'], f'B5-DIR-{code}')

# ---- informal-dept-head IDENTITY (4) ----
dept = defaultdict(list)
for r in R: dept[r['Department']].append(r)
DEPT = [('FIN', 'th', 'หัวหน้าทีมฟินฯ คือใคร', 'ฟินฯ = Finance'),
        ('HR', 'en', 'Who heads the HR team?', 'HR = Human Resources'),
        ('MKT', 'th', 'ใครเป็นหัวหน้าทีมการตลาด (MKT)', 'MKT = Marketing'),
        ('TEC', 'en', 'Who is the head of the TEC (tech) department?', 'TEC = Technology')]
for code, lang, q, note in DEPT:
    rows = dept[code]
    mx = max(RANK[r['Position Level']] for r in rows)
    top = [r for r in rows if RANK[r['Position Level']] == mx]
    if len(top) != 1:
        fails.append(('B5-dept', code, 'non-unique head')); continue
    t = top[0]
    ea = {'must_contain_any_of': [fg(t), lg(t)], 'must_not_contain': []}
    emit(lang, q, ea, [t['Employee ID']],
         f'Informal shorthand ({note}); unique dept head = {nm(t)} ({t["Position in English"]}).',
         ['shorthand', 'informal', 'identity', 'retry_t1'], f'B5-HEAD-{code}')

if fails:
    print('!! FAILED:', fails); raise SystemExit(1)
out = Path(__file__).parent / 'b5_v2_items.json'
json.dump({'questions': items}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'b5_v2_items.json: {len(items)} items  lang={dict(Counter(it["language"] for it in items))}')
for it in items:
    ea = it['expected_answer']
    g = f'count={ea["exact_count"]}' if ea.get('exact_count') is not None else f'{ea["must_contain_any_of"][0][0]} {ea["must_contain_any_of"][1][0]}'
    print(f'  [{it["language"]}] {g[:30]:30} | {it["question"][:48]}')
