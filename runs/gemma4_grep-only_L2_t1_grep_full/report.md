# Run: `gemma4_grep-only_L2_t1_grep_v10full`

**Overall: 554/626 pass (88.5%)**

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
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| refuse | 90/90 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| nickname_grid | 59/61 | 96.7% |
| bilingual | 38/40 | 95.0% |
| noisy_name_form | 19/20 | 95.0% |
| multi_entity_turn | 18/20 | 90.0% |
| evp_vs_vp_disambig | 22/25 | 88.0% |
| dept_member_count | 13/15 | 86.7% |
| listing_count | 17/20 | 85.0% |
| enterprise_shorthand | 17/20 | 85.0% |
| evp_secretary | 4/5 | 80.0% |
| thai_knowledge | 8/10 | 80.0% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| hard_multihop | 19/26 | 73.1% |
| superlative | 7/10 | 70.0% |
| counterfactual | 17/25 | 68.0% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 11/18 | 61.1% |
| name_lookup | 12/20 | 60.0% |
| deep_multihop | 7/12 | 58.3% |
| subsidiary_routing | 4/12 | 33.3% |

## By priority

- P0: 217/226 (96.0%)
- P1: 309/364 (84.9%)
- P2: 28/36 (77.8%)

## Failures (72)

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
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
thought
ผู้บริหารสูงสุดของแผนกดาวเหนือ (DN) คือ คุณวิเชียร พงหอมกลิ่น (General Manager) อีเมล: WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
Saran Awutmani (SARAN.AW@FAHMAI.CO.TH) is the General Manager of Judchuem.
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (Kluensiang) คือ คุณราม ลวรรณ (คุณจุ๊บ) อีเมล RAM.LA@FAHMAI.CO.TH ครับ
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon คือ คุณกฤษ มหาแก้วใส (ขิง) อีเมล KRIS.MA@FAHMAI.CO.TH ครับ
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

**Fails:** missing count 7

**Response:**

```
Hiding the internal thought process...
There are 0 employees in the DN department at the IC level who started in 2020.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 6

**Response:**

```
There are 7 employees in the DN department at the Lead level who started in 2022:

* อภิชัย ธนบุญ (APICHAI THANABUN)
* ธนพล พิไชยา (THANAPHON PHICHAIYAWONG)
* กฤติน อนุเจริญ (KRITTIN ANUCHAROEN)
* ราม มหากิตติ (RAM MAHAKITTIPONG)
* วีระ ชัยโชคดี (VEERA CHAICHOKDEE)
* กิตติศักดิ์ ฟ้าใสทอง (KITTISAK FAHSAITHONG)
* (One additional match from the full directory)

**Total: 7**
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

### g633 [nickname_grid] P1/th
**Q:** ยุ้ย คือใคร มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
มีคนที่ใช้ชื่อเล่นว่า "ยุ้ย" ทั้งหมด 12 คน ดังนี้ครับ:

*   **คุณแตง (ยุ้ย) บุญญาสินธุ์** - เลขานุการของ HRVP (HR) | อีเมล: TAENG.BO@FAHMAI.CO.TH
*   **คุณธีรภพ (ยุ้ย) อัครกำจร** - เจ้าหน้าที่บริการลูกค้าทางโทรศัพท์ (SUP) | อีเมล: THEERAPHOP.AK@FAHMAI.CO.TH
*   **คุณกฤต (ยุ้ย) ธนศรี** - หัวหน้าทีมพนักงานขายสาขาชลบุรี (RET) | อีเมล: KRID.TH@FAHMAI.CO.TH
*   **คุณกฤษ (ยุ้ย) วัชรการเวก** - หัวหน้าทีม
```

### g662 [multi_entity_turn] P1/en
**Q:** ext for SUPVP, OPSVP

**Fails:** missing any-of ['77358']; min_items 2 not met (1)

**Response:**

```
- SUPVP SUP: 79070
- VP OPS: 773 58
```

### g671 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาโคราช มีกี่คน

**Fails:** missing count 30

**Response:**

```
พนักงานสาขาโคราช (NMA) มีทั้งหมด 72 คนครับ
```

### g682 [enterprise_shorthand] P1/th
**Q:** หัวหน้าทีมฟินฯ คือใคร

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
ฝ่ายการเงิน (FIN) มีหัวหน้าทีมในหลายส่วนงาน ดังนี้ครับ:

*   **หัวหน้าทีมนักวิเคราะห์การเงิน:** คุณคึกฤทธิ์ จิรบุญมี (KUKRIT.CH2@FAHMAI.CO.TH) และ คุณกุหลาบ จงรักดี (KULAP.CH3@FAHMAI.CO.TH)
*   **หัวหน้าทีมเจ้าหน้าที่บัญชีลูกหนี้:** คุณดาว แสงทอง (DAO.SA@FAHMAI.CO.TH) และ คุณปกรณ์ บุญดาวใส (PAKORN.BU@FAHMAI.CO.TH)
*   **หัวหน้าทีมนักบัญชี:** คุณไพลิน รัตนใจ (PHAILIN.RA@FAHMAI.CO.TH) และ คุณสุเมธ เ
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าทีมในฝ่ายการตลาด (MKT) มีหลายท่านแบ่งตามสายงานดังนี้ครับ:

*   **ประชาสัมพันธ์ (PR):** คุณทักษอร เกษมใจ (เกม) - `TAKSA-ORN.KA2@FAHMAI.CO.TH`
*   **การตลาดดิจิทัล (Digital Marketing):** คุณไพบูลย์ แซ่ฮวง (ดอกไม้) และ คุณองอาจ สุวรรณชัย
*   **CRM:** คุณมาลี เกียรติกำจรมณี, คุณพลอย อมรจิตรานนท์ และ คุณวิภา ราชกอบสุข (มิว)
*   **จัดอีเวนต์ (Events):** คุณศศิปราภา ดาวเรืองสุข (ชาร์ค) - `SASIPRAP
```

### g746 [counterfactual] P1/en
**Q:** I heard พงษ์กานต์ ราชชากัญญ์ is the CEO — can I get their extension?

**Fails:** missing any-of ['COO', 'Chief Operating', 'ปฏิบัติการ']

**Response:**

```
no record found
```

### g748 [counterfactual] P1/en
**Q:** I heard ฤทธิชัย แก้วใสภิญโญ is the CMO — can I get their extension?

**Fails:** missing any-of ['CTO', 'Chief Technology', 'เทคโนโลยี']

**Response:**

```
no record found
```


_+22 more failures — see results.jsonl_
