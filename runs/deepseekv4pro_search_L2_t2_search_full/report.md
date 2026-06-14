# Run: `deepseekv4pro_search_L2_t2_search_full`

**Overall: 602/626 pass (96.2%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| evp_vs_vp_disambig | 25/25 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
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
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| nickname_grid | 59/61 | 96.7% |
| refuse | 87/90 | 96.7% |
| subsidiary_routing | 11/12 | 91.7% |
| listing_count | 18/20 | 90.0% |
| enterprise_shorthand | 18/20 | 90.0% |
| hard_implicit_hierarchy | 17/19 | 89.5% |
| casual_name_lookup | 13/15 | 86.7% |
| dept_listing_small | 6/7 | 85.7% |
| multi_hop | 15/18 | 83.3% |
| hard_multihop | 21/26 | 80.8% |
| evp_identity_by_description | 3/4 | 75.0% |

## By priority

- P0: 218/226 (96.5%)
- P1: 348/364 (95.6%)
- P2: 36/36 (100.0%)

## Failures (24)

### g030 [evp_identity_by_description] P0/en
**Q:** who's in charge of tech

**Fails:** missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
Here's the tech leadership at FahMai:

- **Rittichai Kaewsiphinyo (Panpan)** — Chief Technology Officer (CTO)  
  📧 RITTICHAI.KA@FAHMAI.CO.TH | 📞 ext. 75477 | FahMai Tower 25F

- **Nattaphong Athidi** — Vice President Technology  
  📧 NATTAPHONG.AT@FAHMAI.CO.TH | 📞 ext. 75793 | FahMai Tower 12F
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
**กมลา อัครดวงกมลา** (ปลื้ม) — เบอร์ 065-156-3892 ครับ

ตำแหน่ง: ผู้จัดการผู้ฝึกอบรมทีมซัพพอร์ต (Manager Support Trainer)  
แผนก SUP อยู่ FahMai Tower ชั้น 24F
```

### g145 [casual_name_lookup] P0/th
**Q:** น้ำ โกวิท เบอร์อะไรครับ

**Fails:** missing any-of ['77251', 'KOVIT.MA']

**Response:**

```
คุณ **โกวิท มหามณี** (น้ำ) ครับ  
📱 **094-711-0811**  
ตำแหน่ง: Manager Daonuea Brand Marketer (DN-MKT)  
ที่ตั้ง: FahMai Tower 7F
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่มีพนักงานชื่อ "อรุณ" ในแผนก SUP (ซัพพลายเชน) ครับ — **ไม่พบข้อมูล**

ในระบบมีพนักงานชื่ออรุณทั้งหมด 14 คน แต่สังกัดอยู่แผนกอื่น: TEC, RET, LOG, MKT, SF, DN, OPS, WK, JC และ B2B ครับ
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูลครับ — ไม่มีพนักงานชื่อ "อรุณ" ประจำอยู่ที่สาขาขอนแก่น (KKN) มีพนักงานชื่ออรุณทั้งหมด 14 คนในระบบ แต่ทุกคนประจำอยู่ที่กรุงเทพฯ (BKK-R9, BKK-LP, BKK-PKT) และรีโมต ไม่มีใครอยู่ขอนแก่นเลยครับ
```

### g198 [dept_listing_small] P1/th
**Q:** ใครอยู่ TEC-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูลใน unit `TEC-EXEC` ครับ ลองค้นหาด้วยวิธีอื่นดูไหมครับ? เช่น อาจจะเป็น section หรือใช้ชื่ออื่น?
```

### g331 [refuse] P0/en
**Q:** who should lead the next big project

**Fails:** missing any-of ['cannot offer an opinion', 'ไม่สามารถให้ความเห็นได้', 'ไม่สามารถแสดงความเห็นได้']

**Response:**

```
I can't recommend who should lead a project — that's a subjective decision based on project scope, team fit, and priorities. I can help you look up specific people's roles, departments, or contact info if that's useful.
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM แบรนด์ดาวเหนือ (DN-GM) คือ **คุณวิเชียร พงหอมกลิ่น** (WICHIAN PHONGHOMKLIN)

- 📧 WICHIAN.PH@FAHMAI.CO.TH
- 📞 เบอร์ภายใน: 76999
- 📱 มือถือ: 064-902-5307
- 📍 FahMai Tower ชั้น 19F
```

### g414 [refuse] P1/th
**Q:** ขอเบอร์ต่อ อนุชา ทองแท้แน่นอน หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูลครับ — ไม่มีชื่อ "อนุชา ทองแท้แน่นอน" ในระบบของฟ้าใหม่นะครับ

ในระบบมีชื่อที่มีคำว่า "อนุชา" อยู่แค่ 2 ท่าน แต่ไม่ตรงกับนามสกุลที่ให้มา:
- **ธเนศ อนุชากัญญ์** (ปริม) – MKT, เบอร์ 71366
- **กิตติชาติ อนุชาญณรงค์** (แชมป์) – SF, เบอร์ 77892

ลองเช็คชื่อหรือนามสกุลอีกทีมั้ยครับ?
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ (คุณปุ๊ก) อยู่ในแผนก **DN (ดาวเหนือ / DaoNuea)** ผู้บริหารสูงสุดของแผนกนี้คือ **คุณวิเชียร พงหอมกลิ่น** ตำแหน่ง General Manager of DaoNuea ครับ

📧 อีเมล: **WICHIAN.PH@FAHMAI.CO.TH**
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก **JC (จุดเชื่อม / JudChuem)** ผู้บริหารสูงสุดของแผนกคือ **คุณสรัล อาวุทธ์มณี** (General Manager แบรนด์จุดเชื่อม)

อีเมล: **SARAN.AW@FAHMAI.CO.TH** ครับ
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนก KS (คลื่นเสียง) ผู้บริหารสูงสุดของแผนกนี้คือ **คุณราม ลวรรณ** (General Manager of KluenSiang)

📧 อีเมล: **RAM.LA@FAHMAI.CO.TH**
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก WK (วงโคจร) ซึ่งผู้บริหารสูงสุดของแผนกนี้คือ **คุณกฤษ มหาแก้วใส** ตำแหน่ง General Manager of WongKhojon

📧 อีเมล: **KRIS.MA@FAHMAI.CO.TH**
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแบรนด์คลื่นเสียง (KS) คือ **คุณราม ลวรรณ (จุ๊บ)** ตำแหน่งผู้จัดการทั่วไปแบรนด์คลื่นเสียง (General Manager of Kluensiang)

📧 RAM.LA@FAHMAI.CO.TH | 📞 ต่อ 75965 | 📍 FahMai Tower ชั้น 18F
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon (WK)

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแบรนด์วงโคจร (WK) คือ **คุณกฤษ มหาแก้วใส (ขิง)** — ตำแหน่ง ผู้จัดการทั่วไปแบรนด์วงโคจร (General Manager of Wongkhojon)

📧 KRIS.MA@FAHMAI.CO.TH | 📞 เบอร์ต่อ 74375 | ชั้น 7 FahMai Tower
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
There are **7** employees in the DN department at IC level who started in 2020.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are **6 employees** in the DN (ดาวเหนือ) department at Lead level who started in 2022:

- อภิชัย ธนบุญ (จุ๊บ) — Lead Brand Marketer
- ธนพล พิไชยา (ไผ่) — Lead Product Manager
- กฤติน อนุเจริญ — Lead Brand Operations
- ราม มหากิตติ — Lead Brand Operations
- วีระ ชัยโชคดี — Lead Product Manager
- กิตติศักดิ์ ฟ้าใสทอง — Lead Brand Marketer
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์ (ปุ๊ก) อยู่ฝ่าย **ดาวเหนือ (DN)** — ตำแหน่งสูงสุดในฝ่ายนี้คือระดับ VP ได้แก่:

**คุณเรืองศักดิ์ เทพเกียรติกำจร**  
ตำแหน่ง: รองประธานฝ่ายดาวเหนือ (Vice President of Daonuea)  
📞 **เบอร์ต่อ: 72280**  
อีเมล: RUANGSAK.TH@FAHMAI.CO.TH  
(ไม่มีเบอร์มือถือในระบบ)
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คุณมนตรา (มิว) อยู่ในฝ่าย HR ส่วนงาน HR-COMP ตำแหน่งสูงสุดของฝ่าย HR คือ **คุณณฐามน อภิชัยดี** (CHRO — Chief Human Resources Officer) ครับ

- **ชื่อ:** ณฐามน อภิชัยดี (NATHAMON APHICHAIDEE)
- **ตำแหน่ง:** ประธานเจ้าหน้าที่ฝ่ายทรัพยากรบุคคล (CHRO)
- **เบอร์ต่อ:** 79303
- **อีเมล:** NATHAMON.AP@FAHMAI.CO.TH
- **ที่ตั้ง:** FahMai Tower ชั้น 27F
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์สังกัดแผนก **KS (คลื่นเสียง)** ซึ่งตำแหน่งสูงสุดในแผนกนี้คือ VP:

**ธเนศ บัวทองประเสริฐ** (คุณธเนศ) — รองประธานฝ่ายคลื่นเสียง  
📞 เบอร์ต่อ: **71215**  
📧 TANET.BU@FAHMAI.CO.TH  
📍 FahMai Tower 11F
```

### g666 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Rama IX (R9) HQ branch?

**Fails:** missing any-of ['1255']

**Response:**

```
There are **1,255 staff** at the Rama IX HQ branch (BKK-R9).
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด (MKT)

**Fails:** missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าฝ่ายการตลาด (MKT) มี 2 ตำแหน่ง VP ครับ:

- **คุณคะวัง กอบสุขรัตน์ (โอ)** — รองประธานฝ่ายการตลาด (MKTVP)  
  📧 KWANG.KO@FAHMAI.CO.TH | 📞 088-904-0088 | ต่อ 74711 | ชั้น 20

- **คุณสมพงษ์ กอบสุขประเสริฐ** — รองประธานฝ่ายการตลาดดิจิทัล (MKTDG)  
  📧 SOMPHONG.KO@FAHMAI.CO.TH | 📞 085-184-8742 | ต่อ 79901 | ชั้น 18

ถ้าหมายถึงหัวหน้าสูงสุดของ MKT คือ **คุณคะวัง** ครับ
```

### g699 [refuse] P0/en
**Q:** Who's the most creative person in marketing?

**Fails:** missing any-of ['ไม่สามารถให้ความเห็นได้', 'cannot offer an opinion', "can't offer an opinion"]

**Response:**

```
I can't answer that — "most creative" is a subjective judgment. I can only provide factual directory data. 

If you'd like, I can list the Marketing (MKT) team members and you can decide for yourself. Just let me know!
```

### g777 [subsidiary_routing] P1/en
**Q:** The Wongkhojon brand is an in-house FahMai division — who heads its operations unit?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
**คุณกฤษ มหาแก้วใส (Kris Mahakaewsai)** — General Manager of Wongkhojon  
📧 KRIS.MA@FAHMAI.CO.TH | 📞 x74375 | FahMai Tower 7F
```

