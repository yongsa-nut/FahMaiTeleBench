"""Build + verify E5 — DEEP / COMPOSITE multi-hop (harder than E1's two-hop).

Builds against employees_v02.csv (the KB the v0.2 questions run on), NOT the frozen v01.

The CSV has NO manager edge (locked E1/E3 design), so a *strictly necessary* chain caps at
~2 joins. E5 gets its difficulty from (a) deeply-NESTED reference resolution that terminates at a
THIRD person, and (b) COMPOSITE items that fuse an aggregation with a relational hop (no shortcut):

  Pattern 1 — 4-level nested secretary (terminal = 3rd person):
    IC X  ->  X's Department  ->  that dept's VP  ->  the VP's secretary  ->  secretary's attribute.
    Airtight: single-VP dept; exactly one "SECRETARY OF <D>VP" row; IC name globally unique.
    Anti-shortcut: gold (secretary's attr) != IC's own attr (different people).

  Pattern 2 — composite superlative + hop (NO shortcut):
    argmax/argmin over a named set of single-VP depts (by headcount)  ->  that dept's VP  ->  attr.
    Airtight: the extremum dept is unique AND single-VP.

  Pattern 3 — section-senior attribute, IC anchor (aggregation + attribute):
    IC X  ->  X's Section  ->  the most-senior person in that section  ->  that person's attribute.
    Section named explicitly (avoid the deliberate E1 grain ambiguity). Airtight: unique section
    senior, surname-unique in section. Anti-shortcut: senior's attr != IC's attr.

All golds are an ATTRIBUTE (ext / email / nickname) so the first/intermediate hops' own values differ.
"""
import csv, json
from collections import defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees_v02.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
RANK = {'C-level': 5, 'VP': 4, 'Director': 3, 'Manager': 2, 'Lead': 1, 'IC': 0}
def G(r, k): return r.get(k, '')
def nm(r): return f"{G(r,'First Name Thai')} {G(r,'Last Name Thai')}"

fullname_count = defaultdict(int)
for r in R: fullname_count[(G(r,'First Name Thai'), G(r,'Last Name Thai'))] += 1
def uniq_name(r): return fullname_count[(G(r,'First Name Thai'), G(r,'Last Name Thai'))] == 1

# single-VP depts + their VP
vp_by_dept = defaultdict(list)
for r in R:
    if G(r,'Position Level') == 'VP': vp_by_dept[G(r,'Department')].append(r)
SINGLE_VP = {d: v[0] for d, v in vp_by_dept.items() if len(v) == 1}

# the unique "SECRETARY OF <D>VP" per single-VP dept
sec_of_vp = {}
for r in R:
    pos = G(r,'Position in English').upper().strip()
    if pos.startswith('SECRETARY OF') and pos.endswith('VP'):
        code = pos.replace('SECRETARY OF', '').strip()        # e.g. FINVP
        d = code[:-2]                                          # FIN
        if d in SINGLE_VP:
            sec_of_vp.setdefault(d, []).append(r)
SEC_OF_VP = {d: v[0] for d, v in sec_of_vp.items() if len(v) == 1}

by_dept = defaultdict(list)
for r in R: by_dept[G(r,'Department')].append(r)
sec_rows = defaultdict(list)
for r in R: sec_rows[G(r,'Section')].append(r)

problems, items = [], []

def attr_val(r, attr):
    return {'ext': G(r,'Phone Extension'), 'email': G(r,'Email Address'),
            'nick': G(r,'Nickname Thai')}[attr]

def gold_for(r, attr):
    if attr == 'nick':
        nicks = [x for x in (G(r,'Nickname Thai'), G(r,'Nickname English').title()) if x]
        return [nicks]
    return [[attr_val(r, attr)]]

def emit(iid, lang, q, gold, gt_ids, rat, tags, anchor=None, anchor_attr=None, terminal=None):
    # anti-shortcut: terminal's chosen attr must differ from the anchor's same field
    if anchor is not None and anchor_attr in ('ext', 'email'):
        if attr_val(anchor, anchor_attr) == attr_val(terminal, anchor_attr):
            problems.append(f'{iid}: anchor {anchor_attr} == terminal (shortcut!)'); return
    if not gold or not gold[0] or not gold[0][0]:
        problems.append(f'{iid}: empty gold'); return
    items.append({'id': iid, 'bucket': 'deep_multihop', 'subtype': 'E5', 'group': 'E',
        'priority': 'P2', 'language': lang, 'question': q, 'expected_behavior': 'answer',
        'expected_answer': {'must_contain_any_of': gold, 'must_not_contain': []},
        'ground_truth_row_ids': gt_ids, 'rationale': rat, 'tags': tags})

DEPT_LABEL = {'DN': ('แผนก Daonuea (DN)', 'the Daonuea (DN) department'),
              'JC': ('แผนก Judchuem (JC)', 'the Judchuem (JC) department'),
              'KS': ('แผนก Kluensiang (KS)', 'the Kluensiang (KS) department'),
              'WK': ('แผนก Wongkhojon (WK)', 'the Wongkhojon (WK) department'),
              'FIN': ('ฝ่ายการเงิน (FIN)', 'the Finance (FIN) department'),
              'HR': ('ฝ่ายทรัพยากรบุคคล (HR)', 'the HR department'),
              'LEG': ('ฝ่ายกฎหมาย (LEG)', 'the Legal (LEG) department'),
              'SF': ('แผนก Saifah (SF)', 'the Saifah (SF) department')}

# ============ Pattern 1 — 4-level nested secretary (terminal = 3rd person) ============
ATTRS = [('ext', 'th'), ('email', 'en'), ('nick', 'th'), ('ext', 'en'), ('email', 'th'), ('nick', 'en')]
# SF (largest) + LEG (smallest) are reserved for the composite-superlative items below → exclude here
p1_depts = [d for d in ('DN', 'FIN', 'HR', 'KS', 'WK', 'JC') if d in SEC_OF_VP]
idx = 1
made = 0
for d in p1_depts:
    if made >= 6: break
    vp = SINGLE_VP[d]; sec = SEC_OF_VP[d]
    attr, lang = ATTRS[made % len(ATTRS)]
    if attr == 'nick' and not G(sec, 'Nickname Thai'):
        attr = 'ext'                                          # secretary has no nickname -> fall back
    ics = [r for r in by_dept[d] if G(r,'Position Level') == 'IC' and uniq_name(r)
           and G(r,'Employee ID') not in (vp['Employee ID'], sec['Employee ID'])
           and attr_val(r, attr if attr != 'nick' else 'ext')]
    if not ics:
        continue
    ic = ics[0]
    val = gold_for(sec, attr)
    thlab, enlab = DEPT_LABEL.get(d, (f'แผนก {d}', f'the {d} department'))
    if lang == 'th':
        head = {'ext': 'ขอเบอร์ต่อของ', 'email': 'ขออีเมลของ', 'nick': 'ขอชื่อเล่นของ'}[attr]
        q = f'{head}เลขานุการของรองประธานฝ่ายที่คุณ{nm(ic)}สังกัดอยู่หน่อยครับ'
    else:
        what = {'ext': "the phone extension", 'email': "the email", 'nick': "the nickname"}[attr]
        q = f"What's {what} of the secretary of the VP who heads the department that {nm(ic)} works in?"
    emit(f'E5-{idx:02d}', lang, q, val, [ic['Employee ID'], vp['Employee ID'], sec['Employee ID']],
         f"4-level nested: {nm(ic)} -> dept {d} -> VP {nm(vp)} -> VP's secretary {nm(sec)} -> {attr}={val[0]}. "
         f"Terminal is a 3rd person; anchor's own {attr} differs.",
         ['multi_hop', 'deep', 'nested_secretary', f'attr_{attr}'],
         anchor=ic, anchor_attr=(attr if attr != 'nick' else None), terminal=sec)
    idx += 1; made += 1

# ===== Patterns 2+3 — composite superlative -> VP, and -> VP's secretary (deepest, no shortcut) =====
sv_sizes = {d: len(by_dept[d]) for d in SINGLE_VP if d != 'CEO' and d in SEC_OF_VP}
vals = sorted(sv_sizes.values())
big = max(sv_sizes, key=sv_sizes.get); small = min(sv_sizes, key=sv_sizes.get)
facts = []                                                          # (sup_en, sup_th, dept) — unique extrema only
if vals.count(sv_sizes[big]) == 1:   facts.append(('the most', 'มากที่สุด', big))
else: problems.append('P2 largest dept not unique')
if vals.count(sv_sizes[small]) == 1: facts.append(('the fewest', 'น้อยที่สุด', small))
else: problems.append('P2 smallest dept not unique')

PLAN = [('vp', 'email', 'en'), ('sec', 'ext', 'th'), ('sec', 'nick', 'en'),
        ('vp', 'ext', 'th'), ('sec', 'email', 'en'), ('sec', 'ext', 'th')]
pi = 0
for sup_en, sup_th, d in facts:
    vp = SINGLE_VP[d]; sec = SEC_OF_VP[d]
    for _ in range(3):
        depth, attr, lang = PLAN[pi % len(PLAN)]; pi += 1
        tgt = vp if depth == 'vp' else sec
        if attr == 'nick' and not G(tgt, 'Nickname Thai'): attr = 'ext'
        val = gold_for(tgt, attr)
        if lang == 'th':
            head = {'email': 'ขออีเมล', 'ext': 'ขอเบอร์ต่อ', 'nick': 'ขอชื่อเล่น'}[attr]
            who = 'รองประธานของแผนกนั้น' if depth == 'vp' else 'เลขานุการของรองประธานของแผนกนั้น'
            q = f'ในบรรดาแผนกที่มีรองประธาน (VP) เป็นหัวหน้า แผนกที่มีพนักงาน{sup_th} {head}ของ{who}หน่อยครับ'
        else:
            what = {'email': 'email', 'ext': 'phone extension', 'nick': 'nickname'}[attr]
            who = "that department's VP" if depth == 'vp' else "the secretary of that department's VP"
            q = (f"Among the departments headed by a VP, take the one with {sup_en} employees — "
                 f"what's the {what} of {who}?")
        chain = f"argmax/argmin headcount over VP-headed depts = {d} (n={sv_sizes[d]}, unique) -> VP {nm(vp)}"
        gt = [vp['Employee ID']] if depth == 'vp' else [vp['Employee ID'], sec['Employee ID']]
        if depth == 'sec': chain += f" -> secretary {nm(sec)}"
        emit(f'E5-{idx:02d}', lang, q, val, gt,
             f"Composite superlative{'+nested secretary' if depth == 'sec' else ''}: {chain} -> {attr}={val[0]}.",
             ['multi_hop', 'deep', 'superlative_hop' if depth == 'vp' else 'nested_superlative', f'attr_{attr}'])
        idx += 1

from collections import Counter
print(f'E5 items: {len(items)}')
print('by pattern:', dict(Counter(t for it in items for t in it['tags'] if t in
      ('nested_secretary', 'superlative_hop', 'section_senior_attr'))))
print('by lang:', dict(Counter(it['language'] for it in items)))
print()
for it in items:
    g = it['expected_answer']['must_contain_any_of'][0]
    print(f"  {it['id']} [{it['language']}] ans={str(g)[:30]:30} | {it['question'][:66]}")
print('\nPROBLEMS:', problems if problems else 'none')
json.dump({'questions': items}, open(Path(__file__).parent / 'e5_items.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('wrote e5_items.json')
