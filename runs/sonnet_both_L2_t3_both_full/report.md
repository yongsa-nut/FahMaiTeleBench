# Run: `sonnet_both_L2_t3_both_v10full`

**Overall: 596/626 pass (95.2%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_vs_vp_disambig | 25/25 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
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
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| nickname_grid | 59/61 | 96.7% |
| enterprise_shorthand | 19/20 | 95.0% |
| hard_multihop | 24/26 | 92.3% |
| dept_listing_small | 6/7 | 85.7% |
| listing_count | 17/20 | 85.0% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| evp_secretary | 4/5 | 80.0% |
| noisy_name_form | 14/20 | 70.0% |
| subsidiary_routing | 8/12 | 66.7% |
| multi_hop | 11/18 | 61.1% |

## By priority

- P0: 221/226 (97.8%)
- P1: 339/364 (93.1%)
- P2: 36/36 (100.0%)

## Failures (30)

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
The TEC-EA is assigned to the **CTO**, not specifically to TECPM. There is no dedicated EA unit for TECPM in the directory.

That said, here's what's available:

- **TEC-EA (EA to CTO):** จุฑามาศ แก้วใสพงศ์ (Mint) — 📧 JUTHAMAS.KA@FAHMAI.CO.TH | 📱 095-228-0338

- **TECPM (VP Platform):** ราชตะ สัมชาญณรงค์ — 📧 RACHATA.SA@FAHMAI.CO.TH | 📱 085-429-2999

If you're looking for a secretary specifically s
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล สำหรับชื่อ "อรุณ" ในแผนก SUP ครับ/ค่ะ

อาจลองตรวจสอบการสะกดชื่อ หรือแจ้งข้อมูลเพิ่มเติม (เช่น นามสกุล หรือชื่อเล่น) เพื่อช่วยค้นหาได้เลยนะครับ/ค่ะ
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล ในระบบไดเรกทอรีของฟ้าใหม่ไม่มีพนักงานชื่อ "อรุณ" ที่สาขาขอนแก่น (KKN) หรือชื่อ "อรุณ ขอนแก่น" ค่ะ
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
There's one person in the CEO secretary/EA role:

**อรญา วัชรกาญจน์ (Orraya Watcharakan)** — ชื่อเล่น: เป้ (Pe)
- Position: เลขานุการของ CEO / Executive Assistant to CEO
- Unit: CEO-EA
- Email: ORRAYA.WA@FAHMAI.CO.TH
- Extension: 75665
- Location: FahMai Tower 7F
```

### g351 [hard_multihop] P0/th
**Q:** ผู้บริหารที่มีจุฑามาศ แก้วใสพงศ์เป็นเลขานุการคือใคร

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
จุฑามาศ แก้วใสพงศ์ (มิ้น) เป็นเลขานุการของ **CTO** ค่ะ

ต้องการทราบข้อมูลของ CTO เพิ่มเติมไหมคะ?
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ของแบรนด์ดาวเหนือ (DN) คือ **คุณวิเชียร พงหอมกลิ่น** ครับ/ค่ะ

- 📧 WICHIAN.PH@FAHMAI.CO.TH
- 📞 064-902-5307
- ต่อภายใน: 76999
- ที่ตั้ง: FahMai Tower 19F
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **ดาวเหนือ (Daonuea)** คือ:

- **วิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**
- ตำแหน่ง: General Manager of Daonuea (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ)
- 📧 WICHIAN.PH@FAHMAI.CO.TH
- 📱 064-902-5307
- 📍 FahMai Tower 19F
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (KS) คือ:

**คุณราม ลวรรณ (Ram Lawan)** ชื่อเล่น: จุ๊บ
- ตำแหน่ง: General Manager of Kluensiang (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง)
- อีเมล: RAM.LA@FAHMAI.CO.TH
- ต่อโทรศัพท์: 75965
- สถานที่ทำงาน: FahMai Tower 18F
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **วงโคจร (WK)** คือ

**คุณกฤษ มหาแก้วใส (Kris Mahakaewsai)** ชื่อเล่น: ขิง
- ตำแหน่ง: General Manager of WongKhoJon (ผู้จัดการทั่วไปแบรนด์วงโคจร)
- อีเมล: KRIS.MA@FAHMAI.CO.TH
- สถานที่ทำงาน: FahMai Tower 7F
```

### g528 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก B2B ระดับ IC และเริ่มงานในปี 2021 ครับ

**Fails:** missing count 5

**Response:**

```
ได้ผลลัพธ์มาแล้ว ขอกรองเฉพาะปี 2021 จากผลที่ได้ครับ

จากผลการค้นหาพนักงานแผนก **B2B** ระดับ **IC** ทั้งหมด 47 คน เมื่อกรองเฉพาะที่เริ่มงานในปี **2021** พบทั้งหมด **4 คน** ได้แก่:

| ชื่อ | ตำแหน่ง |
|---|---|
| ณัฏฐพล ศรีพิทักษ์ | B2B Sales Representative |
| อรอนงค์ รัตนเกษม | B2B Support Specialist |
| อรุณ สัมภิญโญ | B2B Sales Representative |
| ไพบูลย์ บุญมางาม | Solutions Engineer |

รวมทั้งห
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
Now I have all 131 DN department rows. Let me carefully count those with **Department = DN**, **Position Level = IC**, and **Start Year = 2020** from the full results of the first search (which returned all 105 DN IC employees without truncation).

Going through the complete first query results for `start_year = 2020`:

1. ทินกร นราชาญณรงค์ (DN-OPS-70)
2. โยธกา อัมพรสว่าง (DN-ENG-71)
3. วีระ พงอัส
```

### g540 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ IC และเริ่มงานในปี 2020 ครับ

**Fails:** missing count 4

**Response:**

```
จากผลการค้นหา ได้รายชื่อพนักงานแผนก FIN ระดับ IC ทั้งหมด 69 คน ขอกรองเฉพาะที่เริ่มงานปี 2020 ครับ

จากข้อมูลที่ได้รับ มีพนักงานที่ start_year = 2020 ดังนี้ (นับจากผลลัพธ์):
- สนิท อธิบุญนำ (start_year: 2020)

ให้ตรวจสอบให้ครบถ้วนจากผลลัพธ์ทั้งหมด โดยนับจากข้อมูลที่ได้รับ พบว่ามีเพียง **1 คน** ที่ตรงเงื่อนไขทั้งหมด (FIN + IC + 2020) ครับ

---

มีพนักงานแผนก **FIN** ระดับ **IC** ที่เริ่มงานในปี **20
```

### g572 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Sukum Suwanfahsai manager ทีม chat support หน่อยค่ะ

**Fails:** missing any-of ['SUKHUM.SU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ของคุณ Sukum Suwanfahsai ในระบบไดเรกทอรีของฟ้าใหม่ค่ะ กรุณาตรวจสอบชื่อ-นามสกุลอีกครั้ง หรือลองค้นหาด้วยชื่อภาษาไทยได้เลยนะคะ 😊
```

### g575 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Sombat Bunnamngam manager ทีม data scientist เบอร์อะไรครับ

**Fails:** missing any-of ['76059']

**Response:**

```
ไม่พบข้อมูล ของคุณ Sombat Bunnamngam ในระบบไดเรกทอรีของฟ้าใหม่ครับ กรุณาตรวจสอบชื่อ-นามสกุลอีกครั้ง หรืออาจลองค้นหาด้วยชื่อเล่น/ชื่อภาษาไทยได้เลยครับ
```

### g577 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Oraya เลขาของ CEO หน่อยค่ะ

**Fails:** missing any-of ['ORRAYA.WA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ในระบบไดเรกทอรีของฟ้าใหม่ไม่มีพนักงานชื่อ Oraya ที่เป็นเลขาของ CEO ค่ะ

ลองตรวจสอบชื่อสะกดอีกครั้ง หรือแจ้งชื่อเพิ่มเติมได้เลยนะคะ 😊
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล ครับ — ไม่มีพนักงานชื่อเล่น "Vaen" ที่เป็น Director ทีม Escalations ในระบบไดเรกทอรีของฟ้าใหม่เลยครับ

อาจลองตรวจสอบการสะกดชื่อเล่น หรือชื่อ-นามสกุลจริงเพิ่มเติมได้ครับ แล้วผมจะช่วยค้นหาให้ใหม่นะครับ 😊
```

### g583 [noisy_name_form] P1/en
**Q:** Can I get the extension for Sompong, the VP of Digital Marketing?

**Fails:** missing any-of ['79901']

**Response:**

```
I'm unable to find anyone named **Sompong** in the directory — **no record found**. It's possible the name may be spelled differently or they may not be in the system.

Could you double-check the spelling, or do you have any other details (like a nickname or email) that might help me locate them?
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found — there's no one named "Ravi" in the FahMai employee directory. Could you double-check the name or provide additional details (e.g., last name or employee ID)?
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
ในแผนก B2B มี VP อยู่ 2 ท่าน (ไม่มี C-level ในแผนกนี้โดยตรง) ครับ ได้แก่:

| ชื่อ | ตำแหน่ง | เบอร์ต่อ |
|---|---|---|
| **อุกฤษฎ์ วัชรเสริม** | VP B2B Sales | **79274** |
| **ธัญญา เจริญผลภิญโญ** | VP B2B Accounts | **71547** |

ทั้งสองท่านอยู่ในระดับ VP ซึ่งเป็นตำแหน่งสูงสุดในแผนก B2B ครับ ต้องการเบอร์ของท่านใดเป็นพิเศษไหมครับ?
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
ตำแหน่งสูงสุดในแผนก DN (ดาวเหนือ) คือ **VP** ครับ

📋 **คุณเรืองศักดิ์ เทพเกียรติกำจร**
ตำแหน่ง: รองประธานฝ่ายดาวเหนือ (DNVP)
☎️ เบอร์ต่อ: **72280**
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
ตำแหน่งสูงสุดในแผนก FIN คือ **CFO** ครับ

**คุณกมลา ชัยสนธิ์สว่าง** — Chief Financial Officer (CFO)
📞 เบอร์ต่อ: **74921**
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
ตำแหน่งสูงสุดในแผนก HR คือ **CHRO** ครับ

---

**คุณณฐามน อภิชัยดี (NATHAMON APHICHAIDEE)**
ตำแหน่ง: Chief Human Resources Officer (CHRO)
📞 เบอร์ต่อ: **79303**
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
ตำแหน่งสูงสุดในแผนก JC (จุดเชื่อม) คือ **VP** ครับ

📞 **คุณราชินี อาทิตย์สุข** — Vice President of JudChuem
- เบอร์ต่อ: **75642**
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
ตำแหน่งสูงสุดในแผนก KS (คลื่นเสียง) คือ **VP** ครับ ได้เลย:

**คุณธเนศ บัวทองประเสริฐ**
ตำแหน่ง: รองประธานฝ่ายคลื่นเสียง (KSVP)
📞 เบอร์ต่อ: **71215**
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
ตำแหน่งสูงสุดในแผนก OPS คือ **COO** ครับ

---

**คุณพงษ์กานต์ ราชชากัญญ์**
ตำแหน่ง: Chief Operating Officer (COO)
📞 เบอร์ต่อ: **75464**
```

### g683 [enterprise_shorthand] P1/en
**Q:** Who heads the HR team?

**Fails:** missing any-of ['Nathamon', 'ณฐามน']; missing any-of ['Aphichaidee', 'อภิชัยดี']

**Response:**

```
The HR team is headed by **สุเมธ อัครใจงาม (Sumate Akarajaingam)** — nickname: สกาย (Sky)

- **Position:** Vice President, Human Resources
- **Email:** SUMATE.AK@FAHMAI.CO.TH
- **Office:** FahMai Tower 22F, HQ (Rama IX)
```

### g772 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์จุดเชื่อม

**Fails:** missing any-of ['Narong', 'ณรงค์']; missing any-of ['Kobsookbun', 'กอบสุขบุญ']

**Response:**

```
สำหรับแบรนด์ **จุดเชื่อม (JC)** มีผู้บริหารระดับสูงดังนี้ครับ:

- **VP:** คุณราชินี อาทิตย์สุข (RACHINI ARTHITKULSUK)
 ตำแหน่ง: รองประธานฝ่ายจุดเชื่อม
 📧 RACHINI.AR@FAHMAI.CO.TH | ต่อ 75642

- **GM (ผู้จัดการทั่วไป):** คุณสรัล อาวุทธ์มณี (SARAN AWUTMANI)
 ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์จุดเชื่อม
 📧 SARAN.AW@FAHMAI.CO.TH | 📱 064-655-7513 | ต่อ 78762

> หมายเหตุ: ในระบบไดเรกทอรีไม่มีตำแหน่ง "หัวหน้าฝ
```

### g774 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายการตลาดของแบรนด์คลื่นเสียง

**Fails:** missing any-of ['Thongchai', 'ธงชัย']; missing any-of ['Amphomsathit', 'อัมพรสถิต']

**Response:**

```
หัวหน้าฝ่ายคลื่นเสียง (KS) คือ:

**คุณธเนศ บัวทองประเสริฐ (Tanet Buathongprasert)**
- ตำแหน่ง: รองประธานฝ่ายคลื่นเสียง (VP of KluenSiang)
- อีเมล: TANET.BU@FAHMAI.CO.TH
- มือถือ: 099-185-8401
- ที่ตั้ง: FahMai Tower 11F (HQ)
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
The head of the คลื่นเสียง (Kluensiang) brand is:

**ราม ลวรรณ (Ram Lawan)** — ชื่อเล่น: จุ๊บ (Jub)
- Position: General Manager of Kluensiang
- Email: RAM.LA@FAHMAI.CO.TH
- Extension: 75965
- Location: FahMai Tower 18F
```

### g777 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Wongkhojon brand?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
The head of the **วงโคจร (Wongkhojon)** brand is:

- **กฤษ มหาแก้วใส (Kris Mahakaewsai)** — ชื่อเล่น: ขิง (Khing)
- Position: General Manager of Wongkhojon
- Email: KRIS.MA@FAHMAI.CO.TH
- Extension: 74375
- Location: FahMai Tower 7F
```

