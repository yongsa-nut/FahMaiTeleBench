"""Build the E-group v2 backlog: E1 +14, E2 +4, E4 +20 (=38), all airtight.

E1 (section_to_senior, NEW two-hop pattern — no overlap with existing secretary/
    dept bridges): anchor = a globally-unique IC; answer = the ext/email of the
    UNIQUE most-senior person in that IC's section. Anti-shortcut verified
    (IC's own value != senior's). Section senior = unique top of Position-Level
    ladder, surname-unique within section, n>=6.
E2 (+4): English counterparts of the verified Thai brand->GM items g359-362
    (same gold + gt rows -> guaranteed airtight); 3-hop brand->dept->head.
E4 (+20 surname-family): 8 count (gold=[[str(n)]]) + 12 listing (one AND-group
    per member's first-name variants -> model must name ALL members; tighter than
    the old empty-gold listing). Distinct families, none reused from g382-386.

Output -> e_v2_items.json. Aborts on any airtight failure.
"""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
QF = (_REPO_ROOT / "questions" / "questions_v02.json")
R = list(csv.DictReader(open(P, encoding='utf-8')))
RANK = {'C-level': 5, 'VP': 4, 'Director': 3, 'Manager': 2, 'Lead': 1, 'IC': 0}
def nm(r): return f"{r['First Name Thai']} {r['Last Name Thai']}"
fullc = Counter((r['First Name Thai'], r['Last Name Thai']) for r in R)
def uniq(r): return fullc[(r['First Name Thai'], r['Last Name Thai'])] == 1
def fg_lg(r):
    fg = [t for t in [r['First Name Thai'], r['First Name English'].title()] if t]
    lg = [t for t in [r['Last Name Thai'], r['Last Name English'].title()] if t]
    return fg, lg

items, fails = [], []
def emit(sub, lang, q, gold, gt, rat, tags, must_not=None, src=None):
    items.append({'bucket': 'multi_hop', 'subtype': sub, 'group': 'E',
        'v01_bucket': {'E1': 'two_hop', 'E2': 'hard_bridge_lookup', 'E4': 'surname_family'}[sub],
        'priority': 'P1', 'language': lang, 'question': q, 'expected_behavior': 'answer',
        'expected_answer': {'must_contain_any_of': gold, 'must_not_contain': must_not or []},
        'ground_truth_row_ids': gt, 'rationale': rat, 'tags': tags,
        'authored': '2026-05-24', 'src_id': src})

# ================= E1 — section_to_senior (14) =================
sec = defaultdict(list)
for r in R: sec[r['Section']].append(r)
qual = []   # (section, senior, rows)
for s, rows in sorted(sec.items()):
    if len(rows) < 6: continue
    mx = max(RANK[r['Position Level']] for r in rows)
    if mx not in (2, 3): continue
    top = [r for r in rows if RANK[r['Position Level']] == mx]
    if len(top) != 1: continue
    t = top[0]
    if not uniq(t): continue
    if sum(1 for r in rows if r['Last Name Thai'] == t['Last Name Thai']) != 1: continue
    if not t['Phone Extension'] or not t['Email Address']: continue   # senior needs both targets
    qual.append((s, t, rows))

idx = 1
for i, (s, t, rows) in enumerate(qual[:14]):
    lang = 'th' if i % 2 == 0 else 'en'
    attr = 'ext' if i % 2 == 0 else 'email'           # alternate target
    val = t['Phone Extension'] if attr == 'ext' else t['Email Address']
    # pick a globally-unique IC whose own value differs from senior's (anti-shortcut)
    ics = [r for r in rows if r['Position Level'] == 'IC' and uniq(r)
           and (r['Phone Extension'] if attr == 'ext' else r['Email Address'])
           and (r['Phone Extension'] if attr == 'ext' else r['Email Address']) != val]
    if not ics:
        fails.append(('E1', s, 'no anti-shortcut IC')); continue
    a = ics[0]
    if lang == 'th':
        q = (f'ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณ{nm(a)}สังกัดอยู่ หน่อยครับ' if attr == 'ext'
             else f'ขออีเมลของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณ{nm(a)}สังกัดอยู่ หน่อยครับ')
    else:
        q = (f"What's the phone extension of the most senior person in the section that {nm(a)} works in?"
             if attr == 'ext' else
             f"What's the email of the most senior person in the section that {nm(a)} works in?")
    emit('E1', lang, q, [[val]], [t['Employee ID']],
         f"Two-hop section_to_senior: {nm(a)} (IC) -> section {s} -> unique senior "
         f"{t['Position Level']} {nm(t)} -> {attr}={val}. Anchor's own {attr} differs (anti-shortcut).",
         ['multi_hop', 'two_hop', 'section_to_senior', attr], src=f'E1-S{idx:02d}')
    idx += 1

# ================= E2 — EN brand->GM counterparts (4) =================
existing = json.load(open(QF, encoding='utf-8'))['questions']
TH_E2 = {x['id']: x for x in existing if x['subtype'] == 'E2'}
BRAND_EN = {'g359': 'DaoNuea', 'g360': 'Kluensiang', 'g361': 'Wongkhojon', 'g362': 'Judchuem'}
for gid, brand in BRAND_EN.items():
    src = TH_E2[gid]
    q = f'Who is the GM of the {brand} brand?'
    emit('E2', 'en', q, src['expected_answer']['must_contain_any_of'], src['ground_truth_row_ids'],
         f"3-hop brand->dept->head (EN counterpart of {gid}): {brand} brand -> its department -> GM.",
         ['bridge', 'brand', 'gm', 'cross_lang'], src=f'E2-EN-{brand}')

# ================= E4 — surname-family (20, all LISTING) =================
# grade.py matches must_contain by naive substring, so a bare count gold ("2")
# would false-pass any response containing that digit (e.g. "20"). Listing form
# is substring-proof: every member is a required AND-group of name variants, so
# the model must surface ALL members. We also attach exact_count so a model that
# *also* states the family size is checked, without the count being the only gate.
sur = defaultdict(list)
for r in R: sur[r['Last Name Thai']].append(r)
USED = {'อภิกอบสุข', 'อมรจงรัก', 'จิตรานนท์ฟ้า', 'วัชรบุญ'}
size3 = sorted([s for s, v in sur.items() if len(v) == 3 and s not in USED])   # 4
size2 = sorted([s for s, v in sur.items() if len(v) == 2 and s not in USED])   # 22
fams = [(s, sur[s]) for s in size3] + [(s, sur[s]) for s in size2[:16]]        # 20 families

n = 1
for j, (s, mem) in enumerate(fams):
    lang = 'th' if j % 2 == 0 else 'en'
    groups = [sorted({m['First Name Thai'], m['First Name English'].title()}) for m in mem]
    if len({tuple(g) for g in groups}) != len(groups):   # members must be name-distinguishable
        fails.append(('E4', s, 'duplicate member first-names')); continue
    q = (f'พนักงานที่นามสกุล {s} มีใครบ้าง ขอชื่อทุกคน' if lang == 'th'
         else f'List everyone with the surname {s} (give all of them).')
    it_idx = len(items)
    emit('E4', lang, q, groups, [m['Employee ID'] for m in mem],
         f'Surname-family listing: {len(mem)} members share {s}; gold requires every member '
         f'(per-member AND-group of first-name variants), substring-proof.',
         ['surname', 'family', 'listing'], src=f'E4-L{n:02d}')
    items[it_idx]['expected_answer']['exact_count'] = len(mem)   # secondary check
    n += 1

if fails:
    print('!! FAILED:', fails); raise SystemExit(1)

out = Path(__file__).parent / 'e_v2_items.json'
json.dump({'questions': items}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
bys = Counter(it['subtype'] for it in items)
byl = Counter(it['language'] for it in items)
print(f'e_v2_items.json: {len(items)} items  {dict(bys)}  lang={dict(byl)}')
for sub in ['E1', 'E2', 'E4']:
    print(f'\n=== {sub} ===')
    for it in items:
        if it['subtype'] != sub: continue
        g = it['expected_answer']['must_contain_any_of']
        gs = f'{len(g)} members (n={it["expected_answer"].get("exact_count")})' if sub == 'E4' else g[0][0]
        print(f"  [{it['language']}] gold={str(gs)[:24]:24} | {it['question'][:64]}")
