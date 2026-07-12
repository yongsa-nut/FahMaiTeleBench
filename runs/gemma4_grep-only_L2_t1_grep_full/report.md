# Run: `gemma4_grep-only_L2_t1_grep_full`

**Overall: 542/626 pass (86.6%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
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
| nickname_grid | 58/61 | 95.1% |
| bilingual | 38/40 | 95.0% |
| noisy_name_form | 19/20 | 95.0% |
| multi_entity_turn | 18/20 | 90.0% |
| evp_vs_vp_disambig | 22/25 | 88.0% |
| dept_member_count | 13/15 | 86.7% |
| listing_count | 17/20 | 85.0% |
| org_informal_listing | 5/6 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| thai_knowledge | 8/10 | 80.0% |
| enterprise_shorthand | 16/20 | 80.0% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| hard_multihop | 19/26 | 73.1% |
| superlative | 7/10 | 70.0% |
| counterfactual | 17/25 | 68.0% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 11/18 | 61.1% |
| name_lookup | 12/20 | 60.0% |
| deep_multihop | 7/12 | 58.3% |
| surname_family | 13/24 | 54.2% |
| subsidiary_routing | 6/12 | 50.0% |

## By priority

- P0: 215/226 (95.1%)
- P1: 299/364 (82.1%)
- P2: 28/36 (77.8%)

## Failures (84)

### g045 [evp_secretary] P0/th
**Q:** CFO secretary ใคร

**Fails:** missing any-of ['Chokdeekamchon', 'โชคดีกำจร']

**Response:**

```
คุณเบญจวรรณ (มิ้น) - BENJAWAN.CH@FAHMAI.CO.TH ต่อ 75703
```

### g073 [evp_vs_vp_disambig] P0/th
**Q:** ขอ LOGFL หน่อย ไม่เอา LOGVP

**Fails:** missing any-of ['Malee', 'มาลี']; missing any-of ['Amonthong', 'อมรทอง']

**Response:**

```
คุณสุจิรา อภิญญาเฉลิม (บอล) - SUJIRA.AP@FAHMAI.CO.TH ต่อ 79248
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
คุณรัตตนา เจริญฟ้า (RATTANA CHAROENFA) - RATTANA.CH2@FAHMAI.CO.TH
```

### g079 [evp_vs_vp_disambig] P0/th
**Q:** B2BACC ใคร — ไม่ใช่ B2BVP

**Fails:** missing any-of ['Thanya', 'ธัญญา']; missing any-of ['Charoenpholphinyo', 'เจริญผลภิญโญ']

**Response:**

```
คุณงามจิตร ประรักษา (แพร) - NGAMCHIT.PR@FAHMAI.CO.TH ต่อ 76434
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
ไม่พบข้อมูล
```

### g124 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ เมฆา ราชกำจร

**Fails:** missing any-of ['74887', 'MEKHA.RA']

**Response:**

```
ไม่พบข้อมูล
```

### g125 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ วีระ อมรจงรัก

**Fails:** missing any-of ['12774', 'VEERA.AM']

**Response:**

```
ไม่พบข้อมูล
```

### g126 [name_lookup] P1/th
**Q:** ไพบูลย์ อธิเกียรติกำจร เบอร์อะไร

**Fails:** missing any-of ['32610', 'PHAIBUN.AT', '086-112-6325']

**Response:**

```
ไม่พบข้อมูล
```

### g128 [name_lookup] P1/th
**Q:** กานติมา การเวกประเสริฐ เบอร์อะไร

**Fails:** missing any-of ['78422', 'KANTIMA.KA', '095-932-5295']

**Response:**

```
ไม่พบข้อมูล
```

### g130 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ สมบัติ การเวกรัตน์

**Fails:** missing any-of ['72660', 'SOMBAT.KA']

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

* **คุณวชิร จิรบุญ (เบอร์รี่)** - CEO: VACHIR.CH@FAHMAI.CO.TH
* **คุณกมลา ชัยสนธิ์สว่าง** - CFO: KAMALA.CH@FAHMAI.CO.TH
* **คุณฤทธิชัย แก้วใสภิญโญ (ปันปัน)** - CTO: RITTICHAI.KA@FAHMAI.CO.TH
* **คุณพงษ์กานต์ ราชชากัญญ์** - COO: PONGKAN.RA@FAHMAI.CO.TH
* **คุณส้ม กาญจน์สถิต** - CMO: SOM.KA@FAHMAI.CO.TH
* **คุณจิรภัทร วัชรใจงาม** - CPO: JIRAPAT.WA@FAHM
```

### g172 [nickname_grid] P0/th
**Q:** ขิง ที่ SUP เบอร์อะไร

**Fails:** missing any-of ['Pholdech', 'พลเดช']

**Response:**

```
คุณสุณี (ขิง) เบอร์ต่อ 71734 หรือมือถือ 094-546-2762 ครับ
```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
แผนก MKT มีพนักงานทั้งหมด 234 คนครับ
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
The RET department has 437 employees.
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (3)

**Response:**

```
รายชื่อพนักงานแผนกคลื่นเสียง (KS) 5 ท่านครับ:

*   คุณธเนศ บัวทองประเสริฐ (TANET.BU@FAHMAI.CO.TH)
*   คุณปิยนันท์ พรหมพิทักษ์ (PIYANAN.PH@FAHMAI.CO.TH)
*   คุณราม ลวรรณ (RAM.LA@FAHMAI.CO.TH)
*   คุณธเนศ บัวทองประเสริฐ (TANET.BU@FAHMAI.CO.TH)
*   คุณปิยนันท์ พรหมพิทักษ์ (PIYANAN.PH@FAHMAI.CO.TH)

*(หมายเหตุ: ข้อมูลเบื้องต้นจากระบบ)*
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
The Bangkok retail VP is Wiriya Chanchai (Tik).
Email: WIRIYA.CH@FAHMAI.CO.TH | Ext: 79141
```

### g275 [multi_entity_turn] P0/th
**Q:** ขอเบอร์ของ CPO, SFVP

**Fails:** missing any-of ['78052']; missing any-of ['72402']

**Response:**

```
- CPO (คุณจิรภัทร): 096-557-6834
- SFVP (คุณวิรัตน์): 064-970-0992
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ คุณวิเชียร พงหอมกลิ่น (WICHIAN.PH@FAHMAI.CO.TH) ครับ
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
The SFVP (Vice President of SaiFah) is **Wirat Sombusarakham** (วิรัตน์ สมบุษราคัม). As a VP, they report to the CEO, **Vachir Chirabun** (วชิร จิรบุญ).

**Contact:** VACHIR.CH@FAHMAI.CO.TH / Ext. 73048
```

### g377 [thai_knowledge] P1/th
**Q:** สาขาภาคอีสานมีที่ไหนบ้าง

**Fails:** missing any-of ['NMA', 'นครราชสีมา', 'โคราช']

**Response:**

```
สาขาในภาคอีสานคือ สาขาขอนแก่น (KKN) ครับ
```

### g380 [thai_knowledge] P1/th
**Q:** ใครชื่อเล่นเป็นชื่อสีบ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณวิเชียร พงหอมกลิ่น (GM แบรนด์ดาวเหนือ) คือ WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุดของแผนก JC (จุดเชื่อม) ที่คุณละไม บุญพงศ์ สังกัดอยู่ คือ SARAN.AW@FAHMAI.CO.TH (คุณสรัล อาวุทธ์มณี) ครับ
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุด (GM) ของแผนก KS (คลื่นเสียง) ที่คุณอัมพร ประฟ้า สังกัดอยู่ คือ RAM.LA@FAHMAI.CO.TH (คุณราม ลวรรณ) ครับ
```

### g448 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณเกษม วิศอัญชลี สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['PHAIROJ.MA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูลของคุณเกษม วิศอัญชลี ในระบบครับ
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุดของแผนก WK (แบรนด์วงโคจร) ที่คุณธนพล พิประเสริฐ สังกัดอยู่ คือ KRIS.MA@FAHMAI.CO.TH (คุณกฤษ มหาแก้วใส) ครับ
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea (DN)

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (DN) คือ คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN) อีเมล: WICHIAN.PH@FAHMAI.CO.TH
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem (JC) department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the Judchuem (JC) department is Saran Awutmani (General Manager of Judchuem).
Email: SARAN.AW@FAHMAI.CO.TH
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Kluensiang (KS) คือ คุณราม ลวรรณ (คุณจุ๊บ) อีเมล RAM.LA@FAHMAI.CO.TH ครับ
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon (WK)

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon (WK) คือ คุณกฤษ มหาแก้วใส (ขิง) อีเมล KRIS.MA@FAHMAI.CO.TH ครับ
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

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
There are 0 employees in the DN department at the IC level who started in 2020.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are 6 employees in the DN department at the Lead level who started in 2022.
```

### g540 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ IC และเริ่มงานในปี 2020 ครับ

**Fails:** missing count 4

**Response:**

```
มีพนักงานแผนก FIN ระดับ IC ที่เริ่มงานในปี 2020 จำนวน 1 คน คือ คุณสนิท อธิบุญนำ ครับ
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Phongchongrak (Chief of Staff) works on the 16th floor of FahMai Tower.
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดฝ่าย B2B ซึ่งผู้ที่มีตำแหน่งสูงสุดในฝ่ายนี้คือ รองประธาน (VP) โดยมี 2 ท่าน ดังนี้ครับ:

*   **คุณอุกฤษฎ์ วัชรเสริม** (รองประธานฝ่ายขายองค์กร): เบอร์ต่อ 79274
*   **คุณธัญญา เจริญผลภิญโญ** (รองประธานฝ่ายดูแลลูกค้าองค์กร): เบอร์ต่อ 71547
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ สังกัดแผนกดาวเหนือ (DN) ซึ่งผู้ที่มีตำแหน่งสูงสุดคือ คุณวิเชียร พงหอมกลิ่น (General Manager) เบอร์ต่อ 76999 ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
คุณอภิชัย จิตรานนท์เจริญ สังกัดฝ่ายการเงิน (FIN) ซึ่งผู้ที่มีตำแหน่งสูงสุดในฝ่ายนี้คือ คุณกมลา ชัยสนธิ์สว่าง (CFO) เบอร์โทรศัพท์ภายในคือ 74921 ครับ
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คุณมนตรา บุญเรืองโชติ สังกัดฝ่ายทรัพยากรบุคคล (HR) ซึ่งผู้ที่มีตำแหน่งสูงสุดในฝ่ายนี้คือ คุณณฐามน อภิชัยดี (CHRO) เบอร์โทรศัพท์ภายในคือ 79303 ครับ
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
เบอร์ต่อของคุณสรัล อาวุทธ์มณี (GM แบรนด์จุดเชื่อม) คือ 78762 ครับ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
เบอร์ต่อของคุณราม ลวรรณ (GM แบรนด์คลื่นเสียง) คือ 75965 ครับ
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
คุณคำรณ ศรีอัญชลี สังกัดฝ่ายปฏิบัติการ (OPS) ซึ่งผู้ที่มีตำแหน่งสูงสุดในฝ่ายนี้คือ คุณพงษ์กานต์ ราชชากัญญ์ (Chief Operating Officer) เบอร์โทรศัพท์ภายในคือ 75464 ครับ
```

### g605 [surname_family] P1/th
**Q:** พนักงานที่นามสกุล มณีฟ้า มีใครบ้าง ขอชื่อทุกคน

**Fails:** missing count 3

**Response:**

```
พนักงานที่นามสกุล มณีฟ้า มีดังนี้ครับ:
- คุณราชตะ มณีฟ้า
- คุณจันทนา มณีฟ้า
- คุณพฤกษา มณีฟ้า
```

### g606 [surname_family] P1/en
**Q:** List everyone with the surname เขียวขจีศรี (give all of them).

**Fails:** missing count 3

**Response:**

```
Here are the employees with the surname เขียวขจีศรี:

* **Pakorn Kiaokajisi (ปกรณ์ เขียวขจีศรี)** - PAKORN.KI@FAHMAI.CO.TH
* **Atchara Kiaokajisi (อัจฉรา เขียวขจีศรี)** - ATCHARA.KI@FAHMAI.CO.TH
* **Paitoon Kiaokajisi (ไพฑูรย์ เขียวขจีศรี)** - PAITOON.KI@FAHMAI.CO.TH
```

### g607 [surname_family] P1/th
**Q:** พนักงานที่นามสกุล แสงทอง มีใครบ้าง ขอชื่อทุกคน

**Fails:** missing count 3

**Response:**

```
พนักงานที่นามสกุล แสงทอง มีดังนี้ครับ:
- คุณระวี แสงทอง
- คุณดาว แสงทอง
- คุณอนุรักษ์ แสงทอง
```

### g608 [surname_family] P1/en
**Q:** List everyone with the surname ไกรศรีมณี (give all of them).

**Fails:** missing count 3

**Response:**

```
- ยุพา ไกรศรีมณี: YU-PHA.KR@FAHMAI.CO.TH
- วิภา ไกรศรีมณี: WIPHA.KR@FAHMAI.CO.TH
- พาณิช ไกรศรีมณี: PANIT.KR@FAHMAI.CO.TH
```

### g610 [surname_family] P1/en
**Q:** List everyone with the surname บุญเรืองกุล (give all of them).

**Fails:** missing count 2

**Response:**

```
- ศศิ บุญเรืองกุล (SASI BOONRUENGKUN) - SASI.BO@FAHMAI.CO.TH
- น้ำทิพย์ บุญเรืองกุล (NAMTHIP BOONRUENGKUN) - NAMTHIP.BO@FAHMAI.CO.TH
```


_+34 more failures — see results.jsonl_
