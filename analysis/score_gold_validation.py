# -*- coding: utf-8 -*-
"""Score the gold-validation study: agreement + the fix-list.

Usage:  python score_gold_validation.py gold_labels_raterA.json gold_labels_raterB.json

Reports, per check (gold_ok / wellformed / natural):
  - raw percent agreement between the two raters,
  - Krippendorff's alpha (nominal, 2 raters, inline computation — no dependency),
  - gold-confirmation rate (both raters said yes on gold_ok),
and prints every item where either rater answered no/unsure on any check (the fix-list
for adjudication), with comments.
"""
from __future__ import annotations

import io, json, sys
from collections import Counter
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

CHECKS = ["gold_ok", "wellformed", "natural"]


def kripp_alpha_nominal(pairs):
    """pairs = list of (a, b) category labels; nominal-level alpha for 2 raters."""
    vals = [v for p in pairs for v in p]
    n = len(vals)
    if n == 0:
        return float("nan")
    freq = Counter(vals)
    # observed disagreement
    do = sum(1 for a, b in pairs if a != b) / len(pairs)
    # expected disagreement from the pooled distribution
    de = 1 - sum((c / n) ** 2 for c in freq.values())
    if de == 0:
        return 1.0
    return 1 - do / de


def gwet_ac1(pairs):
    """Gwet's AC1 (first-order agreement coefficient), robust to skewed prevalence —
    the appropriate chance-corrected statistic when labels are near-constant
    (Gwet 2008; the 'high agreement, low kappa/alpha' paradox)."""
    if not pairs:
        return float("nan")
    cats = sorted({v for p in pairs for v in p})
    q = len(cats)
    if q < 2:
        return 1.0
    pa = sum(1 for a, b in pairs if a == b) / len(pairs)
    n = len(pairs)
    pe = 0.0
    for k in cats:
        pk = (sum(1 for a, _ in pairs if a == k) / n +
              sum(1 for _, b in pairs if b == k) / n) / 2
        pe += pk * (1 - pk)
    pe /= (q - 1)
    if pe >= 1.0:
        return float("nan")
    return (pa - pe) / (1 - pe)


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    A = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    B = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    la, lb = A["labels"], B["labels"]
    ids = sorted(set(la) & set(lb))
    only = sorted(set(la) ^ set(lb))
    print(f"raters: {A.get('rater')} + {B.get('rater')}  |  co-labeled items: {len(ids)}"
          + (f"  (labeled by one rater only: {only})" if only else ""))

    for ck in CHECKS:
        pairs = [(la[i].get(ck), lb[i].get(ck)) for i in ids
                 if la[i].get(ck) and lb[i].get(ck)]
        agree = sum(1 for a, b in pairs if a == b)
        alpha = kripp_alpha_nominal(pairs)
        ac1 = gwet_ac1(pairs)
        line = (f"{ck:<11} n={len(pairs):<3} agree={agree}/{len(pairs)}"
                f" ({100*agree/max(1,len(pairs)):.0f}%)  Gwet AC1={ac1:.3f}"
                f"  (Krippendorff α={alpha:.3f} — uninformative under near-constant labels)")
        if ck == "gold_ok":
            both_yes = sum(1 for a, b in pairs if a == b == "yes")
            line += f"  |  gold confirmed by BOTH: {both_yes}/{len(pairs)} ({100*both_yes/max(1,len(pairs)):.0f}%)"
        print(line)

    print("\n== fix-list (any rater said no/unsure on any check) ==")
    n_flag = 0
    for i in ids:
        flags = []
        for ck in CHECKS:
            va, vb = la[i].get(ck), lb[i].get(ck)
            if va not in (None, "yes") or vb not in (None, "yes"):
                flags.append(f"{ck}: A={va} B={vb}")
        if flags:
            n_flag += 1
            print(f"  {i}: " + "; ".join(flags))
            for tag, lab in (("A", la[i]), ("B", lb[i])):
                c = (lab.get("comment") or "").strip()
                if c:
                    print(f"      {tag}: {c}")
    if n_flag == 0:
        print("  (none — all checks passed by both raters)")
    print(f"\nflagged items: {n_flag}/{len(ids)} → adjudicate these for the camera-ready.")


if __name__ == "__main__":
    main()
