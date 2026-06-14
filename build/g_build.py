"""Build + verify Group G (bilingual agentic handling) — G1-G4, airtight.

Anchored on UNIQUE ROLES (Position in English count==1) so each item resolves to
exactly one row; gold derived from that row (can't drift). All grading uses the
existing must_contain_any_of infrastructure:

  G1  Thai Q  -> English-only field (email / unit code / employee id)
      gold = the English value. Tests: surface an English field given a Thai query.
  G2  English Q -> Thai field (nickname / Thai given name)
      gold = Thai value OR its romanization (accept either). Tag records script.
  G3  Code-switched Q (Thai sentence + English noun phrase / field word)
      gold = the answer value.
  G4  Thai Q, English output requested
      gold = ENGLISH name/position tokens ONLY (no Thai variant). A model that
      defaults to Thai output produces the Thai form -> fails. The failure mode
      is the grading signal; no separate "is-english" flag needed.
"""
import csv, json, re
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]
from collections import Counter

ACR = ['CEO', 'CFO', 'CTO', 'CMO', 'COO', 'CPO', 'CHRO', 'VP', 'HR', 'B2B', 'IT']
def disp_role(r):  # title-case position but keep acronyms upper (Ceo -> CEO)
    s = r['Position in English'].title()
    for a in ACR:
        s = re.sub(rf'\b{a.title()}\b', a, s)
    return s

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
posc = Counter(r['Position in English'] for r in R)
BYROLE = {r['Position in English']: r for r in R if posc[r['Position in English']] == 1}

# curated anchors: (role_en exact, en_disp, th_disp)
ANCHORS = [
 ('CHIEF EXECUTIVE OFFICER',        'the CEO',                 'CEO'),
 ('CHIEF FINANCIAL OFFICER',        'the CFO',                 'CFO'),
 ('CHIEF TECHNOLOGY OFFICER',       'the CTO',                 'CTO'),
 ('CHIEF OPERATING OFFICER',        'the COO',                 'COO'),
 ('CHIEF MARKETING OFFICER',        'the CMO',                 'CMO'),
 ('CHIEF PRODUCT OFFICER',          'the CPO',                 'CPO'),
 ('CHIEF HUMAN RESOURCES OFFICER',  'the CHRO',                'CHRO'),
 ('CHIEF OF STAFF',                 'the Chief of Staff',      'Chief of Staff'),
 ('VICE PRESIDENT FINANCE',         'the VP of Finance',       'VP ฝ่ายการเงิน'),
 ('VICE PRESIDENT HUMAN RESOURCES', 'the VP of HR',            'VP ฝ่ายบุคคล'),
 ('VICE PRESIDENT MARKETING',       'the VP of Marketing',     'VP ฝ่ายการตลาด'),
 ('VICE PRESIDENT LEGAL',           'the VP of Legal',         'VP ฝ่ายกฎหมาย'),
 ('VICE PRESIDENT TECHNOLOGY',      'the VP of Technology',    'VP ฝ่ายเทคโนโลยี'),
 ('VICE PRESIDENT OPERATIONS',      'the VP of Operations',    'VP ฝ่ายปฏิบัติการ'),
 ('VICE PRESIDENT LOGISTICS',       'the VP of Logistics',     'VP ฝ่ายโลจิสติกส์'),
 ('VICE PRESIDENT CUSTOMER SUPPORT','the VP of Customer Support','VP ฝ่ายลูกค้าสัมพันธ์'),
 ('VICE PRESIDENT QUALITY',         'the VP of Quality',       'VP ฝ่ายคุณภาพ'),
 ('VICE PRESIDENT FLEET',           'the VP of Fleet',         'VP ฝ่ายขนส่ง'),
 ('EXECUTIVE ASSISTANT TO CEO',     "the CEO's executive assistant", 'ผู้ช่วยผู้บริหารของ CEO'),
 ('EXECUTIVE ASSISTANT TO CFO',     "the CFO's executive assistant", 'ผู้ช่วยผู้บริหารของ CFO'),
 ('EXECUTIVE ASSISTANT TO CTO',     "the CTO's executive assistant", 'ผู้ช่วยผู้บริหารของ CTO'),
 ('EXECUTIVE ASSISTANT TO CMO',     "the CMO's executive assistant", 'ผู้ช่วยผู้บริหารของ CMO'),
]
A = []
for role, en, th in ANCHORS:
    assert role in BYROLE, f'role not unique/found: {role}'
    A.append((BYROLE[role], en, th))

def T(s): return (s or '').strip()
def title(s): return T(s).title()

out, problems = [], []

def add(iid, sub, lang, q, gold_groups, gt, rat, tags):
    for g in gold_groups:
        if not any(x for x in g):
            problems.append(f'{iid}: empty gold group')
    out.append({'id': iid, 'bucket': 'bilingual', 'subtype': sub, 'group': 'G',
        'priority': 'P1', 'language': lang, 'question': q,
        'expected_behavior': 'answer',
        'expected_answer': {'must_contain_any_of': gold_groups, 'must_not_contain': []},
        'ground_truth_row_ids': [gt['Employee ID']], 'rationale': rat, 'tags': tags})

# ---------- G1: Thai Q -> English-only field ----------
g1_fields = ['email', 'unit', 'empid']
for i in range(20):
    r, en, th = A[i % len(A)]
    fld = g1_fields[i % 3]
    if fld == 'email':
        q = f'ขออีเมลของ {th} หน่อยครับ'; val = T(r['Email Address']); lbl = 'email'
    elif fld == 'unit':
        q = f'รหัสหน่วยงาน (unit code) ของ {th} คืออะไรครับ'; val = T(r['Unit']); lbl = 'unit code'
    else:
        q = f'รหัสพนักงาน (employee ID) ของ {th} คือเลขอะไรครับ'; val = T(r['Employee ID']); lbl = 'employee id'
    add(f'G1-{i+1:02d}', 'G1', 'th', q, [[val]], r,
        f'Thai Q for English-only field ({lbl}={val}) of {r["Position in English"]}.',
        ['bilingual', 'th_q_en_field', fld])

# ---------- G2: English Q -> Thai field ----------
g2_fields = ['nickname', 'firstname', 'lastname']
ai = 0
for i in range(20):
    # need nickname populated for the nickname asks
    while True:
        r, en, th = A[ai % len(A)]; ai += 1
        fld = g2_fields[i % 3]
        if fld == 'nickname' and not T(r['Nickname Thai']):
            continue
        break
    if fld == 'nickname':
        q = f"What is {en}'s Thai nickname (ชื่อเล่น)?"
        gold = [[T(r['Nickname Thai']), title(r['Nickname English']), T(r['Nickname English'])]]
        lbl = f"nickname {T(r['Nickname Thai'])}"
    elif fld == 'firstname':
        q = f"What is the Thai given (first) name of {en}?"
        gold = [[T(r['First Name Thai']), title(r['First Name English'])]]
        lbl = f"first name {T(r['First Name Thai'])}"
    else:
        q = f"What is the Thai family (last) name of {en}?"
        gold = [[T(r['Last Name Thai']), title(r['Last Name English'])]]
        lbl = f"last name {T(r['Last Name Thai'])}"
    add(f'G2-{i+1:02d}', 'G2', 'en', q, gold, r,
        f'English Q for Thai field ({lbl}); accept Thai script or romanization.',
        ['bilingual', 'en_q_th_field', fld])

# ---------- G3: code-switched (Thai + English noun phrase) ----------
g3 = ['email', 'ext', 'nickname', 'unit']
ai = 0
for i in range(20):
    while True:
        r, en, th = A[ai % len(A)]; ai += 1
        fld = g3[i % 4]
        if fld == 'nickname' and not T(r['Nickname Thai']):
            continue
        break
    dr = disp_role(r)
    if fld == 'email':
        q = f'ขอ email address ของ {dr} หน่อยครับ'; gold = [[T(r['Email Address'])]]; lbl = 'email'
    elif fld == 'ext':
        q = f'{dr} เบอร์ extension อะไรครับ'; gold = [[T(r['Phone Extension'])]]; lbl = 'ext'
    elif fld == 'nickname':
        q = f'nickname ของ {dr} คืออะไรครับ'
        gold = [[T(r['Nickname Thai']), title(r['Nickname English']), T(r['Nickname English'])]]; lbl = 'nickname'
    else:
        q = f'ช่วยหา unit code ของ {dr} ให้ทีครับ'; gold = [[T(r['Unit'])]]; lbl = 'unit'
    add(f'G3-{i+1:02d}', 'G3', 'th', q, gold, r,
        f'Code-switched Thai+English asking {lbl}; gold={gold[0][0]}.',
        ['bilingual', 'code_switch', fld])

# ---------- G4: Thai Q, English output requested (gold = English form ONLY) ----------
g4 = ['name', 'position', 'name2']
for i in range(20):
    r, en, th = A[i % len(A)]
    fld = g4[i % 3]
    if fld in ('name', 'name2'):
        if fld == 'name':
            q = f'ใครเป็น {th} ของฟ้าใหม่ครับ ช่วยตอบเป็นภาษาอังกฤษด้วยนะครับ'
        else:
            q = f'{th} ชื่อ-นามสกุลภาษาอังกฤษว่าอะไรครับ'
        gold = [[title(r['First Name English'])], [title(r['Last Name English'])]]  # English first AND last, no Thai
        lbl = f"EN name {title(r['First Name English'])} {title(r['Last Name English'])}"
    else:
        q = f'ตำแหน่งของ {th} ภาษาอังกฤษเรียกว่าอะไรครับ'
        gold = [[r['Position in English'].title(), r['Position in English']]]  # English position title only
        lbl = f"EN position {r['Position in English'].title()}"
    add(f'G4-{i+1:02d}', 'G4', 'th', q, gold, r,
        f'Thai Q, English output requested; gold = English form only ({lbl}). '
        f'Thai-default output fails (no English tokens).',
        ['bilingual', 'th_q_en_output', fld])

# ---- report ----
from collections import Counter as C
print(f'Group G: {len(out)} items')
sc = C(i['subtype'] for i in out)
print('per-subtype:', dict(sc))
print('lang:', dict(C(i['language'] for i in out)))
print('PROBLEMS:', problems if problems else 'none')
# sample one per subtype
for s in ['G1', 'G2', 'G3', 'G4']:
    ex = next(i for i in out if i['subtype'] == s)
    print(f"  {ex['id']} [{ex['language']}] {ex['question']}  -> {ex['expected_answer']['must_contain_any_of']}")
json.dump({'questions': out}, open(Path(__file__).parent / 'g_items.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('wrote g_items.json')
