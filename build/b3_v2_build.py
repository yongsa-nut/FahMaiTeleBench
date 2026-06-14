"""Build the 20 B3 items for the v2 set (10 easy + 10 hard), derived from CSV.

Selects 10 of the 20 locked easy-tier items (mechanism/field/language spread, no
employee overlap with the hard tier) + all 10 hard-tier items. Gold values and
hard-tier distractors are read from the CSV (not hardcoded), and every item is
re-verified airtight (variant = 0 name-field hits) before emit. Aborts on any fail.

Output -> b3_v2_items.json ({'questions':[...]}), ready for the generic appender.
"""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
NF = ['First Name Thai', 'Last Name Thai', 'First Name English', 'Last Name English']
TGT = {'email': 'Email Address', 'ext': 'Phone Extension', 'office': 'Office Location'}

def hits(t):
    t = t.lower()
    return sum(1 for r in R for f in NF if t in (r[f] or '').lower())
def find(eid):
    return next(r for r in R if r['Employee ID'] == eid)
byfirst = defaultdict(list)
for r in R:
    byfirst[r['First Name English']].append(r)
poscount = Counter(r['Position in English'] for r in R)

# --- 10 easy-tier picks: (id, emp_id, variant, mech, lang, target, question) ---
EASY = [
 ('B3-001','00009440','Chaisonsavang','w->v','en','email',
  "Hi, do you have the email of Khun Kamala Chaisonsavang, our CFO?"),
 ('B3-002','08392510','Jutamas','drop-H(th)','th','ext',
  "เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ"),
 ('B3-003','00006662','Pongchongrak','drop-H(ph)','en','office',
  "Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?"),
 ('B3-004','00001544','Tanida','drop-H(th)','th','email',
  "ขอ email ของ Tanida เลขา COO หน่อยครับ"),
 ('B3-008','00003437','Ritichai','collapse','en','ext',
  "Ext of Ritichai Kaewsaiphinyo (our CTO) please?"),
 ('B3-014','00002568','Sukum','drop-H(kh)','th','email',
  "ขออีเมลของคุณ Sukum Suwanfahsai manager ทีม chat support หน่อยค่ะ"),
 ('B3-015','00008000','Viriya','w->v','en','ext',
  "Can I get the extension for Viriya Chanchai, VP of Retail Network?"),
 ('B3-017','08868941','Ladawan','collapse','en','office',
  "Where's Ladawan Samphat's office? She's the EA to our CHRO."),
 ('B3-018','08672839','Bunnamngam','oo->u','th','ext',
  "เบอร์ต่อของคุณ Sombat Bunnamngam manager ทีม data scientist เบอร์อะไรครับ"),
 ('B3-019','08583872','Suphawadi','ee->i','en','email',
  "Could you share the email of Suphawadi Bundaorueng, the secretary to the WK VP?"),
]

# --- 10 hard-tier picks: (id, emp_id, variant, mech, lang, target, role, question) ---
HARD = [
 ('B3-H01','08902591','Oraya','collapse','th','email',"CEO's EA",
  "ขออีเมลของคุณ Oraya เลขาของ CEO หน่อยค่ะ"),
 ('B3-H02','00005427','Thavan','w->v','en','ext','GM of Saifah',
  "What's the extension for Thavan, the GM of Saifah?"),
 ('B3-H03','08863943','Vaen','w->v','th','ext','Director of Escalations (Support)',
  "ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ"),
 ('B3-H04','00001359','Natamon','drop-H(th)','en','email','CHRO',
  "Could you get me Natamon's email? She's our CHRO."),
 ('B3-H05','00003012','Nattakan','drop-H(th)','th','office','VP Logistics',
  "คุณ Nattakan VP Logistics นั่งตึกไหนชั้นไหนคะ"),
 ('B3-H06','08427848','Wipa','drop-H(ph)','th','ext','secretary to the VP of Logistics',
  "ขอเบอร์ต่อของคุณ Wipa เลขาฯ ของ VP Logistics หน่อยค่ะ"),
 ('B3-H07','08765852','Sompong','drop-H(ph)','en','ext','VP of Digital Marketing',
  "Can I get the extension for Sompong, the VP of Digital Marketing?"),
 ('B3-H08','08612584','Meka','drop-H(kh)','en','email','Director of Accounts Receivable',
  "What's Meka's email — the Director of Accounts Receivable?"),
 ('B3-H09','08210238','Ravi','ee->i','en','ext','Director of Support Training',
  "Ravi, the Director of Support Training — what's his extension?"),
 ('B3-H10','00007097','Natanicha','collapse','th','email','secretary to the VP of Upcountry Retail',
  "ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ"),
]

items, fails = [], []

for pid, eid, var, mech, lang, tgt, q in EASY:
    r = find(eid); gold = r[TGT[tgt]]; h = hits(var)
    if h != 0 or not gold:
        fails.append((pid, 'hits', h)); continue
    items.append({
        'bucket': 'noisy_name_form', 'subtype': 'B3', 'group': 'B',
        'v01_bucket': 'noisy_name_form', 'priority': 'P1', 'language': lang, 'question': q,
        'expected_behavior': 'answer',
        'expected_answer': {'must_contain_any_of': [[gold]], 'must_not_contain': []},
        'ground_truth_row_ids': [eid],
        'rationale': f"Noisy romanization '{var}' ({mech}) = 0 name-field hits -> must normalize; "
                     f"full canonical name+role resolves uniquely. gold={tgt} {gold!r}.",
        'tags': ['noisy_name', 'transliteration', mech.replace('->', '_').replace('(', '_').replace(')', ''),
                 tgt, 'easy_tier', 'retry_t1'],
        'authored': '2026-05-24', 'src_id': pid,
    })

for pid, eid, var, mech, lang, tgt, role, q in HARD:
    r = find(eid); fn = r['First Name English']; homs = byfirst[fn]
    gold = r[TGT[tgt]]; h = hits(var)
    role_unique = poscount[r['Position in English']] == 1
    distractors = sorted({e[TGT[tgt]] for e in homs if e['Employee ID'] != eid and e[TGT[tgt]]})
    gold_unique = gold and gold not in distractors
    if not (h == 0 and role_unique and gold_unique):
        fails.append((pid, f'h={h} role_uniq={role_unique} gold_uniq={gold_unique}')); continue
    items.append({
        'bucket': 'noisy_name_form', 'subtype': 'B3', 'group': 'B',
        'v01_bucket': 'noisy_name_form', 'priority': 'P1', 'language': lang, 'question': q,
        'expected_behavior': 'answer',
        'expected_answer': {'must_contain_any_of': [[gold]], 'must_not_contain': distractors},
        'ground_truth_row_ids': [eid],
        'rationale': f"Hard tier (B3xD1): shared first name '{fn}' x{len(homs)} homonyms; noisy '{var}' "
                     f"({mech}) = 0 hits -> normalize, then company-unique role '{role}' disambiguates. "
                     f"gold={tgt} {gold!r}; {len(distractors)} homonym {tgt}s as must_not_contain.",
        'tags': ['noisy_name', 'transliteration', mech.replace('->', '_').replace('(', '_').replace(')', ''),
                 tgt, 'hard_tier', 'homonym', 'disambiguation', 'retry_t1'],
        'authored': '2026-05-24', 'src_id': pid,
    })

if fails:
    print('!! FAILED:', fails); raise SystemExit(1)

out = Path(__file__).parent / 'b3_v2_items.json'
json.dump({'questions': items}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'b3_v2_items.json: {len(items)} items (10 easy + 10 hard), ALL airtight')
print('  lang:', dict(Counter(it['language'] for it in items)))
print('  target field:', dict(Counter(it['src_id'][:5] and it['tags'][3] for it in items)))
print('  hard-tier distractor counts:',
      [len(it['expected_answer']['must_not_contain']) for it in items if 'hard_tier' in it['tags']])
