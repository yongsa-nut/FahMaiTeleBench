# Run: `deepseekv4pro_both_L2_t3_both_v10full`

**Overall: 597/626 pass (95.4%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
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
| email_identity_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| bilingual | 40/40 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| refuse | 89/90 | 98.9% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| nickname_grid | 58/61 | 95.1% |
| name_lookup | 19/20 | 95.0% |
| listing_count | 19/20 | 95.0% |
| noisy_name_form | 19/20 | 95.0% |
| multi_hop | 17/18 | 94.4% |
| retrieval | 13/14 | 92.9% |
| hard_multihop | 24/26 | 92.3% |
| hard_nickname_variant | 9/10 | 90.0% |
| superlative | 9/10 | 90.0% |
| dept_listing_small | 6/7 | 85.7% |
| email_mobile_lookup | 6/7 | 85.7% |
| enterprise_shorthand | 17/20 | 85.0% |
| hard_bridge_lookup | 5/6 | 83.3% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| subsidiary_routing | 7/12 | 58.3% |

## By priority

- P0: 219/226 (96.9%)
- P1: 344/364 (94.5%)
- P2: 34/36 (94.4%)

## Failures (29)

### g080 [evp_vs_vp_disambig] P0/th
**Q:** หา FIN-ACCDR หน่อย อย่าสับกับ FINVP

**Fails:** has forbidden 'แสงดาว'; has forbidden 'พิดวงกมล'

**Response:**

```
**FIN-ACCDR** — Director ฝ่ายบัญชี:

- **คุณบุษบา อัครพัฒน์** (BUSABA AKARAPHAT)
- 📧 BUSABA.AK@FAHMAI.CO.TH
- 📞 เบอร์ต่อ: 77404
- 🏢 FahMai Tower ชั้น 6

*(ส่วน FINVP คือ คุณมอคค่า — แสงดาว พิดวงกมล — VP Finance อยู่อีกคนละตำแหน่งกันเลยครับ)*
```

### g128 [name_lookup] P1/th
**Q:** กานติมา การเวกประเสริฐ เบอร์อะไร

**Fails:** missing any-of ['78422', 'KANTIMA.KA', '095-932-5295']

**Response:**

```

```

### g183 [nickname_grid] P0/th
**Q:** ชื่อเล่น CMO คืออะไร

**Fails:** has ext pattern

**Response:**

```
CMO คือ **คุณส้ม กาญจน์สถิต** (SOM KANSATHIT) — **ไม่มีชื่อเล่นในระบบ** ครับ

ติดต่อได้ที่ SOM.KA@FAHMAI.CO.TH หรือเบอร์ภายใน 79005 ครับ
```

### g192 [nickname_grid] P0/th
**Q:** ขอเบอร์พี่มุกกี้

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
มี "มุก" หลายคนครับ ขอข้อมูลเพิ่มนิดนึงว่า **พี่มุกกี้** ที่หมายถึงอยู่แผนกไหนหรือทำตำแหน่งอะไรครับ จะได้ระบุตัวให้ถูก — ตอนนี้มี 13 คนที่ชื่อเล่น "มุก" ทั้งบริษัทครับ
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
There's no `CEO-SEC` unit — but the role you're looking for is **CEO-EA** (Executive Assistant to CEO):

**อรญา วัชรกาญจน์ (Orraya Watcharakan)** — Nickname: เป้ (Pe)
- 📧 ORRAYA.WA@FAHMAI.CO.TH
- 📞 Ext: 75665
- 📍 FahMai Tower 7F
- ระดับ: Manager
```

### g297 [email_mobile_lookup] P2/en
**Q:** 098-738-1431 — who?

**Fails:** missing any-of ['Akarajaidi', 'อัครใจดี']

**Response:**

```
**Arthit Akarajaiidi (Aom)** — Manager, DaoNuea Brand Operations (DN-OPS)

- 📞 098-738-1431
- ✉️ ARTHIT.AK@FAHMAI.CO.TH
- 🔢 Ext. 76947
- 📍 FahMai Tower 18F, HQ (BKK-R9)
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
**GM แบรนด์ดาวเหนือ:** คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)

- **ตำแหน่ง:** ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (GENERAL MANAGER OF DAONUEA)
- **อีเมล:** WICHIAN.PH@FAHMAI.CO.TH
- **เบอร์ต่อ:** 76999
- **มือถือ:** 064-902-5307
- **ที่ตั้ง:** FahMai Tower ชั้น 19F
```

### g363 [hard_bridge_lookup] P0/en
**Q:** who manages the SaiFah brand

**Fails:** missing any-of ['Boonnamphong', 'บุญนำพงศ์']

**Response:**

```
**Khun Thawan Boonnampong** — General Manager of SaiFah (ผู้จัดการทั่วไปแบรนด์สายฟ้า)

- 📧 THAWAN.BO@FAHMAI.CO.TH
- 📞 Ext 79517 | Mobile 083-166-7588
- 📍 FahMai Tower 11F
```

### g397 [hard_nickname_variant] P0/en
**Q:** looking for ICEY in SUP

**Fails:** missing any-of ['ศศิ', 'Sasi', 'อารมณ์ดีศรี']

**Response:**

```
ไม่พบข้อมูล
```

### g404 [refuse] P1/th
**Q:** ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูล — ในระบบไม่มีพนักงานชื่อ **ถาวร จิตรานนท์ฟ้า** ครับ

ที่พบคือคนที่มีนามสกุล "จิตรานนท์ฟ้า" มีทั้งหมด 3 ท่าน แต่ชื่อต้นไม่ใช่ "ถาวร" ได้แก่:
- **อิสระ จิตรานนท์ฟ้า** — Phone Support Agent (ต่อ 72554)
- **สุจิรา จิตรานนท์ฟ้า** — Lead Fleet Driver (ต่อ 47209)
- **อิสรา จิตรานนท์ฟ้า** — Events Coordinator (ต่อ 78318)

หากคุณหมายถึงคนใดคนหนึ่งในนี้ หรือต้องการให้ลองค้นหาด้วยชื่ออื่นเพิ่มเติ
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก **JC (จุดเชื่อม / JudChuem)** ซึ่งเป็นหนึ่งใน House Brand ของฟ้าใหม่

ผู้บริหารสูงสุดของแผนกนี้คือ:

- **คุณสรัล อาวุทธ์มณี** — ผู้จัดการทั่วไปแบรนด์จุดเชื่อม (General Manager of JudChuem)
- **อีเมล:** SARAN.AW@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Daonuea (ดาวเหนือ) คือ **วิเชียร พงหอมกลิ่น** (WICHIAN PHONGHOMKLIN) — General Manager of Daonuea

📧 WICHIAN.PH@FAHMAI.CO.TH · ☎️ 76999
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the Judchuem (จุดเชื่อม) department is **Saran Awutmani (สรัล อาวุทธ์มณี)**, General Manager of Judchuem — ext. 78762, SARAN.AW@FAHMAI.CO.TH.
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Kluensiang (คลื่นเสียง) คือ **คุณราม ลวรรณ (จุ๊บ)** — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง
📧 RAM.LA@FAHMAI.CO.TH | ✆ 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon (วงโคจร) คือ **คุณกฤษ มหาแก้วใส (ขิง)** — ผู้จัดการทั่วไปแบรนด์วงโคจร ติดต่อ: KRIS.MA@FAHMAI.CO.TH, เบอร์ 74375
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are **6 employees** in the DN department at Lead level who started in 2022:

- อภิชัย ธนบุญ (จุ๊บ) — DN-MKT
- ธนพล พิไชยา (ไผ่) — DN-PD
- กฤติน อนุเจริญ — DN-OPS
- ราม มหากิตติ — DN-OPS
- วีระ ชัยโชคดี — DN-PD
- กิตติศักดิ์ ฟ้าใสทอง — DN-MKT
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
Peter (Arthit Watcharafa), Lead QA Engineer in TEC-QA, doesn't have a phone extension listed in the directory. His email is **ARTHIT.WA@FAHMAI.CO.TH** if you'd like to reach him that way.
```

### g583 [noisy_name_form] P1/en
**Q:** Can I get the extension for Sompong, the VP of Digital Marketing?

**Fails:** missing any-of ['79901']

**Response:**

```
No record found. There is no "Sompong" in the directory, and the VP of Marketing is **Kwang Kobsookrat** (คะวัง กอบสุขรัตน์), extension 74711. If you meant someone else, let me know and I'll look again!
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
ฝ่าย HR ที่คุณมนตราสังกัดนั้น ตำแหน่งสูงสุดคือ **คุณณฐามน อภิชัยดี** (CHRO — Chief Human Resources Officer) ครับ

📞 **เบอร์ต่อ: 79303**

(อีเมล: NATHAMON.AP@FAHMAI.CO.TH | ชั้น 27 FahMai Tower)
```

### g677 [enterprise_shorthand] P1/th
**Q:** ผู้อำนวยการทีมขายสาขาภูเก็ต คือใคร

**Fails:** missing any-of ['Watcharakaewsai', 'วัชรแก้วใส']

**Response:**

```
ผู้อำนวยการทีมขายสาขาภูเก็ตคือ **คุณถาวร วัชรแกัวใส (เนสท์เล่)**

- **ตำแหน่ง:** ผู้อำนวยการฝ่ายพนักงานขายสาขาภูเก็ต
- **อีเมล:** THAWAN.WA@FAHMAI.CO.TH
- **เบอร์ต่อ:** 09932
- **มือถือ:** 091-455-0102
- **ที่ตั้ง:** สาขาภูเก็ต
```

### g683 [enterprise_shorthand] P1/en
**Q:** Who heads the HR team?

**Fails:** missing any-of ['Nathamon', 'ณฐามน']; missing any-of ['Aphichaidee', 'อภิชัยดี']

**Response:**

```
The HR team is headed by **Sumate Akarajaingam (สุเมธ อัครใจงาม)** — VP Human Resources.

- 📧 SUMATE.AK@FAHMAI.CO.TH
- 📞 Ext: 72146
- 📍 FahMai Tower 22F
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าทีมการตลาด (รองประธานฝ่ายการตลาด) คือ **คุณคะวัง กอบสุขรัตน์ (โอ)**

- 📧 KWANG.KO@FAHMAI.CO.TH
- ☎️ 74711

นอกจากนี้ยังมีรองประธานฝ่ายการตลาดดิจิทัลอีก 1 ท่าน: **คุณสมพงษ์ กอบสุขประเสริฐ** (☎️ 79901)
```

### g725 [nickname_grid] P0/en
**Q:** What's the nickname of the TECVP?

**Fails:** has ext pattern

**Response:**

```
The TECVP is **Nattaphong Athidi** (ณัฐพงษ์ อธิดี). However, no nickname is on file — nickname not listed.

You can reach him at:
- 📧 NATTAPHONG.AT@FAHMAI.CO.TH
- 📞 Ext: 75793 | Mobile: 068-561-3976
```

### g770 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์ดาวเหนือ

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Arthitkulwongs', 'อาทิตย์วงษ์']

**Response:**

```
[agent error: JSONDecodeError: Unterminated string starting at: line 1 column 12 (char 11)]
```

### g771 [subsidiary_routing] P1/en
**Q:** Who heads the marketing unit of the DaoNuea brand?

**Fails:** missing any-of ['Phussadee', 'พุสดี']; missing any-of ['Chaisaidi', 'ชัยสัยดี']

**Response:**

```
The head of the DaoNuea (ดาวเหนือ) brand is **Wichian Phonghomklin** (วิเชียร พงหอมกลิ่น), who serves as **General Manager of DaoNuea** (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ).

- **Email:** WICHIAN.PH@FAHMAI.CO.TH
- **Phone Extension:** 76999
- **Mobile:** 064-902-5307
- **Office:** FahMai Tower 19F, BKK-R9

Note that DaoNuea is a house brand with its own product division (DN), and marketing for the bran
```

### g773 [subsidiary_routing] P1/en
**Q:** Who heads the marketing unit of the Judchuem brand?

**Fails:** missing any-of ['Phaibun', 'ไพบูลย์']; missing any-of ['Anujitranon', 'อนุจิตรานนท์']

**Response:**

```
[agent error: JSONDecodeError: Expecting ',' delimiter: line 1 column 37 (char 36)]
```

### g776 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์วงโคจร

**Fails:** missing any-of ['Phichai', 'พิชัย']; missing any-of ['Amarinfa', 'อมรินทร์ฟ้า']

**Response:**

```
หัวหน้าฝ่าย (VP) ของแบรนด์วงโคจร (WK) คือ **คุณคึกฤทธิ์ อัครเจริญ (ดำ)**

- 📧 KUKRIT.AK@FAHMAI.CO.TH
- 📞 เบอร์ต่อ: 79033 | มือถือ: 097-302-2863
- 📍 FahMai Tower ชั้น 16F

ถ้าคุณหมายถึงหัวหน้าฝ่าย**วิศวกรรม**ของวงโคจรโดยเฉพาะ (ส่วน Engineering) ไม่ใช่ VP ของแบรนด์โดยรวม รบกวนบอกเพิ่มเติมได้นะครับ จะได้ค้นให้ละเอียดขึ้น
```

### g777 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Wongkhojon brand?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
The Wongkhojon (วงโคจร) brand is headed by **Kris Mahakaewsai (กฤษ มหาแก้วใส)** — General Manager of Wongkhojon.

📞 Extension: 74375  
✉️ Email: KRIS.MA@FAHMAI.CO.TH
```

### g832 [superlative] P2/th
**Q:** ใครเป็นพนักงานที่อายุงานยาวนานที่สุดในฟ้าใหม่ครับ

**Fails:** missing any-of ['กนก', 'Kanok']; missing any-of ['เก่งกาจชัย', 'Khaengkadchai']

**Response:**

```
"อายุงาน" (tenure) เป็นข้อมูลที่ไม่ได้เก็บอยู่ในระบบ directory — ระบบเก็บเฉพาะ **Start Year** (ปีที่เริ่มงาน) เท่านั้น ซึ่งไม่เทียบเท่าอายุงานโดยแท้จริง

ถ้าต้องการให้ช่วยดูว่าใครมี **Start Year เก่าที่สุด** (เริ่มงานปีแรกสุด) บอกได้ครับ เดี๋ยวหาข้อมูลให้ได้จาก directory ครับ
```

