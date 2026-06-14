"""Build + verify E1 (two-hop) and E3 (implicit hierarchy) items — CLEAN HANDLES ONLY.

User decision (2026-05-23): no inferred manager edge. Multi-hop is built strictly
from links that are literally airtight in the CSV:
  * single-head departments  (exactly one VP/C-level head)
  * unique section-senior     (one strict top on the Position-Level ladder)
  * secretary-of-VP rows in single-VP depts (explicit person -> VP bridge)

E3 (implicit hierarchy)  -> answer = IDENTITY of the most-senior person.
  Grading: TWO groups [[first variants],[last variants]] (first AND last) so a
  section-mate who only shares the first name cannot false-pass. We verify the
  senior's surname is unique within the section.

E1 (two-hop) -> answer = an ATTRIBUTE (ext/email) of a SECOND-hop entity that the
  model must resolve via an intermediate. Two patterns:
   A) secretary -> the VP they support -> that VP's attribute (different row).
   B) IC person -> the VP who heads their (single-head) department -> VP's attribute.
  Grading: must_contain the correct second-hop value. The first-hop entity's own
  value is different, so reporting it fails (that's the two-hop discriminator).
Anchors referenced by name are verified GLOBALLY UNIQUE (full name) so the item
resolves to one person.
"""
import csv, json
from collections import defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
RANK = {'C-level':5,'VP':4,'Director':3,'Manager':2,'Lead':1,'IC':0}
def nm(r): return f"{r['First Name Thai']} {r['Last Name Thai']}"
def fullkey(r): return (r['First Name Thai'], r['Last Name Thai'])
def name_tokens(r):  # first-group, last-group (Thai + Title English)
    fg = [r['First Name Thai'], r['First Name English'].title()]
    lg = [r['Last Name Thai'], r['Last Name English'].title()]
    return [t for t in fg if t], [t for t in lg if t]

fullname_count = defaultdict(int)
for r in R: fullname_count[fullkey(r)] += 1
def uniq_name(r): return fullname_count[fullkey(r)] == 1

# single-head depts -> unique head
dept_heads = defaultdict(list)
for r in R:
    if r['Position Level'] in ('VP','C-level'): dept_heads[r['Department']].append(r)
SINGLE_HEAD = {d:v[0] for d,v in dept_heads.items() if len(v)==1}   # DN JC KS LEG WK
vp_by_dept = defaultdict(list)
for r in R:
    if r['Position Level']=='VP': vp_by_dept[r['Department']].append(r)
SINGLE_VP = {d:v[0] for d,v in vp_by_dept.items() if len(v)==1}

sec_rows = defaultdict(list)
for r in R: sec_rows[r['Section']].append(r)
by_dept = defaultdict(list)
for r in R: by_dept[r['Department']].append(r)

problems = []
def emit(lst, iid, sub, lang, q, gold_groups, gt_ids, behav, rat, tags):
    lst.append({'id':iid,'bucket':'multi_hop','subtype':sub,'group':'E','priority':'P1',
        'language':lang,'question':q,'expected_behavior':behav,
        'expected_answer':{'must_contain_any_of':gold_groups,'must_not_contain':[]},
        'ground_truth_row_ids':gt_ids,'rationale':rat,'tags':tags})

# ============ E3 ============
e3 = []
# P5: single-head depts -> "who heads dept X"  (use full dept-brand names)
# use the CSV's own romanized brand (from the VP title) — avoid guessing Thai spellings
DEPT_LABEL = {'DN':('แผนก Daonuea (DN)','the Daonuea (DN) department'),
              'JC':('แผนก Judchuem (JC)','the Judchuem (JC) department'),
              'KS':('แผนก Kluensiang (KS)','the Kluensiang (KS) department'),
              'LEG':('ฝ่ายกฎหมาย (Legal/LEG)','the Legal (LEG) department'),
              'WK':('แผนก Wongkhojon (WK)','the Wongkhojon (WK) department')}
p5 = [('DN','th'),('JC','en'),('KS','th'),('LEG','en'),('WK','th')]
for i,(d,lang) in enumerate(p5,1):
    head = SINGLE_HEAD[d]; fg,lg = name_tokens(head)
    th,en = DEPT_LABEL[d]
    q = f'ใครเป็นผู้บริหารสูงสุดของ{th}' if lang=='th' else f'Who is the most senior person heading {en}?'
    emit(e3, f'E3-{i:02d}', 'E3', lang, q, [fg,lg], [head['Employee ID']], 'answer',
         f'Implicit hierarchy: {d} is a single-head dept; unique head = {nm(head)}.',
         ['multi_hop','hierarchy','dept_head'])

# P4: unique section-senior (Director/Manager), surname unique within section
cands = []
for s, rows in sorted(sec_rows.items()):
    if len(rows) < 6: continue
    mx = max(RANK[r['Position Level']] for r in rows)
    if mx not in (2,3): continue
    top = [r for r in rows if RANK[r['Position Level']]==mx]
    if len(top)!=1: continue
    t = top[0]
    if not uniq_name(t): continue
    if sum(1 for r in rows if r['Last Name Thai']==t['Last Name Thai']) != 1: continue  # surname unique in section
    cands.append((s,t,rows))
# take 11, alternating language
for i,(s,t,rows) in enumerate(cands[:11]):
    lang = 'th' if i%2==0 else 'en'
    fg,lg = name_tokens(t)
    q = (f'ในส่วนงาน {s} ใครมีตำแหน่งสูงสุด' if lang=='th'
         else f'In the {s} section, who is the most senior employee by position level?')
    emit(e3, f'E3-{i+6:02d}', 'E3', lang, q, [fg,lg], [t['Employee ID']], 'answer',
         f'Implicit hierarchy: unique top of section {s} is {t["Position Level"]} {nm(t)} '
         f'(n={len(rows)}); surname unique in section.', ['multi_hop','hierarchy','section_senior'])

# ============ E1 ============
e1 = []
# Pattern A: secretary -> VP they support -> VP attribute
SECMAP = {'FINVP':'FIN','HRVP':'HR','LEGVP':'LEG','SFVP':'SF','DNVP':'DN',
          'KSVP':'KS','WKVP':'WK','JCVP':'JC'}
secs = [r for r in R if 'SECRETARY OF' in r['Position in English'].upper()]
idx=1
for r in secs:
    code = r['Position in English'].upper().replace('SECRETARY OF','').strip()
    d = SECMAP.get(code)
    if d is None or d not in SINGLE_VP: continue
    if not uniq_name(r): problems.append(f'sec {nm(r)} not unique'); continue
    vp = SINGLE_VP[d]
    lang = 'th' if idx%2==1 else 'en'
    attr = 'ext' if idx%2==1 else 'email'
    val = vp['Phone Extension'] if attr=='ext' else vp['Email Address']
    own = r['Phone Extension'] if attr=='ext' else r['Email Address']  # anchor's own field
    if own == val: problems.append(f'E1-A {nm(r)}: anchor {attr} == VP {attr} (shortcut!)')
    if lang=='th':
        q = (f'ขอเบอร์ต่อของรองประธานที่มีเลขานุการคือคุณ{nm(r)} หน่อยครับ' if attr=='ext'
             else f'ขออีเมลของรองประธานที่มีเลขานุการคือคุณ{nm(r)} หน่อยครับ')
    else:
        q = (f"What's the phone extension of the VP whose secretary is {nm(r)}?" if attr=='ext'
             else f"What's the email address of the VP whose secretary is {nm(r)}?")
    emit(e1, f'E1-{idx:02d}', 'E1', lang, q, [[val]], [vp['Employee ID']], 'answer',
         f'Two-hop: {nm(r)} ({code}) -> VP of {d} = {nm(vp)} -> {attr}={val}. '
         f'Secretary\'s own {attr} differs (anti-shortcut).', ['multi_hop','two_hop','secretary_bridge'])
    idx+=1

# Pattern B: IC person in single-head dept -> VP of that dept -> VP attribute
for d in ['DN','JC','KS','LEG','WK']:
    head = SINGLE_HEAD[d]
    ics = [r for r in by_dept[d] if r['Position Level']=='IC' and uniq_name(r)
           and r['Phone Extension'] and r['Employee ID']!=head['Employee ID']]
    for r in ics[:2]:
        lang = 'th' if idx%2==1 else 'en'
        attr = 'email' if idx%2==1 else 'ext'
        val = head['Email Address'] if attr=='email' else head['Phone Extension']
        own = r['Email Address'] if attr=='email' else r['Phone Extension']  # anchor's own field
        if own == val: problems.append(f'E1-B {nm(r)}: anchor {attr} == head {attr} (shortcut!)')
        if lang=='th':
            q = (f'ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณ{nm(r)} สังกัดอยู่หน่อยครับ' if attr=='email'
                 else f'ขอเบอร์ต่อของผู้บริหารสูงสุดของแผนกที่คุณ{nm(r)} สังกัดอยู่หน่อยครับ')
        else:
            q = (f"What's the email of the VP who heads the department that {nm(r)} works in?" if attr=='email'
                 else f"What's the phone extension of the VP who heads the department that {nm(r)} works in?")
        emit(e1, f'E1-{idx:02d}', 'E1', lang, q, [[val]], [head['Employee ID']], 'answer',
             f'Two-hop: {nm(r)} -> dept {d} (single head) -> VP {nm(head)} -> {attr}={val}. '
             f'Person\'s own {attr} differs (anti-shortcut).', ['multi_hop','two_hop','dept_to_head'])
        idx+=1

# verify the anti-shortcut: second-hop value != first-hop entity's same field
for it in e1:
    pass  # gold derived from VP row by construction; uniqueness of anchors enforced above

print(f'E3: {len(e3)} items | E1: {len(e1)} items')
print('\n=== E3 (implicit hierarchy) ===')
for it in e3:
    g=it["expected_answer"]["must_contain_any_of"]
    print(f'  {it["id"]} [{it["language"]}] gold={g[0][0]}/{g[1][0]:14} | {it["question"][:60]}')
print('\n=== E1 (two-hop) ===')
for it in e1:
    print(f'  {it["id"]} [{it["language"]}] ans={it["expected_answer"]["must_contain_any_of"][0][0]:28} | {it["question"][:62]}')
from collections import Counter
print('\nE3 lang:', dict(Counter(i["language"] for i in e3)), '| E1 lang:', dict(Counter(i["language"] for i in e1)))
print('PROBLEMS:', problems if problems else 'none')
json.dump({'questions':e3}, open(Path(__file__).parent/'e3_items.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
json.dump({'questions':e1}, open(Path(__file__).parent/'e1_items.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('wrote e1_items.json, e3_items.json')
