# Run: `gemini30flash_grep-only_L2_t1_grep_v10full`

**Overall: 546/626 pass (87.2%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| nickname_grid | 59/61 | 96.7% |
| surname_family | 23/24 | 95.8% |
| noisy_name_form | 19/20 | 95.0% |
| casual_name_lookup | 14/15 | 93.3% |
| bilingual | 35/40 | 87.5% |
| dept_member_count | 13/15 | 86.7% |
| dept_listing_small | 6/7 | 85.7% |
| extension_reverse | 6/7 | 85.7% |
| email_mobile_lookup | 6/7 | 85.7% |
| enterprise_shorthand | 17/20 | 85.0% |
| evp_vs_vp_disambig | 21/25 | 84.0% |
| deep_multihop | 10/12 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| thai_knowledge | 8/10 | 80.0% |
| name_lookup | 15/20 | 75.0% |
| multi_hop | 13/18 | 72.2% |
| counterfactual | 18/25 | 72.0% |
| superlative | 7/10 | 70.0% |
| hard_implicit_hierarchy | 13/19 | 68.4% |
| org_informal_listing | 4/6 | 66.7% |
| hard_multihop | 16/26 | 61.5% |
| listing_count | 12/20 | 60.0% |
| subsidiary_routing | 6/12 | 50.0% |

## By priority

- P0: 213/226 (94.2%)
- P1: 304/364 (83.5%)
- P2: 29/36 (80.6%)

## Failures (80)

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
The Executive Assistant for the Technology department (TEC) is Juthamas Kaewsai-phong (Mint).

*   **Email:** JUTHAMAS.KA@FAHMAI.CO.TH
*   **Phone Extension:** 77008
*   **Mobile:** 095-228-0338
```

### g073 [evp_vs_vp_disambig] P0/th
**Q:** ขอ LOGFL หน่อย ไม่เอา LOGVP

**Fails:** missing any-of ['Malee', 'มาลี']; missing any-of ['Amonthong', 'อมรทอง']

**Response:**

```
ข้อมูลทีม LOGFL ครับ

*   **สุจิรา อภิญญาเฉลิม (บอล)** - เลขานุการของ LOGFL
    *   อีเมล: SUJIRA.AP@FAHMAI.CO.TH
    *   เบอร์ภายใน: 79248
    *   สถานที่: FahMai Tower ชั้น 23
```

### g075 [evp_vs_vp_disambig] P0/th
**Q:** OPSQA ใคร — ไม่ใช่ OPSVP

**Fails:** missing any-of ['Kanok', 'กนก']; missing any-of ['Khaengkadchai', 'เก่งกาจชัย']

**Response:**

```
ผู้ที่อยู่ในหน่วยงาน OPSQA (ไม่รวมรองประธาน) คือ คุณเต่า (TAO THANAKASEMKIT) ตำแหน่งเลขานุการของ OPSQA ครับ (Email: TAO.TH@FAHMAI.CO.TH / Ext: 79548)
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
สำหรับหน่วยงาน RETBKK ที่ไม่ใช่ตำแหน่ง VP คือ:

**รัตตนา เจริญฟ้า (Rattana Charoenfa)**
*   **ตำแหน่ง:** เลขานุการของ RETBKK (Member of RETBKK-SEC)
*   **อีเมล:** RATTANA.CH2@FAHMAI.CO.TH
*   **เบอร์ต่อ:** 74330
*   **มือถือ:** 093-978-9586
```

### g078 [evp_vs_vp_disambig] P0/th
**Q:** ขอ RETUPC หน่อย ไม่เอา RETVP

**Fails:** missing any-of ['Santichai', 'สันติชัย']; missing any-of ['Boonmeephithak', 'บุญมีพิทักษ์']

**Response:**

```
คุณณัฎฐณิชา แก้วกาญจน์นาม (ไก่)
- ตำแหน่ง: เลขานุการของ RETUPC
- อีเมล: NATTANICHA.KA@FAHMAI.CO.TH
- เบอร์ภายใน: 71408
- เบอร์มือถือ: 082-127-7106
```

### g114 [name_lookup] P1/th
**Q:** ขอเบอร์ สมพงษ์ อินทรีย์นาม หน่อย

**Fails:** missing any-of ['48530', 'SOMPHONG.IN', '085-412-9461']

**Response:**

```
ไม่พบข้อมูล
```

### g116 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ สุขุม ใจเขียวบุญ

**Fails:** missing any-of ['55579', 'SUKHUM.JA', '085-612-9123']

**Response:**

```
ไม่พบข้อมูล
```

### g121 [name_lookup] P1/th
**Q:** ขอเบอร์ สรพงษ์ วิศวงษ์ หน่อย

**Fails:** missing any-of ['72279', 'SORAPONG.WI', '091-061-7212']

**Response:**

```
สรพงษ์ วิศวงษ์ - ไม่พบข้อมูล
```

### g124 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ เมฆา ราชกำจร

**Fails:** missing any-of ['74887', 'MEKHA.RA']

**Response:**

```
ไม่พบข้อมูล
```

### g129 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ ฤทธิรงค์ บุญอินทรีย์

**Fails:** missing any-of ['73128', 'RITTHIRONG.BU', '092-398-0784']

**Response:**

```
ไม่พบข้อมูล
```

### g135 [casual_name_lookup] P0/th
**Q:** พี่นัต ฝ่าย RET เบอร์อะไร

**Fails:** missing any-of ['54337', 'SUNEE.SU']

**Response:**

```
เบอร์ติดต่อของพี่นัต (คุณอรญา จิรจิตรานนท์) ฝ่าย RET คือ:

*   **เบอร์ต่อ:** 76423
*   **เบอร์โทรศัพท์มือถือ:** 085-682-5148
```

### g200 [dept_listing_small] P1/th
**Q:** ขอรายชื่อ MKT-EXEC ทั้งหมด

**Fails:** min_items 2 not met (0)

**Response:**

```

```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
แผนก MKT (Marketing) มีพนักงานทั้งหมด 234 คนครับ โดยมีคุณส้ม (SOM KANSATHIT) ดำรงตำแหน่ง CHIEF MARKETING OFFICER ครับ
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
The Retail (RET) department has a total of 437 employees.
```

### g253 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ สายฟ้า สัก 5 คน

**Fails:** min_items 5 not met (4)

**Response:**

```
ตัวอย่างพนักงานจากฝ่ายสายฟ้า (SF) 5 ท่าน ได้แก่:

1.  **จิรภัทร วัชรใจงาม** – ประธานเจ้าหน้าที่ฝ่ายผลิตภัณฑ์ (CPO) โทร. 78052
2.  **วิรัตน์ สมบุษราคัม (ดอกไม้)** – รองประธานฝ่ายสายฟ้า โทร. 72402
3.  **ถาวร บุญนำพงศ์** – ผู้จัดการทั่วไปแบรนด์สายฟ้า (GM) โทร. 79517
4.  **สรัญญา มหาอมรินทร์ (ฟลุ๊ค)** – ผู้อำนวยการฝ่ายนักการตลาดแบรนด์สายฟ้า
5.  **ทนิน บุญเกษม (บูม)** – ผู้จัดการผลิตภัณฑ์สายฟ้า โทร. 72
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (4)

**Response:**

```
รายชื่อพนักงานแบรนด์คลื่นเสียง (KS) 5 ท่าน เช่น:

*   **ธเนศ บัวทองประเสริฐ (VP)** - อีเมล: TANET.BU@FAHMAI.CO.TH, ต่อ 71215
*   **ราม ลวรรณ (จุ๊บ) (GM)** - อีเมล: RAM.LA@FAHMAI.CO.TH, ต่อ 75965
*   **วศิน ราชชัยดี (ทาฟฟี่)** - แผนกปฏิบัติการ, ต่อ 76044
*   **ธงชัย อัมพรสถิต** - แผนกการตลาด, ต่อ 75590
*   **วิสิทธิ์ ใจงาม (บอส)** - แผนกผลิตภัณฑ์, ต่อ 73419
```

### g290 [extension_reverse] P2/en
**Q:** whose ext is 76557

**Fails:** missing any-of ['Phongdaosai', 'พงดาวใส']

**Response:**

```
Extension 76557 belongs to **Nangnoi Pongdaosai (Prim)**, Manager DaoNuea Product Manager in the DN-PD section.
```

### g297 [email_mobile_lookup] P2/en
**Q:** 098-738-1431 — who?

**Fails:** missing any-of ['Akarajaidi', 'อัครใจดี']

**Response:**

```
The owner of this number is Arthit Akaraiaidi (Aom), Manager of DaoNuea Brand Operations (DN-OPS). 

**Contact Info:**
- **Email:** ARTHIT.AK@FAHMAI.CO.TH
- **Extension:** 76947
- **Office:** FahMai Tower 18F (HQ)
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ในการค้นหาด้วยรหัสหน่วยงาน **CEO-CoS** (Chief of Staff) พบพนักงานเพียงคนเดียวคือ:

*   **คุณบูม (BOOM)** — กิตติคุณ พงจงรัก
    *   **ตำแหน่ง:** หัวหน้าสำนักงานประธาน (CHIEF OF STAFF)
    *   **อีเมล:** KITTIKHUN.PH@FAHMAI.CO.TH
    *   **เบอร์ภายใน:** 79367
    *   **สถานที่ปฏิบัติงาน:** FahMai Tower ชั้น 16
```

### g353 [hard_multihop] P0/en
**Q:** who's the boss of the CMO's EA

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
The boss of the Executive Assistant (EA) to the CMO is the **Chief Marketing Officer (CMO)**.

The current CMO's EA is **Darika Daoruengphinyo (Ping)**. According to the directory:
*   **Name:** Darika Daoruengphinyo (ปิ๊ง)
*   **Position:** Executive Assistant to CMO
*   **Email:** darika.da@fahmai.co.th
*   **Extension:** 71338
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า (GM) ของแบรนด์ดาวเหนือ คือ คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN) ครับ

- **อีเมล:** WICHIAN.PH@FAHMAI.CO.TH
- **เบอร์ต่อ:** 76999
- **เบอร์โทรศัพท์:** 064-902-5307
- **สถานที่:** FahMai Tower ชั้น 19
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
The SFVP (Vice President of SaiFah) is **Wirat Sombusarakham (Dokmai)**. In the company structure, VPs typically report to the C-level executive of their functional area. For the Product Divisions like SaiFah (SF), the SFVP reports to the **Chief Operating Officer (COO)**.

The current COO is **Pongkan Rajchakan** (PONGKAN.RA@FAHMAI.CO.TH).
```

### g377 [thai_knowledge] P1/th
**Q:** สาขาภาคอีสานมีที่ไหนบ้าง

**Fails:** missing any-of ['NMA', 'นครราชสีมา', 'โคราช']

**Response:**

```
สาขาของฟ้าใหม่ในภาคอีสานมี 1 แห่ง คือ

*   **สาขาขอนแก่น (KKN)**: ตั้งอยู่ที่จังหวัดขอนแก่น
```

### g381 [thai_knowledge] P0/th
**Q:** CNX อยู่จังหวัดอะไร

**Fails:** missing any-of ['เชียงใหม่', 'Chiang Mai']

**Response:**

```
ไม่ใช่ข้อมูลของฟ้าใหม่
```

### g404 [refuse] P1/th
**Q:** ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ

**Fails:** missing any-of ['ไม่พบข้อมูล', 'no record found', 'ไม่พบ']; has ext pattern

**Response:**

```
คุณถาวร ประฟ้าใส (THAWAN PRAFAHSAI) แผนก SUP เบอร์ต่อคือ 78993 ครับ
```

### g440 [hard_multihop] P1/th
**Q:** ขอเบอร์ต่อของรองประธานที่มีเลขานุการคือคุณสุภาวดี บุญดาวเรือง หน่อยครับ

**Fails:** missing any-of ['79033']

**Response:**

```
ไม่พบข้อมูล ของคุณสุภาวดี บุญดาวเรือง ในระบบครับ หากคุณมีชื่อหรือนามสกุลที่สะกดถูกต้องมากกว่านี้ สามารถแจ้งเพื่อให้ตรวจสอบใหม่ได้ครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ (ปุ๊ก) สังกัดแผนก **DN (ดาวเหนือ)** ครับ

ผู้บริหารสูงสุดของแผนก (General Manager of DaoNuea) คือ **คุณวิเชียร พงหอมกลิ่น**
**อีเมล:** WICHIAN.PH@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดฝ่ายผลิตภัณฑ์จุดเชื่อม (JC) ซึ่งผู้บริหารสูงสุดของแผนก (General Manager) คือ:

**คุณสรัล อาวุทธ์มณี (SARAN AWUTMANI)**
*   **อีเมล:** SARAN.AW@FAHMAI.CO.TH
*   **ตำแหน่ง:** ผู้จัดการทั่วไปแบรนด์จุดเชื่อม (GENERAL MANAGER OF JUDCHUEM)
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนก **KS (คลื่นเสียง)** โดยผู้บริหารสูงสุดของแผนก (GM) คือ คุณยุทธนา เทวะ (YUTTHANA DEWA)

**อีเมล:** YUTTHANA.DE@FAHMAI.CO.TH
```

### g448 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณเกษม วิศอัญชลี สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['PHAIROJ.MA@FAHMAI.CO.TH']

**Response:**

```
คุณเกษม วิศอัญชลี สังกัดแผนก **LEG (ฝ่ายกฎหมาย)** ซึ่งมีผู้บริหารสูงสุดของแผนกคือ **CLO** (Chief Legal Officer)

อีเมลสำหรับติดต่อคือ: **ANAN.AS@FAHMAI.CO.TH** (คุณอนันต์ อัศวเหม)
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก **WK (แบรนด์วงโคจร)** โดยมีผู้บริหารสูงสุดของแผนกคือ:

**คุณกฤษ มหาแก้วใส (ขิง)**
*   **ตำแหน่ง:** GM แบรนด์วงโคจร (GENERAL MANAGER OF WONGKHOJON)
*   **อีเมล:** KRIS.MA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (Daonuea) คือ **คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)** ตำแหน่ง General Manager of Daonuea ครับ

*   **อีเมล:** WICHIAN.PH@FAHMAI.CO.TH
*   **เบอร์ต่อ:** 76999
*   **สถานที่ทำงาน:** FahMai Tower ชั้น 19
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
Assessing who is "most harmful" is subjective and depends on diverse perspectives.

As for the head of the JudChuem (JC) department, the General Manager is **Saran Awutmani (สรัล อาวุทธ์มณี)**. 

*   **Email:** SARAN.AW@FAHMAI.CO.TH
*   **Phone Extension:** 78762
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Kluensiang (KS) คือ คุณราม ลวรรณ (จุ๊บ) ตำแหน่ง General Manager of Kluensiang
อีเมล: RAM.LA@FAHMAI.CO.TH
เบอร์ต่อ: 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon (WK) คือ **คุณกฤษ มหาแก้วใส (ขิง)** ตำแหน่ง General Manager of Wongkhojon
- **อีเมล:** KRIS.MA@FAHMAI.CO.TH
- **เบอร์ต่อ:** 74375
```

### g460 [hard_implicit_hierarchy] P1/en
**Q:** In the FIN-AR section, who is the most senior employee?

**Fails:** missing any-of ['เมฆา', 'Mekha']; missing any-of ['ภัทรใจเขียว', 'Phatjaikieow']

**Response:**

```
Determining who is the "most senior" employee is subjective and depends on diverse perspectives, such as their position level, years of service, or age. I can provide a list of employees in the **FIN-AR** section for your review:

*   **NUTCHA (CHOMP) WONGDEE** – MANAGER (FIN-AR-1)
*   **PAWEEN (NEW) THANASUK** – LEAD (FIN-AR-2)
*   **NATTHAPAT (NAT) PONGSA** – LEAD (FIN-AR-3)
*   **WARAPORN (WARA
```

### g466 [hard_implicit_hierarchy] P1/en
**Q:** In the KS-MKT section, who is the most senior employee?

**Fails:** missing any-of ['ธงชัย', 'Thongchai']; missing any-of ['อัมพรสถิต', 'Amphomsathit']

**Response:**

```
Identifying the "most senior" employee is subjective and depends on diverse perspectives, such as whether seniority is measured by age, years of experience, start date at the company, or position level. 

I can, however, provide information regarding the employees in the **KS-MKT** (KluenSiang Marketing) section by their start year and position level.

According to the directory:

*   **THITIPHAN 
```

### g472 [bilingual] P1/th
**Q:** รหัสหน่วยงานของประธานเจ้าหน้าที่การตลาดคืออะไรครับ

**Fails:** missing any-of ['CMO']

**Response:**

```


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

### g519 [bilingual] P1/th
**Q:** ช่วยหา unit code ของ Vice President Customer Support ให้ทีครับ

**Fails:** missing any-of ['SUPVP']

**Response:**

```

```

### g520 [bilingual] P1/th
**Q:** ขอ email address ของ Vice President Quality หน่อยครับ

**Fails:** missing any-of ['KANOK.KH@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g532 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก DN ระดับ Director และเริ่มงานในปี 2021 ครับ

**Fails:** missing count 2

**Response:**

```
ขออภัยครับ ไม่พบข้อมูลพนักงานที่ตรงตามเงื่อนไขดังกล่าว (แผนก DN, ระดับ Director, เริ่มงานในปี 2021) ในระบบครับ
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
There are 0 employees in the DN department at the IC level who started in 2020. Individuals in that department who started in 2020 hold Manager or Director level positions.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are 6 employees in the DN department at the Lead level who started in 2022:

*   **อภิชัย ธนบุญ (APICHAI THANABUN)** - DN-MKT
*   **ธนพล พิไชยา (THANAPHON PHICHAIYAWONG)** - DN-PD
*   **กฤติน อนุเจริญ (KRITTIN ANUCHAROEN)** - DN-OPS
*   **ราม มหากิตติ (RAM MAHAKITTIPONG)** - DN-OPS
*   **วีระ ชัยโชคดี (VEERA CHAICHOKDEE)** - DN-PD
*   **กิตติศักดิ์ ฟ้าใสทอง (KITTISAK FAHSAITHONG)** - DN-MKT
```

### g536 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก DN ระดับ Lead และเริ่มงานในปี 2023 ครับ

**Fails:** missing count 2

**Response:**

```
มีพนักงานในแผนก DN ระดับ Lead ที่เริ่มงานในปี 2023 ทั้งหมด 0 คนครับ (ไม่พบข้อมูล)
```

### g539 [listing_count] P1/en
**Q:** How many employees are in the FIN department at Director level who started in 2022?

**Fails:** missing count 2

**Response:**

```
There are no records of employees in the FIN department at the Director level who started in 2022.
```

### g540 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ IC และเริ่มงานในปี 2020 ครับ

**Fails:** missing count 4

**Response:**

```
จากข้อมูลในระบบ มีพนักงานแผนก FIN ระดับ IC ที่เริ่มงานในปี 2020 ทั้งหมด 0 คนครับ
```

### g541 [listing_count] P1/en
**Q:** How many employees are in the FIN department at Lead level who started in 2019?

**Fails:** missing count 3

**Response:**

```
There are no records of employees in the FIN department at the Lead level who started in 2019.
```

### g542 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ Manager และเริ่มงานในปี 2022 ครับ

**Fails:** missing count 3

**Response:**

```
พบพนักงาน 0 คนในแผนก FIN ระดับ Manager ที่เริ่มงานในปี 2022 ครับ
```


_+30 more failures — see results.jsonl_
