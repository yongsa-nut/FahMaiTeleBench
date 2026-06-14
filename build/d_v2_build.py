"""Build the D-group v2 backlog: D1 +15, D2 +13, D4 +13 (=41), all airtight.

D1 (homonym): shared NICKNAME held by many -> "who is X / list everyone called X".
   Grade: min_items=3 + all_items_tokens_per_id (per-holder FULL-name tokens, so a
   holder counts only on a full-name match -> no double-count). gold_any=[] (count gate).
D2 (code-collision): a dept-prefixed Unit CODE that's confusable with the dept's
   {DEPT}VP code. gold = the coded person's first+last (AND of OR-variant groups);
   must_not_contain = the {DEPT}VP person (naming the VP fails). Two flavours:
     - secretary/EA units (FINVP-SEC, HRVP-SEC ...) -> code literally CONTAINS the
       VP code = maximal collision; gold=the secretary.
     - GM/Director units (DN-GM, SF-GM, FIN-FINDR ...) -> senior peer of the VP.
D4 (multi-entity): "ext/email for CODE1, CODE2, CODE3" over unique VP/C-level/GM
   codes. gold_any = one value-group per entity (all required) + min_items + tpi.

Output -> d_v2_items.json. Aborts on any airtight failure.
"""
import csv, json, re
from collections import defaultdict, Counter
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees.csv")
QF = (_REPO_ROOT / "questions" / "questions_v02.json")
R = list(csv.DictReader(open(P, encoding='utf-8')))
fullc = Counter((r['First Name Thai'], r['Last Name Thai']) for r in R)
def nm(r): return f"{r['First Name Thai']} {r['Last Name Thai']}"
def fg(r): return sorted({r['First Name Thai'], r['First Name English'].title()})
def lg(r): return sorted({r['Last Name Thai'], r['Last Name English'].title()})
def names(r): return [r['First Name Thai'], r['First Name English'].title(),
                      r['Last Name Thai'], r['Last Name English'].title()]
def fullnames(r): return [f"{r['First Name Thai']} {r['Last Name Thai']}",
                          f"{r['First Name English'].title()} {r['Last Name English'].title()}"]

unit = defaultdict(list)
for r in R: unit[r['Unit']].append(r)
deptvp = {}
for u, rows in unit.items():
    if u.endswith('VP') and len(rows) == 1:
        deptvp[rows[0]['Department']] = rows[0]

existing = json.load(open(QF, encoding='utf-8'))['questions']
items, fails = [], []
def emit(sub, lang, q, ea, gt, rat, tags, src):
    items.append({'bucket': {'D1': 'nickname_grid', 'D2': 'evp_vs_vp_disambig', 'D4': 'multi_entity_turn'}[sub],
        'subtype': sub, 'group': 'D',
        'v01_bucket': {'D1': 'nickname_grid', 'D2': 'evp_vs_vp_disambig', 'D4': 'multi_entity_turn'}[sub],
        'priority': 'P1', 'language': lang, 'question': q, 'expected_behavior': 'answer',
        'expected_answer': ea, 'ground_truth_row_ids': gt, 'rationale': rat, 'tags': tags,
        'authored': '2026-05-24', 'src_id': src})

# ===================== D1 — shared nicknames (15) =====================
used_nick = {it['question'].split()[0] for it in existing if it['subtype'] == 'D1'}
nick = defaultdict(list)
for r in R:
    nk = r['Nickname Thai'].strip()
    if nk: nick[nk].append(r)
shared = sorted([(n, v) for n, v in nick.items() if len(v) >= 6 and n not in used_nick],
                key=lambda x: -len(x[1]))[:15]
for i, (nk, holders) in enumerate(shared):
    lang = 'th' if i % 2 == 0 else 'en'
    tpi = {h['Employee ID']: fullnames(h) for h in holders}
    ea = {'must_contain_any_of': [], 'must_not_contain': [],
          'min_items': 3, 'all_items_tokens_per_id': tpi}
    q = ({0: f'{nk} คือใคร มีใครบ้าง', 1: f'who are the employees nicknamed {nk}?'}[i % 2])
    emit('D1', lang, q, ea, [h['Employee ID'] for h in holders],
         f'Homonym/shared nickname: "{nk}" is held by {len(holders)} people; '
         f'must surface >=3 distinct holders (full-name tokens).',
         ['nickname', 'shared', 'homonym'], f'D1-{i+1:02d}')

# ===================== D2 — code collision (13) =====================
def code_person(u):
    rows = unit.get(u, [])
    if len(rows) == 1 and fullc[(rows[0]['First Name Thai'], rows[0]['Last Name Thai'])] == 1:
        return rows[0]
    return None
# 7 secretary collisions + 6 GM/Director collisions (code, collision_code)
SEC = ['FINVP-SEC', 'HRVP-SEC', 'B2BVP-SEC', 'DNVP-SEC', 'JCVP-SEC', 'KSVP-SEC', 'LEGVP-SEC']
GMD = ['DN-GM', 'SF-GM', 'JC-GM', 'KS-GM', 'WK-GM', 'FIN-FINDR']
d2codes = SEC + GMD
for i, code in enumerate(d2codes):
    r = code_person(code)
    if r is None:
        fails.append(('D2', code, 'not unique')); continue
    d = r['Department']; vp = deptvp.get(d)
    if vp is None or vp['Employee ID'] == r['Employee ID']:
        fails.append(('D2', code, 'no distinct DEPTVP')); continue
    vpcode = d + 'VP'
    lang = 'th' if i % 2 == 0 else 'en'
    q = (f'{code} ใครนะ ไม่ใช่ {vpcode}' if lang == 'th'
         else f'{code} (not {vpcode}) — who is it?')
    ea = {'must_contain_any_of': [fg(r), lg(r)], 'must_not_contain': names(vp)}
    emit('D2', lang, q, ea, [r['Employee ID']],
         f'Code collision: {code} = {nm(r)} ({r["Position in English"]}); confusable with '
         f'{vpcode} = {nm(vp)} (forbidden).', ['disambig', 'code_collision', code.lower()], f'D2-{i+1:02d}')

# ===================== D4 — multi-entity (13) =====================
# resolve a code -> row for VP / C-level / GM
clevel = {}
for r in R:
    if r['Position Level'] == 'C-level':
        pos = r['Position in English'].upper()
        for kw, c in [('EXECUTIVE OFFICER', 'CEO'), ('FINANCIAL', 'CFO'), ('TECHNOLOGY', 'CTO'),
                      ('OPERATING', 'COO'), ('MARKETING', 'CMO'), ('HUMAN', 'CHRO'),
                      ('PEOPLE', 'CPO'), ('PRODUCT', 'CPO')]:
            if kw in pos and c not in clevel:
                clevel[c] = r
GM = {d + '-GM': rows[0] for u, rows in unit.items()
      for d in [rows[0]['Department']] if u.endswith('-GM') and len(rows) == 1}
def resolve(code):
    if code in clevel: return clevel[code]
    if code in GM: return GM[code]
    rows = unit.get(code, [])
    return rows[0] if len(rows) == 1 else None

COMBOS = [  # (lang, attr, [codes])
    ('th', 'ext', ['WKVP', 'JCVP', 'LOGVP']),
    ('en', 'ext', ['OPSVP', 'SUPVP', 'TECVP']),
    ('th', 'email', ['CEO', 'CTO']),
    ('en', 'email', ['FINVP', 'HRVP']),
    ('th', 'ext', ['B2BVP', 'RETVP', 'MKTVP']),
    ('en', 'email', ['CMO', 'CHRO']),
    ('th', 'ext', ['SFVP', 'WKVP']),
    ('en', 'email', ['DNVP', 'JCVP', 'KSVP']),
    ('th', 'ext', ['CEO', 'CFO', 'CTO', 'COO']),
    ('en', 'ext', ['SUPVP', 'OPSVP']),
    ('th', 'email', ['MKTVP', 'TECVP', 'LOGVP', 'B2BVP']),
    ('en', 'ext', ['RETVP', 'SFVP']),
    ('th', 'ext', ['DN-GM', 'SF-GM', 'KS-GM']),
]
FIELD = {'ext': 'Phone Extension', 'email': 'Email Address'}
for i, (lang, attr, codes) in enumerate(COMBOS):
    rows = [resolve(c) for c in codes]
    if any(r is None for r in rows):
        fails.append(('D4', codes, 'unresolved')); continue
    vals = [r[FIELD[attr]] for r in rows]
    if any(not v for v in vals) or len(set(r['Employee ID'] for r in rows)) != len(rows):
        fails.append(('D4', codes, 'blank/dup')); continue
    label = ' '.join(codes) if False else ', '.join(codes)
    q = (f'ขอ {attr} ของ {label}' if lang == 'th' else f'{attr} for {label}')
    ea = {'must_contain_any_of': [[v] for v in vals], 'must_not_contain': [],
          'min_items': len(codes), 'all_items_tokens_per_id': {r['Employee ID']: [r[FIELD[attr]]] for r in rows}}
    emit('D4', lang, q, ea, [r['Employee ID'] for r in rows],
         f'Multi-entity: {len(codes)} codes {codes} -> {attr} each = {vals}.',
         ['multi_entity', attr], f'D4-{i+1:02d}')

if fails:
    print('!! FAILED:', fails); raise SystemExit(1)

out = Path(__file__).parent / 'd_v2_items.json'
json.dump({'questions': items}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'd_v2_items.json: {len(items)}  {dict(Counter(it["subtype"] for it in items))}  '
      f'lang={dict(Counter(it["language"] for it in items))}')
for sub in ['D1', 'D2', 'D4']:
    print(f'\n=== {sub} ===')
    for it in items:
        if it['subtype'] != sub: continue
        ea = it['expected_answer']
        if sub == 'D1':
            g = f'min{ea["min_items"]}/{len(ea["all_items_tokens_per_id"])} holders'
        elif sub == 'D2':
            g = f'{ea["must_contain_any_of"][0][0]} {ea["must_contain_any_of"][1][0]} (¬{ea["must_not_contain"][0]})'
        else:
            g = f'{len(ea["must_contain_any_of"])} vals {[x[0] for x in ea["must_contain_any_of"]]}'
        print(f'  [{it["language"]}] {str(g)[:48]:48} | {it["question"][:40]}')
