# Run: `gpt54med_repl_L2_t4_repl_v10full`

**Overall: 615/626 pass (98.2%)**

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
| refuse | 90/90 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| hard_implicit_hierarchy | 19/19 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| enterprise_shorthand | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| bilingual | 39/40 | 97.5% |
| casual_name_lookup | 14/15 | 93.3% |
| hard_nickname_variant | 9/10 | 90.0% |
| hard_multihop | 22/26 | 84.6% |
| surname_family | 20/24 | 83.3% |

## By priority

- P0: 221/226 (97.8%)
- P1: 358/364 (98.4%)
- P2: 36/36 (100.0%)

## Failures (11)

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
ไม่พบข้อมูล
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มี 1 คน:
- กิตติคุณ พงจงรัก (บูม) — หัวหน้าสำนักงานประธาน, KITTIKHUN.PH@FAHMAI.CO.TH, ต่อ 79367
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น** — **WICHIAN.PH@FAHMAI.CO.TH**, ต่อ **76999**
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
SFVP’s boss is THAWAN BOONNAMPHONG — General Manager of SaiFah, THAWAN.BO@FAHMAI.CO.TH, ext. 79517.
```

### g389 [hard_nickname_variant] P0/th
**Q:** พี่มุกกี้เบอร์อะไร

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอชื่อเล่น “มุก” หลายคนในระบบ รบกวนขอชื่อจริงหรือแผนกเพิ่มหน่อยครับ/ค่ะ แล้วจะเช็กเบอร์ให้ทันที
```

### g448 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณเกษม วิศอัญชลี สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['PHAIROJ.MA@FAHMAI.CO.TH']

**Response:**

```
คุณเกษม วิศอัญชลี สังกัดแผนก LEG; ผู้บริหารสูงสุดของแผนกคือ **ไพโรจน์ มหากุล** — **PAIROJ.MAHAKUL@FAHMAI.CO.TH**
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงานของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g606 [surname_family] P1/en
**Q:** List everyone with the surname เขียวขจีศรี (give all of them).

**Fails:** missing count 3

**Response:**

```
Here are all employees with the surname **เขียวขจีศรี**:

- **ปกรณ์ เขียวขจีศรี** (PAKORN KIAOKAJISI) — DATA ENGINEER, TEC — `PAKORN.KI@FAHMAI.CO.TH` — Remote
- **อัจฉรา เขียวขจีศรี** (ATCHARA KIAOKAJISI) — DIRECTOR CRM SPECIALIST, MKT — `ATCHARA.KI@FAHMAI.CO.TH` — ext. 78341 — 067-671-3743
- **ไพฑูรย์ เขียวขจีศรี** (PAITOON KIAOKAJISI) — LEAD SAIFAH BRAND MARKETER, SF — `PAITOON.KI@FAHMAI.CO.TH` 
```

### g608 [surname_family] P1/en
**Q:** List everyone with the surname ไกรศรีมณี (give all of them).

**Fails:** missing count 3

**Response:**

```
- ยุพา ไกรศรีมณี (YU-PHA KRAISEEMANI) — SAIFAH PRODUCT MANAGER, SF-PD-42, FahMai Tower 22F, BKK-R9 — YU-PHA.KR@FAHMAI.CO.TH, ext. 77475, 061-810-1278
- วิภา ไกรศรีมณี (WIPHA KRAISEEMANI) — B2B SUPPORT SPECIALIST, B2B-SUP-64, FahMai Tower 6F, BKK-R9 — WIPHA.KR@FAHMAI.CO.TH, ext. 75335
- พาณิช ไกรศรีมณี (PANIT KRAISEEMANI) — SOLUTIONS ENGINEER, B2B-SOL-62, สาขาภูเก็ต, HKT — PANIT.KR@FAHMAI.CO.TH, ex
```

### g618 [surname_family] P1/en
**Q:** List everyone with the surname วัชรจงรัก (give all of them).

**Fails:** missing count 2

**Response:**

```
- ปัญญา วัชรจงรัก (ไทเทิล) — หัวหน้าทีมเจ้าหน้าที่สนับสนุนทางเทคนิค, SUP — PANYA.WA@FAHMAI.CO.TH, ext. 72201, 093-616-9898
- จรูญ วัชรจงรัก (ไผ่) — เจ้าหน้าที่พัฒนาบุคลากร, HR — CHAROON.WA@FAHMAI.CO.TH, ext. 71981
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
Here are all employees with the surname **อภิญญาเสริม**:

- **วีระ อภิญญาเสริม** — SAIFAH PRODUCT MANAGER, SF-PD-25, **VEERA.AP@FAHMAI.CO.TH**
- **ดาหลา อภิญญาเสริม** — DAONUEA BRAND OPERATIONS, DN-OPS-81, **DARHA.AP@FAHMAI.CO.TH**, ext. **75781**
```

