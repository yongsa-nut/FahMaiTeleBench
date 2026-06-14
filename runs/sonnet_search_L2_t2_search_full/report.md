# Run: `sonnet_search_L2_t2_search_full`

**Overall: 592/626 pass (94.6%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
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
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| nickname_grid | 59/61 | 96.7% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| bilingual | 38/40 | 95.0% |
| hard_implicit_hierarchy | 18/19 | 94.7% |
| hard_multihop | 24/26 | 92.3% |
| listing_count | 18/20 | 90.0% |
| dept_listing_small | 6/7 | 85.7% |
| enterprise_shorthand | 17/20 | 85.0% |
| subsidiary_routing | 10/12 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| multi_hop | 11/18 | 61.1% |
| noisy_name_form | 10/20 | 50.0% |

## By priority

- P0: 220/226 (97.3%)
- P1: 336/364 (92.3%)
- P2: 36/36 (100.0%)

## Failures (34)

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
The **TEC-EA** is assigned to the CTO, not specifically to TECPM (VP Platform). There is no separate EA record tied directly to the TECPM unit.

The TEC department's EA is:

- **จุฑามาศ แก้วใสพงศ์ (Mint)** — Executive Assistant to CTO
  - 📧 JUTHAMAS.KA@FAHMAI.CO.TH
  - 📱 095-228-0338
  - ☎️ 77008

If you need to reach the VP Platform directly:
- **ราชตะ สัมชาญณรงค์** — VP Platform (TECPM)
  - 📧 RA
```

### g071 [evp_vs_vp_disambig] P0/en
**Q:** MKTDG not MKTVP, who is it

**Fails:** has forbidden 'Kwang'; has forbidden 'คะวัง'; has forbidden 'Kobsookrat'; has forbidden 'กอบสุขรัตน์'

**Response:**

```
Here's the distinction:

- **MKTDG** (VP Digital Marketing) → **สมพงษ์ กอบสุขประเสริฐ (SOMPHONG KOBSOOKPRASERT)** 📧 SOMPHONG.KO@FAHMAI.CO.TH | 📱 085-184-8742
- **MKTVP** (VP Marketing) → คะวัง กอบสุขรัตน์ (KWANG KOBSOOKRAT / ชื่อเล่น: โอ) — คนละคนกัน
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล สำหรับ "อรุณ" ในแผนก SUP ค่ะ

อาจลองตรวจสอบชื่อสะกดอีกครั้ง หรือแจ้งข้อมูลเพิ่มเติม (เช่น นามสกุล หรือชื่อเล่น) เพื่อให้ค้นหาได้แม่นยำขึ้นนะคะ 😊
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล ในระบบไดเรกทอรีของฟ้าใหม่ไม่มีพนักงานชื่อ "อรุณ" ที่สาขาขอนแก่น (KKN) ค่ะ

หากทราบนามสกุล ชื่อเล่น หรือข้อมูลเพิ่มเติม ลองแจ้งมาได้เลยนะคะ จะได้ค้นหาให้ถูกต้องมากขึ้น 😊
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
Here's the person serving as secretary to the CEO:

**อรญา วัชรกาญจน์ (ORRAYA WATCHARAKAN)** — ชื่อเล่น: เป้ (PE)
- 📧 ORRAYA.WA@FAHMAI.CO.TH
- 🏢 FahMai Tower 7F | BKK-R9
- Position: เลขานุการของ CEO (Executive Assistant to CEO)
```

### g351 [hard_multihop] P0/th
**Q:** ผู้บริหารที่มีจุฑามาศ แก้วใสพงศ์เป็นเลขานุการคือใคร

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
จุฑามาศ แก้วใสพงศ์ (มิ้น) ดำรงตำแหน่ง **เลขานุการของ CTO** ค่ะ

ดังนั้นผู้บริหารที่เธอเป็นเลขาฯ คือ **CTO (Chief Technology Officer)** ของฟ้าใหม่นั่นเองค่ะ หากต้องการทราบว่า CTO คือใคร สามารถสอบถามเพิ่มเติมได้เลยนะคะ 😊
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ของแบรนด์ดาวเหนือคือ **คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ
- อีเมล: WICHIAN.PH@FAHMAI.CO.TH
- มือถือ: 064-902-5307
- ที่ตั้ง: FahMai Tower 19F
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **คลื่นเสียง (KS)** คือ:

- **ราม ลวรรณ (RAM LAWAN)** ชื่อเล่น: จุ๊บ
- ตำแหน่ง: General Manager of Kluensiang (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง)
- อีเมล: RAM.LA@FAHMAI.CO.TH
- ต่อโทรศัพท์: 75965
- สถานที่: FahMai Tower 18F
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงาน (employee ID) ของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ ครับ — รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ระบบไม่อนุญาตให้เปิดเผย หากต้องการติดต่อ CTO สามารถสอบถามชื่อ อีเมล หรือเบอร์โทรได้เลยครับ
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงาน (employee ID) ของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ — รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ระบบไม่อนุญาตให้เปิดเผยครับ

หากต้องการข้อมูลอื่นของ CPO เช่น ชื่อ, อีเมล, หรือเบอร์ติดต่อ ยินดีช่วยได้เลยนะครับ 😊
```

### g528 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก B2B ระดับ IC และเริ่มงานในปี 2021 ครับ

**Fails:** missing count 5

**Response:**

```
ได้ผลลัพธ์มาแล้ว ขอกรองเฉพาะปี 2021 จากข้อมูลที่ได้รับครับ

จากผลการค้นหา พนักงานแผนก **B2B** ระดับ **IC** ที่เริ่มงานในปี **2021** มีทั้งหมด **7 คน** ครับ ได้แก่:

| ชื่อ | ตำแหน่ง |
|---|---|
| ณัฏฐพล ศรีพิทักษ์ | B2B Sales Representative |
| อรอนงค์ รัตนเกษม | B2B Support Specialist |
| อรุณ สัมภิญโญ | B2B Sales Representative |
| ไพบูลย์ บุญมางาม | Solutions Engineer |
| ปิยะ ชัยอมรินทร์ | B2B
```

### g542 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ Manager และเริ่มงานในปี 2022 ครับ

**Fails:** missing count 3

**Response:**

```
จากข้อมูลในระบบ แผนก **FIN** ระดับ **Manager** ที่เริ่มงานในปี **2022** มีทั้งหมด **2 คน** ครับ ได้แก่:

1. **ชยพล จงรักบุญ (ปิ๊ง)** — MANAGER FINANCIAL ANALYST (FIN-FP)
2. **จงรัก สุวรรณรักษา** — MANAGER TAX SPECIALIST (FIN-TAX)
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
no record found — there is no employee named **Kittikhun Pongchongrak** in the FahMai directory. Please double-check the name spelling and try again.
```

### g570 [noisy_name_form] P1/th
**Q:** ขอ email ของ Tanida เลขา COO หน่อยครับ

**Fails:** missing any-of ['THANIDA.TH@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ครับ — ไม่พบชื่อ "Tanida" ในระบบ ไม่ว่าจะค้นด้วยชื่อหรือตำแหน่งเลขา COO ก็ตาม

ลองตรวจสอบการสะกดชื่ออีกครั้ง หรือแจ้งชื่อภาษาไทย/นามสกุลเพิ่มเติมได้เลยครับ 😊
```

### g572 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Sukum Suwanfahsai manager ทีม chat support หน่อยค่ะ

**Fails:** missing any-of ['SUKHUM.SU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ของคุณ Sukum Suwanfahsai ในระบบไดเรกทอรีของฟ้าใหม่ค่ะ

กรุณาตรวจสอบชื่อ-นามสกุลอีกครั้ง หรือลองค้นหาด้วยชื่อภาษาไทยได้เลยนะคะ 😊
```

### g573 [noisy_name_form] P1/en
**Q:** Can I get the extension for Viriya Chanchai, VP of Retail Network?

**Fails:** missing any-of ['79141']

**Response:**

```
no record found — I couldn't find anyone named **Viriya Chanchai** in the FahMai directory. Please double-check the spelling and try again!
```

### g574 [noisy_name_form] P1/en
**Q:** Where's Ladawan Samphat's office? She's the EA to our CHRO.

**Fails:** missing any-of ['FahMai Tower 24F', 'ชั้น 24', 'ชั้น24']

**Response:**

```
Found her! Note that her name is **Laddawan** (ลัดดาวรรณ), not "Ladawan." Here are her details:

- **Name:** ลัดดาวรรณ สัมพัฒน์ (LADDAWAN SAMPHAT)
- **Position:** Executive Assistant to CHRO
- **Office:** FahMai Tower **24F**, HQ (Rama IX)
- **Email:** LADDAWAN.SA@FAHMAI.CO.TH
```

### g575 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Sombat Bunnamngam manager ทีม data scientist เบอร์อะไรครับ

**Fails:** missing any-of ['76059']

**Response:**

```
ไม่พบข้อมูล ในระบบไดเรกทอรีของฟ้าใหม่ครับ

ลองตรวจสอบชื่อ-นามสกุลอีกครั้งได้เลยนะครับ อาจมีการสะกดผิดเล็กน้อย หรือถ้ามีข้อมูลอื่น เช่น ชื่อเล่น หรืออีเมล ก็สามารถแจ้งมาได้เลยครับ 😊
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล ครับ

ไม่พบชื่อเล่น "Vaen" ที่เป็น Director ในระบบไดเรกทอรีของฟ้าใหม่เลยครับ อาจลองตรวจสอบชื่อสะกดอีกครั้ง หรือแจ้งชื่อจริง/นามสกุลมาได้เลยครับ 😊
```

### g583 [noisy_name_form] P1/en
**Q:** Can I get the extension for Sompong, the VP of Digital Marketing?

**Fails:** missing any-of ['79901']

**Response:**

```
I'm unable to find anyone named **Sompong** in the Marketing department or at the VP level in the directory. **ไม่พบข้อมูล** — no record found for a VP of Digital Marketing by that name.

Could you double-check the name or provide any additional details (e.g., last name, nickname, or email)? I'm happy to search again!
```

### g584 [noisy_name_form] P1/en
**Q:** What's Meka's email — the Director of Accounts Receivable?

**Fails:** missing any-of ['MEKHA.PH2@FAHMAI.CO.TH']

**Response:**

```
No record found for anyone with the nickname "Meka" in the directory. It's possible the nickname is spelled differently — could you double-check the spelling or provide their full name? That way I can try again! 😊
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found — I couldn't find any Director named Ravi in the FahMai directory. It's possible the name, title, or department may be slightly different. Could you double-check the details?
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
ไม่มี C-level ในแผนก B2B ครับ ดังนั้นตำแหน่งสูงสุดในแผนกคือระดับ **VP** ซึ่งมี 2 ท่าน ได้แก่

| ชื่อ | ตำแหน่ง | เบอร์ต่อ |
|---|---|---|
| คุณอุกฤษฎ์ วัชรเสริม | VP B2B Sales | **79274** |
| คุณธัญญา เจริญผลภิญโญ | VP B2B Accounts | **71547** |

ต้องการเบอร์ต่อของท่านใดเป็นพิเศษ หรือต้องการข้อมูลเพิ่มเติมครับ?
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
ตำแหน่งสูงสุดในแผนก DN (ดาวเหนือ) คือ **VP** ครับ

---

**คุณเรืองศักดิ์ เทพเกียรติกำจร**
ตำแหน่ง: Vice President of DaoNuea
📞 เบอร์ต่อ: **72280**
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
ตำแหน่งสูงสุดในแผนก FIN คือ **CFO** ครับ

📞 **คุณกมลา ชัยสนธิ์สว่าง** (Chief Financial Officer)
- เบอร์ต่อ: **74921**
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
ตำแหน่งสูงสุดในแผนก HR คือ **CHRO** ครับ ได้เลย:

**คุณณฐามน อภิชัยดี (NATHAMON APHICHAIDEE)**
ประธานเจ้าหน้าที่ฝ่ายทรัพยากรบุคคล (CHRO)
📞 เบอร์ต่อ: **79303**
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
ตำแหน่งสูงสุดในแผนก JC (จุดเชื่อม) คือ **VP** ครับ

📞 **คุณราชินี อาทิตย์สุข**
ตำแหน่ง: รองประธานฝ่ายจุดเชื่อม (JCVP)
เบอร์ต่อ: **75642**
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
ตำแหน่งสูงสุดในแผนก KS (คลื่นเสียง) คือ **VP** ครับ

📞 **คุณธเนศ บัวทองประเสริฐ** — Vice President of Kluensiang
**เบอร์ต่อ:** 71215
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
ตำแหน่งสูงสุดในแผนก OPS คือ **COO (ประธานเจ้าหน้าที่ปฏิบัติการ)** ครับ

> **คุณพงษ์กานต์ ราชชากัญญ์** (COO)
> 📞 เบอร์ต่อ: **75464**
```

### g666 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Rama IX (R9) HQ branch?

**Fails:** missing any-of ['1255']

**Response:**

```
The directory shows **1,255 staff** are based at the Rama IX (BKK-R9) HQ branch. 🏢
```

### g682 [enterprise_shorthand] P1/th
**Q:** หัวหน้าทีมฟินฯ คือใคร

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
ในแผนก FIN มีหัวหน้าทีม (Lead) หลายคนแยกตามสายงาน ดังนี้ครับ/ค่ะ:

**Financial Planning (FIN-FP)**
- คึกฤทธิ์ จิรบุญมี — หัวหน้าทีมนักวิเคราะห์การเงิน | `KUKRIT.CH2@FAHMAI.CO.TH`
- กุหลาบ จงรักดี — หัวหน้าทีมนักวิเคราะห์การเงิน | `KULAP.CH3@FAHMAI.CO.TH`

**General Ledger (FIN-GL)**
- ไพลิน รัตนใจ (บูม) — หัวหน้าทีมนักบัญชี | `PHAILIN.RA@FAHMAI.CO.TH`
- สุเมธ เกษมรักษา — หัวหน้าทีมนักบัญชี | `SUMA
```

### g683 [enterprise_shorthand] P1/en
**Q:** Who heads the HR team?

**Fails:** missing any-of ['Nathamon', 'ณฐามน']; missing any-of ['Aphichaidee', 'อภิชัยดี']

**Response:**

```
The HR team is headed by:

**สุเมธ อัครใจงาม (SUMATE AKARAJAINGAM)** — ชื่อเล่น: สกาย (SKY)
- **Position:** Vice President, Human Resources
- **Email:** SUMATE.AK@FAHMAI.CO.TH
- **Extension:** 72146
- **Location:** FahMai Tower 22F
```

### g775 [subsidiary_routing] P1/en
**Q:** The Kluensiang brand is an in-house FahMai division — who heads its operations unit?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
The head of the **คลื่นเสียง (KluenSiang / KS)** division is:

- **ธเนศ บัวทองประเสริฐ (TANET BUATHONGPRASERT)**
- Position: Vice President of KluenSiang (รองประธานฝ่ายคลื่นเสียง)
- 📧 TANET.BU@FAHMAI.CO.TH
- 📱 099-185-8401
- 📍 FahMai Tower 11F, HQ (BKK-R9)
```

### g777 [subsidiary_routing] P1/en
**Q:** The Wongkhojon brand is an in-house FahMai division — who heads its operations unit?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
The **วงโคจร (WongKhoJon / WK)** division has two key leaders at the top:

- **VP:** คึกฤทธิ์ อัครเจริญ (KUKRIT AKARACHAROEN) — รองประธานฝ่ายวงโคจร
  📧 KUKRIT.AK@FAHMAI.CO.TH | 📱 097-302-2863

- **General Manager:** กฤษ มหาแก้วใส (KRIS MAHAKAEWSAI) — ผู้จัดการทั่วไปแบรนด์วงโคจร
  📧 KRIS.MA@FAHMAI.CO.TH

The VP **คุณคึกฤทธิ์** heads the division at the VP level, with **คุณกฤษ** serving as GM overse
```

