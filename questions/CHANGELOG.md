# Dataset changelog

## v1.0 (camera-ready release)

The item set (626 items, ids, subtypes, languages) and the knowledge base are unchanged. Changes:

**1. Question-side hints removed (63 items).** A question no longer glosses a directory code, a
field name, the role of the answer, or the method to compute it. The gloss was deleted; where a
premise could not simply be dropped (F3), the question was rephrased to ask the same thing without it.

| kind | items | example (v0.2 → v1.0) |
|---|---|---|
| directory code | B5 g666–g681, g684, g685; E3 g452–g456; C6 g833–g838 | `พนักงานสาขาเชียงใหม่ (CNX) มีกี่คน` → `พนักงานสาขาเชียงใหม่ มีกี่คน` |
| column name | G1 g469, g470, g472, g473, g475, g476 | `รหัสพนักงาน (employee ID) ของ CTO …` → `รหัสพนักงานของ CTO …` |
| answer role / premise | F3 g770–g781 | `สายฟ้าเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นผู้บริหารสูงสุด (VP) ของแบรนด์นี้` → `รองประธานที่ดูแลแบรนด์สายฟ้าคือใคร` |
| method | E3 g458, g460, g462, g464, g466; C6 g832 | `… who is the most senior employee by position level?` → `… who is the most senior employee?` |
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

**5. Grader: numbers must stand alone.** A count, extension or ID in the gold now matches only as a
standalone number (thousands separators ignored), so gold `2` no longer matches inside `2021`.

Every revised item keeps its previous wording in the field `question_v0_2` and carries a
`revision_v1_0` tag. The items whose question text changed are listed in `v1.0_changed_ids.txt`; they
were re-run for every model and tool configuration, and all released results use v1.0.
`build/camera_ready_fixes.py` applies changes 1–4.

The re-runs (September 2026) used the same model identifiers, system prompt, tools, and round cap as
the original runs (May 2026). DeepSeek's API now serves newer versions under the V4 names, so the DeepSeek
re-runs reached the original April 2026 V4 weights through fp8 hosts on OpenRouter (`deepseekv4pro_fp8`,
`deepseekv4flash_fp8` in `scripts/run_opentyphoon_baseline.py`).

## v0.2

Initial release: 626 items over `knowledge_base/employees_v02.csv`.
