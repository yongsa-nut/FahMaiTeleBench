"""Build a skimmable per-group / per-subtype breakdown of the final v0.2 dataset.

Reads bench/questions/questions_v02.json (604 items) and emits:
  - analysis/dataset-breakdown.md   (plain)
  - analysis/dataset-breakdown.html (self-contained, for a quick skim)

For each subtype: count, language split, answer/refuse, gold-signature type, and 2 example
items (question + a human-readable gold summary). Read-only; no model data, no API.
"""
from __future__ import annotations
import json, html
from collections import defaultdict
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

HERE = Path(__file__).resolve().parent
BENCH = HERE.parents[2] / "the source exam" / _REPO_ROOT
QJSON = BENCH / "questions" / "questions_v02.json"

GROUP_DESC = {
    "A": "Direct identity / canonical-code lookup — the understanding floor.",
    "B": "Nickname & noisy-name resolution (diminutives, honorifics, branch-scoped, homonyms).",
    "C": "Counting & aggregation (nickname counts, org-unit headcount, filtered counts, surname-family, superlative/ranking).",
    "D": "Disambiguation — pick the right person against a near-miss / negative constraint.",
    "E": "Multi-hop, bridge & hierarchy (section/dept-head bridges, secretary→exec, implicit hierarchy, deep 4-level chains).",
    "F": "Org & brand knowledge (subsidiary routing, premise-correction, in-house brand ops).",
    "G": "Bilingual / code-switch — same fact asked across Thai⇄English.",
    "H": ("Refusal & safety — 5 distinct refusal reasons, each with its own canonical phrase "
          "(field-not-in-table · person-not-found · subjective · out-of-company · blank-field). "
          "All also carry a universal “never leak an extension” guard."),
}

def gold_type(it):
    if it["expected_behavior"] == "refuse":
        return "refuse"
    ea = it.get("expected_answer") or {}
    if "exact_count" in ea:
        return "count"
    if "min_items" in ea or "all_items_tokens_per_id" in ea:
        return "listing"
    if ea.get("must_contain_any_of"):
        return "answer+neg" if ea.get("must_not_contain") else "answer"
    return "other"

# refusal reason per H-subtype (all H items also carry a universal "never leak an extension" guard)
REFUSE_REASON = {
    "H1": "REFUSE: field not in table (salary/edu/age) — “ไม่สามารถให้ข้อมูลนี้ได้”",
    "H2": "REFUSE: person not in directory (made-up/combo name) — “ไม่พบข้อมูล”",
    "H3": "REFUSE: subjective, not a data lookup — “ไม่สามารถให้ความเห็นได้”",
    "H4": "REFUSE: out-of-company (competitor) — “ไม่ใช่ข้อมูลของฟ้าใหม่”",
    "H7": "REFUSE: field present but value blank (no nickname) — “ไม่มีชื่อเล่นในระบบ”",
}

def gold_summary(it):
    ea = it.get("expected_answer") or {}
    if it["expected_behavior"] == "refuse":
        return REFUSE_REASON.get(it["subtype"], "MUST REFUSE")
    if "exact_count" in ea:
        return f"COUNT = {ea['exact_count']}"
    if "min_items" in ea:
        return f"LIST ≥{ea['min_items']}"
    grps = ea.get("must_contain_any_of") or []
    parts = [" / ".join(map(str, g)) for g in grps]
    s = "mention " + " AND ".join(f"({p})" for p in parts) if parts else "(see raw)"
    if ea.get("must_not_contain"):
        s += " · NOT " + "/".join(map(str, ea["must_not_contain"][:3]))
    return s

def main():
    q = json.loads(QJSON.read_text(encoding="utf-8"))
    items = q.get("questions") or q.get("items")
    G = defaultdict(lambda: defaultdict(list))
    for it in items:
        G[it["group"]][it["subtype"]].append(it)

    total = len(items)
    en = sum(1 for x in items if x["language"] == "en")
    ans = sum(1 for x in items if x["expected_behavior"] == "answer")

    # ---------- markdown ----------
    md = [f"# FahMai v0.2 — dataset breakdown ({total} items)\n",
          f"- **{total} items** · {en} EN / {total-en} TH ({100*en//total}% EN) · {ans} answer / {total-ans} refuse",
          f"- **8 groups · {sum(len(s) for s in G.values())} subtypes** · KB `employees_v02.csv` (1,995 rows)\n",
          "## Group summary\n",
          "| group | items | subtypes | EN/TH | answer/refuse | theme |",
          "|---|--:|--:|--:|--:|---|"]
    for g in sorted(G):
        al = [x for s in G[g] for x in G[g][s]]
        e = sum(1 for x in al if x["language"] == "en")
        a = sum(1 for x in al if x["expected_behavior"] == "answer")
        md.append(f"| **{g}** | {len(al)} | {len(G[g])} | {e}/{len(al)-e} | {a}/{len(al)-a} | {GROUP_DESC[g]} |")
    md.append("")
    for g in sorted(G):
        md.append(f"\n## Group {g} — {GROUP_DESC[g]}\n")
        md.append("| subtype | bucket | n | EN/TH | gold | example |")
        md.append("|---|---|--:|--:|---|---|")
        for s in sorted(G[g]):
            its = G[g][s]
            e = sum(1 for x in its if x["language"] == "en")
            buckets = sorted({x["bucket"] for x in its})
            blabel = buckets[0] + ("…" if len(buckets) > 1 else "")
            gt = sorted({gold_type(x) for x in its})
            ex = its[0]
            md.append(f"| {s} | {blabel} | {len(its)} | {e}/{len(its)-e} | {'/'.join(gt)} | "
                      f"_{ex['question'][:46]}_ → {gold_summary(ex)} |")
    QJSON_OUT_MD = HERE / "dataset-breakdown.md"
    QJSON_OUT_MD.write_text("\n".join(md), encoding="utf-8")

    # ---------- html ----------
    def esc(x): return html.escape(str(x))
    rows_html = []
    for g in sorted(G):
        al = [x for s in G[g] for x in G[g][s]]
        e = sum(1 for x in al if x["language"] == "en")
        a = sum(1 for x in al if x["expected_behavior"] == "answer")
        rows_html.append(f"<tr class='grp'><td><b>{g}</b></td><td>{len(al)}</td><td>{len(G[g])}</td>"
                         f"<td>{e}/{len(al)-e}</td><td>{a}/{len(al)-a}</td><td class='th'>{esc(GROUP_DESC[g])}</td></tr>")
    sections = []
    for g in sorted(G):
        sub_rows = []
        for s in sorted(G[g]):
            its = G[g][s]
            e = sum(1 for x in its if x["language"] == "en")
            buckets = sorted({x["bucket"] for x in its})
            gt = sorted({gold_type(x) for x in its})
            exs = "".join(
                f"<div class='ex'><span class='q'>{esc(x['question'])}</span>"
                f"<span class='lang {x['language']}'>{x['language']}</span>"
                f"<span class='gold'>{esc(gold_summary(x))}</span></div>"
                for x in its[:2])
            sub_rows.append(
                f"<tr><td class='st'>{s}</td><td class='bk'>{esc(buckets[0])}{'…' if len(buckets)>1 else ''}</td>"
                f"<td class='n'>{len(its)}</td><td class='n'>{e}/{len(its)-e}</td>"
                f"<td class='gt'>{'/'.join(gt)}</td><td>{exs}</td></tr>")
        sections.append(
            f"<h2>Group {g} <span class='gd'>{esc(GROUP_DESC[g])}</span></h2>"
            f"<table class='sub'><thead><tr><th>subtype</th><th>bucket</th><th>n</th><th>EN/TH</th>"
            f"<th>gold</th><th>examples</th></tr></thead><tbody>{''.join(sub_rows)}</tbody></table>")
    html_doc = f"""<!doctype html><html lang=en><meta charset=utf-8>
<title>FahMai v0.2 — dataset breakdown</title>
<style>
 body{{font:14px/1.5 -apple-system,Segoe UI,Roboto,'Noto Sans Thai',sans-serif;margin:0;background:#f6f7f9;color:#1c2530}}
 .wrap{{max-width:1100px;margin:0 auto;padding:24px 28px 80px}}
 h1{{font-size:22px;margin:0 0 4px}} .sub0{{color:#5a6b7b;margin:0 0 18px}}
 table{{border-collapse:collapse;width:100%;background:#fff;border:1px solid #dde3ea;border-radius:8px;overflow:hidden;margin:8px 0 26px}}
 th,td{{padding:7px 10px;text-align:left;border-bottom:1px solid #eef1f5;vertical-align:top}}
 thead th{{background:#eef2f7;font-size:12px;text-transform:uppercase;letter-spacing:.03em;color:#54657a}}
 td.n,th:nth-child(3),th:nth-child(4){{text-align:right;white-space:nowrap}}
 .grp td{{font-size:14px}} .th{{color:#5a6b7b;font-size:13px}}
 h2{{font-size:17px;margin:26px 0 2px;border-left:4px solid #3b82f6;padding-left:10px}}
 h2 .gd{{font-weight:400;font-size:13px;color:#6b7a8a;margin-left:8px}}
 table.sub td.st{{font-weight:700;color:#2563eb}} td.bk{{color:#475569;font-family:ui-monospace,Consolas,monospace;font-size:12px}}
 td.gt{{font-family:ui-monospace,Consolas,monospace;font-size:12px;color:#7c3aed}}
 .ex{{margin:2px 0;padding:3px 0;border-bottom:1px dotted #eceff3}} .ex:last-child{{border:0}}
 .ex .q{{color:#111}} .ex .lang{{font-size:10px;padding:1px 5px;border-radius:3px;margin:0 6px;vertical-align:middle}}
 .lang.en{{background:#dbeafe;color:#1e40af}} .lang.th{{background:#fef3c7;color:#92400e}}
 .ex .gold{{display:block;color:#0f766e;font-size:12px;margin-top:1px}}
</style>
<div class=wrap>
<h1>FahMai Directory Benchmark — v0.2 dataset breakdown</h1>
<p class=sub0>{total} items · {en} EN / {total-en} TH ({100*en//total}% EN) · {ans} answer / {total-ans} refuse · 8 groups · {sum(len(s) for s in G.values())} subtypes · KB <code>employees_v02.csv</code> (1,995 rows)</p>
<table><thead><tr><th>group</th><th>items</th><th>subtypes</th><th>EN/TH</th><th>ans/ref</th><th>theme</th></tr></thead>
<tbody>{''.join(rows_html)}</tbody></table>
{''.join(sections)}
</div></html>"""
    (HERE / "dataset-breakdown.html").write_text(html_doc, encoding="utf-8")
    print(f"Wrote dataset-breakdown.md + dataset-breakdown.html  ({total} items, {len(G)} groups)")

if __name__ == "__main__":
    main()
