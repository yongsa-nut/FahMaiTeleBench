# Run: `gemma4_repl_L2_t4_repl_full`

**Overall: 532/626 pass (85.0%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_vs_vp_disambig | 25/25 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| dept_member_count | 14/15 | 93.3% |
| retrieval | 13/14 | 92.9% |
| hard_nickname_variant | 9/10 | 90.0% |
| bilingual | 36/40 | 90.0% |
| listing_count | 18/20 | 90.0% |
| superlative | 9/10 | 90.0% |
| casual_name_lookup | 13/15 | 86.7% |
| dept_listing_small | 6/7 | 85.7% |
| email_identity_lookup | 5/6 | 83.3% |
| nickname_grid | 49/61 | 80.3% |
| evp_secretary | 4/5 | 80.0% |
| hard_implicit_hierarchy | 14/19 | 73.7% |
| hard_multihop | 19/26 | 73.1% |
| counterfactual | 18/25 | 72.0% |
| thai_knowledge | 7/10 | 70.0% |
| noisy_name_form | 14/20 | 70.0% |
| deep_multihop | 8/12 | 66.7% |
| enterprise_shorthand | 13/20 | 65.0% |
| multi_hop | 11/18 | 61.1% |
| subsidiary_routing | 7/12 | 58.3% |
| org_informal_listing | 3/6 | 50.0% |
| surname_family | 12/24 | 50.0% |

## By priority

- P0: 200/226 (88.5%)
- P1: 301/364 (82.7%)
- P2: 31/36 (86.1%)

## Failures (94)

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
Rachata Samchannarong (RACHATA.SA@FAHMAI.CO.TH, Ext: 76406)
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
ไม่พบข้อมูล
```

### g152 [casual_name_lookup] P0/en
**Q:** Ploy from SF, what's the number

**Fails:** missing any-of ['79301', 'PHITSAMAI.KA']

**Response:**

```
Phloi Daoruengchot (SF): Ext. 79180
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
ผู้บริหารระดับสูง (C-level และ VP) มีหลายท่านครับ ตัวอย่างเช่น:

**ระดับ C-level:**
* คุณวชิร จิรบุญ (CEO)
* คุณกมลา ชัยสนธิ์สว่าง (CFO)
* คุณฤทธิชัย แก้วใสภิญโญ (CTO)
* คุณพงษ์กานต์ ราชชากัญญ์ (COO)
* คุณส้ม กาญจน์สถิต (CMO)
* คุณจิรภัทร วัชรใจงาม (CPO)
* คุณณฐามน อภิชัยดี (CHRO)

**ระดับ VP (ตัวอย่าง):**
* คุณแสงดาว พิดวงกมล (VP Finance)
* คุณสุเมธ อัครใจงาม (VP HR)
* คุณไพโรจน์ มหากุล (VP Legal
```

### g170 [nickname_grid] P0/th
**Q:** นับคนชื่อปลื้มให้หน่อย

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
ไม่พบข้อมูล
```

### g171 [nickname_grid] P0/th
**Q:** เสือ ที่ KS เบอร์อะไร

**Fails:** missing any-of ['Anuboonrueng', 'อนุบุญเรือง']

**Response:**

```
คุณวชิร (เสือ) เบอร์ต่อ 72469 ครับ
```

### g172 [nickname_grid] P0/th
**Q:** ขิง ที่ SUP เบอร์อะไร

**Fails:** missing any-of ['Pholdech', 'พลเดช']

**Response:**

```
คุณสุณี (ขิง) เบอร์โทร 094-546-2762 ต่อ 71734 ครับ
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล ของคุณอรุณในแผนก SUP ครับ
```

### g175 [nickname_grid] P0/th
**Q:** ตะวัน ที่อยู่ DN คือใคร

**Fails:** missing any-of ['Manifa', 'มณีฟ้า']

**Response:**

```
คุณพฤกษา (ตะวัน) ตำแหน่ง PRODUCT MANAGER อีเมล PRIJA.MA@FAHMAI.CO.TH ครับ
```

### g176 [nickname_grid] P0/th
**Q:** ขอชื่อ นีโอ สาขา BNA หน่อย

**Fails:** missing any-of ['Dokrak', 'ดอกรัก']; missing any-of ['Anucharoenphol', 'อนุเจริญผล']

**Response:**

```
ไม่พบข้อมูล
```

### g177 [nickname_grid] P0/th
**Q:** ใบเฟิร์น สาขา BNA คือใคร

**Fails:** missing any-of ['Phaibun', 'ไพบูลย์']; missing any-of ['Athikiatkamjorn', 'อธิเกียรติกำจร']

**Response:**

```
ไม่พบข้อมูล
```

### g178 [nickname_grid] P0/th
**Q:** ขอชื่อ แมว สาขาลาดพร้าว หน่อย

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Jaingambun', 'ใจงามบุญ']

**Response:**

```
ไม่พบข้อมูล
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['จงรัก', 'Chongrak']; missing any-of ['สัมโชติ', 'Samchot']; missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่พบข้อมูล
```

### g193 [nickname_grid] P0/th
**Q:** ใครคือปันปัน

**Fails:** missing any-of ['ปัน', 'ปัน', 'ไม่พบข้อมูล']

**Response:**

```
คุณฤทธิชัย แก้วใสภิญโญ (CTO) อีเมล: RITTICHAI.KA@FAHMAI.CO.TH
```

### g199 [dept_listing_small] P1/th
**Q:** ใครอยู่ OPS-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g230 [dept_member_count] P1/th
**Q:** KS-PD กี่คนนะ

**Fails:** missing any-of ['24']; missing count 24

**Response:**

```
KS-PD มีทั้งหมด 21 คนครับ
```

### g253 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ สายฟ้า สัก 5 คน

**Fails:** min_items 5 not met (1)

**Response:**

```
รายชื่อพนักงานแผนกสายฟ้า (SF) 5 ท่านครับ:

* คุณกิตติชาติ ชัยเจริญมณี - KITTICHAT.CH2@FAHMAI.CO.TH
* คุณพิศสมัย พรหมชากัญญ์ - PHITSAMAI.PH2@FAHMAI.CO.TH
* คุณกิตติ ราชฟ้า - KITTI.RA2@FAHMAI.CO.TH
* คุณเพ็ญศรี นราบุษราคัม - PENSRI.NA@FAHMAI.CO.TH
* คุณอรชร บุญมาชัย - ORACHON.BU@FAHMAI.CO.TH
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (1)

**Response:**

```
รายชื่อพนักงานจากแผนกคลื่นเสียง (KS) 5 ท่านครับ:

* คุณพิศสมัย อัมพรมณี - PHITSAMAI.AM@FAHMAI.CO.TH
* คุณเรืองฤทธิ์ นรากอบสุข - RUANGRIT.NA@FAHMAI.CO.TH
* คุณตะวัน ราชบุญญา - TAWAN.RA@FAHMAI.CO.TH
* คุณปิยนันท์ อัครกิตติ - PIYANAN.AK@FAHMAI.CO.TH
* คุณคำรณ บุษราคัมเฉลิม - KHAMRON.BU@FAHMAI.CO.TH
```

### g258 [org_informal_listing] P0/en
**Q:** give me 5 people from SaiFah

**Fails:** min_items 5 not met (0)

**Response:**

```
Here are 5 people from the SaiFah (SF) department:

* SAKCHAI ATHICHAROEN - SAIFAH PRODUCT ENGINEER (SAKCHAI.AT@FAHMAI.CO.TH)
* PHLOI DAORUENGCHOT - SAIFAH PRODUCT MANAGER (PHLOI.DA@FAHMAI.CO.TH)
* SUKHUM JAIKIEOWBUN - SAIFAH BRAND MARKETER (SUKHUM.JA@FAHMAI.CO.TH)
* SATJA SAMAWUT - SAIFAH BRAND MARKETER (SATJA.SA@FAHMAI.CO.TH)
* ORACHON MANIPHAT - SAIFAH PRODUCT MANAGER (ORACHON.MA@FAHMAI.CO.TH)
```

### g310 [email_identity_lookup] P0/en
**Q:** whose email is nattanicha.ra3@fahmai.co.th

**Fails:** missing any-of ['Nattanicha', 'ณัฎฐณิชา']; missing any-of ['Rajkarawek', 'ราชการเวก']

**Response:**

```
no record found
```

### g317 [refuse] P0/th
**Q:** สัญชาติ CMO

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']; has ext pattern

**Response:**

```
คุณส้ม กาญจน์สถิต (SOM.KA@FAHMAI.CO.TH) ต่อ 79005 ครับ
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มีคุณกิตติคุณ พงจงรัก (บูม) ครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือ คือ คุณวิเชียร พงหอมกลิ่น ครับ
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
The boss of the SFVP (Wirat Sombusarakham) is Thawan Boonnamphong, the General Manager of SaiFah.
```

### g373 [thai_knowledge] P0/th
**Q:** สาขา KKN อยู่จังหวัดไหน

**Fails:** missing any-of ['ขอนแก่น', 'Khon Kaen']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g375 [thai_knowledge] P0/th
**Q:** NMA อยู่ที่ไหน

**Fails:** missing any-of ['นครราชสีมา', 'โคราช', 'Korat']

**Response:**

```
ไม่พบข้อมูล
```

### g376 [thai_knowledge] P0/th
**Q:** CBI สาขาอยู่ไหน

**Fails:** missing any-of ['ชลบุรี', 'Chonburi']

**Response:**

```
ไม่พบข้อมูล
```

### g384 [surname_family] P1/th
**Q:** จิตรานนท์ฟ้า มีกี่คน

**Fails:** missing any-of ['3']; missing count 3

**Response:**

```
มี 1 คนครับ
```

### g390 [hard_nickname_variant] P1/th
**Q:** ปุ๊กกี้อยู่ทีมไหน

**Fails:** missing any-of ['ลัดดาวรรณ', 'Laddawan', 'ประยุทธ์']

**Response:**

```
มีหลายคนที่ชื่อเล่นว่า "ปุ๊ก" รบกวนขอชื่อจริงหรือแผนกเพื่อระบุตัวตนให้ถูกต้องครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณวิเชียร พงษ์หอมกลิ่น (GM ของแผนก DN) คือ WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณ SARAN AWUTMANI (GM ของแผนก JC) คือ SARAN.AW@FAHMAI.CO.TH ครับ
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุดแผนก KS (คลื่นเสียง) คือ RAM.LA@FAHMAI.CO.TH ครับ
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณกฤษ มหาแก้วใส (GM แผนก WK) คือ KRIS.MA@FAHMAI.CO.TH ครับ
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea (DN)

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (DN) คือ คุณวิเชียร พงหอมกลิ่น (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ) ครับ
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem (JC) department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the Judchuem (JC) department is Saran Awutmani (SARAN.AW@FAHMAI.CO.TH).
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Kluensiang (KS) คือ คุณราม ลวรรณ (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง) ครับ
```

### g455 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Legal (LEG) department?

**Fails:** missing any-of ['ไพโรจน์', 'Phairoj']; missing any-of ['มหากุล', 'Mahakun']

**Response:**

```
The most senior person heading the Legal (LEG) department is Namthip Samamphom (NAMTHIP.SA2@FAHMAI.CO.TH).
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon (WK)

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon (WK) คือ คุณกฤษ มหาแก้วใส (ผู้จัดการทั่วไปแบรนด์วงโคจร) ครับ
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงาน (employee ID) ของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงาน (employee ID) ของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงาน (employee ID) ของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g496 [bilingual] P1/en
**Q:** What is the Thai family (last) name of the VP of Technology?

**Fails:** missing any-of ['อธิดี', 'Athidi']

**Response:**

```
The Thai family name of the VP of Technology is แก้วใสภิญโญ.
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
There are 7 employees in the DN department at IC level who started in 2020.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are 6 employees in the DN department at Lead level who started in 2022.
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
no record found
```

### g568 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ

**Fails:** missing any-of ['77008']

**Response:**

```
ไม่พบข้อมูล
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Pongchongrak works on the 16th floor of FahMai Tower.
```

### g573 [noisy_name_form] P1/en
**Q:** Can I get the extension for Viriya Chanchai, VP of Retail Network?

**Fails:** missing any-of ['79141']

**Response:**

```
no record found
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล
```


_+44 more failures — see results.jsonl_
