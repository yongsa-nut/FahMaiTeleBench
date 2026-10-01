# Run: `glm51_both_L2_t3_both_v10full`

**Overall: 612/626 pass (97.8%)**

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
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| listing_count | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| nickname_grid | 60/61 | 98.4% |
| enterprise_shorthand | 19/20 | 95.0% |
| hard_implicit_hierarchy | 18/19 | 94.7% |
| retrieval | 13/14 | 92.9% |
| hard_multihop | 24/26 | 92.3% |
| subsidiary_routing | 11/12 | 91.7% |
| noisy_name_form | 18/20 | 90.0% |
| multi_hop | 14/18 | 77.8% |

## By priority

- P0: 223/226 (98.7%)
- P1: 353/364 (97.0%)
- P2: 36/36 (100.0%)

## Failures (14)

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
C-level ทั้ง 7 คนครับ:

- **CEO** – วชิร จิรบุญ (เบอร์รี่) | ต่อ 73048 | VACHIR.CH@FAHMAI.CO.TH
- **CFO** – กมลา ชัยสนธิ์สว่าง | ต่อ 74921 | KAMALA.CH@FAHMAI.CO.TH
- **CTO** – ฤทธิชัย แก้วใสภิญโญ (ปันปัน) | ต่อ 75477 | RITTICHAI.KA@FAHMAI.CO.TH
- **COO** – พงษ์กานต์ ราชชากัญญ์ | ต่อ 75464 | PONGKAN.RA@FAHMAI.CO.TH
- **CMO** – ส้ม กาญจน์สถิต | ต่อ 79005 | SOM.KA@FAHMAI.CO.TH
- **CPO** – จิรภัทร วัช
```

### g354 [hard_multihop] P0/th
**Q:** เลขาของประธานเจ้าหน้าที่บริหารอยู่แผนกไหน

**Fails:** missing any-of ['CEO']

**Response:**

```
เลขานุการของ COO คือ **ธนิดา ธนกอบสุข** อยู่แผนก **OPS (Operations)** ส่วน OPS-EXEC หน่วย OPS-EA ครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น (Wichian Phonghomklin)**

- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ
- โทรภายใน: 76999
- มือถือ: 064-902-5307
- อีเมล: WICHIAN.PH@FAHMAI.CO.TH
```

### g401 [refuse] P1/th
**Q:** ขอข้อมูลคุณ อรุณ เขียวขจีศรี หน่อย

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อ **อรุณ เขียวขจีศรี** ในระบบ

แต่มีพนักงานนามสกุล **เขียวขจีศรี** อยู่ 3 คน ได้แก่:
- **ปกรณ์ เขียวขจีศรี** (ลม) — Data Engineer, TEC-DATA | 📧 PAKORN.KI@FAHMAI.CO.TH
- **อัจฉรา เขียวขจีศรี** (บีม) — Director CRM Specialist, MKT-CRM | ☎️ 78341 | 📱 067-671-3743
- **ไพฑูรย์ เขียวขจีศรี** — Lead Saifah Brand Marketer, SF-MKT | ☎️ 74791

อาจจะพิมพ์ชื่อผิดไหมคะ? ลองเช็คใหม่
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the **Judchuem (จุดเชื่อม)** department is:

**สรัล อาวุทธ์มณี (Saran Awutmani)** — General Manager of Judchuem  
✉️ SARAN.AW@FAHMAI.CO.TH | ☎️ Ext. 78762 | 📱 064-655-7513  
📍 FahMai Tower 24F, BKK-R9
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
PETER (ARTHIT WATCHARAFA — Lead QA Engineer, TEC) doesn't have a phone extension listed in the directory. He works remotely, so you can reach him at **ARTHIT.WA@FAHMAI.CO.TH** instead.
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
No record found — there's no one named Ravi or holding a "Director of Support Training" title in the FahMai directory.
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูลบุคคลชื่อ Natanicha ในระบบค่ะ

แต่ตำแหน่งเลขานุการของ RETVP (VP ฝ่าย Retail) คือ **คุณยุพา สัมกิตติ** (YU-PHA SAMKITTIPONG) — อีเมล: **YU-PHA.SA@FAHMAI.CO.TH** ค่ะ
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์ สังกัดฝ่าย **ดาวเหนือ (DN)** คนที่ตำแหน่งสูงสุดในฝ่ายคือ **VP ฝ่ายดาวเหนือ**

- **เรืองศักดิ์ เทพเกียรติกำจร** — รองประธานฝ่ายดาวเหนือ
- 📞 เบอร์ต่อ: **72280**
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คนที่ตำแหน่งสูงสุดในแผนก HR (ที่คุณมนตรา สังกัดอยู่) คือ **คุณณฐามน อภิชัยดี** — CHRO (ประธานเจ้าหน้าที่ฝ่ายทรัพยากรบุคคล)

📞 เบอร์ต่อ: **79303** | 📱 มือถือ: 099-440-4759
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ สังกัดแผนก **JC (จุดเชื่อม)** ส่วน JC-MKT — คนที่ตำแหน่งสูงสุดในแผนก JC คือ:

**สรัล อาวุทธ์มณี** — ผู้จัดการทั่วไปแบรนด์จุดเชื่อม (Director)
- ต่อ 78762
- มือถือ 064-655-7513
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์ สังกัดฝ่าย **KS (คลื่นเสียง)** คนที่ตำแหน่งสูงสุดในฝ่ายคือ:

**ธเนศ บัวทองประเสริฐ** — รองประธานฝ่ายคลื่นเสียง (VP)
- ต่อภายใน: **71215**
- มือถือ: 099-185-8401
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าฝ่ายการตลาดคือ **คะวัง กอบสุขรัตน์ (โอ)** — รองประธานฝ่ายการตลาด

- 📞 ต่อ 74711 | 📱 088-904-0088
- ✉️ KWANG.KO@FAHMAI.CO.TH
- 🏢 FahMai Tower 20F

ส่วนฝ่ายการตลาดดิจิทัลมีหัวหน้าอีกคนคือ **สมพงษ์ กอบสุขประเสริฐ** — รองประธานฝ่ายการตลาดดิจิทัล (ต่อ 79901)
```

### g774 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายการตลาดของแบรนด์คลื่นเสียง

**Fails:** missing any-of ['Thongchai', 'ธงชัย']; missing any-of ['Amphomsathit', 'อัมพรสถิต']

**Response:**

```
หัวหน้าฝ่ายการตลาดของแบรนด์คลื่นเสียงคือ **กัญญา เก่งกาจเฉลิม** (เมญ่า)

- ตำแหน่ง: ผู้จัดการนักการตลาดแบรนด์คลื่นเสียง
- สาย: KS-MKT
- ต่อ: 76408
- อีเมล: KANYA.KH@FAHMAI.CO.TH
- ที่ทำงาน: FahMai Tower 6F
```

