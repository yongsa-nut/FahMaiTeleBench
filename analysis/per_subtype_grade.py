"""Re-grade existing OpenTyphoon runs BY SUBTYPE (no API calls).

Joins each run's raw/<id>.md responses to questions_v02_relabeled.json (which
carries the new `subtype`/`group`), regrades with grade.py's exact logic, and
produces a per-subtype x tool-shape pass-rate matrix.

Config of the reused runs: typhoon-v2.5-30b-a3b-instruct, default (L2) prompt,
300-item set, 2026-04-20/21.
"""
import json, re
from collections import defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

BENCH = _REPO_ROOT
REL = BENCH / 'questions' / 'questions_v02_relabeled.json'
RUNS = {
    'search':    'opentyphoon_search_20260420_233420',
    'grep+read': 'opentyphoon_grep_20260420_235637',
    'repl':      'opentyphoon_repl_20260420_234453',
    'grep-only': 'opentyphoon_grep-only_20260421_001439',
}

items = {i['id']: i for i in json.load(open(REL, encoding='utf-8'))['questions']}

def grade(it, resp):  # verbatim from scripts/grade.py
    ea = it['expected_answer']; fails = []
    for g in ea.get('must_contain_any_of', []):
        if g and not any(t.lower() in resp.lower() for t in g if t):
            fails.append('miss')
    for t in ea.get('must_not_contain', []):
        if t and t.lower() in resp.lower():
            fails.append('forbidden')
    if ea.get('exact_count') is not None and str(ea['exact_count']) not in resp:
        fails.append('count')
    if ea.get('min_items'):
        tpi = ea.get('all_items_tokens_per_id', {})
        hits = sum(1 for eid, toks in tpi.items() if any(t.lower() in resp.lower() for t in toks if t))
        if hits < ea['min_items']:
            fails.append('min_items')
    if ea.get('must_not_contain_phone_extension') and re.search(r'\b\d{5}\b', resp):
        fails.append('ext')
    if ea.get('must_not_contain_employee_id_pattern') and re.search(r'\b(0000\d{4}|08\d{6})\b', resp):
        fails.append('empid')
    return len(fails) == 0

# cell[tool][subtype] = [pass, total]
cell = {t: defaultdict(lambda: [0, 0]) for t in RUNS}
overall = {t: [0, 0] for t in RUNS}
for tool, rd in RUNS.items():
    raw = BENCH / 'runs' / rd / 'raw'
    for f in raw.glob('*.md'):
        iid = f.stem
        it = items.get(iid)
        if not it or not it.get('subtype'):
            continue
        ok = grade(it, f.read_text(encoding='utf-8'))
        s = it['subtype']
        cell[tool][s][1] += 1; overall[tool][1] += 1
        if ok:
            cell[tool][s][0] += 1; overall[tool][0] += 1

# all subtypes seen
subs = sorted({s for t in RUNS for s in cell[t]})
def rate(pt):
    return f'{100*pt[0]/pt[1]:4.0f}%' if pt[1] else '  – '

print('Overall per tool:')
for t in RUNS:
    print(f'  {t:10} {overall[t][0]}/{overall[t][1]} = {rate(overall[t])}')
print()
hdr = f"{'sub':4} {'n':>3} " + ' '.join(f'{t:>10}' for t in RUNS)
print(hdr); print('-'*len(hdr))
for s in subs:
    n = max(cell[t][s][1] for t in RUNS)
    row = f'{s:4} {n:>3} ' + ' '.join(f'{rate(cell[t][s]):>10}' for t in RUNS)
    print(row)

# group rollup
print('\nGroup rollup (search tool):')
grp = defaultdict(lambda: [0, 0])
for s in subs:
    g = s[0]; grp[g][0] += cell['search'][s][0]; grp[g][1] += cell['search'][s][1]
for g in sorted(grp):
    print(f'  {g}: {rate(grp[g])}  (n={grp[g][1]})')

# dump for the doc
out = {'overall': {t: overall[t] for t in RUNS},
       'cells': {t: {s: cell[t][s] for s in subs} for t in RUNS}}
json.dump(out, open(Path(__file__).parent / 'per_subtype_results.json', 'w'), indent=2)
print('\nwrote per_subtype_results.json')
