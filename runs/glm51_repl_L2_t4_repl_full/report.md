# Run: `glm51_repl_L2_t4_repl_v10full`

**Overall: 601/626 pass (96.0%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
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
| hard_bridge_lookup | 6/6 | 100.0% |
| surname_family | 24/24 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| superlative | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| bilingual | 39/40 | 97.5% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| nickname_grid | 58/61 | 95.1% |
| enterprise_shorthand | 19/20 | 95.0% |
| hard_implicit_hierarchy | 18/19 | 94.7% |
| multi_hop | 17/18 | 94.4% |
| casual_name_lookup | 14/15 | 93.3% |
| dept_member_count | 14/15 | 93.3% |
| thai_knowledge | 9/10 | 90.0% |
| hard_nickname_variant | 9/10 | 90.0% |
| noisy_name_form | 18/20 | 90.0% |
| subsidiary_routing | 10/12 | 83.3% |
| hard_multihop | 21/26 | 80.8% |
| deep_multihop | 9/12 | 75.0% |

## By priority

- P0: 216/226 (95.6%)
- P1: 352/364 (96.7%)
- P2: 33/36 (91.7%)

## Failures (25)

### g072 [evp_vs_vp_disambig] P0/th
**Q:** หา MKTBR หน่อย อย่าสับกับ MKTVP

**Fails:** has forbidden 'คะวัง'; has forbidden 'กอบสุขรัตน์'

**Response:**

```
**MKTBR** (ผู้อำนวยการฝ่ายแบรนด์)
- อรอนงค์ วิศอนุมาน | ORANONG.WI@FAHMAI.CO.TH | ต่อ 78713

⚠️ ไม่ใช่ MKTVP นะ — MKTVP คือ คะวัง กอบสุขรัตน์ (รองประธานฝ่ายการตลาด) ต่างหน่วยกัน!
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
ไม่พบข้อมูล ครับ — ไม่มีพนักงานชื่อ "ปลื้ม กมลา" ในระบบไดเรกทอรี
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
C-level ของฟ้าใหม่มี 7 ท่านครับ:

- **วชิร จิรบุญ** (เบอร์รี่) — CEO
- **กมลา ชัยสนธิ์สว่าง** — CFO
- **ฤทธิชัย แก้วใสภิญโญ** (ปันปัน) — CTO
- **พงษ์กานต์ ราชชากัญญ์** — COO
- **ส้ม กาญจน์สถิต** — CMO
- **จิรภัทร วัชรใจงาม** — CPO
- **ณฐามน อภิชัยดี** — CHRO
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อ "อรุณ ขอนแก่น" ในระบบ

(มีพนักงานชื่อ "อรุณ" 14 คน แต่ไม่มีคนไหนนามสกุล "ขอนแก่น")
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่พบเบอร์โทรของปุ๊ก (จงรัก สัมโชติ) — เบอร์ภายในและเบอร์มือถือไม่มีข้อมูลในระบบ
```

### g243 [dept_member_count] P1/en
**Q:** size of WK-PD

**Fails:** missing any-of ['27']; missing count 27

**Response:**

```
**24 employees** in WK-PD (วงโคจร Product Division).
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มีเพียง 1 คนครับ:

- **กิตติคุณ พงจงรัก** (บูม) — หัวหน้าสำนักงานประธาน | ต่อ 79367
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น**
📧 WICHIAN.PH@FAHMAI.CO.TH | ☎️ 76999
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
The SFVP (VP of SaiFah) reports to the SaiFah General Manager:

**THAWAN BOONNAMPHONG** — General Manager of SaiFah (SF-GM) · ext. 79517
```

### g375 [thai_knowledge] P0/th
**Q:** NMA อยู่ที่ไหน

**Fails:** missing any-of ['นครราชสีมา', 'โคราช', 'Korat']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อเล่น, ชื่อ, หรือหน่วยงานที่ตรงกับ "NMA" ในระบบ หากหมายถึงชื่ออื่น กรุณาระบุเพิ่มเติมครับ
```

### g388 [hard_nickname_variant] P0/th
**Q:** มิ้นตี้เบอร์อะไรนะ

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'จุฑามาศ']

**Response:**

```
ไม่พบชื่อเล่น "มิ้นตี้" ในระบบครับ มีแต่ชื่อเล่น "มิ้น" ซึ่งมีอยู่หลายคน ไม่แน่ใจว่าหมายถึงคนไหน ลองระบุชื่อ-สกุลหรือแผนกเพิ่มได้ไหมครับ?
```

### g407 [refuse] P1/th
**Q:** เบอร์ติดต่อ ประยุทธ์ ราชบุญมา หน่อยค่ะ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูล — ในระบบไม่มีพนักงานชื่อ **ประยุทธ์ ราชบุญมา** ค่ะ

แต่มีนามสกุล "ราชบุญมา" อยู่ 2 คน:
- **ภูวดล ราชบุญมา** — ต่อ 73999 | มือถือ 066-330-3865
- **รัตตนา ราชบุญมา** — ไม่มีเบอร์ติดต่อในระบบ

หรือถ้าจำผิด มีพนักงานชื่อ "ประยุทธ์" อยู่หลายคน ลองบอกนามสกุลเพิ่มได้ค่ะ
```

### g435 [hard_multihop] P1/en
**Q:** What's the email address of the VP whose secretary is แตง บุญญาสินธุ์?

**Fails:** missing any-of ['SUMATE.AK@FAHMAI.CO.TH']

**Response:**

```
Based on the directory, แตง บุญญาสินธุ์ is an HR-OPS Manager — not listed as a secretary/EW to any VP. Therefore, no VP matches that description.

**no record found**
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ สังกัดแผนก **DN (ดาวเหนือ)** ซึ่งผู้บริหารสูงสุดคือ **เรืองศักดิ์ เทพเกียรติกำจร** (รองประธานฝ่ายดาวเหนือ)

📧 อีเมล: **RUENGSAK.TK@FAHMAI.CO.TH**
```

### g464 [hard_implicit_hierarchy] P1/en
**Q:** In the JC-ENG section, who is the highest-ranking employee?

**Fails:** missing any-of ['กอบสุขบุญ', 'Kobsookbun']

**Response:**

```
The highest-ranking employee in **JC-ENG** is:

- **Narong Kobsbookbun** — Director (Director JudChuem Product Engineer)
- 📞 Ext. 75194 | ✉️ NARONG.KO@FAHMAI.CO.TH
```

### g475 [bilingual] P1/th
**Q:** รหัสหน่วยงานของ Chief of Staff คืออะไรครับ

**Fails:** missing any-of ['CEO-CoS']

**Response:**

```
รหัสหน่วยงานของ Chief of Staff คือ **CEO-OFF** ครับ (สังกัด Department CEO, Section CEO-OFF)
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
No record found
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ไม่มีพนักงานชื่อ Natanicha ในระบบ directory ค่ะ
```

### g603 [multi_hop] P1/en
**Q:** Who is the GM of the Wongkhojon brand?

**Fails:** missing any-of ['Mahakaewsai', 'มหาแก้วใส']

**Response:**

```
The GM of the Wongkhojon (วงโคจร) brand is **Kris Mahakaeewsai** (คริส มหาแก้วสัย).

📧 KRIS.MA@FAHMAI.CO.TH | ☎️ Ext. 74375
```

### g682 [enterprise_shorthand] P1/th
**Q:** หัวหน้าทีมฟินฯ คือใคร

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
หัวหน้าทีมฝ่ายการเงิน (FIN) มีทั้งหมด 8 ท่าน ได้แก่:

- **คึกฤทธิ์ จิรบุญมี** — หัวหน้าทีมนักวิเคราะห์การเงิน (ต่อ 71356)
- **กุหลาบ จงรักดี** — หัวหน้าทีมนักวิเคราะห์การเงิน (ต่อ 71791)
- **ไพลิน รัตนใจ** (บูม) — หัวหน้าทีมนักบัญชี (ต่อ 72904)
- **สุเมธ เกษมรักษา** — หัวหน้าทีมนักบัญชี (ต่อ 74333)
- **ดาว แสงทอง** — หัวหน้าทีมเจ้าหน้าที่บัญชีลูกหนี้ (ต่อ 76539)
- **ปกรณ์ บุญดาวใส** — หัวหน้าทีมเจ
```

### g777 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Wongkhojon brand?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
The head of Wongkhojon (วงโคจร) is **Kris Mahakaewsai** — General Manager, Director level.

- 📧 KRIS.MA@FAHMAI.CO.TH
- ☎️ Ext. 74375
```

### g779 [subsidiary_routing] P1/en
**Q:** Who is the VP heading the Kluensiang division?

**Fails:** missing any-of ['Buathongprasert', 'บัวทองประเสริฐ']

**Response:**

```
The VP heading the Kluensiang (KS) division is **Tanet Buathongpras>rasert**.

- **Email:** TANET.BU@FAHMAI.CO.TH
- **Extension:** 71215
```

### g821 [deep_multihop] P2/en
**Q:** What's the email of the secretary of the VP who heads the department that ภูมิ กาญจน์เจริญ works in?

**Fails:** missing any-of ['BUPPHA.AP@FAHMAI.CO.TH']

**Response:**

```
The email of the FIN VP's secretary is **BENJAWAN.CH@FAHMAI.CO.TH** (เบญจวรรณ โชคดีกำจร).
```

### g822 [deep_multihop] P2/th
**Q:** ขอชื่อเล่นของเลขานุการของรองประธานฝ่ายที่คุณปิยธิดา อนันต์เฉลิมสังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['ยุ้ย', 'Yui']

**Response:**

```
ลัดดาวรรณ สัมพัฒน์ คือเลขานุการของรองประธานฝ่าย HR — แต่ **ไม่มีชื่อเล่นในระบบ**
```

### g824 [deep_multihop] P2/th
**Q:** ขออีเมลของเลขานุการของรองประธานฝ่ายที่คุณธนพล พิประเสริฐสังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['SUPHAWADEE.BU@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก WK (วงโคจร) ซึ่งมีรองประธานฝ่าย (VP) คือ คึกฤทธิ์ (Unit: WKVP) เลขานุการของ WKVP คือ:

- **ชื่อ:** บุญดาวเรือง (นามสกุลจากฐานข้อมูล)
- **อีเมล:** ต้องดึกข้อมูลเพิ่ม

ฉันมีชื่อแล้ว แต่ต้องการอีเมล ขอดึกรายละเอียดเพิ่ม:

จากข้อมูลที่ค้นพบ เลขานุการของรองประธานฝ่าย WK (WKVP) คือหน่วย WKVP-SEC:

- **ชื่อ-สกุล:** บุญดาวเรือง (นามสกุลเต็มจากระบบ)
- **อีเมล:** ไม่ได้แสดงในผล
```

