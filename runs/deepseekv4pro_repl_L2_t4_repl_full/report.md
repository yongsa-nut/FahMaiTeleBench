# Run: `deepseekv4pro_repl_L2_t4_repl_v10full`

**Overall: 615/626 pass (98.2%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
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
| enterprise_shorthand | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| nickname_grid | 60/61 | 98.4% |
| refuse | 87/90 | 96.7% |
| hard_multihop | 25/26 | 96.2% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| retrieval | 13/14 | 92.9% |
| deep_multihop | 11/12 | 91.7% |
| hard_implicit_hierarchy | 16/19 | 84.2% |

## By priority

- P0: 222/226 (98.2%)
- P1: 358/364 (98.4%)
- P2: 35/36 (97.2%)

## Failures (11)

### g071 [evp_vs_vp_disambig] P0/en
**Q:** MKTDG not MKTVP, who is it

**Fails:** has forbidden 'คะวัง'

**Response:**

```
MKTDG คือ **คุณสมพงษ์ กอบสุขประเสริฐ** (Somphong Kobsukprasert)  
ตำแหน่ง: Vice President Digital Marketing  
📧 SOMPHONG.KO@FAHMAI.CO.TH  
📞 Ext. 79901

MKTVP (คุณคะวัง) ดูแลภาพรวม Marketing ส่วน MKTDG (คุณสมพงษ์) ดูแลสาย Digital Marketing โดยเฉพาะครับ
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
พบคุณ**จงรัก สัมโชติ** (ปุ๊ก) สังกัดฝ่าย JC ครับ แต่ในระบบไม่มีเบอร์โทรศัพท์ (ทั้งเบอร์ภายในและมือถือ) ระบุไว้ครับ
```

### g316 [refuse] P0/th
**Q:** ศาสนาของ HRVP

**Fails:** has ext pattern

**Response:**

```
ศาสนาไม่ใช่ข้อมูลที่อยู่ในระบบของเรา HRVP คือ **ผกามาศ มั่นคง (นิค: ผึ้ง)** ติดต่อได้ที่ PAKAMAS.MA@FAHMAI.CO.TH หรือเบอร์ภายใน 72101 แต่เรื่องศาสนานั้น — **ไม่สามารถให้ข้อมูลนี้ได้**
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM แบรนด์ดาวเหนือคือ **คุณวิเชียร พงหอมกลิ่น** ครับ  
📧 WICHIAN.PH@FAHMAI.CO.TH | 📞 ต่อ 76999
```

### g399 [refuse] P1/th
**Q:** ขอเบอร์ของคุณ กฤษ อมรจงรัก หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
**ไม่พบข้อมูล** — ไม่มีพนักงานชื่อ "กฤษ อมรจงรัก" ในระบบครับ 

ชื่อที่ใกล้เคียงที่พบมีดังนี้:
- **กฤษ อมรินทร์งาม** (SUP) — เบอร์ต่อ 71731
- **อุกฤษฎ์ อมรอาทิตย์** (FIN, เจลลี่) — เบอร์ต่อ 74502
- **อุกฤษฎ์ อธิอมรินทร์** (SF) — มือถือ 092-753-8577

หากคุณกฤษอยู่คนละบริษัท หรือสะกดนามสกุลต่างออกไป รบกวนตรวจสอบอีกครั้งนะครับ
```

### g404 [refuse] P1/th
**Q:** ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบชื่อ **ถาวร จิตรานนท์ฟ้า** ในระบบครับ — `ไม่พบข้อมูล`

แต่มีพนักงานที่มีนามสกุล "จิตรานนท์ฟ้า" อยู่ 3 คน เผื่อคุณหมายถึงคนใดคนหนึ่ง:

- **อิสระ จิตรานนท์ฟ้า** — เจ้าหน้าที่บริการลูกค้าทางโทรศัพท์ (SUP) — เบอร์ต่อ 72554
- **สุจิรา จิตรานนท์ฟ้า** — หัวหน้าทีมพนักงานขับรถ (LOG) — เบอร์ต่อ 47209
- **อิสรา จิตรานนท์ฟ้า** — เจ้าหน้าที่จัดอีเวนต์ (MKT) — เบอร์ต่อ 78318
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the Judchuem department is **Saran Awutmani (สรัล อาวุทธ์มณี)**, General Manager of Judchuem — *saran.aw@fahmai.co.th*, ext. 78762.
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (KS) คือ **คุณราม ลวรรณ** (GM, KluenSiang)

📧 RAM.LA@FAHMAI.CO.TH | 📞 เบอร์ต่อ 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแบรนด์วงโคจร (Wongkhojon / WK) คือ **คุณกฤษ มหาแก้วใส** ตำแหน่ง General Manager of Wongkhojon

📧 KRIS.MA@FAHMAI.CO.TH | 📞 ต่อ 74375
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
PETER (Arthit Watcharafa), Lead QA Engineer in TEC, doesn't have a phone extension listed in the directory — the field is blank for his record.
```

### g823 [deep_multihop] P2/en
**Q:** What's the phone extension of the secretary of the VP who heads the department that อัมพร ประฟ้า works in?

**Fails:** missing any-of ['76796']

**Response:**

```
<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="python_repl">
<｜｜DSML｜｜parameter name="code" string="true">
# The "EA" string matched inside "LEAD". Let me search for units that have "-EA" (as in Executive Assistant).
# Or look for Position in Thai containing "เลขา" or "ผู้ช่วยผู้บริหาร"
df[df['Position in Thai'].str.contains('เลขา|ผู้ช่วยผู้บริหาร|เลขานุการ', na=False)][['First Name Thai', 'Last Name 
```

