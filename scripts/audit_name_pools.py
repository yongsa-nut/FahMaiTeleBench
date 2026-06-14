"""Audit the generated name pools for bad mappings + collisions."""
from __future__ import annotations

import io, json, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
POOLS = HERE.parent / "name_pools"


def audit(name: str, items, th_key="th", en_key="en"):
    print(f"\n=== {name} ({len(items)} entries) ===\n")

    # English romanization collisions (multiple TH → same EN)
    en_to_th = defaultdict(list)
    for it in items:
        en_to_th[it[en_key]].append(it[th_key])
    dupe_en = {e: ths for e, ths in en_to_th.items() if len(ths) > 1}
    if dupe_en:
        print(f"  [EN collisions] {len(dupe_en)} English forms with multiple Thai:")
        for e, ths in sorted(dupe_en.items()):
            print(f"    {e}  ←  {', '.join(ths)}")

    # Thai script collisions (same TH → multiple EN)
    th_to_en = defaultdict(list)
    for it in items:
        th_to_en[it[th_key]].append(it[en_key])
    dupe_th = {t: ens for t, ens in th_to_en.items() if len(ens) > 1}
    if dupe_th:
        print(f"  [TH collisions] {len(dupe_th)} Thai forms with multiple English:")
        for t, ens in sorted(dupe_th.items()):
            print(f"    {t}  →  {', '.join(ens)}")

    # Suspect romanization patterns (numbers appended, truncation markers)
    suspect = [it for it in items if any(c.isdigit() for c in it[en_key])]
    if suspect:
        print(f"  [Suspect EN] {len(suspect)} entries with digits (dedup hacks):")
        for s in suspect:
            print(f"    {s[th_key]}  en={s[en_key]}")


def main():
    first = json.load(open(POOLS / "first_names_th.json", encoding="utf-8"))["items"]
    last = json.load(open(POOLS / "last_names_th.json", encoding="utf-8"))["items"]
    nicks = json.load(open(POOLS / "nicknames_th.json", encoding="utf-8"))["items"]

    audit("first_names_th.json", first)
    audit("last_names_th.json", last)
    audit("nicknames_th.json", nicks)

    # Special: check royal/celebrity collision risk in surnames
    print("\n=== Surname safeguard check ===\n")
    ROYAL_WORDS = ["อดุลยเดช", "ภูมิพล", "สิริกิติ์", "รัตนโกสินทร์", "อยุธยา"]
    for w in ROYAL_WORDS:
        hits = [x for x in last if w in x["th"]]
        if hits:
            for h in hits:
                print(f"  ⚠ '{w}' found in surname: {h['th']} / {h['en']} — {h['meaning']}")


if __name__ == "__main__":
    main()
