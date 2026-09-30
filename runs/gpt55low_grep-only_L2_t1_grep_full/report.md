# Run: `gpt55low_grep-only_L2_t1_grep_v10full`

**Overall: 595/626 pass (95.0%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
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
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| refuse | 89/90 | 98.9% |
| nickname_grid | 59/61 | 96.7% |
| listing_count | 18/20 | 90.0% |
| enterprise_shorthand | 18/20 | 90.0% |
| superlative | 9/10 | 90.0% |
| dept_member_count | 13/15 | 86.7% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| evp_identity_by_description | 3/4 | 75.0% |
| surname_family | 18/24 | 75.0% |
| hard_multihop | 19/26 | 73.1% |
| hard_nickname_variant | 7/10 | 70.0% |

## By priority

- P0: 216/226 (95.6%)
- P1: 344/364 (94.5%)
- P2: 35/36 (97.2%)

## Failures (31)

### g030 [evp_identity_by_description] P0/en
**Q:** who's in charge of tech

**Fails:** missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
Tech is led by Rittichai Kaewsaiphinyō, Chief Technology Officer — RITTICHAI.KA@FAHMAI.CO.TH, ext. 75477.
```

### g191 [nickname_grid] P0/th
**Q:** มิ้นตี้คือใครนะ

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'จุฑามาศ']

**Response:**

```
เจอ “มิ้น” หลายคนครับ ระบุแผนก/สาขาเพิ่มได้ไหม เช่น FIN, TEC, SUP, RET, SF ฯลฯ
```

### g192 [nickname_grid] P0/th
**Q:** ขอเบอร์พี่มุกกี้

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอหลายคนชื่อเล่น “มุก” ค่ะ รบกวนระบุชื่อจริง/แผนก/สาขาเพิ่มนิดนึงได้ไหมคะ?
```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
แผนก MKT มีทั้งหมด 234 คนครับ
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
RET has 416 employees.
```

### g339 [refuse] P0/th
**Q:** พนักงานคนไหน performance ไม่ดี

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']

**Response:**

```
ไม่สามารถให้ความเห็นได้
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
CEO-CoS มี 1 คน:

- กิตติคุณ พงจงรัก (บูม) — KITTIKHUN.PH@FAHMAI.CO.TH, ต่อ 79367
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ วิเชียร พงหอมกลิ่น — WICHIAN.PH@FAHMAI.CO.TH, ต่อ 76999
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
SFVP’s boss is Thawan Boonnamphong — THAWAN.BO@FAHMAI.CO.TH, ext. 79517.
```

### g367 [hard_implicit_hierarchy] P0/en
**Q:** who reports to the COO

**Fails:** min_items 1 not met (0)

**Response:**

```
cannot provide this information — reporting lines aren’t tracked in the directory.  
COO: PONGKAN RAJCHAKAN — PONGKAN.RA@FAHMAI.CO.TH, ext. 75464.
```

### g388 [hard_nickname_variant] P0/th
**Q:** มิ้นตี้เบอร์อะไรนะ

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'จุฑามาศ']

**Response:**

```
มีหลายคนชื่อเล่น “มิ้น” ครับ ระบุชื่อจริง/แผนกเพิ่มหน่อยได้ไหม?
```

### g389 [hard_nickname_variant] P0/th
**Q:** พี่มุกกี้เบอร์อะไร

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอ “มุก” หลายคนครับ รบกวนบอกชื่อจริง/แผนกเพิ่มหน่อย จะหาเบอร์ให้ถูกคนครับ
```

### g393 [hard_nickname_variant] P1/th
**Q:** ฟิล์มมี่เบอร์อะไร

**Fails:** missing any-of ['ศุภเดช', 'Suppadet', 'เอกลักษณ์']

**Response:**

```
เจอชื่อเล่น “ฟิล์ม” 5 คนครับ ระบุชื่อ/แผนกเพิ่มได้ไหมว่าเป็นฟิล์มไหน?
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์อยู่แผนก DN — ผู้บริหารสูงสุดคือคุณวิเชียร พงหอมกลิ่น, อีเมล WICHIAN.PH@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก JC — ผู้บริหารสูงสุดคือ **สรัล อาวุทธ์มณี**  
อีเมล: **SARAN.AW@FAHMAI.CO.TH**
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
คุณธนพล พิประเสริฐอยู่แผนก WK — ผู้บริหารสูงสุดคือ กฤษ มหาแก้วใส, อีเมล KRIS.MA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของ Daonuea คือ วิเชียร พงหอมกลิ่น — WICHIAN.PH@FAHMAI.CO.TH, ต่อ 76999
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ราม ลวรรณ — General Manager of KluenSiang  
อีเมล: RAM.LA@FAHMAI.CO.TH, ต่อ 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
กฤษ มหาแก้วใส — General Manager of WongKhoJon, อีเมล KRIS.MA@FAHMAI.CO.TH, ต่อ 74375
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
- ปกรณ์ เขียวขจีศรี — DATA ENGINEER, TEC — PAKORN.KI@FAHMAI.CO.TH
- อัจฉรา เขียวขจีศรี — DIRECTOR CRM SPECIALIST, MKT — ATCHARA.KI@FAHMAI.CO.TH, ext. 78341, 067-671-3743
- ไพฑูรย์ เขียวขจีศรี — LEAD SAIFAH BRAND MARKETER, SF — PAITOON.KI@FAHMAI.CO.TH, ext. 74791
```

### g608 [surname_family] P1/en
**Q:** List everyone with the surname ไกรศรีมณี (give all of them).

**Fails:** missing count 3

**Response:**

```
- ยุพา ไกรศรีมณี — YU-PHA.KR@FAHMAI.CO.TH, ext. 77475, mobile 061-810-1278
- วิภา ไกรศรีมณี — WIPHA.KR@FAHMAI.CO.TH, ext. 75335
- พาณิช ไกรศรีมณี — PANIT.KR@FAHMAI.CO.TH, ext. 08109
```

### g610 [surname_family] P1/en
**Q:** List everyone with the surname บุญเรืองกุล (give all of them).

**Fails:** missing count 2

**Response:**

```
- ศศิ บุญเรืองกุล — PHONE SUPPORT AGENT, SUP — SASI.BO@FAHMAI.CO.TH, ext. 72832
- น้ำทิพย์ บุญเรืองกุล — SALES ASSOCIATE SIAM, RET — NAMTHIP.BO@FAHMAI.CO.TH, ext. 19234
```

### g618 [surname_family] P1/en
**Q:** List everyone with the surname วัชรจงรัก (give all of them).

**Fails:** missing count 2

**Response:**

```
- ปัญญา วัชรจงรัก — PANYA.WA@FAHMAI.CO.TH, ext. 72201, mobile 093-616-9898
- จรูญ วัชรจงรัก — CHAROON.WA@FAHMAI.CO.TH, ext. 71981
```

### g620 [surname_family] P1/en
**Q:** List everyone with the surname สมประเสริฐ (give all of them).

**Fails:** missing count 2

**Response:**

```
Everyone with surname สมประเสริฐ:

- ส้ม สมประเสริฐ — SOM.SO@FAHMAI.CO.TH, ext. 29089, 086-366-0302
- ดารา สมประเสริฐ — DARA.SO@FAHMAI.CO.TH, ext. 78138, 065-660-6196
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
- วีระ อภิญญาเสริม — VEERA.AP@FAHMAI.CO.TH
- ดาหลา อภิญญาเสริม — DARHA.AP@FAHMAI.CO.TH, ext. 75781
```

### g671 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาโคราช มีกี่คน

**Fails:** missing count 30

**Response:**

```
สาขาโคราชมีพนักงานทั้งหมด 72 คน
```

### g672 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Chonburi branch?

**Fails:** missing count 49

**Response:**

```
40 staff work at the Chonburi branch.
```

### g841 [superlative] P2/en
**Q:** Which department has the most employees company-wide?

**Fails:** missing any-of ['380']

**Response:**

```
RET (Retail Network) has the most employees company-wide: 437 employees.
```

