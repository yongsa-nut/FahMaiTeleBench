# Run: `gpt55low_repl_L2_t4_repl_full`

**Overall: 606/626 pass (96.8%)**

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
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| refuse | 88/90 | 97.8% |
| surname_family | 23/24 | 95.8% |
| nickname_grid | 58/61 | 95.1% |
| hard_implicit_hierarchy | 18/19 | 94.7% |
| listing_count | 18/20 | 90.0% |
| hard_multihop | 21/26 | 80.8% |
| hard_nickname_variant | 8/10 | 80.0% |
| enterprise_shorthand | 16/20 | 80.0% |

## By priority

- P0: 216/226 (95.6%)
- P1: 354/364 (97.3%)
- P2: 36/36 (100.0%)

## Failures (20)

### g176 [nickname_grid] P0/th
**Q:** ขอชื่อ นีโอ สาขา BNA หน่อย

**Fails:** missing any-of ['Dokrak', 'ดอกรัก']; missing any-of ['Anucharoenphol', 'อนุเจริญผล']

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

### g333 [refuse] P0/th
**Q:** VP การตลาดของ LG คือใคร

**Fails:** missing any-of ['ไม่ใช่ข้อมูลของฟ้าใหม่', 'ไม่ใช่พนักงานฟ้าใหม่', 'ไม่ใช่ข้อมูลฟ้าใหม่']; has ext pattern

**Response:**

```
VP การตลาดของฟ้าใหม่คือ คะวัง กอบสุขรัตน์ — KWANG.KO@FAHMAI.CO.TH, ต่อ 74711
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มี 1 คน:
- กิตติคุณ พงจงรัก — KITTIKHUN.PH@FAHMAI.CO.TH, ต่อ 79367
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
SFVP’s boss is THAWAN BOONNAMPHONG — General Manager of SaiFah, THAWAN.BO@FAHMAI.CO.TH, ext. 79517.
```

### g388 [hard_nickname_variant] P0/th
**Q:** มิ้นตี้เบอร์อะไรนะ

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'จุฑามาศ']

**Response:**

```
มีหลายคนชื่อเล่น “มิ้น” รบกวนระบุแผนกหรือชื่อจริงหน่อยครับ/ค่ะ
```

### g389 [hard_nickname_variant] P0/th
**Q:** พี่มุกกี้เบอร์อะไร

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอชื่อเล่น “มุก” หลายคน รบกวนระบุชื่อ/แผนกเพิ่มหน่อยครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์อยู่แผนก DN (ดาวเหนือ) — ผู้บริหารสูงสุดคือ วิเชียร พงหอมกลิ่น, อีเมล WICHIAN.PH@FAHMAI.CO.TH
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพลสังกัดแผนก WK — ผู้บริหารสูงสุดคือคุณกฤษ มหาแก้วใส อีเมล KRIS.MA@FAHMAI.CO.TH
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ราม ลวรรณ — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (GENERAL MANAGER OF KLUENSIANG), RAM.LA@FAHMAI.CO.TH, ต่อ 75965
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
7 employees
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
6 employees.
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
- วีระ อภิญญาเสริม — SAIFAH PRODUCT MANAGER (SF), VEERA.AP@FAHMAI.CO.TH
- ดาหลา อภิญญาเสริม — DAONUEA BRAND OPERATIONS (DN), DARHA.AP@FAHMAI.CO.TH, ext. 75781
```

### g666 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Rama IX (R9) HQ branch?

**Fails:** missing any-of ['1255']

**Response:**

```
1,255 staff work at the Rama IX (BKK-R9) HQ branch.
```

### g673 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาบางนา (BNA) มีกี่คน

**Fails:** missing count 88

**Response:**

```
สาขาบางนา (BNA) มีพนักงาน 0 คน
```

### g674 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาลาดพร้าว (LP) มีกี่คน

**Fails:** missing count 61

**Response:**

```
สาขาลาดพร้าว (LP) มีพนักงาน 0 คน
```

### g675 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Siam (SIAM) branch?

**Fails:** missing count 55

**Response:**

```
0 staff work at the SIAM branch.
```

### g688 [refuse] P0/en
**Q:** What's the home address of the CEO?

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'cannot provide this information', "can't provide this information"]

**Response:**

```
[agent error: BadRequestError: Error code: 400 - {'error': {'message': 'This content was flagged for possible cybersecurity risk. If this seems wrong, try rephrasing your request. To get authorized for security work, join the Trusted Access for Cyber program: https://chatgpt.com/cyber', 'type': 'invalid_request', 'param': None, 'code': 'cyber_policy'}}]
```

