# Run: `gpt55med_grep-only_L2_t1_grep_v10full`

**Overall: 596/626 pass (95.2%)**

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
| tier_listing | 6/6 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| nickname_grid | 60/61 | 98.4% |
| refuse | 88/90 | 97.8% |
| counterfactual | 24/25 | 96.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| listing_count | 18/20 | 90.0% |
| dept_member_count | 13/15 | 86.7% |
| org_informal_listing | 5/6 | 83.3% |
| hard_nickname_variant | 8/10 | 80.0% |
| hard_multihop | 20/26 | 76.9% |
| surname_family | 18/24 | 75.0% |
| hard_implicit_hierarchy | 14/19 | 73.7% |
| org_plus_person | 2/3 | 66.7% |

## By priority

- P0: 218/226 (96.5%)
- P1: 342/364 (94.0%)
- P2: 36/36 (100.0%)

## Failures (30)

### g192 [nickname_grid] P0/th
**Q:** ขอเบอร์พี่มุกกี้

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอชื่อเล่น “มุก” หลายคนครับ รบกวนระบุชื่อ/แผนกเพิ่มหน่อยครับว่าเป็นมุกไหน
```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
แผนก MKT มี 234 คน
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
RET has 416 employees.
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (4)

**Response:**

```
รายชื่อคลื่นเสียง 5 คน:

- ธเนศ บัวทองประเสริฐ — TANET.BU@FAHMAI.CO.TH, ต่อ 71215
- ปิยนันท์ พรหมพิทักษ์ — PIYANAN.PH@FAHMAI.CO.TH, ต่อ 76796
- ราม ลวรรณ — RAM.LA@FAHMAI.CO.TH, ต่อ 75965
- อัญชลี พรหมจรรย์ — ANCHALI.PH@FAHMAI.CO.TH, ต่อ 75093
- วิสิทธิ์ ใจงาม — WISIT.JA@FAHMAI.CO.TH, ต่อ 73419
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
WIRIYA CHANCHAI — VP Retail Network, WIRIYA.CH@FAHMAI.CO.TH, ext. 79141, mobile 082-034-8608
```

### g333 [refuse] P0/th
**Q:** VP การตลาดของ LG คือใคร

**Fails:** has ext pattern

**Response:**

```
ไม่ใช่ข้อมูลของฟ้าใหม่ — ถ้าหมายถึง VP ฝ่ายการตลาดของฟ้าใหม่คือ คะวัง กอบสุขรัตน์, KWANG.KO@FAHMAI.CO.TH, ต่อ 74711
```

### g339 [refuse] P0/th
**Q:** พนักงานคนไหน performance ไม่ดี

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']

**Response:**

```
ไม่สามารถให้ความเห็นได้  
ไม่สามารถให้ข้อมูล performance ของพนักงานได้
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มี 1 คน:

- กิตติคุณ พงจงรัก (บูม) — KITTIKHUN.PH@FAHMAI.CO.TH, ต่อ 79367
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ วิเชียร พงหอมกลิ่น — WICHIAN.PH@FAHMAI.CO.TH, ต่อ 76999
```

### g388 [hard_nickname_variant] P0/th
**Q:** มิ้นตี้เบอร์อะไรนะ

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'จุฑามาศ']

**Response:**

```
เจอ “มิ้น” หลายคนครับ หมายถึงคนไหน/แผนกไหน?
```

### g393 [hard_nickname_variant] P1/th
**Q:** ฟิล์มมี่เบอร์อะไร

**Fails:** missing any-of ['ศุภเดช', 'Suppadet', 'เอกลักษณ์']

**Response:**

```
เจอ “ฟิล์ม” 5 คนครับ ระบุชื่อ/แผนกเพิ่มได้ไหมครับว่าเป็นคนไหน?
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก DN คือ วิเชียร พงหอมกลิ่น — WICHIAN.PH@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก JC — ผู้บริหารสูงสุดคือ สรัล อาวุทธ์มณี อีเมล SARAN.AW@FAHMAI.CO.TH
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก KS คือ ราม ลวรรณ — RAM.LA@FAHMAI.CO.TH
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพลสังกัดแผนก WK — ผู้บริหารสูงสุดคือ กฤษ มหาแก้วใส: KRIS.MA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของ Daonuea คือ วิเชียร พงหอมกลิ่น — WICHIAN.PH@FAHMAI.CO.TH, ต่อ 76999
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
Saran Awutmani — General Manager of JudChuem  
SARAN.AW@FAHMAI.CO.TH, ext. 78762
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก KluenSiang (KS) คือ **ราม ลวรรณ** — GM of KluenSiang  
อีเมล: **RAM.LA@FAHMAI.CO.TH**, ต่อ **75965**
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
กฤษ มหาแก้วใส — General Manager of WongKhoJon  
อีเมล: KRIS.MA@FAHMAI.CO.TH, ต่อ 74375
```

### g464 [hard_implicit_hierarchy] P1/en
**Q:** In the JC-ENG section, who is the most senior employee?

**Fails:** missing any-of ['กอบสุขบุญ', 'Kobsookbun']

**Response:**

```
Narong Kobsoookbun — Director, JC-ENG. Email: NARONG.KO@FAHMAI.CO.TH, ext. 75194
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
7 employees.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
6 employees.
```

### g606 [surname_family] P1/en
**Q:** List everyone with the surname เขียวขจีศรี (give all of them).

**Fails:** missing count 3

**Response:**

```
All employees with surname เขียวขจีศรี:

- ปกรณ์ เขียวขจีศรี — DATA ENGINEER, TEC — PAKORN.KI@FAHMAI.CO.TH
- อัจฉรา เขียวขจีศรี — DIRECTOR CRM SPECIALIST, MKT — ATCHARA.KI@FAHMAI.CO.TH, ext. 78341, 067-671-3743
- ไพฑูรย์ เขียวขจีศรี — LEAD SAIFAH BRAND MARKETER, SF — PAITOON.KI@FAHMAI.CO.TH, ext. 74791
```

### g608 [surname_family] P1/en
**Q:** List everyone with the surname ไกรศรีมณี (give all of them).

**Fails:** missing count 3

**Response:**

```
Everyone with surname ไกรศรีมณี:

- ยุพา ไกรศรีมณี — YU-PHA.KR@FAHMAI.CO.TH, ext. 77475, mobile 061-810-1278
- วิภา ไกรศรีมณี — WIPHA.KR@FAHMAI.CO.TH, ext. 75335
- พาณิช ไกรศรีมณี — PANIT.KR@FAHMAI.CO.TH, ext. 08109
```

### g610 [surname_family] P1/en
**Q:** List everyone with the surname บุญเรืองกุล (give all of them).

**Fails:** missing count 2

**Response:**

```
- ศศิ บุญเรืองกุล — PHONE SUPPORT AGENT, SASI.BO@FAHMAI.CO.TH, ext. 72832
- น้ำทิพย์ บุญเรืองกุล — SALES ASSOCIATE SIAM, NAMTHIP.BO@FAHMAI.CO.TH, ext. 19234
```

### g618 [surname_family] P1/en
**Q:** List everyone with the surname วัชรจงรัก (give all of them).

**Fails:** missing count 2

**Response:**

```
- ปัญญา วัชรจงรัก — LEAD TECHNICAL SUPPORT AGENT, SUP — PANYA.WA@FAHMAI.CO.TH, ext. 72201, mobile 093-616-9898
- จรูญ วัชรจงรัก — LEARNING & DEVELOPMENT SPECIALIST, HR — CHAROON.WA@FAHMAI.CO.TH, ext. 71981
```

### g620 [surname_family] P1/en
**Q:** List everyone with the surname สมประเสริฐ (give all of them).

**Fails:** missing count 2

**Response:**

```
Everyone with surname สมประเสริฐ:

- ส้ม สมประเสริฐ — SOM.SO@FAHMAI.CO.TH, ext. 29089, mobile 086-366-0302
- ดารา สมประเสริฐ — DARA.SO@FAHMAI.CO.TH, ext. 78138, mobile 065-660-6196
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
- วีระ อภิญญาเสริม — VEERA.AP@FAHMAI.CO.TH
- ดาหลา อภิญญาเสริม — DARHA.AP@FAHMAI.CO.TH, ext. 75781
```

### g672 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Chonburi branch?

**Fails:** missing count 49

**Response:**

```
40 staff work at the Chonburi branch.
```

### g757 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณคะวัง กอบสุขรัตน์เป็น CMO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['MKTVP', 'VP Marketing', 'ส้ม']

**Response:**

```
คุณคะวัง กอบสุขรัตน์ — เบอร์ต่อ 74711, อีเมล KWANG.KO@FAHMAI.CO.TH
```

