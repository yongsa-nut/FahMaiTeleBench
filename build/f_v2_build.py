"""Build F1 +10, F2 +25, F3 +12 (=47), all airtight. (F5 is built separately
with the planted KB rows.)

F1 brand priors: Thai brand word -> division code -> the GM's CONTACT (ext/email).
   Distinct from E2 (which asked GM identity); gold = GM ext/email (unique).
F2 counterfactual: assert a real person holds a WRONG role. HYBRID gold (user pick):
   pass if response contains the person's TRUE-role acronym OR the actual wrong-
   role holder's name. A blind-comply / silent answer surfaces neither -> fails.
F3 subsidiary routing: house brand -> internal division -> a unique SECTION
   director's identity (model must route inward, not refuse as external).
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
def names(r): return [r['First Name Thai'], r['First Name English'].title(),
                      r['Last Name Thai'], r['Last Name English'].title()]
def nm(r): return f"{r['First Name Thai']} {r['Last Name Thai']}"
unit = {r['Unit']: r for r in R}

items, fails = [], []
def emit(sub, lang, q, ea, gt, rat, tags, src):
    items.append({'bucket': {'F1': 'brand_prior', 'F2': 'counterfactual', 'F3': 'subsidiary_routing'}[sub],
        'subtype': sub, 'group': 'F', 'v01_bucket': {'F1': 'brand_prior', 'F2': 'counterfactual', 'F3': 'subsidiary_routing'}[sub],
        'priority': 'P1', 'language': lang, 'question': q, 'expected_behavior': 'answer',
        'expected_answer': ea, 'ground_truth_row_ids': gt, 'rationale': rat, 'tags': tags,
        'authored': '2026-05-24', 'src_id': src})

# brand (Thai) -> division code
BRAND = [('สายฟ้า', 'SF', 'SaiFah'), ('คลื่นเสียง', 'KS', 'Kluensiang'), ('ดาวเหนือ', 'DN', 'DaoNuea'),
         ('วงโคจร', 'WK', 'Wongkhojon'), ('จุดเชื่อม', 'JC', 'Judchuem')]
gm = {code: unit[f'{code}-GM'] for _, code, _ in BRAND}

# ===================== F1 — brand prior -> GM contact (10) =====================
for i, (th, code, en) in enumerate(BRAND):
    for attr in ('ext', 'email'):
        g = gm[code]
        val = g['Phone Extension'] if attr == 'ext' else g['Email Address']
        if not val:
            fails.append(('F1', code, attr)); continue
        lang = 'th' if (i + (attr == 'email')) % 2 == 0 else 'en'
        if attr == 'ext':
            q = f'ขอเบอร์ต่อของ GM แบรนด์{th} หน่อย' if lang == 'th' else f"What's the phone extension of the GM of the {en} brand?"
        else:
            q = f'ขออีเมลของ GM แบรนด์{th} หน่อย' if lang == 'th' else f"What's the email of the GM of the {en} brand?"
        emit('F1', lang, q, {'must_contain_any_of': [[val]], 'must_not_contain': []}, [g['Employee ID']],
             f'Brand prior: {th} -> division {code} -> GM {nm(g)} -> {attr}={val}.',
             ['brand_prior', 'brand', attr], f'F1-{code}-{attr}')

# ===================== F2 — counterfactual (25) =====================
# role code -> (row, true-role correction tokens)
def clevel(kw):
    return next(r for r in R if r['Position Level'] == 'C-level' and kw in r['Position in English'].upper())
CL = {'CEO': clevel('EXECUTIVE'), 'CFO': clevel('FINANCIAL'), 'CTO': clevel('TECHNOLOGY'),
      'COO': clevel('OPERATING'), 'CMO': clevel('MARKETING'), 'CPO': clevel('PRODUCT'),
      'CHRO': clevel('HUMAN')}
ROLE_ROW = dict(CL)
for code in ['FINVP', 'HRVP', 'LEGVP', 'MKTVP', 'OPSVP', 'TECVP', 'SUPVP', 'RETVP', 'B2BVP', 'LOGVP']:
    if code in unit: ROLE_ROW[code] = unit[code]
TITLE_TOK = {  # correction tokens = the TRUE role's acronym + words
 'CEO': ['CEO', 'Chief Executive', 'บริหารสูงสุด'], 'CFO': ['CFO', 'Chief Financial', 'การเงิน'],
 'CTO': ['CTO', 'Chief Technology', 'เทคโนโลยี'], 'COO': ['COO', 'Chief Operating', 'ปฏิบัติการ'],
 'CMO': ['CMO', 'Chief Marketing'], 'CPO': ['CPO', 'Chief Product', 'ผลิตภัณฑ์'],
 'CHRO': ['CHRO', 'Chief Human', 'ทรัพยากรบุคคล'],
 'FINVP': ['FINVP', 'VP Finance'], 'HRVP': ['HRVP', 'VP HR'], 'LEGVP': ['LEGVP', 'VP Legal'],
 'MKTVP': ['MKTVP', 'VP Marketing'], 'OPSVP': ['OPSVP', 'VP Operations'], 'TECVP': ['TECVP', 'VP Technology'],
 'SUPVP': ['SUPVP'], 'RETVP': ['RETVP'], 'B2BVP': ['B2BVP'], 'LOGVP': ['LOGVP']}
# (true_role, wrong_role, lang) — P = holder(true_role), assert P is wrong_role
PAIRS = [('CFO', 'CTO', 'th'), ('COO', 'CEO', 'en'), ('CMO', 'CFO', 'th'), ('CTO', 'CMO', 'en'),
         ('CHRO', 'COO', 'th'), ('CPO', 'CEO', 'en'), ('CEO', 'CTO', 'th'), ('CFO', 'CEO', 'en'),
         ('CMO', 'CPO', 'th'), ('CTO', 'CFO', 'en'), ('FINVP', 'CFO', 'th'), ('HRVP', 'CHRO', 'en'),
         ('MKTVP', 'CMO', 'th'), ('TECVP', 'CTO', 'en'), ('OPSVP', 'COO', 'th'), ('LEGVP', 'CEO', 'en'),
         ('RETVP', 'CMO', 'th'), ('B2BVP', 'CFO', 'en'), ('CEO', 'COO', 'th'), ('COO', 'CMO', 'en'),
         ('CHRO', 'CFO', 'th'), ('CPO', 'CTO', 'en'), ('CFO', 'CHRO', 'th'), ('CMO', 'CEO', 'en'),
         ('SUPVP', 'COO', 'th')]
for i, (tr, wr, lang) in enumerate(PAIRS):
    P = ROLE_ROW.get(tr); H = ROLE_ROW.get(wr)
    if P is None or H is None or P['Employee ID'] == H['Employee ID']:
        fails.append(('F2', tr, wr, 'unresolved/same')); continue
    gold = list(dict.fromkeys(TITLE_TOK[tr] + names(H)))   # true-role tokens OR actual wrong-role holder
    if lang == 'th':
        q = f'ได้ยินว่าคุณ{nm(P)}เป็น {wr} ขอเบอร์ต่อหน่อยครับ'
    else:
        q = f"I heard {nm(P)} is the {wr} — can I get their extension?"
    emit('F2', lang, q, {'must_contain_any_of': [gold], 'must_not_contain': []}, [P['Employee ID']],
         f'Counterfactual: claims {nm(P)} (actually {tr}) is {wr}. Correct = flag true role {tr} '
         f'or name the actual {wr} = {nm(H)}. Hybrid gold.', ['counterfactual', 'grounding', tr.lower()], f'F2-{i+1:02d}')

# ===================== F3 — subsidiary routing -> section director (12) =====================
sec = defaultdict(list)
for r in R: sec[r['Section']].append(r)
SECNAME = {'ENG': ('วิศวกรรม', 'engineering'), 'MKT': ('การตลาด', 'marketing'),
           'OPS': ('ปฏิบัติการ', 'operations'), 'SALES': ('ขาย', 'sales')}
brand_secs = []
for s, rows in sorted(sec.items()):
    dep = rows[0]['Department']
    if dep not in ('SF', 'KS', 'DN', 'WK', 'JC'): continue
    if len(rows) < 5: continue
    mx = max(RANK[r['Position Level']] for r in rows)
    if mx not in (2, 3): continue
    top = [r for r in rows if RANK[r['Position Level']] == mx]
    if len(top) != 1: continue
    t = top[0]
    if sum(1 for r in rows if r['Last Name Thai'] == t['Last Name Thai']) != 1: continue
    brand_secs.append((s, dep, t))
bmap = {c: (th, en) for th, c, en in BRAND}
for i, (s, dep, t) in enumerate(brand_secs[:12]):
    th, en = bmap[dep]
    suffix = s.split('-')[-1]
    sec_th, sec_en = SECNAME.get(suffix, (suffix, suffix))
    lang = 'th' if i % 2 == 0 else 'en'
    if lang == 'th':
        q = f'แบรนด์{th}เป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นหัวหน้าฝ่าย{sec_th}ของแบรนด์นี้'
    else:
        q = f'The {en} brand is an in-house FahMai division — who heads its {sec_en} unit?'
    emit('F3', lang, q, {'must_contain_any_of': [fg(t), lg(t)], 'must_not_contain': []}, [t['Employee ID']],
         f'Subsidiary routing: {th} = internal division {dep}; {s} unique head = {nm(t)} '
         f'({t["Position in English"]}). Must route inward, not refuse.',
         ['subsidiary_routing', 'brand', 'section_head'], f'F3-{i+1:02d}')

# +brand-division VP identity (subsidiary routing) to reach F3 = 12
need = 12 - sum(1 for it in items if it['subtype'] == 'F3')
k = 0
for th, code, en in BRAND:
    if k >= need: break
    vp = unit.get(f'{code}VP')
    if vp is None: continue
    lang = 'th' if k % 2 == 0 else 'en'
    q = (f'{th}เป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นผู้บริหารสูงสุด (VP) ของแบรนด์นี้'
         if lang == 'th' else f'{en} is an in-house FahMai brand — who is the VP heading this division?')
    emit('F3', lang, q, {'must_contain_any_of': [fg(vp), lg(vp)], 'must_not_contain': []}, [vp['Employee ID']],
         f'Subsidiary routing: {th} = internal division {code}; division VP = {nm(vp)}. Route inward.',
         ['subsidiary_routing', 'brand', 'division_vp'], f'F3-VP-{code}')
    k += 1

if fails:
    print('!! FAILED:', fails); raise SystemExit(1)
out = Path(__file__).parent / 'f_v2_items.json'
json.dump({'questions': items}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'f_v2_items.json: {len(items)}  {dict(Counter(it["subtype"] for it in items))}  '
      f'lang={dict(Counter(it["language"] for it in items))}')
for sub in ['F1', 'F2', 'F3']:
    print(f'\n=== {sub} ===')
    for it in items:
        if it['subtype'] != sub: continue
        g = it['expected_answer']['must_contain_any_of']
        gs = g[0][0] if sub == 'F1' else (f'{len(g[0])} toks' if sub == 'F2' else f'{g[0][0]} {g[1][0]}')
        print(f'  [{it["language"]}] {str(gs)[:26]:26} | {it["question"][:58]}')
