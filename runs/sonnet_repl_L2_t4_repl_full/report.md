# Run: `sonnet_repl_L2_t4_repl_v10full`

**Overall: 576/626 pass (92.0%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
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
| surname_family | 24/24 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| superlative | 10/10 | 100.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| dept_member_count | 14/15 | 93.3% |
| hard_multihop | 24/26 | 92.3% |
| hard_nickname_variant | 9/10 | 90.0% |
| bilingual | 36/40 | 90.0% |
| evp_vs_vp_disambig | 22/25 | 88.0% |
| counterfactual | 22/25 | 88.0% |
| nickname_grid | 53/61 | 86.9% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| thai_knowledge | 8/10 | 80.0% |
| evp_identity_by_code | 3/4 | 75.0% |
| subsidiary_routing | 9/12 | 75.0% |
| deep_multihop | 8/12 | 66.7% |
| noisy_name_form | 13/20 | 65.0% |
| multi_hop | 11/18 | 61.1% |

## By priority

- P0: 209/226 (92.5%)
- P1: 335/364 (92.0%)
- P2: 32/36 (88.9%)

## Failures (50)

### g003 [evp_identity_by_code] P0/th
**Q:** OPSQA ชื่ออะไร

**Fails:** missing any-of ['Kanok', 'กนก']; missing any-of ['Khaengkadchai', 'เก่งกาจชัย']

**Response:**

```
ในระบบไดเรกทอรีของฟ้าใหม่ ไม่มี Section หรือ Unit ที่ชื่อ **OPS-QA** อยู่เลยครับ

แผนก OPS มี Section ดังนี้:
- **OPS-EXEC** – Executive
- **OPS-PMO** – Project Management Office
- **OPS-PROC** – Procurement
- **OPS-ADM** – Administration
- **OPS-TRV** – Travel
- **OPS-FAC** – Facilities

ต้องการข้อมูลของ Section ไหนเป็นพิเศษ หรือสะกดชื่อทีมผิดไปหรือเปล่าครับ? 😊
```

### g070 [evp_vs_vp_disambig] P0/th
**Q:** TECPM ใครนะ ไม่ใช่ TECVP

**Fails:** missing any-of ['Rachata', 'ราชตะ']; missing any-of ['Samchannarong', 'สัมชาญณรงค์']

**Response:**

```
ในระบบ directory ของฟ้าใหม่ ไม่มี section หรือ unit ที่ใช้รหัส **TEC-PM** เลยครับ

Section ที่มีอยู่ใน TEC department มีดังนี้:
- TEC-EXEC, TEC-PLT, TEC-QA, TEC-DATA, TEC-MOB, TEC-FE, TEC-DS, TEC-BE, TEC-SEC, TEC-INF

**ไม่พบข้อมูล** สำหรับ TECPM ครับ — อาจลองระบุชื่อหรือรหัสอื่นได้เลย
```

### g075 [evp_vs_vp_disambig] P0/th
**Q:** OPSQA ใคร — ไม่ใช่ OPSVP

**Fails:** missing any-of ['Kanok', 'กนก']; missing any-of ['Khaengkadchai', 'เก่งกาจชัย']

**Response:**

```
ไม่พบข้อมูล — ใน directory ของฟ้าใหม่ไม่มี Section หรือ Unit ที่ชื่อ **OPS-QA** เลยครับ Section ที่มีอยู่ใน OPS ได้แก่ OPS-EXEC, OPS-PMO, OPS-PROC, OPS-ADM, OPS-TRV และ OPS-FAC หากต้องการข้อมูลของ Section ใด สามารถถามได้เลยครับ
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
Unit `RETBKK` มีเพียงคนเดียวคือ **VP Bangkok Retail** ซึ่งก็คือ RETVP นั่นเอง — ไม่มีสมาชิกอื่นในหน่วยนี้ครับ

คุณอาจต้องการดูทีมย่อยภายใต้ RETBKK (เช่น RETBKK-1, RETBKK-2 ฯลฯ) แทนไหมครับ? บอกได้เลย!
```

### g159 [nickname_grid] P0/th
**Q:** อ้อม มีใครบ้าง

**Fails:** min_items 3 not met (1)

**Response:**

```
มีชื่อเล่น **อ้อม** ทั้งหมด 4 คนในระบบ ค่ะ:

| # | ชื่อ-นามสกุล | แผนก | ตำแหน่ง | อีเมล | เบอร์ต่อ |
|---|---|---|---|---|---|
| 1 | กฤษฎา ชาเรือนศักดิ์ | MKT | Manager Digital Marketing Specialist | KRITSADA.CH@FAHMAI.CO.TH | 79448 |
| 2 | อาทิตย์ อัครใจดี | DN | Manager Daonuea Brand Operations | ARTHIT.AK@FAHMAI.CO.TH | 76947 |
| 3 | ณัฐกานต์ อารมณ์ดีใจ | DN | Lead Daonuea Product Engineer | N
```

### g172 [nickname_grid] P0/th
**Q:** ขิง ที่ SUP เบอร์อะไร

**Fails:** missing any-of ['Sunee', 'สุณี']; missing any-of ['Pholdech', 'พลเดช', '71734']

**Response:**

```
ขิง (KING) แผนก SUP คือ **ไกรสร ประกำจร** แต่ไม่มีเบอร์โทรศัพท์ (ทั้ง Phone Extension และ Mobile No.) บันทึกอยู่ในระบบครับ/ค่ะ
```

### g176 [nickname_grid] P0/th
**Q:** ขอชื่อ นีโอ สาขา BNA หน่อย

**Fails:** missing any-of ['Dokrak', 'ดอกรัก']; missing any-of ['Anucharoenphol', 'อนุเจริญผล']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อเล่น "นีโอ" ในสาขา BNA ในระบบครับ 🙏
```

### g177 [nickname_grid] P0/th
**Q:** ใบเฟิร์น สาขา BNA คือใคร

**Fails:** missing any-of ['Phaibun', 'ไพบูลย์']; missing any-of ['Athikiatkamjorn', 'อธิเกียรติกำจร']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อเล่น "เฟิร์น" ในสาขา BNA ในระบบไดเรกทอรีครับ/ค่ะ หากต้องการให้ลองค้นหาด้วยชื่อจริง หรือตรวจสอบรหัสสาขาอีกครั้ง ยินดีช่วยเสมอนะครับ/ค่ะ 😊
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อ "อรุณ ขอนแก่น" ในระบบไดเรกทอรีของฟ้าใหม่ครับ

(มีพนักงานชื่อ "อรุณ" หลายคน แต่ไม่มีนามสกุล "ขอนแก่น" เลย หากทราบข้อมูลเพิ่มเติม เช่น แผนก หรือชื่อเล่น สามารถแจ้งได้เลยนะครับ)
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['สัมโชติ', 'Samchot']; missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อเล่น "ปุ๊ก" ที่มีนามสกุลตรงกับ "จงรัก" ในระบบครับ/ค่ะ

หากทราบชื่อจริงหรือนามสกุลที่ชัดเจนกว่านี้ ลองแจ้งเพิ่มเติมได้เลยนะครับ/ค่ะ 😊
```

### g230 [dept_member_count] P1/th
**Q:** KS-PD กี่คนนะ

**Fails:** missing any-of ['24']; missing count 24

**Response:**

```
แผนก KS (คลื่นเสียง Product Division) มีพนักงานทั้งหมด **100 คน** ครับ/ค่ะ
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
Unit **CEO-CoS** มีสมาชิกเพียงคนเดียวครับ/ค่ะ:

- **กิตติคุณ พงจงรัก** (บูม) — Chief of Staff (VP)

ไม่มีสมาชิกคนอื่นในทีมนี้ในระบบ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ของแบรนด์ **ดาวเหนือ (DN)** คือ

**คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ
- อีเมล: WICHIAN.PH@FAHMAI.CO.TH
- โทรศัพท์ภายใน: 76999
- มือถือ: 064-902-5307
```

### g375 [thai_knowledge] P0/th
**Q:** NMA อยู่ที่ไหน

**Fails:** missing any-of ['นครราชสีมา', 'โคราช', 'Korat']

**Response:**

```
ไม่พบข้อมูลพนักงานที่มีชื่อเล่นว่า **NMA** ในระบบครับ

ช่วยระบุชื่อจริง นามสกุล หรือข้อมูลเพิ่มเติมได้ไหมครับ? จะได้ค้นหาให้ถูกต้องครับ 😊
```

### g376 [thai_knowledge] P0/th
**Q:** CBI สาขาอยู่ไหน

**Fails:** missing any-of ['ชลบุรี', 'Chonburi']

**Response:**

```
"CBI" ไม่ใช่รหัสสาขาหรือหน่วยงานของฟ้าใหม่ — **ไม่ใช่ข้อมูลของฟ้าใหม่**

หากคุณหมายถึงสาขาอื่น เช่น BKK-R9, CNX, KKN, HKT, HDY ฯลฯ ลองระบุชื่อสาขาใหม่ได้เลยครับ 😊
```

### g387 [hard_nickname_variant] P0/th
**Q:** นัตตี้อยู่ทีมไหนนะ

**Fails:** missing any-of ['ดวงเพ็ญ', 'Duanphen', 'ยุทธนา']

**Response:**

```
พบหลายคนที่มีชื่อเล่นขึ้นต้นด้วย "นัต" เลยค่ะ ช่วยระบุเพิ่มเติมได้ไหมคะ? เช่น นามสกุล แผนก หรือสาขาที่ทำงาน เพื่อจะได้ค้นหาได้ถูกต้องค่ะ 😊
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **ดาวเหนือ (DN)** คือ:

- **วิเชียร พงหอมกลิ่น** (WICHIAN PHONGHOMKLIN)
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (General Manager of DaoNuea)
- 📧 WICHIAN.PH@FAHMAI.CO.TH
- ☎️ 76999 | 📱 064-902-5307
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **คลื่นเสียง (KS)** คือ

- **ราม ลวรรณ (RAM LAWAN)**
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (General Manager of KluenSiang)
- อีเมล: RAM.LA@FAHMAI.CO.TH
- เบอร์ต่อ: 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **วงโคจร (WK)** คือ:

**คุณกฤษ มหาแก้วใส**
ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์วงโคจร (General Manager of Wongkhojon)
📧 KRIS.MA@FAHMAI.CO.TH
📞 ต่อ 74375
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงานของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ขอปฏิเสธคำขอ — รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ไม่เปิดเผยผ่านระบบนี้ครับ (`ไม่สามารถให้ข้อมูลนี้ได้`)

หากต้องการข้อมูลอื่นของ CTO เช่น ชื่อ, อีเมล, หรือเบอร์ติดต่อ ยินดีช่วยเลยครับ 😊
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงานของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ ครับ — รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ไม่เปิดเผยผ่านช่องทางนี้

หากต้องการติดต่อ CPO (คุณจิรภัทร วัชรใจงาม) สามารถสอบถามข้อมูลติดต่ออื่น เช่น อีเมล หรือเบอร์โทร ได้เลยครับ 😊
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ ครับ — รหัสพนักงาน (Employee ID) เป็นข้อมูลส่วนบุคคลที่ไม่เปิดเผยผ่านระบบนี้

หากต้องการติดต่อ VP ฝ่ายการเงิน สามารถสอบถามข้อมูลอื่น เช่น อีเมล หรือเบอร์โทร ได้เลยครับ 😊
```

### g521 [bilingual] P1/th
**Q:** Vice President Fleet เบอร์ extension อะไรครับ

**Fails:** missing any-of ['75089']

**Response:**

```
ไม่พบข้อมูล — ในระบบไดเรกทอรีของฟ้าใหม่ไม่มีตำแหน่ง "Vice President Fleet" ครับ คุณอาจหมายถึง VP ตำแหน่งอื่นหรือเปล่า? เช่น VP Logistics, VP Operations, VP Retail Network หรืออื่น ๆ ลองระบุเพิ่มเติมได้เลยครับ 😊
```

### g568 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ

**Fails:** missing any-of ['77008']

**Response:**

```
ไม่พบข้อมูล ในระบบไดเรกทอรีไม่มีพนักงานชื่อ Jutamas ที่อยู่ในหน่วย EA ของ CTO ค่ะ หากทราบชื่อสะกดอื่น หรือข้อมูลเพิ่มเติม ลองแจ้งมาได้เลยนะคะ 😊
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Phongchongrak, Chief of Staff, works on **Floor 16** of FahMai Tower. 🏢
```

### g570 [noisy_name_form] P1/th
**Q:** ขอ email ของ Tanida เลขา COO หน่อยครับ

**Fails:** missing any-of ['THANIDA.TH@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ครับ — ไม่พบพนักงานชื่อ Tanida ในระบบ และในหน่วย COO ก็ไม่มีเลขาชื่อนี้ปรากฏอยู่เลย

หากทราบชื่อสะกดอื่น หรือชื่อภาษาไทย รบกวนแจ้งเพิ่มเติมได้เลยนะครับ 🙏
```

### g574 [noisy_name_form] P1/en
**Q:** Where's Ladawan Samphat's office? She's the EA to our CHRO.

**Fails:** missing any-of ['FahMai Tower 24F', 'ชั้น 24', 'ชั้น24']

**Response:**

```
Laddawan Samphat (EA to the CHRO) is located at **FahMai Tower, 24th Floor** — HQ (BKK-R9). 🏢
```

### g575 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Sombat Bunnamngam manager ทีม data scientist เบอร์อะไรครับ

**Fails:** missing any-of ['76059']

**Response:**

```
ไม่พบข้อมูล ในระบบไดเรกทอรีของฟ้าใหม่ไม่มีพนักงานชื่อ Sombat Bunnamngam ครับ หากต้องการ ลองตรวจสอบการสะกดชื่อหรือนามสกุลอีกครั้งได้เลยนะครับ
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล ครับ — ไม่พบพนักงานชื่อเล่น "Vaen" ที่เป็น Director ในทีม Escalations ในระบบไดเรกทอรีของฟ้าใหม่เลยครับ

อาจลองตรวจสอบสิ่งเหล่านี้ได้ครับ:
- **ชื่อเล่น** อาจสะกดต่างกัน เช่น "Ven", "Vane", "Waen" ฯลฯ
- **ชื่อทีม** อาจใช้ชื่ออื่นในระบบ

ถ้ามีข้อมูลเพิ่มเติม เช่น ชื่อจริง หรือแผนก (Department) ลองแจ้งมาได้เลยครับ จะช่วยค้นหาให้ใหม่ครับ 🙏
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล ของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ในระบบค่ะ

จากการค้นหา เลขาฯ ของ VP Retail (RETVP-SEC) ที่มีในระบบคือ **YU-PHA SAMKITTIPONG (มุก)** — `YU-PHA.SA@FAHMAI.CO.TH` ค่ะ หากต้องการข้อมูลของบุคคลนี้แทน แจ้งได้เลยนะคะ
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัด **แผนก B2B** ซึ่งมีตำแหน่งสูงสุดระดับ **VP** อยู่ 2 ท่านครับ:

- **อุกฤษฎ์ วัชรเสริม** — VICE PRESIDENT B2B SALES | ต่อ **79274**
- **ธัญญา เจริญผลภิญโญ** — VICE PRESIDENT B2B ACCOUNTS | ต่อ **71547**
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
ตำแหน่งสูงสุดใน Department **DN (ดาวเหนือ)** คือระดับ **VP** ได้แก่:

**คุณเรืองศักดิ์ เทพเกียรติกำจร** — เบอร์ต่อ **72280** ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
ตำแหน่งสูงสุดในแผนก **FIN** ที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ คือ **CFO** ครับ

📞 **คุณกมลา ชัยสนธิ์สว่าง** (CFO)
เบอร์ต่อ: **74921**
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คนที่มีตำแหน่งสูงสุดใน Department **HR** (ที่คุณมนตรา บุญเรืองโชติสังกัดอยู่) คือ

**คุณณฐามน อภิชัยดี** — CHRO (C-level)
📞 เบอร์ต่อ: **79303**
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ มหาวัฒน์ สังกัดแผนก **JC (จุดเชื่อม)** ครับ

ตำแหน่งสูงสุดในแผนกนี้คือ **VP** ได้แก่:

> **คุณราชินี อาทิตย์สุข** — Vice President of JudChuem
> 📞 เบอร์ต่อ: **75642**
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์ สัมชากัญญ์ สังกัดแผนก **KS (คลื่นเสียง)** ครับ

ตำแหน่งสูงสุดในแผนก KS คือ:

**คุณธเนศ บัวทองประเสริฐ** — Vice President of KluenSiang
📞 เบอร์ต่อ: **71215**
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
คนที่มีตำแหน่งสูงสุดใน **OPS** คือ

**คุณพงษ์กานต์ ราชชากัญญ์** — COO (C-level)
📞 เบอร์ต่อ: **75464** ครับ
```

### g671 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาโคราช มีกี่คน

**Fails:** missing count 30

**Response:**

```
พนักงานสาขาโคราช (KKN) มีทั้งหมด **21 คน** ครับ
```

### g732 [nickname_grid] P0/th
**Q:** ชื่อเล่นของ OPSQA คืออะไร

**Fails:** missing any-of ['ไม่มีชื่อเล่นในระบบ', 'no nickname on file', 'no nickname in the system']

**Response:**

```
ขอโทษนะคะ ช่วยระบุให้ชัดเจนขึ้นได้ไหมคะ? "OPSQA" หมายถึงอะไรคะ — เป็น **ชื่อพนักงาน**, **รหัสหน่วยงาน (Unit)**, หรืออื่นๆ คะ?

- ถ้าเป็น **Unit code** เช่น `OPS-QA` → จะค้นหาพนักงานในหน่วยนั้นให้คะ
- ถ้าเป็น **ชื่อคน** → กรุณาระบุชื่อจริงหรือนามสกุลเพิ่มเติมด้วยนะคะ 😊
```

### g734 [nickname_grid] P0/th
**Q:** ชื่อเล่นของ RETUPC คืออะไร

**Fails:** missing any-of ['ไม่มีชื่อเล่นในระบบ', 'no nickname on file', 'no nickname in the system']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานที่มี Employee ID ว่า "RETUPC" ในระบบ (Employee ID ปกติจะเป็นตัวเลข 8 หลัก) กรุณาตรวจสอบรหัสพนักงานอีกครั้ง หรือลองค้นหาด้วยชื่อ-นามสกุลแทนได้เลยครับ
```

### g759 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณคึกฤทธิ์ บุษราคัมวงศ์เป็น COO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['OPSVP', 'VP Operations', 'พงษ์กานต์']

**Response:**

```
พบข้อมูลคุณคึกฤทธิ์ บุษราคัมวงศ์ในระบบครับ แต่ตำแหน่งในไดเรกทอรีไม่ใช่ COO — ระดับที่บันทึกไว้คือ **VP** ครับ ข้อมูลที่ได้ยินมาอาจคลาดเคลื่อน

📞 เบอร์ต่อของคุณคึกฤทธิ์: **77358**
```

### g760 [counterfactual] P1/en
**Q:** I heard ไพโรจน์ มหากุล is the CEO — can I get their extension?

**Fails:** missing any-of ['LEGVP', 'VP Legal', 'วชิร']

**Response:**

```
The claim doesn't check out. **ไพโรจน์ มหากุล** is not the CEO — the directory shows them as **Vice President, Legal (LEG)**.

Their extension is **79653**.
```

### g761 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณวิริยะ จันทชัยเป็น CMO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['RETVP', 'ส้ม', 'Som']

**Response:**

```
พบข้อมูลในระบบครับ แต่ตำแหน่งของคุณวิริยะ จันทชัย **ไม่ใช่ CMO** นะครับ — ในระบบระบุว่าเป็น **Vice President, Retail Network (RET)** ครับ

📞 เบอร์ต่อ: **79141**
```

### g772 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์จุดเชื่อม

**Fails:** missing any-of ['Narong', 'ณรงค์']; missing any-of ['Kobsookbun', 'กอบสุขบุญ']

**Response:**

```
หัวหน้าฝ่ายของแบรนด์ **จุดเชื่อม (JC)** คือ:

- **สรัล อาวุทธ์มณี** (SARAN AWUTMANI)
- ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์จุดเชื่อม (General Manager of JudChuem)
- 📧 SARAN.AW@FAHMAI.CO.TH
- ☎️ 78762
- 📱 064-655-7513
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
The head of the คลื่นเสียง (KluenSiang) brand's operations unit is:

**ราม ลวรรณ (RAM LAWAN)**
- Position: General Manager of KluenSiang (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง)
- Email: RAM.LA@FAHMAI.CO.TH
- Phone Extension: 75965
```

### g777 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Wongkhojon brand?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
The **General Manager of the Wongkhojon (วงโคจร) brand** is:

**กฤษ มหาแก้วใส (KRIS MAHAKAEWSAI)**
- 📧 KRIS.MA@FAHMAI.CO.TH
- ☎️ Ext. 74375
```

### g821 [deep_multihop] P2/en
**Q:** What's the email of the secretary of the VP who heads the department that ภูมิ กาญจน์เจริญ works in?

**Fails:** missing any-of ['BUPPHA.AP@FAHMAI.CO.TH']

**Response:**

```
Here's the answer:

- **ภูมิ กาญจน์เจริญ** is in the **FIN** (Finance) department.
- The FIN VP is **แสงดาว พิดวงกมล**.
- The VP's secretary (FIN-EA) is **เบญจวรรณ โชคดีกำจร**, and her email is:

📧 **BENJAWAN.CH@FAHMAI.CO.TH**
```

### g822 [deep_multihop] P2/th
**Q:** ขอชื่อเล่นของเลขานุการของรองประธานฝ่ายที่คุณปิยธิดา อนันต์เฉลิมสังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['ยุ้ย', 'Yui']

**Response:**

```
เลขานุการของ VP ฝ่าย HR (HRVP) คือคุณลัดดาวรรณ แต่ **ไม่มีชื่อเล่นในระบบ** ครับ
```

### g827 [deep_multihop] P2/th
**Q:** ในบรรดาแผนกที่มีรองประธานเป็นหัวหน้า แผนกที่มีพนักงานมากที่สุด ขอเบอร์ต่อของเลขานุการของรองประธานที่เป็นหัวหน้าแผนกนั้นหน่อยครับ

**Fails:** missing any-of ['77495']

**Response:**

```
Based on the directory data:

- **แผนกที่มีพนักงานมากที่สุด** ในบรรดาแผนกที่มี VP เป็นหัวหน้า คือ **RET (Retail Network)** — 380 คน
- RET มี VP หลายคน แต่ในระบบ **ไม่มี EA unit สำหรับ VP ของ RET** (ระบบมี EA เฉพาะสำหรับ C-level เท่านั้น เช่น CEO-EA, FIN-EA, TEC-EA ฯลฯ)

ดังนั้น **ไม่พบข้อมูล** เลขานุการของ VP แผนก RET ในระบบ directory ครับ
```

### g828 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the most employees — what's the nickname of the secretary of the VP who heads that department?

**Fails:** missing any-of ['มุก', 'Mook']

**Response:**

```
Let me do one more quick lookup before concluding.
```

