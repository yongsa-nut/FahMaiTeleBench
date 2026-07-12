# Run: `deepseekv4pro_both_L2_t3_both_full`

**Overall: 606/626 pass (96.8%)**

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
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| nickname_grid | 59/61 | 96.7% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| name_lookup | 19/20 | 95.0% |
| listing_count | 19/20 | 95.0% |
| noisy_name_form | 19/20 | 95.0% |
| multi_hop | 17/18 | 94.4% |
| retrieval | 13/14 | 92.9% |
| hard_multihop | 24/26 | 92.3% |
| hard_nickname_variant | 9/10 | 90.0% |
| hard_implicit_hierarchy | 17/19 | 89.5% |
| dept_listing_small | 6/7 | 85.7% |
| email_mobile_lookup | 6/7 | 85.7% |
| enterprise_shorthand | 17/20 | 85.0% |
| hard_bridge_lookup | 5/6 | 83.3% |

## By priority

- P0: 220/226 (97.3%)
- P1: 351/364 (96.4%)
- P2: 35/36 (97.2%)

## Failures (20)

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
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea (DN)

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
**ผู้บริหารสูงสุดของแผนก DN (Daonuea/ดาวเหนือ):**

**คุณวิเชียร พงหอมกลิ่น** (WICHIAN PHONGHOMKLIN)  
ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (General Manager of Daonuea)  
อีเมล: WICHIAN.PH@FAHMAI.CO.TH  
มือถือ: 064-902-5307  
เบอร์ต่อ: 76999  
ที่ตั้ง: FahMai Tower ชั้น 19F
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (KS) คือ **คุณราม ลวรรณ (จุ๊บ)** ตำแหน่ง ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (General Manager of Kluensiang) ครับ

- 📧 RAM.LA@FAHMAI.CO.TH
- 📞 ต่อ 75965
- 🏢 FahMai Tower ชั้น 18F
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

### g666 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Rama IX (R9) HQ branch?

**Fails:** missing any-of ['1255']

**Response:**

```
There are **1,255** staff at the Rama IX HQ branch (BKK-R9).
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
**Q:** ใครเป็นหัวหน้าทีมการตลาด (MKT)

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าทีมการตลาด (MKT) คือ **คุณคะวัง กอบสุขรัตน์ (โอ)** — รองประธานฝ่ายการตลาด (VICE PRESIDENT MARKETING)

- 📧 KWANG.KO@FAHMAI.CO.TH
- 📞 เบอร์ต่อ: 74711 | มือถือ: 088-904-0088
- 📍 FahMai Tower ชั้น 20
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

