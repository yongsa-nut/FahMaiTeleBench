# FahMai — Organisational Chart (Level 2 reference)

**Human-only reference. NOT given to the bot.**

This file is the source-of-truth for the code scheme used in `knowledge_base/employees.csv`. It is for benchmark authors and future auditors. Participants see only the CSV; they must infer hierarchy from it.

---

## Leadership

```
Founder & Chairman : สมชาย ฟ้าสว่าง  (canon, not queryable as "CEO")
│
├── Board of Directors   (~5 external directors; not in CSV)
│
└── Chief Executive Officer  (1 — fresh synthetic person; generated at Gate D)
    │
    ├── Chief Financial Officer   (CFO)
    ├── Chief Technology Officer  (CTO)
    ├── Chief Operating Officer   (COO)
    ├── Chief Marketing Officer   (CMO)
    ├── Chief Product Officer     (CPO)   ← owns all 5 house brands
    ├── Chief Human Resources Off (CHRO)
    │
    └── Chief of Staff             (reports directly to CEO)
```

Exec Office (under CEO): CEO's Executive Assistant, Secretary, Chief of Staff, ~4 Strategy & Ops ICs.

## Departments — 16 top-level codes

Corporate functions (11):

| Code | Name EN | Name TH | Headcount target |
|---|---|---|---|
| `CEO` | Executive Office | สำนักประธานเจ้าหน้าที่บริหาร | ~10 |
| `FIN` | Finance | การเงินและบัญชี | ~90 |
| `HR` | Human Resources | ทรัพยากรบุคคล | ~50 |
| `LEG` | Legal & Compliance | กฎหมายและกำกับดูแล | ~25 |
| `MKT` | Marketing & Brand | การตลาดและแบรนด์ | ~110 |
| `TEC` | Technology & Engineering | เทคโนโลยีและวิศวกรรม | ~240 |
| `OPS` | Operations | ปฏิบัติการ | ~120 |
| `LOG` | Logistics & Warehouse | คลังสินค้าและโลจิสติกส์ | ~180 |
| `SUP` | Customer Support | บริการลูกค้า | ~200 |
| `RET` | Retail Network | เครือข่ายร้านค้าและศูนย์บริการ | ~380 |
| `B2B` | B2B Sales | การขายองค์กร | ~60 |

Product divisions (5 — one per house brand; each has Product, Engineering, Brand Ops teams):

| Code | Brand (TH / EN) | Product category | Headcount target |
|---|---|---|---|
| `SF` | สายฟ้า (SaiFah) | Smartphones & Tablets | ~140 |
| `DN` | ดาวเหนือ (DaoNuea) | Computers & Laptops | ~130 |
| `KS` | คลื่นเสียง (KluenSiang) | Audio & Multimedia | ~100 |
| `WK` | วงโคจร (WongKhoJon) | Wearables & Fitness | ~80 |
| `JC` | จุดเชื่อม (JudChuem) | Accessories & Connectivity | ~80 |

Total across 16 departments: ~**1,995** employees + ~5 executive-tier → **~2,000**.

## Sections — ~80 total

Section code pattern: `<DEPT>-<TEAM>` (2–4 letters for the team identifier).

### Corporate sections

**Convention:** each department with a C-level leader has a `<DEPT>-EXEC` section that houses the C-level row and their Executive Assistant. Everyone else sits in a function-specific section below.

```
CEO    CEO-OFF   Office of the CEO
       CEO-SEC   Secretariat
       CEO-STR   Strategy & Special Projects

FIN    FIN-EXEC  Finance Executive Office (CFO + EA)
       FIN-AP    Accounts Payable
       FIN-AR    Accounts Receivable
       FIN-GL    General Ledger
       FIN-FP    Financial Planning & Analysis
       FIN-TR    Treasury
       FIN-TAX   Tax

HR     HR-EXEC   HR Executive Office (CHRO + EA)
       HR-TA     Talent Acquisition
       HR-LD     Learning & Development
       HR-OPS    HR Operations
       HR-COMP   Compensation & Benefits
       HR-CUL    Culture & Engagement

LEG    LEG-CNT   Contracts
       LEG-IP    Intellectual Property
       LEG-COM   Compliance & Regulatory

MKT    MKT-EXEC  Marketing Executive Office (CMO + EA)
       MKT-BR    Brand Marketing
       MKT-DIG   Digital & Performance
       MKT-CON   Content Studio
       MKT-PR    Public Relations
       MKT-CRM   CRM & Retention
       MKT-EVT   Events & Partnerships

TEC    TEC-EXEC  Tech Executive Office (CTO + EA)
       TEC-BE    Backend Engineering
       TEC-FE    Frontend Engineering
       TEC-MOB   Mobile Engineering
       TEC-DS    Data Science & ML
       TEC-SEC   Information Security
       TEC-INF   Infrastructure & DevOps
       TEC-PLT   Platform Engineering
       TEC-QA    QA Engineering
       TEC-DATA  Data Engineering

OPS    OPS-EXEC  Ops Executive Office (COO + EA)
       OPS-FAC   Facilities
       OPS-PROC  Procurement
       OPS-PMO   Program Management
       OPS-ADM   Administration
       OPS-TRV   Travel & Expense

LOG    LOG-WH    Warehouse
       LOG-SHP   Shipping & Delivery
       LOG-INV   Inventory Control
       LOG-RET   Returns Processing
       LOG-FLT   Fleet Management

SUP    SUP-CHAT  Chat & Line Support
       SUP-PHN   Phone Support
       SUP-EML   Email Support
       SUP-TECH  Technical Support
       SUP-ESC   Escalations
       SUP-TRN   Training

RET    RET-HQ    Retail Operations HQ
       RET-BKK-SIAM    Bangkok Siam branch
       RET-BKK-LP      Bangkok Lad Phrao branch
       RET-BKK-R9      Bangkok Rama IX branch (co-located with HQ)
       RET-CNX         Chiang Mai Nimmanhaemin branch
       RET-HKT         Phuket Central branch
       RET-TRN         Retail Training

B2B    B2B-SLS   Corporate Sales
       B2B-ACC   Account Management
       B2B-SOL   Solutions Engineering
       B2B-SUP   B2B Support
```

### Product-division sections (same pattern in each brand)

The CPO's row sits in `SF-EXEC` (primary home = SaiFah, the flagship brand) but their scope is all five divisions.

```
SF     SF-EXEC   SaiFah Executive Office (houses CPO + EA)
       SF-PD     Product Management
       SF-ENG    Hardware/Software Engineering
       SF-OPS    Brand Operations
       SF-MKT    Brand Marketing (dotted-line to MKT)

DN     DN-PD
       DN-ENG
       DN-OPS
       DN-MKT

KS     KS-PD, KS-ENG, KS-OPS, KS-MKT

WK     WK-PD, WK-ENG, WK-OPS, WK-MKT

JC     JC-PD, JC-ENG, JC-OPS, JC-MKT
```

## Unit codes

Narrow scope — typically 1–5 employees per Unit. Three patterns:

1. **VP of a function:** `<DEPT>VP` or `<DEPT>-<ROLE>VP`. Examples: `CFOVP` (= CFO's own row), `FINVP` (VP Finance, usually same person as CFO in small orgs — we split roles so CFO ≠ FIN-VP), `SFVP` (VP of SaiFah division).
2. **Team leaf:** `<SECTION>-<n>` when a section has > 1 team. Example: `TEC-BE-1` vs `TEC-BE-2` (two backend squads).
3. **Special roles:** `CEO-CoS` (Chief of Staff), `CEO-EA` (CEO Executive Assistant), `<SECTION>-LEAD` (team lead row), `<SECTION>-MGR` (manager row).

Unique Unit codes target: ~**600** across 2,000 employees (≈3.3 per unit on average, heavy tail).

## Position Level (column 19)

Six-level enum. Controls role distribution.

| Level | Target headcount | Who |
|---|---|---|
| `C-level` | ~8 | CEO + 6 C-suite + Chief of Staff |
| `VP` | ~25 | Division / functional VPs (one per dept, product-div VP) |
| `Director` | ~45 | Senior reports to VPs |
| `Manager` | ~120 | People managers |
| `Lead` | ~150 | Team leads / ICs with scope |
| `IC` | ~1,650 | Individual contributors |

## Branches (column 17)

**11 enum values.** The 5 original service-center locations (from Level 1 canon) + 5 newer field offices / branches / warehouses the company has opened since + `REMOTE`. `Branch` is independent of `Department` — a Tech engineer can sit at any branch; retail staff are pinned to their branch.

| Code | Name EN | Name TH | Role |
|---|---|---|---|
| `BKK-R9` | Rama IX HQ | สำนักงานใหญ่ พระราม 9 | HQ — most corporate staff |
| `BKK-SIAM` | Siam | สาขาสยาม | branch + service center (canon) |
| `BKK-LP` | Lad Phrao | สาขาลาดพร้าว | branch + service center (canon) |
| `BKK-BNA` | Bangna | สาขาบางนา | branch + warehouse (new) |
| `BKK-PKT` | Samut Prakan / Bang Phli | ศูนย์กระจายสินค้า บางพลี | main distribution warehouse |
| `CNX` | Chiang Mai | สาขาเชียงใหม่ นิมมานเหมินทร์ | branch + service center (canon) |
| `KKN` | Khon Kaen | สาขาขอนแก่น | regional office NE |
| `NMA` | Nakhon Ratchasima / Korat | สาขานครราชสีมา (โคราช) | regional office NE |
| `CBI` | Chonburi / Pattaya | สาขาชลบุรี พัทยา | East coast branch |
| `HKT` | Phuket | สาขาภูเก็ต เซ็นทรัล | branch + service center (canon) |
| `HDY` | Hat Yai | สาขาหาดใหญ่ | Southern regional office |
| `REMOTE` | Remote | ทำงานทางไกล | ~10% of Tech + Marketing |

**Branch distribution target** (sums to 100%):

| Code | % | Who lives there |
|---|---|---|
| `BKK-R9` | 55% | HQ — most corporate, most C-suite, most TEC/FIN/HR/LEG/MKT leadership |
| `BKK-PKT` | 9% | Warehouse — LOG staff |
| `REMOTE` | 9% | ~10% TEC + some MKT/DS |
| `BKK-SIAM` | 5% | branch retail + service |
| `BKK-LP` | 5% | branch retail + service |
| `BKK-BNA` | 4% | branch retail + small warehouse |
| `CNX` | 4% | branch + regional |
| `HKT` | 3% | branch + regional |
| `CBI` | 2.5% | East-coast branch |
| `KKN` | 1.5% | regional office |
| `NMA` | 1.5% | regional office |
| `HDY` | 0.5% | southern outpost |

Note: only the 5 canon branches (BKK-SIAM, BKK-LP, CNX, HKT, plus BKK-R9 HQ) are service centers per Level 1. The others are offices / warehouses — referenced in questions but not customer-facing.

## Shorthand / informal patterns

These show up in natural questions but NOT as CSV values — models must map them to formal codes or refuse.

### Dept informal → formal

| Shorthand | Maps to | Shown how in question |
|---|---|---|
| "DN" | Department `DN` | "ใครอยู่ใน DN บ้าง" |
| "DaoNuea team" / "ทีมดาวเหนือ" | Department `DN` | "VP ของ DaoNuea คือใคร" |
| "Retail" / "RET" / "ฝ่ายร้านค้า" | Department `RET` | |
| "Support" / "SUP" / "ฝ่ายลูกค้า" | Department `SUP` | |
| "Finance" / "FIN" / "บัญชี" | Department `FIN` | |
| "Tech" / "TEC" / "ไอที" / "เทคโนโลยี" | Department `TEC` | |

### Acronym collisions (adversarial)

Near-miss codes we plant to stress-test disambiguation — the EVPN↔EVPP pattern from the source project. **6 pairs: 5 English-code pairs + 1 Thai-language pair.**

| Code A | Code B | Who they are |
|---|---|---|
| `SFVP` | `SFDR` | VP of SaiFah brand vs. Director of SF operations |
| `FINVP` | `FINFP` | VP Finance vs. Director Financial Planning |
| `TECVP` | `TECPM` | CTO / VP of Tech vs. VP of Platform |
| `MKTVP` | `MKTBR` | CMO vs. Director Brand |
| `FIN-AP` | `FIN-AR` | Accounts Payable lead vs. Accounts Receivable lead |
| **Thai position text:** `ผู้อำนวยการฝ่ายบัญชี` | `ผู้อำนวยการฝ่ายการเงิน` | Director Accounting vs. Director Finance — same `FIN` department, different sections, near-identical Thai position text only 2 chars apart |

### Branch shorthand

| Shorthand | Maps to |
|---|---|
| "สาขาสยาม" / "Siam" | `BKK-SIAM` |
| "สาขาเชียงใหม่" / "Chiang Mai" / "นิมมาน" | `CNX` |
| "ภูเก็ต" / "Phuket" | `HKT` |
| "ลาดพร้าว" | `BKK-LP` |
| "พระราม 9" / "HQ" / "สำนักงานใหญ่" | `BKK-R9` |

### Role shorthand (Thai)

| Shorthand | Maps to |
|---|---|
| "เลขา" | Position contains `SECRETARY` or `EXECUTIVE ASSISTANT` |
| "หัวหน้าแผนก" | Director / Manager of that Department |
| "ผู้จัดการ" | Manager level |
| "ผอ." / "ผู้อำนวยการ" | Director level |

## Generation rules (for `scripts/generate_employees.py`)

1. **Determinism:** single seed `20260419`.
2. **ID format:** `0000<4 digits>` for pre-2020 hires, `08<6 digits>` for 2020+ (both are 8-digit; matches the source project regex guards).
3. **Email:** `<FIRSTNAME>.<FIRSTLETTEROFLAST>@FAHMAI.CO.TH`, all uppercase. Collisions resolved by appending middle-initial or digit (to give the bot realistic near-miss cases).
4. **Phone Extension:** 5 digits, seeded by branch prefix (BKK-R9 starts `7xxxx`, BKK-SIAM `1xxxx`, etc.). Blank for remote + ~5% field staff.
5. **Mobile:** `08x-xxx-xxxx` or `09x-xxx-xxxx` Thai format; 55% blank.
6. **Planted disambiguation (for harder question buckets):**
   - At least 3 employees share each of ~20 seeded "ambiguous nicknames" (e.g., 3 people with nickname `ไอซ์`).
   - At least 5 employees share each of ~10 seeded common first-names for name_lookup stress.
   - Every house-brand division has exactly one GM row with `Position in English` containing `GENERAL MANAGER OF <BRAND>`.

7. **Secretary / Executive Assistant rows — explicit coverage.** This is the the source project `evp_secretary` bucket's load-bearing design. Every senior leader has **exactly one** named secretary or executive assistant row in the CSV, constructed so that questions like `"เลขาของ CFO คือใคร"` have a unique, unambiguous answer.

   | Leader | Secretary position text (TH) | Position text (EN) | Unit code |
   |---|---|---|---|
   | CEO | `เลขานุการของ CEO` | `EXECUTIVE ASSISTANT TO CEO` | `CEO-EA` |
   | CFO | `เลขานุการของ CFO` | `EXECUTIVE ASSISTANT TO CFO` | `FIN-EA` |
   | CTO | `เลขานุการของ CTO` | `EXECUTIVE ASSISTANT TO CTO` | `TEC-EA` |
   | COO | `เลขานุการของ COO` | `EXECUTIVE ASSISTANT TO COO` | `OPS-EA` |
   | CMO | `เลขานุการของ CMO` | `EXECUTIVE ASSISTANT TO CMO` | `MKT-EA` |
   | CPO | `เลขานุการของ CPO` | `EXECUTIVE ASSISTANT TO CPO` | `CPO-EA` |
   | CHRO | `เลขานุการของ CHRO` | `EXECUTIVE ASSISTANT TO CHRO` | `HR-EA` |
   | Every VP (~25) | `เลขานุการของ <UNIT>` | `SECRETARY OF <UNIT>` | `<UNIT>-SEC` |

   Total: ~**33 secretary rows** (7 C-level + 25 VP + CEO Chief of Staff). All secretaries sit in the **same Department / Branch as their boss**, so org-level questions don't accidentally leak them.

   **Adversarial wrinkle (the source project lesson):** sign two of the secretaries as women with the SAME nickname but different bosses — e.g., both `เลขาของ CFO` and `เลขาของ COO` have nickname `มิ้น`. This stresses the `evp_secretary` + `casual_name_lookup` intersection the way the the source project EVPN/EVPP confusion did in production.

---

**End of ORG_CHART.md.** Next file to produce: `name_pools/*.json` (Gate B).
