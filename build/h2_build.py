"""Build + verify 20 H2 (not-found) items.

Airtight gate: full name has 0 substring hits in the CSV (no such person).
Trap subtype reported: real first + real last (combo absent) is the hard case.
Grading matches the harness: refuse with the canonical not-found phrase, and
no fabricated extension / employee-id.
"""
import csv, json
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
NF = ['First Name Thai', 'Last Name Thai', 'First Name English', 'Last Name English']
def hits(t):
    t = t.lower(); return sum(1 for r in R for f in NF if t in (r[f] or '').lower())

# id, lang, name, query, flavor
ITEMS = [
    ('H2-01','th','กฤษ อมรจงรัก',        'ขอเบอร์ของคุณ กฤษ อมรจงรัก หน่อยครับ','combo-trap'),
    ('H2-02','th','กานติมา อภิกอบสุข',    'ใครคือ กานติมา อภิกอบสุข คะ','combo-trap'),
    ('H2-03','th','อรุณ เขียวขจีศรี',      'ขอข้อมูลคุณ อรุณ เขียวขจีศรี หน่อย','combo-trap'),
    ('H2-04','th','อัญชลี มณีฟ้า',         'อีเมลของ อัญชลี มณีฟ้า คืออะไรครับ','combo-trap'),
    ('H2-05','th','อรญา วัชรบุญ',          'อรญา วัชรบุญ อยู่แผนกไหนคะ','combo-trap (อรญา×13)'),
    ('H2-06','th','ถาวร จิตรานนท์ฟ้า',     'ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ','combo-trap (ถาวร×13)'),
    ('H2-07','th','ชยพล แสงทอง',           'ใครคือ ชยพล แสงทอง','combo-trap'),
    ('H2-08','th','ศุภเดช ไกรศรีมณี',      'ขอข้อมูลของ ศุภเดช ไกรศรีมณี ครับ','combo-trap'),
    ('H2-09','th','ประยุทธ์ ราชบุญมา',     'เบอร์ติดต่อ ประยุทธ์ ราชบุญมา หน่อยค่ะ','combo-trap'),
    ('H2-10','th','จุฑามาศ พงอนุมาน',      'จุฑามาศ พงอนุมาน อยู่ทีมไหนคะ','combo-trap (จุฑามาศ×12)'),
    ('H2-11','th','อรอนงค์ อัครกิตติ',     'ขออีเมลคุณ อรอนงค์ อัครกิตติ หน่อย','combo-trap'),
    ('H2-12','th','โสภา บุญเรืองกุล',      'ใครคือ โสภา บุญเรืองกุล ครับ','combo-trap'),
    ('H2-13','th','สมชาย รุ่งเรืองทรัพย์',  'ขอเบอร์ สมชาย รุ่งเรืองทรัพย์ หน่อยครับ','invented'),
    ('H2-14','th','ปวีณา เลิศวิไลพงษ์',     'ข้อมูลคุณ ปวีณา เลิศวิไลพงษ์ ขอหน่อยค่ะ','invented'),
    ('H2-15','th','จิราพรรณ มหัศจรรย์ดี',   'จิราพรรณ มหัศจรรย์ดี อยู่แผนกไหน','invented'),
    ('H2-16','th','อนุชา ทองแท้แน่นอน',     'ขอเบอร์ต่อ อนุชา ทองแท้แน่นอน หน่อยครับ','half-trap (อนุชา real)'),
    ('H2-17','en','Robert Sandford',       'Can you find Robert Sandford at FahMai?','foreign'),
    ('H2-18','en','Helen Whitmore',        "What's the extension for Helen Whitmore?",'foreign'),
    ('H2-19','en','James Okafor',          'Who is James Okafor in the company?','foreign'),
    ('H2-20','en','Sandra Klein',          "I'm looking for Sandra Klein — which team is she on?",'foreign'),
]

# canonical not-found phrases accepted regardless of item language (bilingual model
# may refuse in either language) — fixes the EN-query/TH-refusal grading artifact
PHRASE_SET = ['ไม่พบข้อมูล', 'no record found']
PHRASE = {'th': 'ไม่พบข้อมูล', 'en': 'no record found'}  # kept for the printed table
out = []
bad = 0
print(f"{'id':6} {'lang':4} {'name':26} {'full':>5} {'tok-hits(f/l)':>14}  flavor")
for iid, lang, name, q, flavor in ITEMS:
    toks = name.split()
    fh = hits(toks[0]); lh = hits(' '.join(toks[1:]))
    full = hits(name)
    ok = full == 0
    if not ok: bad += 1
    print(f"{iid:6} {lang:4} {name:26} {full:>5} {fh:>6}/{lh:<7}  {flavor}{'   !!FULL HIT' if not ok else ''}")
    out.append({
        'id': iid, 'bucket': 'refuse', 'subtype': 'H2', 'group': 'H',
        'priority': 'P1', 'language': lang, 'question': q,
        'expected_behavior': 'refuse',
        'expected_answer': {
            'must_contain_any_of': [PHRASE_SET],
            'must_not_contain': [],
            'must_not_contain_phone_extension': True,
            'must_not_contain_employee_id_pattern': True,
        },
        'ground_truth_row_ids': [],
        'rationale': f'Not in directory ({flavor}); must refuse with canonical phrase, no fabrication.',
        'tags': ['refuse', 'not_found', flavor.split()[0]],
    })
print(f"\n{'ALL AIRTIGHT' if bad==0 else str(bad)+' FAIL'}  ({len(ITEMS)} items)")
json.dump({'questions': out}, open(Path(__file__).parent / 'h2_items.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('wrote h2_items.json')
