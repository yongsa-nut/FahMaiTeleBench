"""v1.0 dataset revision: remove question-side hints, fix answer-echo golds, repair gold defects.

Applies three kinds of change to questions/questions_v02.json, each asserted against the
current text so the script is idempotent-safe (it refuses to run on an unexpected state):

  1. Hint removal (63 items; plus g354 echo and g272 naturalness rewrites). A question must not gloss a directory code, a column name, the
     answer's role, or the method to compute the answer. Only the gloss is deleted; the rest
     of the wording is unchanged.
  2. Answer-echo fixes. g354/g469/g472 asked for a value that appears verbatim in the question
     ("unit code of CFO" -> "CFO"); they now name the role by its Thai title. g190-g195 accepted
     a base nickname that is a substring of the queried variant; they now require the resolved
     person(s) or the not-found phrase. g193 is re-targeted: the directory has an employee whose
     nickname is exactly the queried form.
  3. Gold repairs. g171/g172/g396 ask for a phone number but did not accept it.
  4. Contiguous subtype codes (B5->B4, C3..C6->C2..C5, D4->D3, E5->E4, G3->G2, H7->H5); the v0.2 code
     is kept in `subtype_v0_2`.

Changed-question items are listed in questions/v1.0_changed_ids.txt (these need a model re-run);
gold-only items are re-graded from the existing responses.

Usage: python build/camera_ready_fixes.py
"""
from __future__ import annotations

import csv, io, json, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
QJSON = ROOT / "questions" / "questions_v02.json"
QCSV = ROOT / "questions" / "questions_v02_all.csv"
KB = ROOT / "knowledge_base" / "employees_v02.csv"

# id -> (current question, revised question, reason)
REWRITES = {
    # --- B5: branch / department name glossed with its directory code ---
    "g666": ("How many staff work at the Rama IX (R9) HQ branch?", "How many staff work at the Rama IX HQ branch?", "hint:code"),
    "g667": ("พนักงานสาขาเชียงใหม่ (CNX) มีกี่คน", "พนักงานสาขาเชียงใหม่ มีกี่คน", "hint:code"),
    "g668": ("พนักงานสาขาภูเก็ต (HKT) มีกี่คน", "พนักงานสาขาภูเก็ต มีกี่คน", "hint:code"),
    "g669": ("How many staff work at the Hat Yai (HDY) branch?", "How many staff work at the Hat Yai branch?", "hint:code"),
    "g670": ("พนักงานสาขาขอนแก่น (KKN) มีกี่คน", "พนักงานสาขาขอนแก่น มีกี่คน", "hint:code"),
    "g671": ("พนักงานสาขาโคราช (NMA) มีกี่คน", "พนักงานสาขาโคราช มีกี่คน", "hint:code"),
    "g672": ("How many staff work at the Chonburi (CBI) branch?", "How many staff work at the Chonburi branch?", "hint:code"),
    "g673": ("พนักงานสาขาบางนา (BNA) มีกี่คน", "พนักงานสาขาบางนา มีกี่คน", "hint:code"),
    "g674": ("พนักงานสาขาลาดพร้าว (LP) มีกี่คน", "พนักงานสาขาลาดพร้าว มีกี่คน", "hint:code"),
    "g675": ("How many staff work at the Siam (SIAM) branch?", "How many staff work at the Siam branch?", "hint:code"),
    "g676": ("พนักงานที่ทำงานทางไกล (REMOTE) มีกี่คน", "พนักงานที่ทำงานทางไกล มีกี่คน", "hint:code"),
    "g677": ("ผู้อำนวยการทีมขายสาขาภูเก็ต (HKT) คือใคร", "ผู้อำนวยการทีมขายสาขาภูเก็ต คือใคร", "hint:code"),
    "g678": ("Who is the sales director at the Hat Yai (HDY) branch?", "Who is the sales director at the Hat Yai branch?", "hint:code"),
    "g679": ("ผู้อำนวยการทีมขายสาขาโคราช (NMA) คือใคร", "ผู้อำนวยการทีมขายสาขาโคราช คือใคร", "hint:code"),
    "g680": ("Who is the sales director at the Siam (SIAM) branch?", "Who is the sales director at the Siam branch?", "hint:code"),
    "g681": ("ผู้อำนวยการทีมขายสาขาลาดพร้าว (LP) คือใคร", "ผู้อำนวยการทีมขายสาขาลาดพร้าว คือใคร", "hint:code"),
    "g684": ("ใครเป็นหัวหน้าทีมการตลาด (MKT)", "ใครเป็นหัวหน้าทีมการตลาด", "hint:code"),
    "g685": ("Who is the head of the TEC (tech) department?", "Who is the head of the tech department?", "hint:code"),
    # --- E3: department name glossed with its code; "by position level" names the column ---
    "g452": ("ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea (DN)", "ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea", "hint:code"),
    "g453": ("Who is the most senior person heading the Judchuem (JC) department?", "Who is the most senior person heading the Judchuem department?", "hint:code"),
    "g454": ("ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)", "ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang", "hint:code"),
    "g455": ("Who is the most senior person heading the Legal (LEG) department?", "Who is the most senior person heading the Legal department?", "hint:code"),
    "g456": ("ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon (WK)", "ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon", "hint:code"),
    "g458": ("In the DN-ENG section, who is the most senior employee by position level?", "In the DN-ENG section, who is the most senior employee?", "hint:method"),
    "g460": ("In the FIN-AR section, who is the most senior employee by position level?", "In the FIN-AR section, who is the most senior employee?", "hint:method"),
    "g462": ("In the FIN-TR section, who is the most senior employee by position level?", "In the FIN-TR section, who is the most senior employee?", "hint:method"),
    "g464": ("In the JC-ENG section, who is the most senior employee by position level?", "In the JC-ENG section, who is the most senior employee?", "hint:method"),
    "g466": ("In the KS-MKT section, who is the most senior employee by position level?", "In the KS-MKT section, who is the most senior employee?", "hint:method"),
    # --- C6: department code / level value glossed; tenure defined ---
    "g832": ("ใครเป็นพนักงานที่อายุงานยาวนานที่สุดในฟ้าใหม่ (เริ่มงานก่อนใครเพื่อน) ครับ", "ใครเป็นพนักงานที่อายุงานยาวนานที่สุดในฟ้าใหม่ครับ", "hint:method"),
    "g833": ("ในบรรดาผู้อำนวยการ (Director) ของฝ่ายการเงิน (FIN) ใครที่อายุงานยาวนานที่สุดครับ", "ในบรรดาผู้อำนวยการของฝ่ายการเงิน ใครที่อายุงานยาวนานที่สุดครับ", "hint:code"),
    "g834": ("Among the Directors in the Technology (TEC) department, who has been at FahMai the longest?", "Among the Directors in the Technology department, who has been at FahMai the longest?", "hint:code"),
    "g835": ("ในบรรดาผู้อำนวยการ (Director) ของฝ่ายปฏิบัติการ (OPS) ใครที่อายุงานยาวนานที่สุดครับ", "ในบรรดาผู้อำนวยการของฝ่ายปฏิบัติการ ใครที่อายุงานยาวนานที่สุดครับ", "hint:code"),
    "g836": ("Among the Directors in the Marketing (MKT) department, who has been at FahMai the longest?", "Among the Directors in the Marketing department, who has been at FahMai the longest?", "hint:code"),
    "g837": ("ในบรรดาผู้อำนวยการ (Director) ของแผนก Retail (RET) ใครที่อายุงานยาวนานที่สุดครับ", "ในบรรดาผู้อำนวยการของแผนก Retail ใครที่อายุงานยาวนานที่สุดครับ", "hint:code"),
    "g838": ("Among the Directors in the Support (SUP) department, who has been at FahMai the longest?", "Among the Directors in the Support department, who has been at FahMai the longest?", "hint:code"),
    # --- F3: "X is an in-house FahMai brand" premise (the item tests routing inward) + answer-role gloss ---
    "g770": ("แบรนด์ดาวเหนือเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์นี้", "ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์ดาวเหนือ", "hint:premise"),
    "g771": ("The DaoNuea brand is an in-house FahMai division — who heads its marketing unit?", "Who heads the marketing unit of the DaoNuea brand?", "hint:premise"),
    "g772": ("แบรนด์จุดเชื่อมเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์นี้", "ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์จุดเชื่อม", "hint:premise"),
    "g773": ("The Judchuem brand is an in-house FahMai division — who heads its marketing unit?", "Who heads the marketing unit of the Judchuem brand?", "hint:premise"),
    "g774": ("แบรนด์คลื่นเสียงเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นหัวหน้าฝ่ายการตลาดของแบรนด์นี้", "ใครเป็นหัวหน้าฝ่ายการตลาดของแบรนด์คลื่นเสียง", "hint:premise"),
    "g775": ("The Kluensiang brand is an in-house FahMai division — who heads its operations unit?", "Who heads the operations unit of the Kluensiang brand?", "hint:premise"),
    "g776": ("แบรนด์วงโคจรเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์นี้", "ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์วงโคจร", "hint:premise"),
    "g777": ("The Wongkhojon brand is an in-house FahMai division — who heads its operations unit?", "Who heads the operations unit of the Wongkhojon brand?", "hint:premise"),
    "g778": ("สายฟ้าเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นผู้บริหารสูงสุด (VP) ของแบรนด์นี้", "รองประธานที่ดูแลแบรนด์สายฟ้าคือใคร", "hint:premise+role"),
    "g779": ("Kluensiang is an in-house FahMai brand — who is the VP heading this division?", "Who is the VP heading the Kluensiang division?", "hint:premise+role"),
    "g780": ("ดาวเหนือเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นผู้บริหารสูงสุด (VP) ของแบรนด์นี้", "รองประธานที่ดูแลแบรนด์ดาวเหนือคือใคร", "hint:premise+role"),
    "g781": ("Wongkhojon is an in-house FahMai brand — who is the VP heading this division?", "Who is the VP heading the Wongkhojon division?", "hint:premise+role"),
    # --- G1: Thai field term glossed with the English column name (G1 = Thai question, English-only field) ---
    "g469": ("รหัสหน่วยงาน (unit code) ของ CFO คืออะไรครับ", "รหัสหน่วยงานของประธานเจ้าหน้าที่การเงินคืออะไรครับ", "hint:column+echo"),
    "g470": ("รหัสพนักงาน (employee ID) ของ CTO คือเลขอะไรครับ", "รหัสพนักงานของ CTO คือเลขอะไรครับ", "hint:column"),
    "g472": ("รหัสหน่วยงาน (unit code) ของ CMO คืออะไรครับ", "รหัสหน่วยงานของประธานเจ้าหน้าที่การตลาดคืออะไรครับ", "hint:column+echo"),
    "g473": ("รหัสพนักงาน (employee ID) ของ CPO คือเลขอะไรครับ", "รหัสพนักงานของ CPO คือเลขอะไรครับ", "hint:column"),
    "g475": ("รหัสหน่วยงาน (unit code) ของ Chief of Staff คืออะไรครับ", "รหัสหน่วยงานของ Chief of Staff คืออะไรครับ", "hint:column"),
    "g476": ("รหัสพนักงาน (employee ID) ของ VP ฝ่ายการเงิน คือเลขอะไรครับ", "รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ", "hint:column"),
    "g488": ("What is the CEO's Thai nickname (ชื่อเล่น)?", "What is the CEO's Thai nickname?", "hint:gloss"),
    "g491": ("What is the Chief of Staff's Thai nickname (ชื่อเล่น)?", "What is the Chief of Staff's Thai nickname?", "hint:gloss"),
    "g494": ("What is the VP of Marketing's Thai nickname (ชื่อเล่น)?", "What is the VP of Marketing's Thai nickname?", "hint:gloss"),
    "g497": ("What is the VP of Logistics's Thai nickname (ชื่อเล่น)?", "What is the VP of Logistics's Thai nickname?", "hint:gloss"),
    # --- Thai title glossed with its English code ---
    "g356": ("รองประธาน (VP) ที่อยู่สังกัดเดียวกับ GM ของแบรนด์สายฟ้าคือใคร", "รองประธานที่อยู่สังกัดเดียวกับ GM ของแบรนด์สายฟ้าคือใคร", "hint:gloss"),
    "g827": ("ในบรรดาแผนกที่มีรองประธาน (VP) เป็นหัวหน้า แผนกที่มีพนักงานมากที่สุด ขอเบอร์ต่อของเลขานุการของรองประธานที่เป็นหัวหน้าแผนกนั้นหน่อยครับ",
             "ในบรรดาแผนกที่มีรองประธานเป็นหัวหน้า แผนกที่มีพนักงานมากที่สุด ขอเบอร์ต่อของเลขานุการของรองประธานที่เป็นหัวหน้าแผนกนั้นหน่อยครับ", "hint:gloss"),
    "g829": ("ในบรรดาแผนกที่มีรองประธาน (VP) เป็นหัวหน้า แผนกที่มีพนักงานน้อยที่สุด ขอเบอร์ต่อของรองประธานของแผนกนั้นหน่อยครับ",
             "ในบรรดาแผนกที่มีรองประธานเป็นหัวหน้า แผนกที่มีพนักงานน้อยที่สุด ขอเบอร์ต่อของรองประธานของแผนกนั้นหน่อยครับ", "hint:gloss"),
    "g831": ("ในบรรดาแผนกที่มีรองประธาน (VP) เป็นหัวหน้า แผนกที่มีพนักงานน้อยที่สุด ขอเบอร์ต่อของเลขานุการของรองประธานของแผนกนั้นหน่อยครับ",
             "ในบรรดาแผนกที่มีรองประธานเป็นหัวหน้า แผนกที่มีพนักงานน้อยที่สุด ขอเบอร์ต่อของเลขานุการของรองประธานของแผนกนั้นหน่อยครับ", "hint:gloss"),
    # --- B2: "(real)" signals that the queried token is not a real name ---
    "g558": ("What is LALIN's full (real) name?", "What is LALIN's full name?", "hint:gloss"),
    "g564": ("What is COTTON's full (real) name?", "What is COTTON's full name?", "hint:gloss"),
    # --- answer echo (not a hint) ---
    "g354": ("เลขา CEO อยู่แผนกไหน", "เลขาของประธานเจ้าหน้าที่บริหารอยู่แผนกไหน", "echo"),
    # --- naturalness (human-validation style notes) ---
    "g272": ("ขอ ext ของ HRVP กับ LEGVP, FINVP", "ขอ ext ของ HRVP, LEGVP กับ FINVP", "naturalness"),
}

NOT_FOUND = ["ไม่พบข้อมูล", "no record found"]

# v0.2 subtype code -> contiguous v1.0 code (codes not listed are unchanged)
RENUMBER = {"B5": "B4", "C3": "C2", "C4": "C3", "C5": "C4", "C6": "C5", "D4": "D3", "E5": "E4",
            "G3": "G2", "H7": "H5"}


def holders_first_names(rows, nick_th):
    out = []
    for r in rows:
        if r["Nickname Thai"] == nick_th:
            out += [r["First Name Thai"], r["First Name English"].title()]
    return list(dict.fromkeys(out))


def main() -> None:
    data = json.loads(QJSON.read_text(encoding="utf-8"))
    items = {it["id"]: it for it in data["questions"]}
    with open(KB, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_id = {r["Employee ID"]: r for r in rows}

    # 1+2a. question rewrites
    for iid, (old, new, why) in REWRITES.items():
        it = items[iid]
        if it["question"] == new:
            continue  # already applied
        assert it["question"] == old, f"{iid}: unexpected text {it['question']!r}"
        it["question_v0_2"] = old
        it["question"] = new
        it["revision_v1_0"] = why

    # 2b. nickname-variant echo: base nickname is a substring of the queried variant
    for iid, base in [("g190", "นัต"), ("g191", "มิ้น"), ("g192", "มุก"), ("g194", "ออม")]:
        names = holders_first_names(rows, base)
        assert names, iid
        it = items[iid]
        it["expected_answer"]["must_contain_any_of"] = [names + NOT_FOUND]
        it["ground_truth_row_ids"] = [r["Employee ID"] for r in rows if r["Nickname Thai"] == base]
        it["revision_v1_0"] = "echo:gold"
    # g193: the directory has an employee whose nickname is exactly the queried form
    cto = by_id["00003437"]
    assert cto["Nickname Thai"] == "ปันปัน"
    items["g193"]["expected_answer"]["must_contain_any_of"] = [
        [cto["First Name Thai"], cto["First Name English"].title()],
        [cto["Last Name Thai"], cto["Last Name English"].title()]]
    items["g193"]["ground_truth_row_ids"] = ["00003437"]
    items["g193"]["revision_v1_0"] = "gold:exact-nickname-holder"
    # g195: no employee has the base nickname -> not-found is the only correct outcome
    assert not any(r["Nickname Thai"] == "เก่ง" for r in rows)
    items["g195"]["expected_answer"]["must_contain_any_of"] = [NOT_FOUND]
    items["g195"]["revision_v1_0"] = "echo:gold"

    # 3. phone-number questions whose gold did not accept the number
    for iid, grp in [("g171", 1), ("g172", 1), ("g396", 0)]:
        it = items[iid]
        ext = by_id[it["ground_truth_row_ids"][0]]["Phone Extension"]
        g = it["expected_answer"]["must_contain_any_of"][grp]
        if ext not in g:
            g.append(ext)
        it["revision_v1_0"] = "gold:accept-extension"

    # 4. contiguous subtype codes (the v0.2 code is kept in subtype_v0_2)
    for it in data["questions"]:
        if "subtype_v0_2" not in it:
            it["subtype_v0_2"] = it["subtype"]
        it["subtype"] = RENUMBER.get(it["subtype_v0_2"], it["subtype_v0_2"])

    data["meta"]["version"] = "1.0"
    data["meta"]["revision_note"] = ("v1.0: question-side hints removed (63 items), answer-echo golds "
                                     "tightened (9 items), phone-number golds repaired (3 items), subtype codes made contiguous "
                                     "(v0.2 code in subtype_v0_2). "
                                     "Previous wording kept in question_v0_2; see questions/CHANGELOG.md.")
    QJSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    with open(QCSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "language", "question"])
        for it in data["questions"]:
            w.writerow([it["id"], it.get("language", ""), it["question"]])

    changed = sorted(REWRITES, key=lambda s: int(s[1:]))
    (ROOT / "questions" / "v1.0_changed_ids.txt").write_text(",".join(changed) + "\n", encoding="utf-8")
    gold_only = sorted({k for k, it in items.items() if it.get("revision_v1_0") and k not in REWRITES},
                       key=lambda s: int(s[1:]))
    print(f"question rewrites: {len(changed)}  gold-only: {len(gold_only)} {gold_only}")


if __name__ == "__main__":
    main()
