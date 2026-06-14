"""Score the Track-3 grader-review labels into the numbers for the paper.

Inputs: review/review_items.json (carries the auto-grader pass/fail per (item,answer),
the blind flag, group, behaviour) + the per-rater labels_<id>.json files.

Computes:
  • Krippendorff α (nominal) on rater agreement — answer-correctness, gold_ok, query_ok
    (the reliability ceiling: "do two humans agree on what counts as correct?").
  • Grader validity — on (item, answer) pairs where the raters AGREE (consensus human
    verdict), compared to the auto-grader's PASS/FAIL:
        false-neg = grader FAIL ∧ human CORRECT   (too strict — the substring missed)
        false-pos = grader PASS ∧ human INCORRECT (lucky/incidental substring)
    reported overall + by group + by expected_answer signature, and crucially the
    unbiased rate on the BLIND sample alone (triage is enriched, reported separately).
  • Gold-error fix list (items a rater marked wrong/ambiguous) + the disagreement list.

Krippendorff α is inlined (nominal), exact for 2 raters — same as the Phase-6 scorer,
no third-party dependency.

  python score_review.py --labels review/dist/labels_raterA.json review/dist/labels_raterB.json
  python score_review.py --labels ... --items review/review_items.json
  python score_review.py --selftest
"""
from __future__ import annotations

import argparse, io, json, math, sys
from collections import defaultdict
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
OUT = HERE / "review"


# ============================ Krippendorff α (nominal; from score_calibration.py) ============================

def krippendorff_alpha(units: list[list], level: str = "nominal") -> float:
    o: dict[tuple, float] = defaultdict(float)
    for u in units:
        vals = [v for v in u if v is not None]
        m = len(vals)
        if m < 2:
            continue
        for i in range(m):
            for j in range(m):
                if i != j:
                    o[(vals[i], vals[j])] += 1.0 / (m - 1)
    values = sorted({c for c, _ in o} | {k for _, k in o})
    if len(values) < 2:
        return float("nan")
    n_c = {v: sum(o.get((v, k), 0.0) for k in values) for v in values}
    n = sum(n_c.values())
    if n < 2:
        return float("nan")
    if level == "nominal":
        def d2(c, k): return 0.0 if c == k else 1.0
    elif level == "ordinal":
        def d2(c, k):
            lo, hi = (c, k) if c <= k else (k, c)
            s = sum(n_c[g] for g in values if lo <= g <= hi)
            return (s - (n_c[c] + n_c[k]) / 2.0) ** 2
    else:
        raise ValueError(level)
    do = sum(cnt * d2(c, k) for (c, k), cnt in o.items())
    de = sum(n_c[c] * n_c[k] * d2(c, k) for c in values for k in values)
    return float("nan") if de == 0 else 1.0 - (n - 1) * do / de


# ============================ loading ============================

def load_labels(paths: list[Path]) -> list[tuple[str, dict]]:
    out = []
    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        out.append((data.get("annotator", p.stem), data.get("labels", {})))
    return out


def ea_sig(it) -> str:
    if it.get("expected_behavior") == "refuse":
        return "refusal"
    ea = it.get("gold_raw", {})
    if ea.get("min_items"):
        return "listing"
    if ea.get("exact_count") is not None:
        return "count"
    return "answer"


def index_items(items: list[dict]) -> dict:
    """id -> {blind, group, sig, grader: {akey: pass_bool}}."""
    idx = {}
    for it in items:
        idx[it["id"]] = {
            "blind": bool(it.get("blind")),
            "group": it.get("group"),
            "sig": ea_sig(it),
            "grader": {a["key"]: bool(a["grader_pass"]) for a in it.get("answers", [])},
        }
    return idx


# ============================ agreement ============================

def alpha_answer(items_idx, labelsets):
    units = []
    for iid, meta in items_idx.items():
        for akey in meta["grader"]:
            vals = [ls.get(iid, {}).get("answers", {}).get(akey) for _, ls in labelsets]
            vals = [v for v in vals if v]
            if len(vals) >= 2:
                units.append(vals)
    return krippendorff_alpha(units, "nominal"), len(units)


def alpha_field(items_idx, labelsets, field):
    units = []
    for iid in items_idx:
        vals = [ls.get(iid, {}).get(field) for _, ls in labelsets]
        vals = [v for v in vals if v]
        if len(vals) >= 2:
            units.append(vals)
    return krippendorff_alpha(units, "nominal"), len(units)


# ============================ grader validity ============================

def _stat():
    return {"n": 0, "fp": 0, "fn": 0, "tp": 0, "tn": 0, "partial": 0, "disagree": 0}


def grader_validity(items_idx, labelsets):
    """For each (item, answer) where raters agree: compare consensus human verdict
    to grader pass/fail. Returns nested stats by scope/group/sig + raw rows."""
    scopes = {"blind": _stat(), "triage": _stat(), "all": _stat()}
    by_group, by_sig = defaultdict(_stat), defaultdict(_stat)
    rows = []
    for iid, meta in items_idx.items():
        for akey, gpass in meta["grader"].items():
            verdicts = [ls.get(iid, {}).get("answers", {}).get(akey) for _, ls in labelsets]
            verdicts = [v for v in verdicts if v]
            if len(verdicts) < 2:
                continue
            agree = len(set(verdicts)) == 1
            buckets = [scopes["all"], by_group[meta["group"]], by_sig[meta["sig"]],
                       scopes["blind"] if meta["blind"] else scopes["triage"]]
            if not agree:
                for b in buckets:
                    b["n"] += 1; b["disagree"] += 1
                continue
            v = verdicts[0]
            kind = None
            if v == "partial":
                kind = "partial"
            elif gpass and v == "correct":
                kind = "tp"
            elif (not gpass) and v == "incorrect":
                kind = "tn"
            elif gpass and v == "incorrect":
                kind = "fp"
            elif (not gpass) and v == "correct":
                kind = "fn"
            for b in buckets:
                b["n"] += 1; b[kind] += 1
            if kind in ("fp", "fn"):
                rows.append({"id": iid, "akey": akey, "group": meta["group"], "sig": meta["sig"],
                             "grader": "PASS" if gpass else "FAIL", "human": v, "kind": kind,
                             "blind": meta["blind"]})
    return scopes, dict(by_group), dict(by_sig), rows


def gold_issues(items_idx, labelsets):
    """Items where ≥1 rater flagged gold_ok != ok, with consensus + notes."""
    out = []
    for iid in items_idx:
        per = [(r, ls.get(iid, {})) for r, ls in labelsets if iid in ls]
        golds = [(r, d.get("gold_ok"), d.get("note", "")) for r, d in per if d.get("gold_ok")]
        flagged = [g for g in golds if g[1] != "ok"]
        if flagged:
            vals = {g[1] for g in golds}
            consensus = golds[0][1] if len(vals) == 1 else "DISAGREE"
            out.append({"id": iid, "consensus": consensus,
                        "raters": [{"rater": r, "gold_ok": v, "note": n} for r, v, n in golds]})
    return out


# ============================ reporting ============================

def _fmt(x): return "  n/a" if (isinstance(x, float) and math.isnan(x)) else f"{x:5.3f}"


def _rates(s):
    gp = s["tp"] + s["fp"]              # grader said PASS (within agreed, non-partial)
    gf = s["fn"] + s["tn"]             # grader said FAIL
    fp_rate = s["fp"] / gp if gp else float("nan")
    fn_rate = s["fn"] / gf if gf else float("nan")
    decided = s["tp"] + s["tn"] + s["fp"] + s["fn"]
    err = (s["fp"] + s["fn"]) / decided if decided else float("nan")
    return fp_rate, fn_rate, err


def report(items_idx, labelsets):
    raters = [r for r, _ in labelsets]
    L = ["# Track-3 grader-review findings", "",
         f"- raters: **{', '.join(raters)}**  ·  reviewed items present: {len(items_idx)}"]

    # agreement
    aa, na = alpha_answer(items_idx, labelsets)
    ag, ng = alpha_field(items_idx, labelsets, "gold_ok")
    aq, nq = alpha_field(items_idx, labelsets, "query_ok")
    L += ["", "## Inter-rater agreement (Krippendorff α, nominal)", "",
          "| dimension | α | units |", "|---|---|---|",
          f"| answer-correctness | {_fmt(aa)} | {na} |",
          f"| gold_ok | {_fmt(ag)} | {ng} |",
          f"| query_ok | {_fmt(aq)} | {nq} |"]

    scopes, by_group, by_sig, rows = grader_validity(items_idx, labelsets)

    def tbl(title, d):
        out = ["", f"## Grader validity — {title}", "",
               "| bucket | n | tp | tn | fp(false-pos) | fn(false-neg) | partial | disagree | fp-rate | fn-rate | err |",
               "|---|---|---|---|---|---|---|---|---|---|---|"]
        for k, s in d.items():
            fpr, fnr, err = _rates(s)
            out.append(f"| {k} | {s['n']} | {s['tp']} | {s['tn']} | {s['fp']} | {s['fn']} | "
                       f"{s['partial']} | {s['disagree']} | {_fmt(fpr)} | {_fmt(fnr)} | {_fmt(err)} |")
        return out

    L += tbl("by scope (BLIND = unbiased rate; triage = enriched)", scopes)
    L += tbl("by group", dict(sorted(by_group.items(), key=lambda x: str(x[0]))))
    L += tbl("by expected_answer signature", by_sig)

    # candidate grader bugs (agreed fp/fn)
    L += ["", f"## Grader↔human mismatches (agreed) — {len(rows)}", "",
          "_false-neg = grader too strict · false-pos = lucky substring. These are the rows to fix._", "",
          "| id | answer | group/sig | grader | human | kind | blind |", "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["kind"], r["group"] or "")):
        L.append(f"| {r['id']} | `{r['akey']}` | {r['group']}/{r['sig']} | {r['grader']} | "
                 f"{r['human']} | **{r['kind']}** | {'✓' if r['blind'] else ''} |")

    # gold issues
    gi = gold_issues(items_idx, labelsets)
    L += ["", f"## Gold to fix (rater flagged gold_ok ≠ ok) — {len(gi)}", ""]
    if gi:
        L += ["| id | consensus | rater verdicts / notes |", "|---|---|---|"]
        for g in gi:
            notes = " · ".join(f"{r['rater']}:{r['gold_ok']}" + (f" ({r['note']})" if r['note'] else "")
                               for r in g["raters"])
            L.append(f"| {g['id']} | {g['consensus']} | {notes} |")
    else:
        L.append("_none flagged._")

    text = "\n".join(L) + "\n"
    (OUT / "review-findings.md").write_text(text, encoding="utf-8")
    (OUT / "review_scored.json").write_text(json.dumps(
        {"raters": raters, "alpha": {"answer": aa, "gold_ok": ag, "query_ok": aq},
         "scopes": scopes, "by_group": by_group, "by_sig": by_sig,
         "mismatches": rows, "gold_issues": gi}, ensure_ascii=False, indent=1), encoding="utf-8")

    # console
    print(f"raters: {', '.join(raters)}  ·  items: {len(items_idx)}")
    print(f"α  answer={_fmt(aa)}  gold_ok={_fmt(ag)}  query_ok={_fmt(aq)}")
    for k, s in scopes.items():
        fpr, fnr, err = _rates(s)
        print(f"  [{k:6}] n={s['n']:4} fp={s['fp']} fn={s['fn']} partial={s['partial']} "
              f"disagree={s['disagree']}  fp-rate={_fmt(fpr)} fn-rate={_fmt(fnr)} err={_fmt(err)}")
    print(f"mismatches(agreed fp/fn): {len(rows)}  ·  gold-issues: {len(gi)}")
    print(f"wrote {(OUT/'review-findings.md').relative_to(HERE)}  +  review_scored.json")


# ============================ selftest ============================

def selftest():
    assert krippendorff_alpha([["a", "a"], ["b", "b"], ["c", "c"]], "nominal") == 1.0
    a = krippendorff_alpha([["a", "a"], ["b", "b"], ["a", "b"], ["b", "a"]], "nominal")
    assert round(a, 3) == 0.125, a
    # grader-validity math on a synthetic item set
    items_idx = {
        "i1": {"blind": True, "group": "A", "sig": "answer", "grader": {"m::t": True}},   # grader PASS
        "i2": {"blind": True, "group": "A", "sig": "count", "grader": {"m::t": True}},    # grader PASS but wrong
        "i3": {"blind": False, "group": "B", "sig": "answer", "grader": {"m::t": False}}, # grader FAIL but right
    }
    labelsets = [
        ("rA", {"i1": {"gold_ok": "ok", "query_ok": "ok", "answers": {"m::t": "correct"}},
                "i2": {"gold_ok": "ok", "query_ok": "ok", "answers": {"m::t": "incorrect"}},
                "i3": {"gold_ok": "ok", "query_ok": "ok", "answers": {"m::t": "correct"}}}),
        ("rB", {"i1": {"gold_ok": "ok", "query_ok": "ok", "answers": {"m::t": "correct"}},
                "i2": {"gold_ok": "wrong", "query_ok": "ok", "answers": {"m::t": "incorrect"}},
                "i3": {"gold_ok": "ok", "query_ok": "ok", "answers": {"m::t": "correct"}}}),
    ]
    scopes, _, _, rows = grader_validity(items_idx, labelsets)
    assert scopes["all"]["tp"] == 1, scopes  # i1
    assert scopes["all"]["fp"] == 1, scopes  # i2 grader PASS, human incorrect
    assert scopes["all"]["fn"] == 1, scopes  # i3 grader FAIL, human correct
    kinds = {(r["id"], r["kind"]) for r in rows}
    assert ("i2", "fp") in kinds and ("i3", "fn") in kinds, kinds
    gi = gold_issues(items_idx, labelsets)
    assert any(g["id"] == "i2" and g["consensus"] == "DISAGREE" for g in gi), gi
    print("selftest OK  (α balanced-2x2=0.125; fp/fn detection + gold-issue surfacing verified)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--items", type=Path, default=OUT / "review_items.json")
    ap.add_argument("--labels", type=Path, nargs="+", help="labels_<id>.json files (≥2 for α)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        selftest(); return
    if not args.labels:
        ap.error("need --labels (or --selftest)")
    items = json.loads(args.items.read_text(encoding="utf-8"))
    items_idx = index_items(items)
    labelsets = load_labels(args.labels)
    if len(labelsets) < 2:
        print("⚠ only one label set — α needs ≥2 raters; reporting single-rater comparison.")
    report(items_idx, labelsets)


if __name__ == "__main__":
    main()
