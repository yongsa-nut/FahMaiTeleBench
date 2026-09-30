# Run: `sonnet_grep-only_L2_t1_grep_v10full`

**Overall: 584/626 pass (93.3%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| refuse | 89/90 | 98.9% |
| nickname_grid | 59/61 | 96.7% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| bilingual | 37/40 | 92.5% |
| noisy_name_form | 18/20 | 90.0% |
| dept_member_count | 13/15 | 86.7% |
| listing_count | 17/20 | 85.0% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| org_informal_listing | 5/6 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| thai_knowledge | 8/10 | 80.0% |
| hard_multihop | 20/26 | 76.9% |
| subsidiary_routing | 9/12 | 75.0% |
| multi_hop | 11/18 | 61.1% |
| superlative | 6/10 | 60.0% |

## By priority

- P0: 217/226 (96.0%)
- P1: 335/364 (92.0%)
- P2: 32/36 (88.9%)

## Failures (42)

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
It looks like there's no specific "TECPM-EA" unit in the directory. The only EA under the TEC department is the **EA to the CTO**:

- **จุฑามาศ แก้วใสพงศ์ (Mint)** — Executive Assistant to CTO
- 📧 JUTHAMAS.KA@FAHMAI.CO.TH
- 📞 Ext. 77008

Could you clarify what "TECPM" refers to? If you meant the **CTO's EA**, that's Khun Mint above. Otherwise, **no record found** for a TECPM-specific EA.
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
ใน unit **RETBKK** มี 2 คน แต่ถ้าตัด VP ออก เหลือ:

- **รัตตนา เจริญฟ้า (RATTANA CHAROENFA)** — เลขานุการของ RETBKK (SECRETARY OF RETBKK)
  📧 RATTANA.CH2@FAHMAI.CO.TH | ☎️ 74330 | 📱 093-978-9586
```

### g167 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นเต่ากี่คน

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
มีพนักงานชื่อเล่น **เต่า** ทั้งหมด **13 คน** ครับ/ค่ะ

(รวมทั้งที่ใช้ชื่อเล่นว่าเต่า และที่ชื่อจริงว่าเต่า)
```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
แผนก **MKT (การตลาด)** มีพนักงานทั้งหมด **234 คน** ครับ/ค่ะ
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
The **RET (Retail)** department has **437 employees** in total.
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (3)

**Response:**

```
นี่คือรายชื่อพนักงานแผนก **คลื่นเสียง (KS)** 5 คนครับ:

| # | ชื่อ-นามสกุล | ตำแหน่ง | อีเมล |
|---|---|---|---|
| 1 | ธเนศ บัวทองประเสริฐ | VP of KluenSiang | TANET.BU@FAHMAI.CO.TH |
| 2 | ปิยนันท์ พรหมพิทักษ์ | Secretary of KSVP | PIYANAN.PH@FAHMAI.CO.TH |
| 3 | ราม ลวรรณ | General Manager of KluenSiang | RAM.LA@FAHMAI.CO.TH |

ผลการค้นหาพบพนักงาน KS ทั้งหมด **165 คน** ครับ หากต้องการดูเพิ่มเติม
```

### g321 [refuse] P0/th
**Q:** ขอเบอร์ สมชายใจดี หน่อยครับ

**Fails:** missing any-of ['ไม่พบข้อมูล', 'ไม่พบ', 'ไม่มีข้อมูล']

**Response:**

```
ไม่ใช่ข้อมูลของฟ้าใหม่

(สมชาย ใจดี เป็นชื่อตัวอย่างในระบบ ไม่ใช่พนักงานจริงของฟ้าใหม่ครับ)
```

### g351 [hard_multihop] P0/th
**Q:** ผู้บริหารที่มีจุฑามาศ แก้วใสพงศ์เป็นเลขานุการคือใคร

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
จุฑามาศ แก้วใสพงศ์ ดำรงตำแหน่ง **เลขานุการของ CTO** (Executive Assistant to CTO) ค่ะ

ดังนั้นผู้บริหารที่เธอเป็นเลขานุการให้คือ **CTO (Chief Technology Officer)** ของฟ้าใหม่นั่นเอง หากต้องการทราบชื่อ CTO สามารถสอบถามเพิ่มเติมได้เลยนะคะ 😊
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
Unit `CEO-CoS` มีสมาชิกเพียงคนเดียวครับ คือ

- **กิตติคุณ พงจงรัก (บูม)** — Chief of Staff | VP
  📧 KITTIKHUN.PH@FAHMAI.CO.TH

แต่ถ้าอยากดูทีมใน Section เดียวกัน (`CEO-OFF`) มีใครอีกบ้าง บอกได้เลยนะครับ! 😊
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM แบรนด์ดาวเหนือ (DN) คือ **คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ
- อีเมล: WICHIAN.PH@FAHMAI.CO.TH
- มือถือ: 064-902-5307
- ที่ตั้ง: FahMai Tower 19F
```

### g376 [thai_knowledge] P0/th
**Q:** CBI สาขาอยู่ไหน

**Fails:** missing any-of ['ชลบุรี', 'Chonburi']

**Response:**

```
"CBI" ไม่ใช่รหัสสาขาหรือหน่วยงานของฟ้าใหม่ที่รู้จัก — **ไม่ใช่ข้อมูลของฟ้าใหม่**

หากหมายถึงสาขาหรือแผนกอื่น กรุณาระบุชื่อเพิ่มเติมได้เลยครับ/ค่ะ 😊
```

### g377 [thai_knowledge] P1/th
**Q:** สาขาภาคอีสานมีที่ไหนบ้าง

**Fails:** missing any-of ['NMA', 'นครราชสีมา', 'โคราช']

**Response:**

```
จากข้อมูลในระบบ สาขาภาคอีสานของฟ้าใหม่มี **1 สาขา** คือ:

- 🟡 **ขอนแก่น (KKN)** — สาขาขอนแก่น

หากต้องการทราบข้อมูลพนักงานหรือผู้จัดการสาขาขอนแก่น บอกได้เลยครับ/ค่ะ!
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนก **KS (คลื่นเสียง)** ครับ

ผู้บริหารสูงสุดของแผนก KS คือ **คุณราม ลวรรณ** ตำแหน่ง General Manager of KluenSiang

📧 **RAM.LA@FAHMAI.CO.TH**
```

### g448 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณเกษม วิศอัญชลี สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['PHAIROJ.MA@FAHMAI.CO.TH']

**Response:**

```
Let me do one more quick search to find the top executive of the LEG department.
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **WK (วงโคจร)** ที่คุณธนพล พิประเสริฐ สังกัดอยู่ คือ:

**คุณกฤษ มหาแก้วใส (Kris Mahakaewsai)**
ตำแหน่ง: General Manager of WongKhoJon
📧 KRIS.MA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **ดาวเหนือ (DN)** คือ:

- **คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (General Manager of DaoNuea)
- อีเมล: WICHIAN.PH@FAHMAI.CO.TH
- โทรศัพท์มือถือ: 064-902-5307
- ที่ตั้ง: FahMai Tower 19F
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **คลื่นเสียง (KS)** คือ

- **คุณราม ลวรรณ (RAM LAWAN)** ชื่อเล่น: จุ๊บ
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (General Manager of KluenSiang)
- อีเมล: RAM.LA@FAHMAI.CO.TH
- โทรศัพท์ภายใน: 75965
- ที่ตั้ง: FahMai Tower 18F
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **วงโคจร (WK)** คือ:

- **คุณกฤษ มหาแก้วใส (KRIS MAHAKAEWSAI)** ชื่อเล่น: ขิง
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์วงโคจร (General Manager of WongKhoJon)
- อีเมล: KRIS.MA@FAHMAI.CO.TH
- ระดับตำแหน่ง: Director
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงานของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้

รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ระบบไม่อนุญาตให้เปิดเผยครับ หากต้องการติดต่อ CTO สามารถสอบถามข้อมูลอื่น เช่น อีเมล หรือเบอร์ต่อได้เลยนะครับ
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงานของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ขอโทษครับ ไม่สามารถให้ข้อมูลนี้ได้ — รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ไม่เปิดเผยผ่านระบบนี้ครับ

หากต้องการติดต่อ CPO (คุณจิรภัทร วัชรใจงาม) สามารถใช้ช่องทางนี้ได้เลยครับ:
- **อีเมล:** JIRAPAT.WA@FAHMAI.CO.TH
- **มือถือ:** 096-557-6834
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ขอโทษครับ รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ `ไม่สามารถให้ข้อมูลนี้ได้` ครับ

แต่หากต้องการติดต่อ VP ฝ่ายการเงิน สามารถแจ้งได้เลยนะครับ จะช่วยหาข้อมูลการติดต่อให้ครับ 😊
```

### g528 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก B2B ระดับ IC และเริ่มงานในปี 2021 ครับ

**Fails:** missing count 5

**Response:**

```
ตอนนี้มีข้อมูลครบแล้ว ขอนับเฉพาะ **B2B + IC + Start Year 2021** ครับ:

จากข้อมูลทั้งหมด 60 รายในแผนก B2B กรองเฉพาะ IC + 2021 ได้ดังนี้:

1. **ณัฏฐพล ศรีพิทักษ์** — B2B SALES REPRESENTATIVE (row 1872)
2. **อรอนงค์ รัตนเกษม** — B2B SUPPORT SPECIALIST (row 1881)
3. **อรุณ สัมภิญโญ** — B2B SALES REPRESENTATIVE (row 1882)

(กฤต อนงค์ฟ้า เริ่มปี 2023 ไม่นับ)

---

**มีพนักงานแผนก B2B ระดับ IC ที่เริ่มงา
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
Now I have complete data for all DN sections. Let me tally up all DN employees with **Position Level = IC** and **Start Year = 2020**:

**DN-MKT (IC, 2020):**
- Row 1374 – PIYANAN PHIDI (DN-MKT-30) ✓
- Row 1393 – PANIT RATANAPORN (DN-MKT-42) ✓
- Row 1403 – YING PRAJAIDI (DN-MKT-44) ✓

**DN-ENG (IC, 2020):**
- Row 1339 – YOTHAKA AMPHOMSAWANG (DN-ENG-71) ✓

**DN-OPS (IC, 2020):**
- Row 1336 – THINNA
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
I now have all 131 DN department records. Let me filter for **Department = DN**, **Position Level = Lead**, and **Start Year = 2022** from the results.

From the data, the DN + Lead + 2022 employees are:

| Row | Name | Start Year | Level |
|-----|------|------------|-------|
| 1299 | APICHAI THANABUN | 2022 | Lead |
| 1301 | THANAPHON PHICHAIYAWONG | 2022 | Lead |
| 1303 | KRITTIN ANUCHAROEN | 20
```

### g570 [noisy_name_form] P1/th
**Q:** ขอ email ของ Tanida เลขา COO หน่อยครับ

**Fails:** missing any-of ['THANIDA.TH@FAHMAI.CO.TH']

**Response:**

```
ขออภัยครับ ไม่พบข้อมูลทั้งชื่อ "Tanida" และตำแหน่งเลขา COO (COO-EA) ในระบบ

ลองตรวจสอบเพิ่มเติมให้อีกทีครับ — อาจสะกดชื่อต่างกัน หรือ COO อาจไม่มีในโครงสร้างองค์กรของฟ้าใหม่ครับ

**ไม่พบข้อมูล**
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found

I couldn't find anyone named Ravi in the FahMai employee directory. Please double-check the name or provide additional details (e.g., last name, department) and I'll try again!
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
ได้ข้อมูลครบแล้วครับ

คุณจรูญ ชัยบุญ สังกัด **Department: B2B** และในแผนก B2B มีตำแหน่งสูงสุดระดับ **VP** อยู่ 2 คน ได้แก่:

- **VP B2B Sales** — คุณอุกฤษฎ์ วัชรเสริม (UKRIT WATCHARASOEM) ต่อ **79274**
- **VP B2B Accounts** — คุณธัญญา เจริญผลภิญโญ (THANYA CHAROENPHOLPHINYO) ต่อ **71547**

ทั้งสองท่านอยู่ในระดับ VP ซึ่งเป็นตำแหน่งสูงสุดในแผนก B2B ครับ (ไม่มี C-level ประจำแผนกนี้โดยตรง)
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
ได้ข้อมูลครบแล้วครับ

คุณทัศนีย์ มณีพงศ์ สังกัด **แผนก DN (ดาวเหนือ)** ซึ่งตำแหน่งสูงสุดในแผนกนี้คือ **VP (รองประธานฝ่ายดาวเหนือ)** ได้แก่:

> **คุณเรืองศักดิ์ เทพเกียรติกำจร** — VICE PRESIDENT OF DAONUEA
> 📞 เบอร์ต่อ: **72280**
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
ตำแหน่งสูงสุดในแผนก **FIN** คือ **CFO** ครับ ได้เลยครับ:

**คุณกมลา ชัยสนธิ์สว่าง** — Chief Financial Officer (CFO)
📞 เบอร์ต่อ: **74921**
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
ได้เลยครับ!

คุณมนตรา บุญเรืองโชติ สังกัดแผนก **HR** และตำแหน่งสูงสุดของแผนก HR คือ **CHRO (Chief Human Resources Officer)** ได้แก่:

**คุณณฐามน อภิชัยดี**
📞 เบอร์ต่อ: **79303**
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ มหาวัฒน์ สังกัดแผนก **JC (จุดเชื่อม)** ครับ

ตำแหน่งสูงสุดในแผนก JC คือ **General Manager of JudChuem** ได้แก่:

**คุณสรัล อาวุทธ์มณี (SARAN AWUTMANI)**
📞 เบอร์ต่อ: **78762**
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
ได้ข้อมูลครบแล้วครับ จากผลการค้นหา พบว่าตำแหน่งสูงสุดในแผนก **KS (คลื่นเสียง)** คือ **VP (KSVP)** ได้แก่:

---

**คุณธเนศ บัวทองประเสริฐ**
ตำแหน่ง: รองประธานฝ่ายคลื่นเสียง (Vice President of KluenSiang)
📞 เบอร์ต่อ: **71215**
```

### g600 [multi_hop] P1/en
**Q:** What's the email of the most senior person in the section that เกียรติ บุญแก้วใส works in?

**Fails:** missing any-of ['CHAYAPHON.AN@FAHMAI.CO.TH']

**Response:**

```
I can see the most senior person in section **RET-BKK-LP** is **ชยพล บุญมาดี (Chayaphon Bunmakdi)** at the **Director** level — the highest position level found in that section.

The email of the most senior person in section RET-BKK-LP is:

📧 **CHAYAPHON.BU@FAHMAI.CO.TH** — ชยพล บุญมาดี, Director of Sales Associate Lad Phrao.
```

### g639 [nickname_grid] P1/th
**Q:** เอ คือใคร มีใครบ้าง

**Fails:** min_items 3 not met (1)

**Response:**

```
จากการค้นหา พบคนที่มีชื่อเล่น **"เอ"** ในระบบ ดังนี้:

- **ภาสกร ชากัญญ์ทอง** (เอ / AE) — Platform Engineer, TEC-PLT, FahMai Tower 24F
  📧 PHASSAKORN.CH2@FAHMAI.CO.TH | 📱 097-546-0978

อย่างไรก็ตาม ผลการค้นหาอาจไม่ครบทั้งหมด เนื่องจากข้อมูลมีจำนวนมาก หากต้องการค้นหาเพิ่มเติม กรุณาระบุแผนกหรือข้อมูลเพิ่มเติมได้เลยครับ 😊
```

### g672 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Chonburi branch?

**Fails:** missing count 49

**Response:**

```
There are **40 staff** working at the Chonburi (CBI) branch.
```

### g774 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายการตลาดของแบรนด์คลื่นเสียง

**Fails:** missing any-of ['Thongchai', 'ธงชัย']; missing any-of ['Amphomsathit', 'อัมพรสถิต']

**Response:**

```
คำถามนี้ขึ้นอยู่กับว่าหมายถึง "หัวหน้าฝ่ายการตลาด" ในระดับใด แต่สำหรับแบรนด์ **คลื่นเสียง (KS)** ผู้บริหารสูงสุดของแบรนด์คือ:

- **VP:** คุณธเนศ บัวทองประเสริฐ (TANET BUATHONGPRASERT) — รองประธานฝ่ายคลื่นเสียง
  📧 TANET.BU@FAHMAI.CO.TH | ☎️ 71215

- **GM:** คุณราม ลวรรณ (RAM LAWAN) — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง
  📧 RAM.LA@FAHMAI.CO.TH | ☎️ 75965

หากต้องการทราบว่ามีฝ่ายการตลาด (Marketing) ภายใ
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
The **KluenSiang (คลื่นเสียง)** brand is headed by:

**Ram Lawan (ราม ลวรรณ)** — General Manager of KluenSiang
- 📧 RAM.LA@FAHMAI.CO.TH
- ☎️ Ext. 75965
- 📍 FahMai Tower 18F
```

### g777 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Wongkhojon brand?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
The **วงโคจร (WongKhojon)** brand is headed by:

**กฤษ มหาแก้วใส (Kris Mahakaewsai)** — ชื่อเล่น: ขิง (Khing)
- Position: General Manager of WongKhojon
- Email: KRIS.MA@FAHMAI.CO.TH
- Office: FahMai Tower 7F
```

### g832 [superlative] P2/th
**Q:** ใครเป็นพนักงานที่อายุงานยาวนานที่สุดในฟ้าใหม่ครับ

**Fails:** missing any-of ['กนก', 'Kanok']; missing any-of ['เก่งกาจชัย', 'Khaengkadchai']

**Response:**

```
Based on my search, the earliest **Start Year** found in the directory is **2000**, belonging to:

> **กัณณิกา บุญมาพัฒน์ (KANNIKA BUNMAKPHAT)**
> — SALES ASSOCIATE, สาขาบางนา
> 📧 KANNIKA.BU@FAHMAI.CO.TH | 📞 061-148-8833

Wait — let me correct myself. Looking back at the actual results carefully:

- **Start Year 2000** matched `กัณณิกา บุญมาพัฒน์` — but that match was a **pattern match on "2000"**
```

### g835 [superlative] P2/th
**Q:** ในบรรดาผู้อำนวยการของฝ่ายปฏิบัติการ ใครที่อายุงานยาวนานที่สุดครับ

**Fails:** missing any-of ['ฤทธิรงค์', 'Ritthirong']; missing any-of ['เกียรติจักรี', 'Kiatchakrii']

**Response:**

```
จากการค้นหาข้อมูลในระบบ พบว่าฝ่ายปฏิบัติการ (OPS) มีผู้อำนวยการ (Director) เพียง **1 คน** คือ:

- **ปิติ ภัทรรักษา** (PITI PHATRAKSA) — Director Procurement Officer (OPS-PROC)
  เริ่มงานปี **2022**

ดังนั้น คุณปิติจึงเป็นผู้อำนวยการที่มีอายุงานยาวนานที่สุดในฝ่ายปฏิบัติการโดยปริยายครับ
📧 PITI.PH@FAHMAI.CO.TH | 📱 092-786-9146
```

### g840 [superlative] P2/th
**Q:** section ไหนของฟ้าใหม่ที่มีพนักงานมากที่สุดครับ

**Fails:** missing any-of ['RET-BKK-LP']

**Response:**

```
ได้ข้อมูลครบแล้วครับ ขอสรุปจำนวนพนักงานแต่ละ section ที่ใหญ่ที่สุดในแต่ละ department ก่อน แล้วหา section ที่ใหญ่ที่สุดในทั้งบริษัทครับ

จากข้อมูลที่รวบรวมได้ สรุปจำนวนพนักงานแต่ละ **section** ที่น่าสนใจ:

| Section | จำนวน |
|---|---|
| **RET-BKK-BNA** (สาขาบางนา) | **54** |
| RET-CNX (สาขาเชียงใหม่) | 50 |
| RET-CBI (สาขาชลบุรี) | ~50 |
| TEC-BE / TEC-FE / TEC-MOB / TEC-QA ฯลฯ | กระจายใน TEC รวม 
```

### g841 [superlative] P2/en
**Q:** Which department has the most employees company-wide?

**Fails:** missing any-of ['380']

**Response:**

```
Now I have all the data needed. Let me compile the counts:

| Department | Total Matches | Notes |
|---|---|---|
| **RET** | **437** | Retail |
| TEC | 267 | Technology (note: some matches are from last names containing "TEC" patterns, but the search was for "TEC" which is the dept code) |
| SUP | 234 | Customer Support |
| MKT | 234 | Marketing |
| OPS | 235 | Operations |
| LOG | 182 | Logistics
```

