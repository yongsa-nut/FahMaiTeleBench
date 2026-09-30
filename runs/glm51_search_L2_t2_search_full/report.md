# Run: `glm51_search_L2_t2_search_v10full`

**Overall: 602/626 pass (96.2%)**

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
| dept_listing_medium | 8/8 | 100.0% |
| dept_member_count | 15/15 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
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
| retrieval | 14/14 | 100.0% |
| enterprise_shorthand | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| bilingual | 39/40 | 97.5% |
| nickname_grid | 57/61 | 93.4% |
| listing_count | 18/20 | 90.0% |
| noisy_name_form | 18/20 | 90.0% |
| dept_listing_small | 6/7 | 85.7% |
| hard_multihop | 22/26 | 84.6% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 12/18 | 66.7% |

## By priority

- P0: 220/226 (97.3%)
- P1: 346/364 (95.1%)
- P2: 36/36 (100.0%)

## Failures (24)

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
C-level ทั้ง 7 ท่านครับ:

- **วชิร จิรบุญ** (เบอร์รี่) — CEO 🏢 ต่อ 73048 | vachir.ch@fahmai.co.th
- **กมลา ชัยสนธิ์สว่าง** — CFO 📊 ต่อ 74921 | 088-542-7748 | kamala.ch@fahmai.co.th
- **ฤทธิชัย แก้วใสภิญโญ** (ปันปัน) — CTO 💻 ต่อ 75477 | 082-837-1298 | rittichai.ka@fahmai.co.th
- **พงษ์กานต์ ราชชากัญญ์** — COO ⚙️ ต่อ 75464 | pongkan.ra@fahmai.co.th
- **ส้ม กาญจน์สถิต** — CMO 📣 ต่อ 79005 | som.ka@fah
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล — ไม่มีบุคคลชื่อ "อรุณ" ในแผนก SUP ครับ

(มีพนักงานชื่อ อรุณ ทั้งหมด 14 คน แต่ไม่มีคนอยู่แผนก SUP)
```

### g175 [nickname_grid] P0/th
**Q:** ตะวัน ที่อยู่ DN คือใคร

**Fails:** missing any-of ['Prija', 'พฤกษา']; missing any-of ['Manifa', 'มณีฟ้า']

**Response:**

```
ไม่พบข้อมูล — ไม่มีชื่อ "ตะวัน" ในแผนก DN (ดาวเหนือ)

พบชื่อ "ตะวัน" ทั้งหมด 7 คน แต่อยู่แผนกอื่น: TEC, RET, MKT, KS, FIN, HR
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
No unit called **CEO-SEC** exists, but the CEO's secretary/EA is:

- **อรญา วัชรกาญจน์ (ORRAYA WATCHARAKAN)** — น้องเป้ (PE)
- Position: Executive Assistant to CEO / เลขานุการของ CEO
- Unit: **CEO-EA**
- Ext: 75665 | Email: ORRAYA.WA@FAHMAI.CO.TH
- Office: FahMai Tower 7F

It looks like the unit code is **CEO-EA** rather than CEO-SEC.
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
**Wiriya Chanchai (วิริยะ จันทชัย)** — VP, Retail Network

- 📞 Ext: 79141 | 📱 082-034-8608
- ✉️ WIRIYA.CH@FAHMAI.CO.TH
- 📍 FahMai Tower 23F, BKK-R9
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มีเพียง 1 คน:

- **กิตติคุณ พงจงรัก** (บูม) — หัวหน้าสำนักงานประธาน / Chief of Staff
  - 📞 ต่อ 79367 | 📱 062-174-6941
  - 📧 KITTIKHUN.PH@FAHMAI.CO.TH
  - 📍 FahMai Tower 16F
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น (Wichian Phonghomklin)** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ

📞 ต่อ 76999 | 📱 064-902-5307 | ✉️ WICHIAN.PH@FAHMAI.CO.TH | 📍 FahMai Tower 19F
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
อัมพร ประฟ้า สังกัดแผนก **KS (คลื่นเสียง)** ซึ่งผู้บริหารสูงสุดของแผนกคือ **ราม ลวรรณ** (GM คลื่นเสียง) อีเมล: **RAM.LA@FAHMAI.CO.TH**
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล สังกัดแผนก WK (วงโคจร) ซึ่งผู้บริหารสูงสุดคือ **กฤษ มหาแก้วใส (คุณขิง)** — GM แบรนด์วงโคจร

📧 **KRIS.MA@FAHMAI.CO.TH**
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the **Judchuem (จุดเชื่อม)** department is:

- **สรัล อาวุทธ์มณี (Saran Awutmani)** — General Manager of Judchuem (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม)
- 📧 SARAN.AW@FAHMAI.CO.TH
- ☎️ Ext. 78762 | 📱 064-655-7513
- 📍 FahMai Tower 24F, BKK-R9
```

### g460 [hard_implicit_hierarchy] P1/en
**Q:** In the FIN-AR section, who is the most senior employee?

**Fails:** missing any-of ['เมฆา', 'Mekha']; missing any-of ['ภัทรใจเขียว', 'Phatjaikieow']

**Response:**

```
The most senior employees in FIN-AR both started in **2020** (the earliest year in the section):

- **สนิท อธิบุญนำ** (SANIT ATHIBOONNAM) — AR Officer, ext 79860, mobile 082-744-7187
- **ธนวัฒน์ อารีวัฒน์** (TANAWAT AREEWAT) — AR Officer, ext 74381, mobile 068-728-6438

They share the longest tenure in the section at ~5 years.
```

### g464 [hard_implicit_hierarchy] P1/en
**Q:** In the JC-ENG section, who is the most senior employee?

**Fails:** missing any-of ['กอบสุขบุญ', 'Kobsookbun']

**Response:**

```
The earliest start year in JC-ENG is **2020**, and three employees share it:

- **สุขุม เกษมแช้มช้อย** (SUKHUM KASEMCHAEMCHOI) — Manager, ext. 74900, SUKHUM.KA@FAHMAI.CO.TH
- **อุมา ประเกียรติกำจร** (UMA PRAKIATKAMJORN) — IC, ext. 78200, UMA.PR2@FAHMAI.CO.TH
- **ฤทธิรงค์ ชาญณรงค์นาม** (RITTHIRONG CHANNARONGNAM) — IC, ext. 36615, RITTHIRONG.CH@FAHMAI.CO.TH

All three started in 2020, making them th
```

### g521 [bilingual] P1/th
**Q:** Vice President Fleet เบอร์ extension อะไรครับ

**Fails:** missing any-of ['75089']

**Response:**

```
VP Logistics (Fleet) คือ **คุณณัฐกานต์ ศรีอารมณ์ดี (ติ๊ก)** — Extension: **75105** 📞
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
**7 employees** in the DN department at IC level started in 2020.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
**6 employees** in the DN department are at Lead level and started in 2022.
```

### g568 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ

**Fails:** missing any-of ['77008']

**Response:**

```
ไม่พบข้อมูลค่ะ
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดแผนก B2B ตำแหน่งสูงสุดใน B2B คือ **อุกฤษฎ์ วัชรเสริม** (VP B2B Sales)

- 📞 ต่อ **79274**
- 📧 UKRIT.WA@FAHMAI.CO.TH
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์ สังกัดแผนก **DN (ดาวเหนือ)** ตำแหน่งสูงสุดคือ VP ของฝ่ายดาวเหนือ:

**คุณเรืองศักดิ์ เทพเกียรติกำจร** — รองประธานฝ่ายดาวเหนือ
- 📞 Ext. **72280**
- ✉️ RUANGSAK.TH@FAHMAI.CO.TH
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คุณมนตรา (มิว) สังกัดแผนก **HR** → ตำแหน่งสูงสุดคือ **CHRO (C-level)**

**ณฐามน อภิชัยดี** — ประธานเจ้าหน้าที่ฝ่ายทรัพยากรบุคคล
- ต่อ: 79303
- มือถือ: 099-440-4759
- อีเมล: NATHAMON.AP@FAHMAI.CO.TH
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ สังกัดแผนก **JC (จุดเชื่อม)** — ตำแหน่งสูงสุดในแผนกคือ **VP ราชินี อาทิตย์สุข** (รองประธานฝ่ายจุดเชื่อม)

- 📞 ต่อ 75642
- 📧 RACHINI.AR@FAHMAI.CO.TH
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์สังกัดแผนก **KS (คลื่นเสียง)** ซึ่งตำแหน่งสูงสุดคือ **VP of KluenSiang**

- **ธเนศ บัวทองประเสริฐ** — รองประธานฝ่ายคลื่นเสียง
  - 📞 Ext. **71215** | 📱 **099-185-8401**
  - ✉️ TANET.BU@FAHMAI.CO.TH
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
คุณคำรณ ศรีอัญชลี สังกัดแผนก **OPS** (ฝ่ายปฏิบัติการ) — ตำแหน่งสูงสุดคือ **COO (ประธานเจ้าหน้าที่ปฏิบัติการ)**

👤 **พงษ์กานต์ ราชชากัญญ์** — COO
- 📞 Ext: **75464**
- 📧 PONGKAN.RA@FAHMAI.CO.TH
- 🏢 FahMai Tower 22F
```

### g639 [nickname_grid] P1/th
**Q:** เอ คือใคร มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
รายชื่อ EA (Executive Assistant) ทั้งหมด 7 คน ครับ:

- **CEO-EA** → อรญา วัชรกาญจน์ (เป้) · 75665 · ORRAYA.WA@FAHMAI.CO.TH
- **FIN-EA** → เบญจวรรณ โชคดีกำจร (มิ้น) · 75703 · BENJAWAN.CH@FAHMAI.CO.TH
- **TEC-EA** → จุฑามาศ แก้วใสพงศ์ (มิ้น) · 77008 · JUTHAMAS.KA@FAHMAI.CO.TH
- **OPS-EA** → ธนิดา ธนกอบสุข · 74037 · THANIDA.TH@FAHMAI.CO.TH
- **MKT-EA** → ดาริกา ดาวเรืองภิญโญ (ปิ๊ง) · 71338 · DARIKA.D
```

