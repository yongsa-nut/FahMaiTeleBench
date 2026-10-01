"""Reconcile the staged G/I/H5 items to taxonomy v2 (Group I dissolved).

Produces v2-aligned item files + an archive_v2/ folder. Non-destructive: originals
(g_items.json, i_items.json, h5_items.json) are left intact.

  Group G:  drop G4; relabel G2 -> G1 (cross-lingual field, both directions); keep G1, G3
            -> g_v2_items.json
  I4 -> C4  (Group C filtered-count)            -> c4_items.json
  I1 -> B2  (retrieval; retry-relevant under T1) -> b2_retry_items.json
  I2, I3, G4, H5 -> archive_v2/*.json (kept, not in v2 main set)
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
ARCH = HERE / 'archive_v2'; ARCH.mkdir(exist_ok=True)
def load(fn): return json.load(open(HERE / fn, encoding='utf-8'))['questions']
def dump(items, fn):
    json.dump({'questions': items}, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    return len(items)

G = load('g_items.json'); I = load('i_items.json')
H5 = load('h5_items.json') if (HERE / 'h5_items.json').exists() else []  # H5 items are not part of the release

# ---- Group G -> v2 ----
g_v2, g4_arch = [], []
for it in G:
    s = it['subtype']
    if s == 'G4':
        g4_arch.append(it); continue
    if s == 'G2':                       # merge into G1
        it = {**it, 'subtype': 'G1', 'tags': it['tags'] + ['merged_from_G2']}
    g_v2.append(it)                     # G1, (G2->G1), G3 kept

# ---- I4 -> C4 ; I1 -> B2 ; I2/I3 archived ----
c4, b2_retry, i_arch = [], [], []
for it in I:
    s = it['subtype']
    if s == 'I4':
        c4.append({**it, 'group': 'C', 'subtype': 'C4', 'bucket': 'listing_count',
                   'tags': [t for t in it['tags'] if t != 'agentic'] + ['filtered_count', 'from_I4']})
    elif s == 'I1':
        b2_retry.append({**it, 'group': 'B', 'subtype': 'B2', 'bucket': 'retrieval',
                         'tags': [t for t in it['tags'] if t != 'agentic'] + ['retry_t1', 'from_I1']})
    else:                               # I2, I3
        i_arch.append(it)

# ---- H5 -> separate-work archive ----
n_gv2 = dump(g_v2, HERE / 'g_v2_items.json')
n_c4 = dump(c4, HERE / 'c4_items.json')
n_b2 = dump(b2_retry, HERE / 'b2_retry_items.json')
n_g4 = dump(g4_arch, ARCH / 'g4_archived.json')
n_i = dump(i_arch, ARCH / 'i2_i3_archived.json')
n_h5 = dump(H5, ARCH / 'h5_separate_work.json')

from collections import Counter
print('=== v2-aligned (kept) ===')
print(f'  g_v2_items.json     : {n_gv2}  subtypes={dict(Counter(x["subtype"] for x in g_v2))}')
print(f'  c4_items.json (I4)  : {n_c4}')
print(f'  b2_retry_items.json (I1): {n_b2}')
print('=== archived (out of v2 main) ===')
print(f'  archive_v2/g4_archived.json     : {n_g4}')
print(f'  archive_v2/i2_i3_archived.json  : {n_i}  ({dict(Counter(x["subtype"] for x in i_arch))})')
print(f'  archive_v2/h5_separate_work.json: {n_h5}')
print(f'\nv2 net new question items: {n_gv2 + n_c4 + n_b2} (G {n_gv2} + C4 {n_c4} + B2 {n_b2})')
print(f'archived: {n_g4 + n_i + n_h5}')
