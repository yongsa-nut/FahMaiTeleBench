# Run: `deepseekv4pro_grep-only_L2_t1_grep_v10full`

**Overall: 608/626 pass (97.1%)**

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
| nickname_grid | 61/61 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| dept_member_count | 15/15 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| listing_count | 20/20 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| refuse | 89/90 | 98.9% |
| enterprise_shorthand | 19/20 | 95.0% |
| retrieval | 13/14 | 92.9% |
| subsidiary_routing | 11/12 | 91.7% |
| deep_multihop | 11/12 | 91.7% |
| casual_name_lookup | 13/15 | 86.7% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| hard_multihop | 21/26 | 80.8% |
| superlative | 7/10 | 70.0% |

## By priority

- P0: 223/226 (98.7%)
- P1: 353/364 (97.0%)
- P2: 32/36 (88.9%)

## Failures (18)

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
คุณปลื้ม (กมลา อัครดวงกมล) — เบอร์มือถือ: **065-156-3892** ครับ
```

### g145 [casual_name_lookup] P0/th
**Q:** น้ำ โกวิท เบอร์อะไรครับ

**Fails:** missing any-of ['77251', 'KOVIT.MA']

**Response:**

```
คุณน้ำ (โกวิท มหามณี) — ผู้จัดการนักการตลาดแบรนด์ดาวเหนือ — เบอร์มือถือ **094-711-0811** ครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM ดาวเหนือคือ **คุณวิเชียร พงหอมกลิ่น** (Wichian Phonghomklin) ครับ

- 📧 WICHIAN.PH@FAHMAI.CO.TH
- 📞 เบอร์ต่อ: 76999
- 🏢 FahMai Tower 19F
```

### g404 [refuse] P1/th
**Q:** ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูลครับ — ในระบบไม่มีพนักงานชื่อ "ถาวร จิตรานนท์ฟ้า" ครับ

คนที่มีนามสกุล "จิตรานนท์ฟ้า" มี 3 ท่านคือ:
- **อิสระ จิตรานนท์ฟ้า** (SUP-PHN) เบอร์ต่อ 72554
- **สุจิรา จิตรานนท์ฟ้า** (LOG-FLT) เบอร์ต่อ 47209
- **อิสรา จิตรานนท์ฟ้า** (MKT-EVT) เบอร์ต่อ 78318

ส่วนชื่อ "ถาวร" ทั้ง 13 คนในระบบไม่มีใครใช้นามสกุลนี้ครับ อาจจะจำชื่อหรือนามสกุลผิดหรือเปล่าครับ?
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ สังกัดแผนก **DN (ดาวเหนือ)** ซึ่งผู้บริหารสูงสุดของแผนกคือ **GM (General Manager of DaoNuea)**

- **คุณวิเชียร พงหอมกลิ่น** — อีเมล: WICHIAN.PH@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก **JC (จุดเชื่อม)** ครับ ผู้บริหารสูงสุดของแผนกนี้คือ:

**สรัล อาวุทธ์มณี** — ผู้จัดการทั่วไปแบรนด์จุดเชื่อม (General Manager of JudChuem)  
📧 **SARAN.AW@FAHMAI.CO.TH**
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนก **KS (คลื่นเสียง)** ตำแหน่งนักการตลาดแบรนด์คลื่นเสียง

ผู้บริหารสูงสุดของแผนก KS คือ **คุณราม ลวรรณ** ตำแหน่งผู้จัดการทั่วไปแบรนด์คลื่นเสียง (General Manager of Kluensiang)

อีเมล: **RAM.LA@FAHMAI.CO.TH**
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก **WK (วงโคจร / WongKhoJon)** ครับ

ผู้บริหารสูงสุดของแผนก WK คือ **คุณกฤษ มหาแก้วใส (ขิง)** — ตำแหน่ง General Manager แบรนด์วงโคจร

📧 อีเมล: **KRIS.MA@FAHMAI.CO.TH**
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading Judchuem (จุดเชื่อม) is **Saran Awutmani** (สรัล อาวุทธ์มณี), General Manager of Judchuem.

- Email: SARAN.AW@FAHMAI.CO.TH
- Phone Extension: 78762
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Kluensiang (คลื่นเสียง) คือ **คุณราม ลวรรณ (จุ๊บ)** — General Manager of Kluensiang
📧 RAM.LA@FAHMAI.CO.TH | โทร 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนกวงโคจร (WK) คือ **กฤษ มหาแก้วใส (ขิง)** — ผู้จัดการทั่วไปแบรนด์วงโคจร
อีเมล: KRIS.MA@FAHMAI.CO.TH | เบอร์ต่อ: 74375
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
Peter (Arthit Watcharafa) — Lead QA Engineer, TEC-QA — doesn't have a phone extension listed in the directory. You can reach him at **ARTHIT.WA@FAHMAI.CO.TH** instead.
```

### g671 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาโคราช มีกี่คน

**Fails:** missing count 30

**Response:**

```
สาขาขอนแก่น (KKN) มีพนักงานทั้งหมด **21 คน** แบ่งเป็น:

- **Manager** 3 คน
- **Lead** 4 คน
- **IC (พนักงานขาย)** 14 คน
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
The Kluensiang brand is headed by **Ram Lawan** (ราม ลวรรณ), General Manager of Kluensiang.

📧 RAM.LA@FAHMAI.CO.TH · ☎️ 75965 · FahMai Tower 18F
```

### g828 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the most employees — what's the nickname of the secretary of the VP who heads that department?

**Fails:** missing any-of ['มุก', 'Mook']

**Response:**

```
Let me search for employees in each VP-headed department more directly.

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="grep_csv">
<｜｜DSML｜｜parameter name="max_matches" string="false">300</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="pattern" string="true">B2B</｜｜DSML｜｜parameter>
</｜｜DSML｜｜invoke>
<｜｜DSML｜｜invoke name="grep_csv">
<｜｜DSML｜｜parameter name="max_matches" string="false">300</｜｜DSML｜｜paramet
```

### g832 [superlative] P2/th
**Q:** ใครเป็นพนักงานที่อายุงานยาวนานที่สุดในฟ้าใหม่ครับ

**Fails:** missing any-of ['กนก', 'Kanok']; missing any-of ['เก่งกาจชัย', 'Khaengkadchai']

**Response:**

```
เท่าที่ตรวจสอบจากระบบ พนักงานที่เริ่มงานเร็วที่สุดที่พบคือ **คุณประยุทธ์ สมไชยา** ครับ  
- ตำแหน่ง: Director B2B Support Specialist  
- เริ่มงานปี: 2017  
- อีเมล: PRAYUT.SO2@FAHMAI.CO.TH
```

### g840 [superlative] P2/th
**Q:** section ไหนของฟ้าใหม่ที่มีพนักงานมากที่สุดครับ

**Fails:** missing any-of ['RET-BKK-LP']

**Response:**

```
Let me check the remaining departments and some specific RET section sizes.

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="grep_csv">
<｜｜DSML｜｜parameter name="max_matches" string="false">1</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="pattern" string="true">RET-HQ</｜｜DSML｜｜parameter>
</｜｜DSML｜｜invoke>
<｜｜DSML｜｜invoke name="grep_csv">
<｜｜DSML｜｜parameter name="max_matches" string="false">1</｜｜DSML｜｜para
```

### g841 [superlative] P2/en
**Q:** Which department has the most employees company-wide?

**Fails:** missing any-of ['380']

**Response:**

```
Based on the directory, here are the department headcounts:

| Department | Count |
|---|---|
| **RET** (Retail) | **416** |
| TEC (Technology) | 240 |
| MKT (Marketing) | 234 |
| OPS (Operations) | 232 |
| SUP (Customer Support) | 217 |
| LOG (Logistics) | 180 |
| SF (สายฟ้า) | 140 |
| DN (ดาวเหนือ) | 130 |
| KS (คลื่นเสียง) | 100 |
| FIN (Finance) | 94 |
| WK (วงโคจร) | 80 |
| JC (จุดเชื่อม) | 8
```

