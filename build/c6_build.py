"""Build + verify C6 — SUPERLATIVE / RANKING (argmax/argmin over the whole table).

Builds against employees_v02.csv. No single CSV field holds the answer: the model must scan +
aggregate + compare, then return the UNIQUE extremum row. Every superlative is asserted unique
(no tie) before emitting — ties are skipped (would break airtight grading).

Two families:
  Tenure (argmin Start Year) -> answer = a PERSON (gold = first AND last name groups, airtight).
    * longest-tenured overall; longest-tenured Director within each department (unique ones).
  Headcount (argmax counts) -> answer = an ORG UNIT.
    * section with most Directors; section with most employees  -> gold = section code (specific).
    * largest department by headcount -> gold = dept code/name AND the count (RET-style codes are
      short, so the count gates incidental substring matches).
Smallest-department is intentionally skipped (CEO + lone-digit gold = false-positive risk).
"""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

P = (_REPO_ROOT / "knowledge_base" / "employees_v02.csv")
R = list(csv.DictReader(open(P, encoding='utf-8')))
def G(r, k): return r.get(k, '')
def nm(r): return f"{G(r,'First Name Thai')} {G(r,'Last Name Thai')}"
def yr(r): return int(G(r,'Start Year')) if G(r,'Start Year').isdigit() else 9999
def name_tokens(r):
    fg = [t for t in (G(r,'First Name Thai'), G(r,'First Name English').title()) if t]
    lg = [t for t in (G(r,'Last Name Thai'), G(r,'Last Name English').title()) if t]
    return fg, lg

items, problems, skipped = [], [], []   # skipped = expected tie-drops (airtight guard), not errors
def emit(iid, lang, q, gold, gt_ids, rat, tags):
    if not all(g and g[0] for g in gold):
        problems.append(f'{iid}: empty gold group'); return
    items.append({'id': iid, 'bucket': 'superlative', 'subtype': 'C6', 'group': 'C',
        'priority': 'P2', 'language': lang, 'question': q, 'expected_behavior': 'answer',
        'expected_answer': {'must_contain_any_of': gold, 'must_not_contain': []},
        'ground_truth_row_ids': gt_ids, 'rationale': rat, 'tags': tags})

def unique_argmin_year(rows):
    m = min(yr(r) for r in rows); top = [r for r in rows if yr(r) == m]
    return (top[0], m) if len(top) == 1 else (None, m)

by_dept = defaultdict(list); by_sec = defaultdict(list)
for r in R:
    by_dept[G(r,'Department')].append(r); by_sec[G(r,'Section')].append(r)

# ---------- Tenure: longest-tenured overall (person) ----------
idx = 1
top, m = unique_argmin_year(R)
if top:
    fg, lg = name_tokens(top)
    emit(f'C6-{idx:02d}', 'th', 'ใครเป็นพนักงานที่อายุงานยาวนานที่สุดในฟ้าใหม่ (เริ่มงานก่อนใครเพื่อน) ครับ',
         [fg, lg], [top['Employee ID']],
         f'argmin Start Year over all 1,995 rows = {nm(top)} ({m}, unique).',
         ['superlative', 'tenure', 'overall']); idx += 1

# ---------- Tenure: longest-tenured Director per department (unique only) ----------
DEPT_LABEL = {'FIN': ('ฝ่ายการเงิน (FIN)', 'the Finance (FIN) department'),
              'TEC': ('ฝ่ายเทคโนโลยี (TEC)', 'the Technology (TEC) department'),
              'OPS': ('ฝ่ายปฏิบัติการ (OPS)', 'the Operations (OPS) department'),
              'MKT': ('ฝ่ายการตลาด (MKT)', 'the Marketing (MKT) department'),
              'HR': ('ฝ่ายทรัพยากรบุคคล (HR)', 'the HR department'),
              'RET': ('แผนก Retail (RET)', 'the Retail (RET) department'),
              'LOG': ('แผนก Logistics (LOG)', 'the Logistics (LOG) department'),
              'SUP': ('แผนก Support (SUP)', 'the Support (SUP) department')}
made_dir = 0
for d in ['FIN', 'TEC', 'OPS', 'MKT', 'HR', 'RET', 'LOG', 'SUP']:
    if made_dir >= 6: break
    dirs = [r for r in by_dept[d] if G(r,'Position Level') == 'Director']
    if len(dirs) < 2: continue                                   # need a real comparison
    top, m = unique_argmin_year(dirs)
    if not top: skipped.append(f'tenure-dir {d} tie'); continue
    fg, lg = name_tokens(top)
    lang = 'th' if made_dir % 2 == 0 else 'en'
    thlab, enlab = DEPT_LABEL.get(d, (f'แผนก {d}', f'the {d} department'))
    q = (f'ในบรรดาผู้อำนวยการ (Director) ของ{thlab} ใครที่อายุงานยาวนานที่สุดครับ' if lang == 'th'
         else f'Among the Directors in {enlab}, who has been at FahMai the longest?')
    emit(f'C6-{idx:02d}', lang, q, [fg, lg], [top['Employee ID']],
         f'argmin Start Year over {len(dirs)} Directors in {d} = {nm(top)} ({m}, unique).',
         ['superlative', 'tenure', 'director_by_dept']); idx += 1; made_dir += 1

# ---------- Headcount: section with most Directors (code) ----------
dir_per_sec = Counter(G(r,'Section') for r in R if G(r,'Position Level') == 'Director')
(s_top, n_top), (_, n_2) = dir_per_sec.most_common(2)
if n_top != n_2:
    emit(f'C6-{idx:02d}', 'en', 'Which section has the most Directors?',
         [[s_top]], [r['Employee ID'] for r in by_sec[s_top] if G(r,'Position Level') == 'Director'],
         f'argmax Director-count over sections = {s_top} ({n_top}, unique vs {n_2}).',
         ['superlative', 'headcount', 'most_directors']); idx += 1
else:
    problems.append('most-directors section tie')

# ---------- Headcount: section with most employees (code) ----------
sec_sizes = Counter({s: len(v) for s, v in by_sec.items() if s})
(bs, bn), (_, bn2) = sec_sizes.most_common(2)
if bn != bn2:
    emit(f'C6-{idx:02d}', 'th', f'section ไหนของฟ้าใหม่ที่มีพนักงานมากที่สุดครับ',
         [[bs]], [r['Employee ID'] for r in by_sec[bs]][:50],
         f'argmax headcount over sections = {bs} ({bn}, unique vs {bn2}).',
         ['superlative', 'headcount', 'biggest_section']); idx += 1
else:
    problems.append('biggest section tie')

# ---------- Headcount: largest department (code AND count — short code, so count gates) ----------
dep_sizes = Counter({d: len(v) for d, v in by_dept.items()})
(bd, bdn), (_, bdn2) = dep_sizes.most_common(2)
if bd != '' and bdn != bdn2:
    thlab, enlab = DEPT_LABEL.get(bd, (f'แผนก {bd}', f'the {bd} department'))
    emit(f'C6-{idx:02d}', 'en', 'Which department has the most employees company-wide?',
         [[bd, 'Retail'], [str(bdn)]],
         [r['Employee ID'] for r in by_dept[bd]][:50],
         f'argmax headcount over departments = {bd} (n={bdn}, unique vs {bdn2}); gold = code AND count.',
         ['superlative', 'headcount', 'largest_dept']); idx += 1
else:
    problems.append('largest dept tie')

print(f'C6 items: {len(items)}')
print('by family:', dict(Counter(t for it in items for t in it['tags'] if t in ('tenure', 'headcount'))))
print('by lang:', dict(Counter(it['language'] for it in items)))
print()
for it in items:
    g = it['expected_answer']['must_contain_any_of']
    print(f"  {it['id']} [{it['language']}] gold={str(g)[:34]:34} | {it['question'][:60]}")
print('skipped (expected ties):', skipped if skipped else 'none')
print('PROBLEMS:', problems if problems else 'none')
json.dump({'questions': items}, open(Path(__file__).parent / 'c6_items.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('wrote c6_items.json')
