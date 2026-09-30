# Run: `gpt54med_grep-only_L2_t1_grep_v10full`

**Overall: 606/626 pass (96.8%)**

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
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| refuse | 89/90 | 98.9% |
| nickname_grid | 59/61 | 96.7% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| listing_count | 19/20 | 95.0% |
| noisy_name_form | 19/20 | 95.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| hard_implicit_hierarchy | 18/19 | 94.7% |
| superlative | 9/10 | 90.0% |
| surname_family | 21/24 | 87.5% |
| tier_listing | 5/6 | 83.3% |
| deep_multihop | 10/12 | 83.3% |
| hard_multihop | 21/26 | 80.8% |

## By priority

- P0: 220/226 (97.3%)
- P1: 353/364 (97.0%)
- P2: 33/36 (91.7%)

## Failures (20)

### g073 [evp_vs_vp_disambig] P0/th
**Q:** ขอ LOGFL หน่อย ไม่เอา LOGVP

**Fails:** missing any-of ['Malee', 'มาลี']; missing any-of ['Amonthong', 'อมรทอง']

**Response:**

```
LOGFL / LOG-FLT มี 47 คน (ไม่รวม LOGVP) ตัวอย่างรายชื่อ:

- สุจิรา อภิญญาเฉลิม — เลขานุการของ LOGFL • 79248 • SUJIRA.AP@FAHMAI.CO.TH
- พิชิต วิศบุญเรือง — ผู้อำนวยการฝ่ายพนักงานขับรถ • 46562 • PHICHIT.WI@FAHMAI.CO.TH
- สมตา บุญอัญชลี — ผู้จัดการพนักงานขับรถ • 46811 • SOMTA.BU@FAHMAI.CO.TH
- อภิชัย กิตติพัฒน์ — ผู้จัดการพนักงานขับรถ • 77345 • APICHAI.KI2@FAHMAI.CO.TH
- สุจิรา จิตรานนท์ฟ้า — หัวหน้า
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
จงรัก สัมโชติ (ปุ๊ก) — ไม่มีเบอร์ในระบบ
```

### g265 [tier_listing] P0/th
**Q:** ขอรายชื่อ director สัก 10 คน

**Fails:** min_items 10 not met (9)

**Response:**

```
ได้ครับ ตัวอย่าง Director 10 คน:

- ธนิดา อภิใจ — Director Financial Planning — THANIDA.AP@fahmai.co.th — ต่อ 79096
- แสงดาว อาวุทธ์พัฒน์ — Director of SaiFah Operations — SAENGDAO.AW@fahmai.co.th — ต่อ 72674
- อรอนงค์ วิศอนุมาน — Director Brand — ORANONG.WI@fahmai.co.th — ต่อ 78713
- บุษบา อัครพัฒน์ — Director Accounting — BUSABA.AK@fahmai.co.th — ต่อ 77404
- อุกฤษฎ์ อมรอาทิตย์ — Director Finance
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
ทีม **CEO-CoS** ตอนนี้มี **1 คน** คือ  
- **กิตติคุณ พงจงรัก (บูม)** — Chief of Staff, `KITTIKHUN.PH@fahmai.co.th` ต่อ **79367**
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ, **WICHIAN.PH@FAHMAI.CO.TH**
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก JC โดยผู้บริหารสูงสุดของแผนกคือ คุณสรัล อาวุทธ์มณี — อีเมล `SARAN.AW@FAHMAI.CO.TH`
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนก KS โดยผู้บริหารสูงสุดของแผนกคือ ราม ลวรรณ — RAM.LA@FAHMAI.CO.TH
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก WK และผู้บริหารสูงสุดของแผนกคือ **กฤษ มหาแก้วใส** — **KRIS.MA@FAHMAI.CO.TH**
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Daonuea คือ **วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ, **WICHIAN.PH@FAHMAI.CO.TH**, ต่อ **76999**
```

### g542 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ Manager และเริ่มงานในปี 2022 ครับ

**Fails:** missing count 3

**Response:**

```
มี **4 คน** ครับ
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล Natanicha ในบทบาทนี้ — เลขาฯ ของ RETVP ในระบบคือ คุณยุพา สัมกิตติ, อีเมล **YU-PHA.SA@FAHMAI.CO.TH**
```

### g608 [surname_family] P1/en
**Q:** List everyone with the surname ไกรศรีมณี (give all of them).

**Fails:** missing count 3

**Response:**

```
- ยุพา ไกรศรีมณี — SAIFAH PRODUCT MANAGER, YU-PHA.KR@FAHMAI.CO.TH, ext. 77475
- วิภา ไกรศรีมณี (ฮูก) — B2B SUPPORT SPECIALIST, WIPHA.KR@FAHMAI.CO.TH, ext. 75335
- พาณิช ไกรศรีมณี — SOLUTIONS ENGINEER, PANIT.KR@FAHMAI.CO.TH, ext. 08109
```

### g618 [surname_family] P1/en
**Q:** List everyone with the surname วัชรจงรัก (give all of them).

**Fails:** missing count 2

**Response:**

```
- ปัญญา วัชรจงรัก — Lead Technical Support Agent, SUP-TECH — PANYA.WA@fahmai.co.th, ext. 72201
- จรูญ วัชรจงรัก — Learning & Development Specialist, HR-LD — CHAROON.WA@fahmai.co.th, ext. 71981
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
Here are all employees with the surname อภิญญาเสริม:

- วีระ อภิญญาเสริม — SaiFah Product Manager, SF-PD-25, `VEERA.AP@fahmai.co.th`
- ดาหลา อภิญญาเสริม — Daonuea Brand Operations, DN-OPS-81, `DARHA.AP@fahmai.co.th`, ext. 75781
```

### g639 [nickname_grid] P1/th
**Q:** เอ คือใคร มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ค้นคำว่า **“เอ”** ตรงหลายฟิลด์ในระบบ เจอ **78 รายการ** เลยครับ  
ถ้าหมายถึงคนชื่อขึ้นต้น/มี **“เอก”** เจอ **14 คน** เช่น

- **เอกพล ศรีพงศ์** — ผู้จัดการวิศวกรโมบาย, TEC-MOB — `EAKPHOL.SR@FAHMAI.CO.TH` ต่อ **75012**
- **เอกพล ภัทรแก้วกาญจน์** — วิศวกรโครงสร้างพื้นฐาน, TEC-INF — `EAKPHOL.PH@FAHMAI.CO.TH`
- **เอกลักษณ์ อนุอภิญญา** — วิศวกรโมบาย, TEC-MOB — `EKKALUCK.AN@FAHMAI.CO.TH`
- **เอกพล ชัยวัฒน
```

### g676 [enterprise_shorthand] P1/th
**Q:** พนักงานที่ทำงานทางไกล มีกี่คน

**Fails:** missing count 160

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ เนื่องจากระบบไดเรกทอรีไม่มีข้อมูลสถานะการทำงานทางไกลของพนักงาน
```

### g826 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the most employees — what's the email of the VP who heads that department?

**Fails:** missing any-of ['WIRIYA.CH@FAHMAI.CO.TH']

**Response:**

```
The largest VP-led department is **SF (43 employees)**, and its VP’s email is **WIRAT.SO@FAHMAI.CO.TH**.
```

### g830 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the fewest employees — what's the email of the secretary of that department's VP?

**Fails:** missing any-of ['MONTRA.WI@FAHMAI.CO.TH']

**Response:**

```
It’s a tie: **WK** and **JC** have the fewest employees among VP-led departments (**80 each**).

- **WK VP secretary:** SUPHAWADEE.BU@FAHMAI.CO.TH  
- **JC VP secretary:** RATAPON.CH@FAHMAI.CO.TH
```

### g841 [superlative] P2/en
**Q:** Which department has the most employees company-wide?

**Fails:** missing any-of ['380']

**Response:**

```
RET has the most employees company-wide: 416.
```

