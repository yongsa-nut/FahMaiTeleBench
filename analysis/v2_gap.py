"""Per-subtype gap vs taxonomy v2, simulating the 37->21 relabel over questions_v02.json.

Does NOT write anything — just reports current v2-subtype coverage vs target so the
authoring queue is exact.
"""
import json
from collections import defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

BENCH = _REPO_ROOT
items = json.load(open(BENCH / 'questions' / 'questions_v02.json', encoding='utf-8'))['questions']

# v2 targets (from the taxonomy design)
TARGET = {'A1':25,'A2':20,'A3':20, 'B1':25,'B2':30,'B3':20,'B5':20,
          'C1':25,'C3':20,'C4':20, 'D1':25,'D2':25,'D4':20,
          'E1':40,'E2':10,'E3':25,'E4':25, 'F1':20,'F2':25,'F3':20,'F5':20,
          'G1':20,'G3':20, 'H1':25,'H2':25,'H3':20,'H4':20,'H7':15}
GROUP_TARGET = {'A':65,'B':95,'C':65,'D':70,'E':100,'F':85,'G':40,'H':105}

# 37 -> v2 relabel (DROP = no v2 home -> removed in full relabel)
REMAP = {'A4':'A1','B4':'B3','C2':'C1','C5':'E3','D3':'D1','G2':'G1','I1':'B2','I4':'C4',
         'F4':'DROP','G4':'DROP','H5':'DROP','H6':'DROP','H8':'DROP','I2':'DROP','I3':'DROP'}
def v2sub(s):
    if s in REMAP: return REMAP[s]
    return s  # identity for already-v2 subtypes (incl new B2/C4/G1/G3/H2/E1/E3)

cur = defaultdict(int); dropped = defaultdict(int); unknown = defaultdict(int)
for it in items:
    s = it.get('subtype')
    v = v2sub(s)
    if v == 'DROP':
        dropped[s] += 1
    elif v in TARGET:
        cur[v] += 1
    else:
        unknown[s] += 1  # subtype with no v2 target row

order = ['A1','A2','A3','B1','B2','B3','B5','C1','C3','C4','D1','D2','D4',
         'E1','E2','E3','E4','F1','F2','F3','F5','G1','G3','H1','H2','H3','H4','H7']
print(f"{'sub':4} {'target':>6} {'now':>4} {'gap':>5}  status")
print('-'*42)
g_now = defaultdict(int); g_tgt = defaultdict(int)
tot_t = tot_c = 0
for s in order:
    t = TARGET[s]; c = cur.get(s, 0); gap = c - t
    tot_t += t; tot_c += c; g_now[s[0]] += c; g_tgt[s[0]] += t
    if c == 0: st = 'EMPTY — author all'
    elif gap < 0: st = f'author +{-gap}'
    elif gap == 0: st = 'on target'
    else: st = f'TRIM {gap}'
    print(f"{s:4} {t:>6} {c:>4} {gap:>+5}  {st}")
print('-'*42)
print(f"{'TOT':4} {tot_t:>6} {tot_c:>4} {tot_c-tot_t:>+5}")
print('\nGroup rollup (after relabel):')
for g in 'ABCDEFGH':
    print(f"  {g}: now {g_now[g]:>3} / target {GROUP_TARGET[g]:>3}  ({g_now[g]-GROUP_TARGET[g]:+d})")
print('\nDropped (no v2 home, removed in full relabel):', dict(dropped) or 'none')
print('Unknown subtype (no target row):', dict(unknown) or 'none')
# net authoring summary
auth = sum(max(0, TARGET[s]-cur.get(s,0)) for s in order)
trim = sum(max(0, cur.get(s,0)-TARGET[s]) for s in order)
empty = [s for s in order if cur.get(s,0)==0]
print(f'\nNET: author +{auth} across {sum(1 for s in order if cur.get(s,0)<TARGET[s])} subtypes; '
      f'trim -{trim}; EMPTY subtypes ({len(empty)}): {empty}')
