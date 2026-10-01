# Dataset changelog

## v1.0 (camera-ready release)

The item set (626 items, ids, languages) and the knowledge base are unchanged. Subtype codes are
renumbered to be contiguous (B5→B4, C3–C6→C2–C5, D4→D3, E5→E4, G3→G2, H7→H5); the v0.2 code is kept in
`subtype_v0_2`. Changes:

**1. Question-side hints removed (63 items).** A question no longer glosses a directory code, a
field name, the role of the answer, or the method to compute it. The gloss was deleted; where a
premise could not simply be dropped (F3), the question was rephrased to ask the same thing without it.

| kind | items | example (v0.2 → v1.0) |
|---|---|---|
| directory code | B5 g666–g681, g684, g685; E3 g452–g456; C6 g833–g838 | `พนักงานสาขาเชียงใหม่ (CNX) มีกี่คน` → `พนักงานสาขาเชียงใหม่ มีกี่คน` |
| column name | G1 g469, g470, g472, g473, g475, g476 | `รหัสพนักงาน (employee ID) ของ CTO …` → `รหัสพนักงานของ CTO …` |
| answer role / premise | F3 g770–g781 | `สายฟ้าเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นผู้บริหารสูงสุด (VP) ของแบรนด์นี้` → `รองประธานที่ดูแลแบรนด์สายฟ้าคือใคร` |
| method | E3 g458, g460, g462, g464, g466; C6 g832 | `… who is the most senior employee by position level?` → `… who is the highest-ranking employee?` (see 5) |
| term gloss | g356, g827, g829, g831, g488, g491, g494, g497, g558, g564 | `รองประธาน (VP)` → `รองประธาน` |

**2. Answer-echo golds tightened (9 items).** The gold token also appeared in the question, so
repeating the question passed.
- g354, g469, g472: the role is now named by its Thai title (e.g., `ประธานเจ้าหน้าที่การเงิน`), so the
  expected unit or department code no longer appears in the question.
- g190, g191, g192, g194 (nickname variants such as `นัตตี้`): the gold now requires the first name of
  an employee holding the base nickname, or the not-found phrase, instead of the base nickname itself.
- g193 (`ใครคือปันปัน`): an employee's nickname is exactly `ปันปัน`; the gold now names that employee.
- g195 (`เก่งกี้คือใครนะ`): no employee holds the base nickname; the gold is the not-found phrase.

**3. Phone-number golds repaired (3 items).** g171, g172, g396 ask for a phone number; the gold now
accepts the number (it previously required only the name).

**4. Naturalness (1 item).** g272 `ขอ ext ของ HRVP กับ LEGVP, FINVP` → `ขอ ext ของ HRVP, LEGVP กับ FINVP`.

**5. Ambiguous questions (16 items).** A re-check of every item against the directory found
questions that more than one employee satisfies.
- g135 (`พี่นัต ฝ่าย RET`), g146 (`Chompoo from TEC`): three and two employees match; the question now
  adds the target's level (`ที่เป็นผู้จัดการ`, `the manager`).
- English section items E3 g458–g466 and E1 g588–g600 (even ids): "most senior" can also mean longest
  tenure; they now ask for the "highest-ranking" person, as the Thai items do (`ตำแหน่งสูงสุด`).
- g363 (`who manages the SaiFah brand`) and g266 (`VP SUP ใคร`): two employees fit each question; the
  gold accepts either.

**6. Listing and count golds (48 items).**
- g533, g535: compound counts recomputed on the released directory (7 and 6; they had been computed
  before 99 rows received their Section and Department).
- C4 surname listings g605–g624 ask for the names; the gold no longer also requires the family size.
- Unit and level listings (`who's in WK-PD`, `list 5 people from SaiFah`, `list all VPs`; g206, g210–g215,
  g217, g218, g247–g249, g252–g255, g258–g262, g265), nickname categories (g379, g380: fruits, colours) and reporting lines
  (g367, g371: the department has two VPs): the gold credits every employee who fits, not only the
  first rows the generator kept.

**7. Grader: numbers must stand alone.** A count, extension or ID in the gold now matches only as a
standalone number (thousands separators ignored), so gold `2` no longer matches inside `2021`.

Every revised item keeps its previous wording in the field `question_v0_2` and carries a
`revision_v1_0` tag. The items whose question text changed are listed in `v1.0_changed_ids.txt`; they
were re-run for every model and tool configuration, and all released results use v1.0. g533 and g535
were also re-run, because some of their original cells predate the Section/Department fill-in.
`build/camera_ready_fixes.py` applies changes 1–6 and the subtype renumbering to the v0.2 file.

The re-runs (September 2026) used the same model identifiers, system prompt, tools, and round cap as
the original runs (May 2026). DeepSeek's API now serves newer versions under the V4 names, so the DeepSeek
re-runs reached the original April 2026 V4 weights through fp8 hosts on OpenRouter (`deepseekv4pro_fp8`,
`deepseekv4flash_fp8` in `scripts/run_opentyphoon_baseline.py`).

## v0.2

Initial release: 626 items over `knowledge_base/employees_v02.csv`.
