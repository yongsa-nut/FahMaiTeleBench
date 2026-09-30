# Run: `gemma4_search_L2_t2_search_v10full`

**Overall: 558/626 pass (89.1%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| dept_member_count | 15/15 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| refuse | 90/90 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| nickname_grid | 58/61 | 95.1% |
| multi_entity_turn | 19/20 | 95.0% |
| casual_name_lookup | 14/15 | 93.3% |
| bilingual | 37/40 | 92.5% |
| thai_knowledge | 9/10 | 90.0% |
| enterprise_shorthand | 18/20 | 90.0% |
| hard_multihop | 22/26 | 84.6% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| deep_multihop | 10/12 | 83.3% |
| listing_count | 16/20 | 80.0% |
| superlative | 8/10 | 80.0% |
| surname_family | 18/24 | 75.0% |
| dept_listing_small | 5/7 | 71.4% |
| counterfactual | 17/25 | 68.0% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 11/18 | 61.1% |
| noisy_name_form | 11/20 | 55.0% |
| subsidiary_routing | 4/12 | 33.3% |

## By priority

- P0: 216/226 (95.6%)
- P1: 310/364 (85.2%)
- P2: 32/36 (88.9%)

## Failures (68)

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
ไม่พบข้อมูล
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
ไม่พบข้อมูล
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
ผู้บริหารระดับ C-level ของฟ้าใหม่มีดังนี้ครับ:

* **คุณวชิร จิรบุญ (เบอร์รี่)** - CEO: VACHIR.CH@FAHMAI.CO.TH (ต่อ 73048)
* **คุณกมลา ชัยสนธิ์สว่าง** - CFO: KAMALA.CH@FAHMAI.CO.TH (ต่อ 74921)
* **คุณฤทธิชัย แก้วใสภิญโญ (ปันปัน)** - CTO: RITTICHAI.KA@FAHMAI.CO.TH (ต่อ 75477)
* **คุณพงษ์กานต์ ราชชากัญญ์** - COO: PONGKAN.RA@FAHMAI.CO.TH (ต่อ 75464)
* **คุณส้ม กาญจน์สถิต** - CMO: SOM.KA@FAHMAI.CO.TH (
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

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

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
Orraya Watcharakan (Pe) - ORRAYA.WA@FAHMAI.CO.TH (Ext: 75665)
```

### g199 [dept_listing_small] P1/th
**Q:** ใครอยู่ OPS-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
The Bangkok retail VP is Wiriya Chanchai (Tik).
Email: WIRIYA.CH@FAHMAI.CO.TH
Ext: 79141
```

### g275 [multi_entity_turn] P0/th
**Q:** ขอเบอร์ของ CPO, SFVP

**Fails:** missing any-of ['78052']; missing any-of ['72402']

**Response:**

```
- CPO: คุณจิรภัทร วัชรใจงาม (096-557-6834)
- SFVP: คุณวิรัตน์ สมบุษราคัม (064-970-0992)
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มีคุณกิตติคุณ พงจงรัก (บูม) เพียงคนเดียวครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือ คือ คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN) ติดต่อได้ที่เบอร์ภายใน 76999 หรืออีเมล WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g379 [thai_knowledge] P0/th
**Q:** ใครมีชื่อเล่นเป็นชื่อผลไม้บ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณสรัล อาวุทธ์มณี (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม) คือ SARAN.AW@FAHMAI.CO.TH ครับ
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณกฤษ มหาแก้วใส (GM แบรนด์วงโคจร) คือ KRIS.MA@FAHMAI.CO.TH ครับ
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (Daonuea) คือ คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN) ตำแหน่งผู้จัดการทั่วไปแบรนด์ดาวเหนือ ติดต่อได้ที่เบอร์ภายใน 76999 หรืออีเมล WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (Kluensiang) คือ คุณราม ลวรรณ (จุ๊บ) ติดต่อได้ที่ RAM.LA@FAHMAI.CO.TH หรือต่อ 75965 ครับ
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon คือ คุณกฤษ มหาแก้วใส (ขิง) อีเมล KRIS.MA@FAHMAI.CO.TH ต่อ 74375 ครับ
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงานของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงานของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
There are 7 employees in the DN department at the IC level who started in 2020:

*   ทินกร นราชาญณรงค์ (THINNAKORN NARACHANNARONG)
*   โยธกา อัมพรสว่าง (YOTHAKA AMPHOMSAWANG)
*   วีระ พงอัสนี (VEERA PHONGASNEE)
*   พฤกษา มณีฟ้า (PRIJA MANIFA)
*   ปิยนันท์ พิดี (PIYANAN PHIDI)
*   พาณิช รัตนพร (PANIT RATANAPORN)
*   หญิง ประใจดี (YING PRAJAIDI)
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are 6 employees in the DN department at Lead level who started in 2022.
```

### g540 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ IC และเริ่มงานในปี 2020 ครับ

**Fails:** missing count 4

**Response:**

```
มีพนักงานแผนก FIN ระดับ IC ที่เริ่มงานในปี 2020 ทั้งหมด 3 คนครับ
```

### g545 [listing_count] P1/th
**Q:** ช่วยบอกชื่อทุกคนที่เป็นระดับ Manager ในส่วนงาน CEO-STR หน่อยครับ

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูลครับ
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
Kittikhun Pongchongrak is working on the 16th floor of FahMai Tower.
```

### g570 [noisy_name_form] P1/th
**Q:** ขอ email ของ Tanida เลขา COO หน่อยครับ

**Fails:** missing any-of ['THANIDA.TH@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g571 [noisy_name_form] P1/en
**Q:** Ext of Ritichai Kaewsaiphinyo (our CTO) please?

**Fails:** missing any-of ['75477']

**Response:**

```
no record found
```

### g572 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Sukum Suwanfahsai manager ทีม chat support หน่อยค่ะ

**Fails:** missing any-of ['SUKHUM.SU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g575 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Sombat Bunnamngam manager ทีม data scientist เบอร์อะไรครับ

**Fails:** missing any-of ['76059']

**Response:**

```
ไม่พบข้อมูล
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดแผนก B2B ซึ่งมีผู้บริหารระดับสูงสุด (VP) 2 ท่าน ดังนี้ครับ:

* คุณอุกฤษฎ์ วัชรเสริม: เบอร์ต่อ 79274
* คุณธัญญา เจริญผลภิญโญ: เบอร์ต่อ 71547
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
เบอร์ต่อของคุณเรืองศักดิ์ เทพเกียรติกำจร (รองประธานฝ่ายดาวเหนือ) คือ 72280 ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
เบอร์ต่อของคุณกมลา ชัยสนธิ์สว่าง (CFO) คือ 74921 ครับ
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
เบอร์ต่อของคุณณฐามน อภิชัยดี (CHRO) คือ 79303 ครับ
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
เบอร์ต่อของคุณสรัล อาวุทธ์มณี (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม) คือ 78762 ครับ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์ สัมชากัญญ์ สังกัดฝ่ายคลื่นเสียง (KS) ซึ่งผู้ที่มีตำแหน่งสูงสุดในส่วนงานนี้คือ คุณธเนศ บัวทองประเสริฐ (รองประธานฝ่ายคลื่นเสียง) เบอร์ต่อ 71215 ครับ
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
เบอร์ต่อของคุณพงษ์กานต์ ราชชากัญญ์ (COO) คือ 75464 ครับ
```

### g606 [surname_family] P1/en
**Q:** List everyone with the surname เขียวขจีศรี (give all of them).

**Fails:** missing count 3

**Response:**

```
Here are the employees with the surname เขียวขจีศรี:

* **ปกรณ์ เขียวขจีศรี (Lom)** - DATA ENGINEER (TEC), Email: PAKORN.KI@FAHMAI.CO.TH
* **อัจฉรา เขียวขจีศรี (Beam)** - DIRECTOR CRM SPECIALIST (MKT), Email: ATCHARA.KI@FAHMAI.CO.TH, Ext: 78341
* **ไพฑูรย์ เขียวขจีศรี** - LEAD SAIFAH BRAND MARKETER (SF), Email: PAITOON.KI@FAHMAI.CO.TH, Ext: 74791
```

### g608 [surname_family] P1/en
**Q:** List everyone with the surname ไกรศรีมณี (give all of them).

**Fails:** missing count 3

**Response:**

```
Here are the employees with the surname ไกรศรีมณี:

* **ยุพา ไกรศรีมณี** (YU-PHA KRAISEEMANI) - YU-PHA.KR@FAHMAI.CO.TH
* **วิภา ไกรศรีมณี** (WIPHA KRAISEEMANI) - WIPHA.KR@FAHMAI.CO.TH
* **พาณิช ไกรศรีมณี** (PANIT KRAISEEMANI) - PANIT.KR@FAHMAI.CO.TH
```

### g610 [surname_family] P1/en
**Q:** List everyone with the surname บุญเรืองกุล (give all of them).

**Fails:** missing count 2

**Response:**

```
- ศศิ บุญเรืองกุล (SASI BOONRUENGKUN) - SASI.BO@FAHMAI.CO.TH
- น้ำทิพย์ บุญเรืองกุล (NAMTHIP BOONRUENGKUN) - NAMTHIP.BO@FAHMAI.CO.TH
```

### g618 [surname_family] P1/en
**Q:** List everyone with the surname วัชรจงรัก (give all of them).

**Fails:** missing count 2

**Response:**

```
- ปัญญา วัชรจงรัก (ไทเทิล): PANYA.WA@FAHMAI.CO.TH, Ext. 72201
- จรูญ วัชรจงรัก (ไผ่): CHAROON.WA@FAHMAI.CO.TH, Ext. 71981
```

### g620 [surname_family] P1/en
**Q:** List everyone with the surname สมประเสริฐ (give all of them).

**Fails:** missing count 2

**Response:**

```
- ส้ม สมประเสริฐ (SOM SOMPRASERT): SOM.SO@FAHMAI.CO.TH
- ดารา สมประเสริฐ (DARA SOMPRASERT): DARA.SO@FAHMAI.CO.TH
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
- วีระ อภิญญาเสริม (VEERA APINYASOEM) - VEERA.AP@FAHMAI.CO.TH
- ดาหลา อภิญญาเสริม (DARHA APINYASOEM) - DARHA.AP@FAHMAI.CO.TH
```

### g682 [enterprise_shorthand] P1/th
**Q:** หัวหน้าทีมฟินฯ คือใคร

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
หัวหน้าฝ่ายการเงิน (VP Finance) คือ คุณแสงดาว พิดวงกมล (มอคค่า) อีเมล SAENGDAO.PH@FAHMAI.CO.TH ต่อ 77907 ครับ
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
ในแผนกการตลาด (MKT) มีผู้จัดการหลายท่านแบ่งตามสายงาน ดังนี้ครับ:

*   **ด้านแบรนด์:** คุณสรพงษ์ อารีฟ้า (โทร. 79726 / 091-419-6218)
*   **ด้านดิจิทัล:** คุณนงเยาว์ ภัทรจิตรานนท์ และ คุณกฤษฎา ชาเรือนศักดิ์ (โทร. 79448)
*   **ด้านอีเวนต์:** คุณเพ็ญศรี กาญจน์กำจร และ คุณสถาพร อมรอัสนี (โทร. 13648 / 081-270-5243)
*   **ด้าน CRM:** คุณอุษณี จินดาบุญ (โทร. 73121 / 081-786-8407)
```

### g755 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณแสงดาว พิดวงกมลเป็น CFO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['FINVP', 'VP Finance', 'กมลา']

**Response:**

```
คุณแสงดาว พิดวงกมล เบอร์ต่อ 77907 ครับ
```

### g756 [counterfactual] P1/en
**Q:** I heard สุเมธ อัครใจงาม is the CHRO — can I get their extension?

**Fails:** missing any-of ['HRVP', 'VP HR', 'ณฐามน']

**Response:**

```
Sumate Akarajaingam's extension is 72146.
```


_+18 more failures — see results.jsonl_
