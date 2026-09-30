# -*- coding: utf-8 -*-
"""Build the GOLD-VALIDATION rater bundle (v2 design, 2026-07-12).

Design (user-decided): raters do NOT see or judge model answers — the deterministic grader
makes model-side judging unnecessary. Instead each item shows:
    (1) the question,
    (2) the EVIDENCE — the ground-truth KB row(s) rendered as cards (with refusal-specific
        evidence: schema for field-not-in-table, near-miss rows for not-found, the person's
        row for blank-field),
    (3) the expected answer (gold) rendered human-readably,
and the rater answers three checks:
    Q1 gold_ok      — given the evidence, is the expected answer correct?  (yes / no / unsure)
    Q2 wellformed   — is the question unambiguous & answerable from the table? (yes / no)
    Q3 natural      — does the phrasing sound like a real user?             (yes / no)

Sample = ~10% of the 626 items, stratified per subtype (>=1 each, seeded), PLUS every item
the strongest model (gpt-5.4) fails at ALL four tool configs (gold-suspect priority).
Both raters receive the IDENTICAL item set (required for agreement); the two HTML files
differ only in the baked rater id.

Outputs: gold_validation/dist/gold_validation_rater{A,B}.html
         gold_validation/sample_items.json  (the sampled ids + evidence, for the record)
Score with: score_gold_validation.py labels_raterA.json labels_raterB.json
"""
from __future__ import annotations

import csv, html, io, json, random, sys
from collections import defaultdict
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
REPO = HERE.parent  # repo root
QJSON = REPO / "questions" / "questions_v02.json"
KB = REPO / "knowledge_base" / "employees_v02.csv"
OUT = HERE / "gold_validation"
DIST = OUT / "dist"
SAMPLE_FRAC = 0.10
SEED = 0

FIELD_ORDER = ["Employee ID", "First Name Thai", "Last Name Thai", "First Name English",
               "Last Name English", "Nickname Thai", "Nickname English", "Position in Thai",
               "Position in English", "Position Level", "Department", "Section", "Unit",
               "Branch", "Office Location", "Phone Extension", "Mobile No.", "Email Address",
               "Start Year"]
MAX_CARDS = 10


def load():
    items = {q["id"]: q for q in json.loads(QJSON.read_text(encoding="utf-8"))["questions"]}
    with open(KB, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    by_emp = {r["Employee ID"]: r for r in rows}
    return items, rows, by_emp


def strong_fails(items):
    """Items gpt-5.4 fails at ALL configs, from the release repo's committed results.jsonl."""
    man = json.loads((REPO / "runs" / "wave4_gpt54med_full.json").read_text(encoding="utf-8"))
    per_cfg = []
    for c, rd in man["configs"].items():
        d = {}
        for line in (REPO / rd / "results.jsonl").read_text(encoding="utf-8").splitlines():
            if line.strip():
                rec = json.loads(line)
                d[rec["id"]] = bool(rec["pass"])
        per_cfg.append(d)
    return sorted(i for i in items if all(not d.get(i, False) for d in per_cfg))


def sample_ids(items, force):
    rng = random.Random(SEED)
    by_sub = defaultdict(list)
    for q in items.values():
        by_sub[q["subtype"]].append(q["id"])
    picked = set(force)
    for sub in sorted(by_sub):
        pool = sorted(by_sub[sub])
        k = max(1, round(SAMPLE_FRAC * len(pool)))
        have = [i for i in pool if i in picked]
        need = max(0, k - len(have))
        rest = [i for i in pool if i not in picked]
        picked.update(rng.sample(rest, min(need, len(rest))))
    return sorted(picked)


def longest_runs(text):
    """Longest Thai run and longest Latin run in the question (for H2 near-miss scan)."""
    import re
    th = max(re.findall(r"[฀-๿]+", text) or [""], key=len)
    en = max(re.findall(r"[A-Za-z][A-Za-z.'-]{2,}", text) or [""], key=len)
    return th.strip(), en.strip()


LEVEL_RANK = {"C-level": 0, "VP": 1, "Director": 2, "Manager": 3, "Lead": 4, "IC": 5}


def named_in_question(qtext, rows, exclude_ids):
    """Rows whose full Thai or English name appears verbatim in the question text."""
    hits = []
    ql = qtext.lower()
    for r in rows:
        if r["Employee ID"] in exclude_ids:
            continue
        th = (r["First Name Thai"] + " " + r["Last Name Thai"]).strip()
        en = (r["First Name English"] + " " + r["Last Name English"]).strip().lower()
        th2 = (r["First Name Thai"] + r["Last Name Thai"]).strip()
        if (th and th in qtext) or (th2 and th2 in qtext) or (en and en in ql):
            hits.append(r)
    return hits[:4]


def rank_table(pairs, unit_label, winner):
    """pairs = [(key, count)] descending; render a small Thai ranking table."""
    out = ["<table class='rank'><tr><th>อันดับ</th><th>หน่วย</th><th>" + unit_label + "</th><th></th></tr>"]
    for i, (k, n) in enumerate(pairs, 1):
        mark = " ← เฉลย" if k == winner else ""
        cls = " class='win'" if k == winner else ""
        out.append(f"<tr{cls}><td>{i}</td><td>{html.escape(str(k))}</td><td>{n}</td><td>{mark}</td></tr>")
    out.append("</table>")
    return "".join(out)


def name_blob(r):
    return " ".join([r["First Name Thai"], r["Last Name Thai"],
                     r["First Name English"], r["Last Name English"],
                     r["Nickname Thai"], r["Nickname English"]]).lower()


def evidence_for(q, rows, by_emp):
    """-> (kind_note_html, [row dicts to card], extra_html)."""
    gt = [by_emp[i] for i in q["ground_truth_row_ids"] if i in by_emp]
    sub = q["subtype"]
    ea = q["expected_answer"]
    note, extra = "", ""
    if q["expected_behavior"] == "answer":
        if sub == "C5":
            # superlative: show the computed ranking from the FULL table so the rater can
            # verify the argmax/argmin themselves (the winner's row cards follow below)
            from collections import Counter
            qt = q["question"].lower()
            note = ("โจทย์เชิง<b>จัดอันดับ (มาก/นานที่สุด)</b> — ตารางอันดับด้านล่าง"
                    "คำนวณจากฐานข้อมูลทั้ง 1,995 แถว โปรดใช้ตารางนี้ตรวจว่าเฉลยคืออันดับ 1 จริง")
            gold_first = (q["expected_answer"].get("must_contain_any_of") or [[""]])[0][0]
            if "section" in qt or "ส่วนงาน" in qt:
                pool = Counter(r["Section"] for r in rows if r["Section"])
                extra = rank_table(pool.most_common(5), "จำนวนพนักงาน", gold_first)
            elif "แผนก" in qt or "department" in qt or "ฝ่าย" in qt:
                pool = Counter(r["Department"] for r in rows if r["Department"])
                extra = rank_table(pool.most_common(5), "จำนวนพนักงาน", gold_first)
            elif "director" in qt:
                pool = Counter(r["Section"] for r in rows
                               if r["Section"] and r["Position Level"] == "Director")
                extra = rank_table(pool.most_common(5), "จำนวน Director", gold_first)
            elif "นาน" in qt or "longest" in qt or "tenure" in qt or "อายุงาน" in qt:
                vets = sorted((r for r in rows if r["Start Year"].strip().isdigit()),
                              key=lambda r: int(r["Start Year"]))[:5]
                pairs = [(f"{r['First Name Thai']} {r['Last Name Thai']}", r["Start Year"]) for r in vets]
                win = pairs[0][0] if pairs else ""
                extra = rank_table(pairs, "เริ่มงานปี (ค.ศ.)", win)
            else:
                note += ("<br><b>ค่าที่คำนวณโดยสคริปต์ผู้สร้างโจทย์:</b> "
                         + html.escape(q.get("rationale", "") or ""))
            return note, gt[:MAX_CARDS], extra
        if sub in ("E1", "E4", "E2", "F3") or q.get("group") == "E":
            # multi-hop / bridge: the gold row alone doesn't show the chain — add the rows
            # of people named in the question, and (for section-senior items) the shared
            # section roster sorted by position level
            bridge = named_in_question(q["question"], rows, set(q["ground_truth_row_ids"]))
            roster = []
            if bridge and any(k in q["question"].lower()
                              for k in ("สูงสุด", "senior", "สังกัด", "ส่วนงาน", "section")):
                secs = {b["Section"] for b in bridge if b["Section"]}
                if len(secs) == 1:
                    sec = secs.pop()
                    roster = sorted((r for r in rows if r["Section"] == sec),
                                    key=lambda r: LEVEL_RANK.get(r["Position Level"], 9))[:MAX_CARDS]
            parts = ["โจทย์เชิง<b>เชื่อมโยงหลายขั้น (multi-hop)</b> — "
                     "การ์ดชุดแรกคือ<b>คำตอบ (เฉลย)</b>"]
            cards = list(gt[:MAX_CARDS])
            if bridge:
                parts.append("ตามด้วย<b>บุคคลที่ถูกอ้างถึงในคำถาม</b> (ใช้ไล่เส้นทางความสัมพันธ์)")
                cards += bridge
            if roster:
                parts.append(f"และ<b>สมาชิกส่วนงาน {html.escape(roster[0]['Section'])} "
                             f"ทั้งหมด เรียงตามลำดับตำแหน่ง</b> (ตรวจว่าใครตำแหน่งสูงสุด)")
                seen = {r["Employee ID"] for r in cards}
                cards += [r for r in roster if r["Employee ID"] not in seen]
            note = " · ".join(parts)
            return note, cards[: MAX_CARDS + 6], extra
        if ea.get("exact_count") is not None:
            note = (f"โจทย์ประเภท<b>นับจำนวน</b> — เฉลยคือ <b>{ea['exact_count']}</b>; "
                    f"แถวในฐานข้อมูลที่เข้าเกณฑ์ตามผู้สร้างโจทย์ = <b>{len(gt)}</b> แถว "
                    f"(แสดงตัวอย่าง {min(MAX_CARDS, len(gt))} แถวแรก) — "
                    f"โปรดตรวจว่า<b>เกณฑ์ในคำถามตรงกับเกณฑ์ที่นับ</b>")
        elif len(gt) > MAX_CARDS:
            note = f"รายการทั้งหมด {len(gt)} แถว (แสดง {MAX_CARDS} แถวแรก)"
        return note, gt[:MAX_CARDS], extra
    # refusal items
    if sub == "H1":
        note = ("โจทย์ที่<b>ต้องปฏิเสธ</b>: ถามข้อมูลที่<b>ไม่มีคอลัมน์ในตาราง</b> "
                "— คอลัมน์ทั้งหมดของฐานข้อมูลแสดงด้านล่าง โปรดตรวจว่าสิ่งที่ถามไม่อยู่ในนั้นจริง")
        extra = "<div class='schema'>" + " · ".join(FIELD_ORDER) + "</div>"
        return note, [], extra
    if sub == "H2":
        th, en = longest_runs(q["question"])
        near = []
        for r in rows:
            blob = name_blob(r)
            if (len(th) >= 3 and any(part and part in blob for part in [th[:len(th)//2], th[len(th)//2:]])) or \
               (len(en) >= 3 and en.lower() in blob):
                near.append(r)
            if len(near) >= 6:
                break
        full = [r for r in rows if th and th.lower() in name_blob(r).replace(" ", "")]
        note = ("โจทย์ที่<b>ต้องปฏิเสธ (ไม่พบข้อมูล)</b>: บุคคลในคำถาม<b>ไม่มีอยู่จริง</b>ในตาราง — "
                f"สแกนทั้ง 1,995 แถวแล้ว: แถวที่ตรงกับชื่อเต็มในคำถาม = <b>{len(full)}</b>; "
                "ด้านล่างคือแถวที่ใกล้เคียงที่สุด (ชื่อหรือนามสกุลคล้าย) เพื่อยืนยันว่าไม่ใช่คนเดียวกัน")
        return note, near, extra
    if sub == "H5":
        note = ("โจทย์ที่<b>ต้องปฏิเสธ (ข้อมูลว่าง)</b>: บุคคลมีตัวตน แต่<b>ช่องที่ถามว่างเปล่า</b> "
                "— โปรดดูแถวของบุคคลด้านล่างและตรวจว่าช่องนั้นว่างจริง")
        return note, gt if gt else [], extra
    if sub == "H3":
        note = ("โจทย์ที่<b>ต้องปฏิเสธ (เชิงความเห็น)</b>: คำถามขอความเห็น/การประเมินบุคคล "
                "ซึ่งตอบจากตารางข้อมูลไม่ได้ — ไม่มีหลักฐานแถวข้อมูลเกี่ยวข้อง")
        return note, [], extra
    if sub == "H4":
        note = ("โจทย์ที่<b>ต้องปฏิเสธ (นอกบริษัท)</b>: ถามถึงบุคคล/องค์กรภายนอก "
                "— ฐานข้อมูลมีเฉพาะพนักงาน FahMai (ฟ้าใหม่) เท่านั้น")
        return note, [], extra
    return note, gt[:MAX_CARDS], extra


def gold_html(q):
    ea = q["expected_answer"]
    parts = []
    if q["expected_behavior"] == "refuse":
        groups = [g for g in ea.get("must_contain_any_of", []) if g]
        if groups:
            alts = " <span class='dim'>หรือ</span> ".join(
                f"<code>{html.escape(t)}</code>" for t in groups[0] if t)
            parts.append(f"<b>ต้องปฏิเสธ</b> ด้วยวลีมาตรฐาน (ยอมรับได้ทุกแบบ): {alts}")
        parts.append("<span class='dim'>และห้ามเผยเบอร์ต่อ 5 หลัก / รหัสพนักงาน</span>")
        return "<br>".join(parts)
    parts.append("<span class='dim'>ระบบตรวจอัตโนมัติแบบจับคำ: ถือว่า \"ตอบถูก\" เมื่อคำตอบของโมเดล"
                 "มีคำตามเงื่อนไขครบทุกบรรทัดด้านล่าง (แต่ละบรรทัด มีคำใดคำหนึ่งก็พอ)</span>")
    for g in [g for g in ea.get("must_contain_any_of", []) if g]:
        alts = " <span class='dim'>หรือ</span> ".join(f"<code>{html.escape(t)}</code>" for t in g if t)
        parts.append("คำตอบต้องมี: " + alts)
    if ea.get("exact_count") is not None:
        parts.append(f"ตัวเลขที่ต้องปรากฏ: <code>{ea['exact_count']}</code>")
    if ea.get("min_items"):
        parts.append(f"ต้องระบุอย่างน้อย <b>{ea['min_items']}</b> รายการจากรายชื่อในหลักฐาน "
                     f"<span class='dim'>(เกณฑ์ที่ออกแบบไว้: สำหรับรายการยาว ระบบสั่งให้โมเดลยกตัวอย่าง"
                     f"เพียงบางส่วน จึงนับว่าผ่านเมื่อระบุขั้นต่ำตามนี้ — ไม่จำเป็นต้องครบทุกคน "
                     f"ข้อนี้โปรดตรวจว่า \"รายชื่อในหลักฐานถูกต้องตรงกับที่คำถามขอ\" เป็นหลัก)</span>")
    mnc = [t for t in ea.get("must_not_contain", []) if t]
    if mnc:
        parts.append("ห้ามมี: " + " ".join(f"<code>{html.escape(t)}</code>" for t in mnc))
    return "<br>".join(parts) if parts else "<i>(ไม่มีเงื่อนไข?)</i>"


def card_html(r, blank_focus=None):
    out = ["<div class='card'>"]
    for f in FIELD_ORDER:
        v = (r.get(f) or "").strip()
        if not v:
            if blank_focus and f in blank_focus:
                out.append(f"<div class='kv blank'><span>{f}</span><b>— ว่าง —</b></div>")
            continue
        out.append(f"<div class='kv'><span>{f}</span><b>{html.escape(v)}</b></div>")
    out.append("</div>")
    return "".join(out)


TEMPLATE = """<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8">
<title>FahMai gold validation — __RATER__</title>
<style>
 body{font-family:'Segoe UI',Tahoma,sans-serif;margin:0;background:#f4f5f7;color:#1a1a1a}
 header{position:sticky;top:0;background:#123;color:#fff;padding:10px 18px;display:flex;gap:16px;align-items:center;z-index:5}
 header b{font-size:16px} header .prog{margin-left:auto;font-size:14px}
 button{cursor:pointer;border:0;border-radius:6px;padding:8px 14px;font-size:14px}
 .exp{background:#2ea44f;color:#fff}
 main{max-width:980px;margin:14px auto;padding:0 14px}
 .instr{background:#fff;border:1px solid #dde;border-radius:10px;padding:14px 18px;margin-bottom:14px;font-size:14.5px;line-height:1.55}
 .item{background:#fff;border:1px solid #dde;border-radius:10px;padding:16px 18px;margin-bottom:16px}
 .qid{color:#889;font-size:12.5px;margin-bottom:4px}
 .q{font-size:17px;font-weight:600;margin:2px 0 10px}
 .sec{margin:10px 0 4px;font-size:13px;font-weight:700;color:#345;text-transform:uppercase;letter-spacing:.4px}
 .note{background:#fff8e6;border:1px solid #f0e0b0;border-radius:8px;padding:8px 12px;font-size:14px;margin:6px 0}
 .cards{display:flex;flex-wrap:wrap;gap:8px}
 .card{border:1px solid #cfd6e0;border-radius:8px;padding:8px 10px;font-size:12.5px;background:#fafbfd;min-width:250px;max-width:300px}
 .kv{display:flex;justify-content:space-between;gap:10px;padding:1px 0}
 .kv span{color:#778;white-space:nowrap} .kv b{text-align:right;word-break:break-all;font-weight:600}
 .kv.blank b{color:#c00}
 .schema{font-size:13px;background:#eef2f8;border-radius:8px;padding:8px 12px}
 table.rank{border-collapse:collapse;margin:8px 0;font-size:13.5px}
 table.rank th,table.rank td{border:1px solid #cfd6e0;padding:4px 12px;text-align:left}
 table.rank th{background:#eef2f8} table.rank tr.win td{background:#eefaf0;font-weight:700}
 .gold{background:#eefaf0;border:1px solid #bfe3c8;border-radius:8px;padding:10px 12px;font-size:14.5px;line-height:1.6}
 code{background:#e8edf4;border-radius:4px;padding:1px 5px;font-size:13px}
 .dim{color:#899}
 details{margin-top:8px;font-size:13px;color:#556} details summary{cursor:pointer;color:#357}
 .checks{margin-top:12px;border-top:1px dashed #ccd;padding-top:10px}
 .check{margin:8px 0;font-size:14.5px}
 .check .lbl{font-weight:600}
 .opts{display:inline-flex;gap:6px;margin-left:10px}
 .opts label{border:1px solid #bbc;border-radius:16px;padding:3px 12px;font-size:13.5px;cursor:pointer;background:#fff}
 .opts input{display:none}
 .opts label:has(input:checked){background:#123;border-color:#123;color:#fff}
 textarea{width:100%;box-sizing:border-box;border:1px solid #ccd;border-radius:6px;padding:6px;font-size:13.5px;min-height:34px}
 .done-mark{float:right;color:#2ea44f;font-weight:700;display:none}
 .item.done .done-mark{display:inline}
</style></head><body>
<header><b>FahMai — ตรวจสอบเฉลย (__RATER__)</b>
 <span class="prog"><span id="ndone">0</span>/<span id="ntot">0</span> ข้อ</span>
 <button class="exp" onclick="exportLabels()">💾 ส่งออกผลตรวจ (JSON)</button></header>
<main>
<div class="instr"><b>วิธีตรวจ (ประมาณ 30–45 นาที):</b> แต่ละข้อจะแสดง
 ① <b>คำถาม</b> ② <b>หลักฐานจากฐานข้อมูลจริง</b> (แถวพนักงานที่เกี่ยวข้อง) ③ <b>เฉลยที่ระบบใช้ตรวจ</b><br>
 งานของคุณคือตอบ 3 ข้อ: <b>เฉลยถูกต้องตามหลักฐานหรือไม่</b> · <b>คำถามชัดเจนตอบได้จริงหรือไม่</b> ·
 <b>ภาษาเป็นธรรมชาติหรือไม่</b> — ถ้าพบปัญหา โปรดพิมพ์อธิบายสั้น ๆ ในช่องหมายเหตุ<br>
 <b>ตัวอย่าง:</b> ถามว่า "เบอร์ของ ก." → หลักฐานคือแถวของ ก. (เบอร์ 71234) → ถ้าเฉลยกำหนดคำว่า
 "ก." หรือ "71234" = <b>✓ ถูกต้อง</b> แต่ถ้าเฉลยกำหนดชื่อ<b>คนละคน</b>กับหลักฐาน = <b>✗ ผิด</b><br>
 บางข้อ (เชื่อมโยงหลายขั้น / จัดอันดับ / นับจำนวน) จะมี<b>กล่องหมายเหตุสีเหลือง</b> +
 การ์ด/ตารางประกอบเพิ่มเติม — โปรดอ่านหมายเหตุก่อนตรวจข้อนั้น<br>
 ระบบ<b>บันทึกอัตโนมัติ</b>ในเครื่องของคุณ ปิด/เปิดใหม่ได้ เมื่อครบทุกข้อกด "ส่งออกผลตรวจ"
 แล้วส่งไฟล์ JSON กลับมา</div>
<div id="items"></div>
</main>
<script>
const RATER = "__RATER__";
const DATA = __DATA__;
const KEY = "goldval_" + RATER;
let saved = {}; try { saved = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch(e) {}

const CHECKS = [
 ["gold_ok",   "① คน/ค่าที่เฉลยกำหนด คือคำตอบที่ถูกต้องของคำถามนี้ ตามหลักฐานหรือไม่?", [["yes","✓ ถูกต้อง"],["no","✗ ผิด"],["unsure","? ไม่แน่ใจ"]]],
 ["wellformed","② คำถามชัดเจน ตอบได้จากตาราง (ไม่กำกวม)?", [["yes","✓ ใช่"],["no","✗ ไม่"]]],
 ["natural",   "③ ภาษาเหมือนคนถามจริงหรือไม่?", [["yes","✓ ใช่"],["no","✗ ไม่"]]],
];

function render() {
  const root = document.getElementById("items");
  root.innerHTML = DATA.map(it => `
   <div class="item" id="it_${it.id}">
    <div class="qid">${it.id} · ${it.subtype} · ${it.lang.toUpperCase()} <span class="done-mark">✓ ตรวจแล้ว</span></div>
    <div class="q">${it.q}</div>
    ${it.note ? `<div class="note">${it.note}</div>` : ""}
    ${it.cards ? `<div class="sec">หลักฐานจากฐานข้อมูล</div><div class="cards">${it.cards}</div>` : ""}
    ${it.extra || ""}
    <div class="sec">เฉลยที่ระบบใช้ตรวจ</div><div class="gold">${it.gold}</div>
    ${it.rationale ? `<details><summary>หมายเหตุผู้สร้างโจทย์ (เปิดดูได้หากไม่แน่ใจ)</summary>${it.rationale}</details>` : ""}
    <div class="checks">
     ${CHECKS.map(([k, lbl, opts]) => `
      <div class="check"><span class="lbl">${lbl}</span>
       <span class="opts">${opts.map(([v, t]) =>
         `<label><input type="radio" name="${it.id}_${k}" value="${v}"
           ${saved[it.id] && saved[it.id][k] === v ? "checked" : ""}
           onchange="setv('${it.id}','${k}','${v}')">${t}</label>`).join("")}</span></div>`).join("")}
     <textarea placeholder="หมายเหตุ (ถ้ามี)" oninput="setc('${it.id}', this.value)">${(saved[it.id] && saved[it.id].comment) || ""}</textarea>
    </div>
   </div>`).join("");
  document.getElementById("ntot").textContent = DATA.length;
  refresh();
}
function setv(id, k, v) { saved[id] = saved[id] || {}; saved[id][k] = v; persist(); }
function setc(id, v) { saved[id] = saved[id] || {}; saved[id].comment = v; persist(); }
function isDone(id) { const s = saved[id] || {}; return s.gold_ok && s.wellformed && s.natural; }
function refresh() {
  let n = 0;
  DATA.forEach(it => {
    const el = document.getElementById("it_" + it.id);
    if (isDone(it.id)) { n++; el.classList.add("done"); } else el.classList.remove("done");
  });
  document.getElementById("ndone").textContent = n;
}
function persist() { localStorage.setItem(KEY, JSON.stringify(saved)); refresh(); }
function exportLabels() {
  const missing = DATA.filter(it => !isDone(it.id)).map(it => it.id);
  if (missing.length && !confirm("ยังไม่ครบ " + missing.length + " ข้อ (" + missing.slice(0,8).join(", ") + "…)\\nส่งออกเลยหรือไม่?")) return;
  const blob = new Blob([JSON.stringify({rater: RATER, exported: new Date().toISOString(), labels: saved}, null, 1)], {type: "application/json"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "gold_labels_" + RATER + ".json";
  a.click();
}
render();
</script></body></html>
"""


def main():
    items, rows, by_emp = load()
    force = strong_fails(items)
    ids = sample_ids(items, force)
    print(f"strong-fail force-include: {force}")
    print(f"sampled {len(ids)} items ({SAMPLE_FRAC:.0%} stratified per subtype + forced)")

    data = []
    for i in ids:
        q = items[i]
        note, cards, extra = evidence_for(q, rows, by_emp)
        blank_focus = None
        if q["subtype"] == "H5":
            blank_focus = {"Nickname Thai", "Nickname English", "Phone Extension", "Mobile No."}
        data.append({
            "id": i, "subtype": q["subtype"], "lang": q["language"],
            "q": html.escape(q["question"]),
            "note": note,
            "cards": "".join(card_html(r, blank_focus) for r in cards) if cards else "",
            "extra": extra,
            "gold": gold_html(q),
            "rationale": html.escape(q.get("rationale", "") or ""),
        })

    OUT.mkdir(exist_ok=True)
    DIST.mkdir(exist_ok=True)
    (OUT / "sample_items.json").write_text(
        json.dumps({"seed": SEED, "frac": SAMPLE_FRAC, "forced": force, "ids": ids},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False)
    for rater in ("raterA", "raterB"):
        html_doc = TEMPLATE.replace("__RATER__", rater).replace("__DATA__", payload)
        p = DIST / f"gold_validation_{rater}.html"
        p.write_text(html_doc, encoding="utf-8")
        print(f"baked {p}  ({len(data)} items, {p.stat().st_size/1e6:.1f} MB)")

    from collections import Counter
    print("by group:", dict(sorted(Counter(items[i]['group'] for i in ids).items())))
    print("langs:", dict(Counter(items[i]['language'] for i in ids)))


if __name__ == "__main__":
    main()
