"""Build + verify Group I (advanced agentic) — I1-I4.

I1 retry-after-empty (25): reference a person by their UNIQUE nickname *as if it
   were a name* (no "nickname" hint). Naive name-search returns empty → model must
   pivot to the nickname field. Airtight: nickname unique + 0 hits in name fields.
   Grade = final answer contains the requested attribute (recovered or not).
I2 tool-choice (20): query with a clear best-tool (search-favored field lookup vs
   grep-favored listing/count). Gold = correct answer; `intended_tool` tag. The
   tool-CHOICE signal is read from the trace under a multi-tool run config (baseline).
I3 proactive clarification (20): ambiguous shared-first-name query, no disambiguator.
   Pass = asks for clarification AND does NOT commit to a specific contact.
   Grade = must_contain a clarify marker + must_not_contain ext/employee-id.  [soft]
I4 compound constraints (25): multi-filter single query. Count flavor → exact_count;
   list flavor → min_items + per-member tokens. Counts recomputed from the CSV.
"""
import csv, json
from pathlib import Path
from collections import Counter, defaultdict

P = Path(__file__).resolve().parents[1] / 'knowledge_base' / 'employees.csv'
R = list(csv.DictReader(open(P, encoding='utf-8')))
NF = ['First Name Thai', 'Last Name Thai', 'First Name English', 'Last Name English']
def T(s): return (s or '').strip()
def title(s): return T(s).title()
def name_hits(t):
    t = t.lower(); return sum(1 for r in R for f in NF if t == T(r[f]).lower())

out, problems = [], []
def add(iid, sub, lang, q, ea, gt, behav, rat, tags):
    out.append({'id': iid, 'bucket': 'advanced_agentic', 'subtype': sub, 'group': 'I',
        'priority': 'P1', 'language': lang, 'question': q, 'expected_behavior': behav,
        'expected_answer': ea, 'ground_truth_row_ids': gt, 'rationale': rat, 'tags': tags})

# ---------- I1: retry-after-empty (nickname-as-name) ----------
nick_en = Counter(T(r['Nickname English']).upper() for r in R if T(r['Nickname English']))
I1A = [r for r in R if T(r['Nickname English']) and nick_en[T(r['Nickname English']).upper()] == 1
       and name_hits(T(r['Nickname English'])) == 0 and name_hits(T(r['Nickname Thai'])) == 0][:25]
attrs = ['ext', 'email', 'name']
for i, r in enumerate(I1A):
    a = attrs[i % 3]; lang = 'th' if i % 2 == 0 else 'en'
    nick = T(r['Nickname English'])
    if a == 'ext':
        q = (f'ขอเบอร์ต่อของคุณ {nick} หน่อยครับ' if lang == 'th' else f"What's {nick}'s phone extension?")
        ea = {'must_contain_any_of': [[T(r['Phone Extension'])]], 'must_not_contain': []}; g = f"ext {T(r['Phone Extension'])}"
    elif a == 'email':
        q = (f'ขออีเมลของคุณ {nick} หน่อยครับ' if lang == 'th' else f"What is {nick}'s email address?")
        ea = {'must_contain_any_of': [[T(r['Email Address'])]], 'must_not_contain': []}; g = 'email'
    else:
        q = (f'คุณ {nick} ชื่อจริง-นามสกุลว่าอะไรครับ' if lang == 'th' else f"What is {nick}'s full (real) name?")
        ea = {'must_contain_any_of': [[T(r['First Name Thai']), title(r['First Name English'])],
                                      [T(r['Last Name Thai']), title(r['Last Name English'])]], 'must_not_contain': []}; g = 'full name'
    add(f'I1-{i+1:02d}', 'I1', lang, q, ea, [r['Employee ID']], 'answer',
        f'Retry-after-empty: "{nick}" is a nickname (0 name-field hits) used as a name; '
        f'naive name search empty → pivot to nickname field. gold={g}.',
        ['agentic', 'retry_after_empty', a])

# ---------- I4: compound constraints ----------
by_dly = defaultdict(list)
for r in R: by_dly[(r['Department'], r['Position Level'], r['Start Year'])].append(r)
count_combos = sorted([(k, v) for k, v in by_dly.items()
                        if 2 <= len(v) <= 6 and T(k[0]) and T(k[2])])[:15]  # non-empty dept+year
LVL_TH = {'Manager': 'ผู้จัดการ (Manager)', 'Director': 'ผู้อำนวยการ (Director)',
          'Lead': 'หัวหน้างาน (Lead)', 'IC': 'พนักงาน (IC)', 'VP': 'รองประธาน (VP)'}
for i, ((d, lvl, yr), members) in enumerate(count_combos):
    lang = 'th' if i % 2 == 0 else 'en'
    if lang == 'th':
        q = f'มีพนักงานกี่คนที่อยู่แผนก {d} ระดับ {lvl} และเริ่มงานในปี {yr} ครับ'
    else:
        q = f'How many employees are in the {d} department at {lvl} level who started in {yr}?'
    add(f'I4-{i+1:02d}', 'I4', lang, q,
        {'must_contain_any_of': [], 'must_not_contain': [], 'exact_count': len(members)},
        [m['Employee ID'] for m in members], 'answer',
        f'Compound count: {d} ∧ {lvl} ∧ start {yr} = {len(members)}.',
        ['agentic', 'compound', 'count'])
# list flavor: (section, level) small
by_sl = defaultdict(list)
for r in R: by_sl[(r['Section'], r['Position Level'])].append(r)
list_combos = sorted([(k, v) for k, v in by_sl.items()
                       if 2 <= len(v) <= 4 and T(k[0]) and k[1] in ('Director', 'Manager')])[:10]
for i, ((sec, lvl), members) in enumerate(list_combos):
    lang = 'th' if i % 2 == 0 else 'en'
    if lang == 'th':
        q = f'ช่วยบอกชื่อทุกคนที่เป็นระดับ {lvl} ในส่วนงาน {sec} หน่อยครับ'
    else:
        q = f'List everyone at {lvl} level in the {sec} section.'
    tpi = {m['Employee ID']: [T(m['Last Name Thai']), title(m['Last Name English'])] for m in members}
    add(f'I4-{16+i:02d}', 'I4', lang, q,
        {'must_contain_any_of': [], 'must_not_contain': [], 'min_items': len(members),
         'all_items_tokens_per_id': tpi},
        [m['Employee ID'] for m in members], 'answer',
        f'Compound list: {lvl} in {sec} = {len(members)} people (must name all).',
        ['agentic', 'compound', 'list'])

# ---------- I3: proactive clarification (ambiguous shared first name) ----------
fn_th = Counter(r['First Name Thai'] for r in R)
shared = [n for n, c in fn_th.most_common() if c >= 6][:20]
CLARIFY = ['คนไหน', 'ท่านไหน', 'หลายคน', 'หลายท่าน', 'ระบุ', 'นามสกุล', 'แผนก', 'คุณหมายถึง',
           'more than one', 'multiple', 'which', 'specify', 'could you', 'clarify', 'several']
for i, fn in enumerate(shared):
    lang = 'th' if i % 2 == 0 else 'en'
    cnt = fn_th[fn]
    if lang == 'th':
        q = f'ขอเบอร์ต่อของคุณ {fn} หน่อยครับ'
    else:
        q = f"Can you give me {fn}'s phone extension?"
    add(f'I3-{i+1:02d}', 'I3', lang, q,
        {'must_contain_any_of': [CLARIFY], 'must_not_contain': [],
         'must_not_contain_phone_extension': True, 'must_not_contain_employee_id_pattern': True},
        [], 'clarify',
        f'Ambiguous: first name "{fn}" has {cnt} bearers, no disambiguator → should ask which, '
        f'not commit to a specific contact. [soft grade: clarify marker + no committed ext/id]',
        ['agentic', 'clarification', 'ambiguous'])

# ---------- I2: tool-choice (clear best-tool) ----------
posc = Counter(r['Position in English'] for r in R)
roles = [r for r in R if posc[r['Position in English']] == 1 and T(r['Email Address'])][:10]
secs = [k for k, c in Counter(r['Section'] for r in R).items() if T(k) and 8 <= c <= 40]
for i in range(10):  # search-favored: structured field lookup by unique role
    r = roles[i]; lang = 'th' if i % 2 == 0 else 'en'
    role_disp = r["Position in English"].title()
    q = (f'ขออีเมลของตำแหน่ง {role_disp} หน่อยครับ' if lang == 'th'
         else f'What is the email of the {role_disp}?')
    add(f'I2-{i+1:02d}', 'I2', lang, q,
        {'must_contain_any_of': [[T(r['Email Address'])]], 'must_not_contain': []},
        [r['Employee ID']], 'answer',
        f'Tool-choice (search-favored: structured field lookup). gold email; intended_tool=search.',
        ['agentic', 'tool_choice', 'search_favored'])
for i in range(10):  # grep-favored: count within a section (free-text scan)
    sec = secs[i]; members = [r for r in R if r['Section'] == sec]; lang = 'th' if i % 2 == 0 else 'en'
    q = (f'มีพนักงานทั้งหมดกี่คนในส่วนงาน {sec} ครับ' if lang == 'th'
         else f'How many employees are there in total in the {sec} section?')
    add(f'I2-{11+i:02d}', 'I2', lang, q,
        {'must_contain_any_of': [], 'must_not_contain': [], 'exact_count': len(members)},
        [], 'answer',
        f'Tool-choice (grep-favored: count over a section = {len(members)}); intended_tool=grep.',
        ['agentic', 'tool_choice', 'grep_favored'])

# ---- report ----
from collections import Counter as C
print(f'Group I: {len(out)} items | per-subtype:', dict(C(i["subtype"] for i in out)),
      '| lang:', dict(C(i["language"] for i in out)))
print('PROBLEMS:', problems if problems else 'none')
for s in ['I1', 'I2', 'I3', 'I4']:
    ex = next(i for i in out if i['subtype'] == s)
    eak = {k: v for k, v in ex['expected_answer'].items() if v and k != 'must_not_contain'}
    print(f"  {ex['id']} [{ex['language']}] {ex['question'][:58]}")
    print(f"       gold: {eak}")
json.dump({'questions': out}, open(Path(__file__).parent / 'i_items.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('wrote i_items.json')
