# Run: `minimax_grep-only_L2_t1_grep_v10full`

**Overall: 549/626 pass (87.7%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| section_listing | 4/4 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| bilingual | 40/40 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 88/90 | 97.8% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| surname_family | 23/24 | 95.8% |
| multi_entity_turn | 19/20 | 95.0% |
| listing_count | 19/20 | 95.0% |
| retrieval | 13/14 | 92.9% |
| nickname_grid | 56/61 | 91.8% |
| subsidiary_routing | 11/12 | 91.7% |
| thai_knowledge | 9/10 | 90.0% |
| hard_implicit_hierarchy | 17/19 | 89.5% |
| dept_listing_medium | 7/8 | 87.5% |
| dept_member_count | 13/15 | 86.7% |
| noisy_name_form | 17/20 | 85.0% |
| hard_bridge_lookup | 5/6 | 83.3% |
| casual_name_lookup | 12/15 | 80.0% |
| hard_nickname_variant | 8/10 | 80.0% |
| enterprise_shorthand | 16/20 | 80.0% |
| counterfactual | 19/25 | 76.0% |
| org_informal_listing | 4/6 | 66.7% |
| deep_multihop | 8/12 | 66.7% |
| hard_multihop | 17/26 | 65.4% |
| multi_hop | 11/18 | 61.1% |
| superlative | 6/10 | 60.0% |
| name_lookup | 9/20 | 45.0% |
| org_plus_person | 1/3 | 33.3% |

## By priority

- P0: 204/226 (90.3%)
- P1: 317/364 (87.1%)
- P2: 28/36 (77.8%)

## Failures (77)

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
**รัตตนา เจริญฟ้า** — Secretary of RETBKK 📞 74330 | 📱 093-978-9586 | RATTANA.CH2@FAHMAI.CO.TH
```

### g114 [name_lookup] P1/th
**Q:** ขอเบอร์ สมพงษ์ อินทรีย์นาม หน่อย

**Fails:** missing any-of ['48530', 'SOMPHONG.IN', '085-412-9461']

**Response:**

```
ไม่พบข้อมูล
```

### g115 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ อรุณ ธนใจดี

**Fails:** missing any-of ['79827', 'AROON.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g116 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ สุขุม ใจเขียวบุญ

**Fails:** missing any-of ['55579', 'SUKHUM.JA', '085-612-9123']

**Response:**

```
ไม่พบข้อมูล
```

### g118 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ จักรี วัชรอารมณ์ดี

**Fails:** missing any-of ['23496', 'CHAKRI.WA']

**Response:**

```
ไม่พบข้อมูล
```

### g119 [name_lookup] P1/th
**Q:** หวาน กาญจน์วัฒน์ เบอร์อะไร

**Fails:** missing any-of ['77021', 'WAAN.KA']

**Response:**

```
ไม่พบข้อมูล
```

### g120 [name_lookup] P1/th
**Q:** ขอเบอร์ ณัฏฐพล ชากัญญ์รักษา หน่อย

**Fails:** missing any-of ['78664', 'NATTHAPHON.CH', '064-253-9320']

**Response:**

```
ไม่พบข้อมูล
```

### g121 [name_lookup] P1/th
**Q:** ขอเบอร์ สรพงษ์ วิศวงษ์ หน่อย

**Fails:** missing any-of ['72279', 'SORAPONG.WI', '091-061-7212']

**Response:**

```
ไม่พบข้อมูล
```

### g124 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ เมฆา ราชกำจร

**Fails:** missing any-of ['74887', 'MEKHA.RA']

**Response:**

```
ไม่พบข้อมูล
```

### g125 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ วีระ อมรจงรัก

**Fails:** missing any-of ['12774', 'VEERA.AM']

**Response:**

```
ไม่พบข้อมูล
```

### g126 [name_lookup] P1/th
**Q:** ไพบูลย์ อธิเกียรติกำจร เบอร์อะไร

**Fails:** missing any-of ['32610', 'PHAIBUN.AT', '086-112-6325']

**Response:**

```
ไม่พบข้อมูล
```

### g128 [name_lookup] P1/th
**Q:** กานติมา การเวกประเสริฐ เบอร์อะไร

**Fails:** missing any-of ['78422', 'KANTIMA.KA', '095-932-5295']

**Response:**

```
ไม่พบข้อมูล
```

### g136 [casual_name_lookup] P0/th
**Q:** พี่วิน อยู่ DN เบอร์อะไร

**Fails:** missing any-of ['71975', 'KITTICHAT.AR']

**Response:**

```
พี่วินใน DN คือ **กิตติชาติ อาทิตย์เฉลิม** — เบอร์ **068-463-2877** 📞
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
กมลา อัครดวงกมล (ชื่อเล่น ปลื้ม) — เบอร์มือถือ **065-156-3892** ครับ
```

### g145 [casual_name_lookup] P0/th
**Q:** น้ำ โกวิท เบอร์อะไรครับ

**Fails:** missing any-of ['77251', 'KOVIT.MA']

**Response:**

```
**น้ำ โกวิท** (ชื่อเล่น: น้ำ) — ผู้จัดการนักการตลาดแบรนด์ดาวเหนือ (DN)

📞 094-711-0811
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
**C-level (7 คน):**

| ตำแหน่ง | ชื่อ | Email |
|---|---|---|
| CEO | วชิร จิรบุญ (เบอร์รี่) | VACHIR.CH@fahmai.co.th |
| CFO | กมลา ชัยสนธิ์สว่าง | KAMALA.CH@fahmai.co.th |
| CTO | ฤทธิชัย แก้วใสภิญโญ (ปันปัน) | RITTICHAI.KA@fahmai.co.th |
| COO | พงษ์กานต์ ราชชากัญญ์ | PONGKAN.RA@fahmai.co.th |
| CMO | ส้ม กาญจน์สถิต | SOM.KA@fahmai.co.th |
| CPO | จิรภัทร วัชรใจงาม | JIRAPAT.WA@fahmai.co.th |
|
```

### g167 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นเต่ากี่คน

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
มี **13 คน** ที่มีชื่อเล่นหรือชื่อว่า "เต่า" ค่ะ
```

### g173 [nickname_grid] P0/th
**Q:** กบ ที่อยู่ B2B คือใคร

**Fails:** missing any-of ['Oranong', 'อรอนงค์']; missing any-of ['Ratanakasemkit', 'รัตนเกษม']

**Response:**

```
ไม่พบข้อมูล
```

### g192 [nickname_grid] P0/th
**Q:** ขอเบอร์พี่มุกกี้

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
ไม่พบชื่อเล่น "มุกกี้" ในระบบโดยตรงค่ะ แต่พบพนักงานชื่อเล่น "มุก" ทั้งหมด 13 คน ขอทราบแผนกหรือตำแหน่งที่ต้องการเพิ่มเติมได้ไหมคะ?
```

### g212 [dept_listing_medium] P1/en
**Q:** who's in OPS-FAC

**Fails:** min_items 5 not met (4)

**Response:**

```
**OPS-FAC — Facilities Section (23 people)**

- **Managers (2):** KRITSADA THANAKAEWSAI (ext. 76199) · NARIN KAEWSAIJAI (ext. 76684)
- **Leads (2):** YING THANACHAIDEE (ext. 79536) · CHONLATHEE ATHIKOBSOOK / Pudding (ext. 74105)
- **ICs (19):** Facilities Officers across various units (OPS-FAC-15, 16, 19, 22, 30, 51, 59, 63, 67, 72, 75, 81, 87, 88)

Most are based at FahMai Tower (BKK-R9), except 
```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
แผนก MKT มี **234 คน**
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
**RET (แผนกรีเทล):** มีพนักงานทั้งหมด **437 คน**
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (3)

**Response:**

```
รายชื่อพนักงานแผนก **คลื่นเสียง (KS)** 5 คน:

1. **ธเนศ บัวทองประเสริฐ** — รองประธานฝ่ายคลื่นเสียง (VP) | TANET.BU@FAHMAI.CO.TH | ต่อ 71215
2. **ปิยนันท์ พรหมพิทักษ์** — เลขานุการของ KSVP (Manager) | PIYANAN.PH@FAHMAI.CO.TH | ต่อ 76796
3. **ราม ลวรรณ (จุ๊บ)** — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (Director) | RAM.LA@FAHMAI.CO.TH | ต่อ 75965
4. **งามจิตร ประรักษา (แพร)** — เลขานุการของ B2BACC (Manager)
```

### g255 [org_informal_listing] P0/th
**Q:** วงโคจร มีใครบ้าง

**Fails:** min_items 5 not met (4)

**Response:**

```
## ฝ่ายวงโคจร (WK) — พบ 102 คน

### ผู้บริหาร
| ตำแหน่ง | ชื่อ | ชื่อเล่น | ติดต่อ |
|---|---|---|---|
| VP | คึกฤทธิ์ อัครเจริญ | ดำ | 097-302-2863 |
| GM | กฤษ มหาแก้วใส | ขิง | 74375 |
| Director (Engineering) | พิชัย อมรินทร์ฟ้า | — | 78177 |
| Director (Operations) | นางน้อย กาญจน์ชัย | เจน | 098-883-9879 |

### หัวหน้าทีม (Lead)
- จันทรา อภิกอบสุข (ไทเทิล) — MKT
- พิชัย สุวรรณเขียวขจี (โฟล์ค
```

### g266 [org_plus_person] P0/th
**Q:** VP SUP ใคร

**Fails:** missing any-of ['Awutdi', 'อาวุทธ์ดี']

**Response:**

```
**VP SUP (แผนกบริการลูกค้า)** มี 2 คน:

| ชื่อ | ตำแหน่ง | ช่องทางติดต่อ |
|---|---|---|
| ดาริกา อาวุทธดี (ตูน) | รองประธานฝ่ายบริการลูกค้า | darika.aw@fahmai.co.th, ต่อ 79070 |
| บุญชู ไกรศรีสว่าง | รองประธานฝ่ายประสบการณ์ลูกค้า | boonchu.kr@fahmai.co.th, ต่อ 73680 |

ทั้งคู่อยู่ที่ FahMai Tower ชั้น 5 และ 23 ตามลำดับครับ
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
The Bangkok retail VP is **Wiriya Chanchai (วิริยะ จันทชัย)**, nickname ติ๊ก — Vice President Retail Network, based at FahMai Tower 23F.  
Contact: WIRIYA.CH@FAHMAI.CO.TH · ext. 79141.
```

### g273 [multi_entity_turn] P0/en
**Q:** ext for SFVP, DNVP, KSVP

**Fails:** missing any-of ['72402']; missing any-of ['71215']

**Response:**

```
| Unit | ชื่อ (Nickname) | เบอร์โทร | Email |
|---|---|---|---|
| **SFVP** | วิรัตน์ สมบุษราคัม (ดอกไม้) | 064-970-0992 | WIRAT.SO@FAHMAI.CO.TH |
| **DNVP** | เรืองศักดิ์ เทพเกียรติกำจร | 72280 | RUANGSAK.TH@FAHMAI.CO.TH |
| **KSVP** | ธเนศ บัวทองประเสริฐ | 099-185-8401 | TANET.BU@FAHMAI.CO.TH |
```

### g317 [refuse] P0/th
**Q:** สัญชาติ CMO

**Fails:** has ext pattern

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้

(ระบบไม่บันทึกข้อมูลสัญชาติของพนักงาน)

---

แต่ขอแจ้งข้อมูล CMO ให้ทราบ:

**ส้ม กาญจน์สถิต (SOM KANSATHIT)**
- ตำแหน่ง: ประธานเจ้าหน้าที่การตลาด (CMO)
- แผนก: MKT
- Email: SOM.KA@FAHMAI.CO.TH
- ต่อ: 79005
- สังกัด: FahMai Tower 25F, สาขา BKK-R9 (HQ)
- เริ่มงาน: 2016
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
หน่วย **CEO-CoS** มีเพียงคนเดียว:

- **กิตติคุณ พงจงรัก (บูม)** — CHIEF OF STAFF | `@FAHMAI.CO.TH` | ต่อ 79367
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
**วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (DN-GM)

📧 WICHIAN.PH@FAHMAI.CO.TH | 📞 76999
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
**วชิร จิรบุญ (VACHIR CHIRABUN)** — CEO, FahMai Tower 12F | VACHIR.CH@FAHMAI.CO.TH
```

### g360 [hard_bridge_lookup] P0/th
**Q:** GM คลื่นเสียง ใคร

**Fails:** missing any-of ['Lawan', 'ลวรรณ']

**Response:**

```
**GM คลื่นเสียง (KluenSiang):** ราม ลวรณ (จุ๊บ) | RAM.LA@FAHMAI.CO.TH | Ext. 75965
```

### g379 [thai_knowledge] P0/th
**Q:** ใครมีชื่อเล่นเป็นชื่อผลไม้บ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล

ไม่มีพนักงานคนไหนในระบบที่มีชื่อเล่นเป็นชื่อผลไม้ค่ะ
```

### g386 [surname_family] P1/en
**Q:** how many employees share the surname วัชรบุญ

**Fails:** missing any-of ['3']; missing count 3

**Response:**

```
**6 employees** share the surname วัชรบุญ.
```

### g388 [hard_nickname_variant] P0/th
**Q:** มิ้นตี้เบอร์อะไรนะ

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'จุฑามาศ']

**Response:**

```

```

### g389 [hard_nickname_variant] P0/th
**Q:** พี่มุกกี้เบอร์อะไร

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอ 13 คนชื่อเล่น "มุก" ในระบบ พี่มุกกี้หมายถึงคนไหนคะ? เช่น แผนกไหน หรือตำแหน่งอะไร?
```

### g439 [hard_multihop] P1/en
**Q:** What's the email address of the VP whose secretary is ปิยนันท์ พรหมพิทักษ์?

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล

หากต้องการค้นหาด้วยชื่ออื่น หรือต้องการข้อมูลเพิ่มเติม กรุณาแจ้งมาได้เลยครับ
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก JC (จุดเชื่อม) คือ **คุณสรัล อาวุทธ์มณี** — อีเมล SARAN.AW@FAHMAI.CO.TH 📧
```

### g445 [hard_multihop] P1/en
**Q:** What's the phone extension of the VP who heads the department that สมตา ประเสริม works in?

**Fails:** missing any-of ['75642']

**Response:**

```
สมตา ประเสริม works in department **JC (จุดเชื่อม / Jud Chuem)**. The head of this department is **สรัล อาวุทธ์มณี (SARAN.AW)** — General Manager of Jud Chuem (Position Level: Director).

Phone extension: **78762**
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g448 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณเกษม วิศอัญชลี สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['PHAIROJ.MA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
**วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (DN-GM)

- 📧 WICHIAN.PH@FAHMAI.CO.TH
- 📞 064-902-5307
- 📍 FahMai Tower 19F
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **คลื่นเสียง (KS)** คือ **ราม ลวรรณ (จุ๊บ)** — ตำแหน่ง General Manager ของแบรนด์คลื่นเสียง 📧 RAM.LA@FAHMAI.CO.TH | ☎️ 75965
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
Based on the directory data, there are **0** employees in the DN department at IC level who started in 2020.

The search returned 50 DN department records, but none of them match both criteria (IC level AND start year 2020). The closest matches were DN employees at IC level with start years like 2021, 2022, 2023, 2024, and 2025, but no one with 2020.
```

### g559 [retrieval] P1/th
**Q:** ขอเบอร์ต่อของคุณ OKAY หน่อยครับ

**Fails:** missing any-of ['79936']

**Response:**

```
**คุณ OKAY (เจ้าหน้าที่จัดการข้อร้องเรียน / SUP-ESC-53)**

เบอร์ต่อ: **79996**
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
no record found
```

### g575 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Sombat Bunnamngam manager ทีม data scientist เบอร์อะไรครับ

**Fails:** missing any-of ['76059']

**Response:**

```
ไม่พบข้อมูลครับ
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดแผนก **B2B** (ฝ่ายขายองค์กร)

ผู้บริหารสูงสุดใน B2B คือ **อุกฤษฎ์ วัชรเสริม** — ตำแหน่ง รองประธานฝ่ายขายองค์กร (VP B2B Sales)

เบอร์ต่อ: **79274**
```


_+27 more failures — see results.jsonl_
