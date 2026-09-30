# Run: `glm51_grep-only_L2_t1_grep_v10full`

**Overall: 607/626 pass (97.0%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| evp_vs_vp_disambig | 25/25 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| refuse | 90/90 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| nickname_grid | 60/61 | 98.4% |
| multi_hop | 17/18 | 94.4% |
| dept_member_count | 14/15 | 93.3% |
| retrieval | 13/14 | 92.9% |
| deep_multihop | 11/12 | 91.7% |
| listing_count | 18/20 | 90.0% |
| enterprise_shorthand | 18/20 | 90.0% |
| superlative | 9/10 | 90.0% |
| hard_multihop | 23/26 | 88.5% |
| hard_implicit_hierarchy | 13/19 | 68.4% |

## By priority

- P0: 224/226 (99.1%)
- P1: 349/364 (95.9%)
- P2: 34/36 (94.4%)

## Failures (19)

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
C-level ทั้ง 7 ท่านครับ:

- 🏢 **CEO** — วชิร จิรบุญ (เบอร์รี่) · VACHIR.CH@FAHMAI.CO.TH · ต่อ 73048
- 💰 **CFO** — กมลา ชัยสนธิ์สว่าง · KAMALA.CH@FAHMAI.CO.TH · ต่อ 74921
- 💻 **CTO** — ฤทธิชัย แก้วใสภิญโญ (ปันปัน) · RITTICHAI.KA@FAHMAI.CO.TH · ต่อ 75477
- ⚙️ **COO** — พงษ์กานต์ ราชชากัญญ์ · PONGKAN.RA@FAHMAI.CO.TH · ต่อ 75464
- 📣 **CMO** — ส้ม กาญจน์สถิต · SOM.KA@FAHMAI.CO.TH · ต่อ 79005
- 📦 **CPO*
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
**RET department size: 437 employees**

Breakdown by section:
- **RET-HQ** (HQ staff): 15
- **RET-BKK-SIAM** (Siam branch): 51
- **RET-BKK-LP** (Lad Phrao branch): 60
- **RET-BKK-BNA** (Bangna branch): 54
- **RET-CBI** (Chonburi branch): 40
- **RET-CNX** (Chiang Mai branch): 50
- **RET-HDY** (Hat Yai branch): 26
- **RET-HKT** (Phuket branch): 33
- **RET-KKN** (Khon Kaen branch): 21
- **RET-NMA** (
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM ดาวเหนือคือ **คุณวิเชียร พงหอมกลิ่น** (Wichian Phanghomklin)

- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (General Manager of DaoNuea)
- อีเมล: WICHIAN.PH@FAHMAI.CO.TH
- โทรภายใน: 76999
- สาขา: FahMai Tower 19F (BKK-R9)
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ สังกัดแผนก **DN (ดาวเหนือ)** ผู้บริหารสูงสุดของแผนกคือ **วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ

📧 **WICHIAN.PH@FAHMAI.CO.TH**
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
ธนพล พิประเสริฐ สังกัดแผนก WK (วงโคจร) — ผู้บริหารสูงสุดของแผนกคือ **กฤษ มหาแก้วใส** (ผู้จัดการทั่วไปแบรนด์วงโคจร) อีเมล: **KRIS.MA@FAHMAI.CO.TH**
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Daonuea (ดาวเหนือ) คือ **วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ

- 📧 WICHIAN.PH@FAHMAI.CO.TH
- 📞 ต่อ 76999 | มือถือ 064-902-5307
- 📍 FahMai Tower 19F
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The head of the Judchuem (จุดเชื่อม) department is **สรัล อาวุทธ์มณี (Saran Awutmani)**, General Manager of Judchuem (Director level).

- 📧 saran.aw@fahmai.co.th
- 📞 Ext. 78762 | 📱 064-655-7513
- 📍 FahMai Tower 24F, BKK-R9
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
**ราม ลวรรณ** (จุ๊บ) — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (KS-GM)

📧 RAM.LA@FAHMAI.CO.TH | ☎️ ต่อ 75965 | 📍 FahMai Tower 18F
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนกวงโคจร (WK) คือ **กฤษ มหาแก้วใส** (ชื่อเล่น: ขิง)

- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์วงโคจร (General Manager of WongkhoJon)
- อีเมล: KRIS.MA@FAHMAI.CO.TH
- โทรศัพท์: ต่อ 74375
- สถานที่: FahMai Tower 7F
```

### g460 [hard_implicit_hierarchy] P1/en
**Q:** In the FIN-AR section, who is the most senior employee?

**Fails:** missing any-of ['เมฆา', 'Mekha']; missing any-of ['ภัทรใจเขียว', 'Phatjaikieow']

**Response:**

```
The most senior employees in **FIN-AR** both started in **2020** (tied for earliest):

- **สนิท อธิบุญนำ** (SANIT ATHIBOONNAM) — Accounts Receivable Officer · ext. 79860
- **ธนวัฒน์ อารีวัฒน์** (TANAWAT AREEWAT) — Accounts Receivable Officer · ext. 74381
```

### g464 [hard_implicit_hierarchy] P1/en
**Q:** In the JC-ENG section, who is the most senior employee?

**Fails:** missing any-of ['กอบสุขบุญ', 'Kobsookbun']

**Response:**

```
Three employees in JC-ENG share the earliest start year of **2020**, making them the most senior:

- **สุขุม เกษมแช้มช้อย** (SUKHUM KASEMCHAEMCHOI) — Manager, ext 74900, SUKHUM.KA@FAHMAI.CO.TH
- **อุมา ประเกียรติกำจร** (UMA PRAKIATKAMJORN) — IC, ext 78200, UMA.PR2@FAHMAI.CO.TH
- **ฤทธิรงค์ ชาญณรงค์นาม** (RITTHIRONG CHANNARONGNAM) — IC, ext 36615, RITTHIRONG.CH@FAHMAI.CO.TH

All three started in 20
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
**7** employees in the DN department are at IC level and started in 2020.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
**6 employees** in the DN department are at Lead level and started in 2022:

- อภิชัย ธนบุญ — Lead DAONUEA BRAND MARKETER (DN-MKT)
- ธนพล พิไชยา — Lead DAONUEA PRODUCT MANAGER (DN-PD)
- กฤติน อนุเจริญ — Lead DAONUEA BRAND OPERATIONS (DN-OPS)
- ราม มหากิตติ — Lead DAONUEA BRAND OPERATIONS (DN-OPS)
- วีระ ชัยโชคดี — Lead DAONUEA PRODUCT MANAGER (DN-PD)
- กิตติศักดิ์ ฟ้าใสทอง — Lead DAONUEA BRAND MAR
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
PETER (ปีเตอร์) doesn't have a phone extension listed in the directory. He works remotely.
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ มหาวัฒน์ สังกัดอยู่ส่วน **JC-MKT** (แผนกการตลาดแบรนด์จุดเชื่อม) ตำแหน่งสูงสุดในส่วนงานนี้คือ **รองประธานฝ่ายจุดเชื่อม (JCVP)**

- **ราชินี อาทิตย์สุข** — รองประธานฝ่ายจุดเชื่อม
- 📞 ต่อ **75642**

หากต้องการติดต่อผู้จัดการทั่วไปแบรนด์จุดเชื่อม (GM) ซึ่งระดับรองลงมา:
- **สรัล อาวุทธ์มณี** — ผู้จัดการทั่วไปแบรนด์จุดเชื่อม
- 📞 ต่อ **78762**
```

### g672 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Chonburi branch?

**Fails:** missing count 49

**Response:**

```
**40** staff work at the Chonburi branch (CBI).
```

### g676 [enterprise_shorthand] P1/th
**Q:** พนักงานที่ทำงานทางไกล มีกี่คน

**Fails:** missing count 160

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ — ไดเรกทอรีไม่มีฟิลด์บันทึกสถานะการทำงานทางไกล จึงไม่สามารถนับได้ครับ
```

### g829 [deep_multihop] P2/th
**Q:** ในบรรดาแผนกที่มีรองประธานเป็นหัวหน้า แผนกที่มีพนักงานน้อยที่สุด ขอเบอร์ต่อของรองประธานของแผนกนั้นหน่อยครับ

**Fails:** missing any-of ['79653']

**Response:**

```
[agent error: BadRequestError: Error code: 400 - {'error': {'code': '1261', 'message': 'Prompt 超长'}}]
```

### g841 [superlative] P2/en
**Q:** Which department has the most employees company-wide?

**Fails:** missing any-of ['380']

**Response:**

```
Now I have the total counts from the search results. Let me compile them:

| Department | Total |
|---|---|
| CEO | 10 |
| FIN | 94 |
| TEC | 267 |
| OPS | 235 |
| MKT | 234 |
| SF | 140 |
| HR | 183 |
| LEG | 25 |
| LOG | 182 |
| SUP | 234 |
| RET | 437 |
| B2B | 60 |
| DN | 130 |
| KS | 100 |
| WK | 80 |
| JC | 80 |

**RET (Retail)** has the most employees with **437**, making it the largest dep
```

