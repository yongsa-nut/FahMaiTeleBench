# Name pools — source provenance

All Thai names used in `knowledge_base/employees.csv` are **synthetic combinations** of entries drawn from the following public name lists. No specific individual was replicated.

Retrieval date: **2026-04-19** (all sources).

## First names — `first_names_th.json` (253 entries)

| # | Source | URL | Retrieved |
|---|---|---|---|
| 1 | Ling-app — "150+ Names In Thai: Meanings And Cultural Insights" | https://ling-app.com/blog/names-in-thai/ | 2026-04-19 |
| 2 | Legit.ng — "130+ beautiful Thai female and male names with meanings" | https://www.legit.ng/1176191-common-thailand-names-meanings.html | 2026-04-19 |
| 3 | Moonboon — "110 cute Thai names for boys and girls" | https://moonboon.com/blogs/baby-names/thai-names | 2026-04-19 |

**Curation bias**: skewed toward *uncommon* / non-top-100 names. Common Thai first names like สมชาย (Somchai), สมศักดิ์ (Somsak), มะลิ (Mali) are deliberately underrepresented so that first-name-alone disambiguation is frequently ambiguous or empty — forcing the bot to combine with other fields.

## Last names — `last_names_th.json` (150 entries)

| # | Source | URL | Retrieved |
|---|---|---|---|
| 1 | Ling-app Medium — "100 Common Thai Surnames You Need To Know" | https://ling-app.medium.com/100-common-thai-surnames-you-need-to-know-be797a12c3bf | 2026-04-19 |
| 2 | Forebears.io — "Thailand: most common family names" | https://forebears.io/thailand/surnames | 2026-04-19 |

**Important context** — under Thailand's Surname Act 1913, Thai surnames are legally required to be unique to a family. Recurring surnames are mostly Sino-Thai (e.g., `แซ่ตั้ง` SAETANG, `แซ่ลิ้ม` SAELIM, `แซ่เล่า` SAELAU). Our pool includes 118 Thai-origin + 32 Sino-Thai to reflect real urban Thai company demographics (~20% Sino-Thai in Bangkok-centric office populations).

## Nicknames — `nicknames_th.json` (210 entries, 10 categories)

| # | Source | URL | Retrieved |
|---|---|---|---|
| 1 | EliteNameCrew — "501+ Common Thai Nicknames 2025–2026" | https://elitenamecrew.com/thai-nicknames/ | 2026-04-19 |
| 2 | FindNameZ — "120+ Common Thai Nicknames to Know" | https://findnamez.com/thai-nicknames/ | 2026-04-19 |
| 3 | Learn Thai with Mod — "Top 10 most Common Thai nicknames, and some weird ones" | https://learnthaiwithmod.com/2013/06/top-10-common-thai-nicknames-and-some-weird-ones/ | 2026-04-19 |

**Curation bias**: heavy on modern / weird / Gen-Z / English-loan forms (มิ้น Mint, เบนซ์ Benz, โฟกัส Focus, คอตตอน Cotton, เจแปน Japan, ไอโฟน iPhone, ปันปัน PanPan, etc.) and light on common baby nicknames (น้อง Nong, บอย Boy) to raise the real-person-collision risk bar and create harder nickname-lookup questions.

Category counts:
- modern 38 · food 35 · classic 25 · nature 21 · weird 17 · teen 17 · animal 15 · soft 15 · aesthetic 14 · doubled 13

## Nickname variants — `nickname_variants.json` (52 base nicknames)

No external source. These follow standard Thai diminutive/affectionate patterns documented across multiple cultural write-ups:

- **Suffix `-ตี้`** (Nat → Natty, Min → Minty) — most common modern diminutive
- **Doubled** (Pan → PanPan) — affectionate repetition
- **Honorific prefixes** `พี่-` (pee, elder) / `น้อง-` (nong, younger) / `เจ๊-` (jae)
- **Elongation** (Muk → MukNee)

These variants live **outside** the CSV. The question generator uses them to create adversarial items where the question asks about `นัตตี้` but the CSV only stores `นัต`. Participants' systems must either (a) strip diminutives, (b) do bidirectional substring match, or (c) refuse on zero results.

## Safeguards against real-person collision

1. **Random recombination** — first names, last names, nicknames are independently drawn and combined. No pool entry is tied to any specific real person's full name.
2. **Uncommon-first-name bias** — reduces overlap with celebrity/public-figure names.
3. **Unique-surname reality** — Thai surnames are legally family-unique, so recombining them with unrelated first names creates a full name that, statistically, no real Thai person has.
4. **Spot-check audit** (Gate D) — 50 randomly-sampled generated full names will be checked against a public-figure filter (Thai Wikipedia prominent-names + entertainment-industry lists). Any collision triggers re-seed and regeneration.

## Reproducibility

Pools are built by `scripts/build_name_pools.py` with inline-embedded source data. To regenerate:

```bash
python scripts/build_name_pools.py
```

Sort order: alphabetical by English form. Byte-stable output for diffs.
