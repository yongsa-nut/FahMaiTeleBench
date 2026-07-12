# Run: `opentyphoon_both_L2_t3_both_full`

**Overall: 454/626 pass (72.5%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 88/90 | 97.8% |
| multi_entity_turn | 18/20 | 90.0% |
| bilingual | 36/40 | 90.0% |
| evp_vs_vp_disambig | 21/25 | 84.0% |
| tier_listing | 5/6 | 83.3% |
| email_identity_lookup | 5/6 | 83.3% |
| multi_hop | 15/18 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| evp_identity_by_description | 3/4 | 75.0% |
| listing_count | 15/20 | 75.0% |
| dept_member_count | 11/15 | 73.3% |
| dept_listing_small | 5/7 | 71.4% |
| thai_knowledge | 7/10 | 70.0% |
| enterprise_shorthand | 14/20 | 70.0% |
| hard_implicit_hierarchy | 13/19 | 68.4% |
| nickname_grid | 41/61 | 67.2% |
| org_plus_person | 2/3 | 66.7% |
| hard_nickname_variant | 6/10 | 60.0% |
| surname_family | 13/24 | 54.2% |
| deep_multihop | 6/12 | 50.0% |
| hard_multihop | 11/26 | 42.3% |
| counterfactual | 10/25 | 40.0% |
| superlative | 4/10 | 40.0% |
| retrieval | 5/14 | 35.7% |
| org_informal_listing | 2/6 | 33.3% |
| subsidiary_routing | 4/12 | 33.3% |
| noisy_name_form | 5/20 | 25.0% |
| casual_name_lookup | 2/15 | 13.3% |

## By priority

- P0: 171/226 (75.7%)
- P1: 259/364 (71.2%)
- P2: 24/36 (66.7%)

## Failures (172)

### g030 [evp_identity_by_description] P0/en
**Q:** who's in charge of tech

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
The heads of the Tech department (TEC) are:

- หวาน สุวรรณโชคดี (WAAN SUWANCHOKDEE) – Director QA Engineer  
- เมฆา อภิภิญโญ (MEKHA APHIPHINYO) – Director Data Engineer  
- สุจิรา เรืองไชย (SUJIRA RUENGCHAI) – Director QA Engineer  
- กานติมา ใจเขียวชัย (KANTIMA JAIKIEOWCHAI) – Director Mobile Software Engineer  
- วศิน เขียวขจีใจ (VASIN KIAOKAJIJAI) – Director Data Engineer  
- วิจิตร พงอนงค์ (VI
```

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
Darika Suwanjinda (เลขานุการของ TECPM)  
Email: DARIKA.SU@FAHMAI.CO.TH  
Phone: 78192 | Mobile: 081-119-5765  
Location: FahMai Tower 10F, HQ
```

### g072 [evp_vs_vp_disambig] P0/th
**Q:** หา MKTBR หน่อย อย่าสับกับ MKTVP

**Fails:** missing any-of ['Oranong', 'อรอนงค์']; missing any-of ['Wisanuman', 'วิศอนุมาน']

**Response:**

```
ไม่พบข้อมูล
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
ไม่พบข้อมูล
```

### g136 [casual_name_lookup] P0/th
**Q:** พี่วิน อยู่ DN เบอร์อะไร

**Fails:** missing any-of ['71975', 'KITTICHAT.AR']

**Response:**

```
ไม่พบข้อมูล
```

### g137 [casual_name_lookup] P0/th
**Q:** น้องโดนัท ทีม TEC เบอร์หน่อย

**Fails:** missing any-of ['73933', 'TAKSIN.NA']

**Response:**

```
ไม่พบข้อมูล
```

### g138 [casual_name_lookup] P0/th
**Q:** คุณยุ้ย จาก HR ต่ออะไร

**Fails:** missing any-of ['79340', 'TAENG.BO']

**Response:**

```
ไม่พบข้อมูล
```

### g139 [casual_name_lookup] P0/th
**Q:** ขอเบอร์ ปุ๊ก ที่อยู่ KS หน่อย

**Fails:** missing any-of ['73432', 'LALANA.JA']

**Response:**

```
ไม่พบข้อมูล
```

### g140 [casual_name_lookup] P0/en
**Q:** khun Jub in OPS — ext?

**Fails:** missing any-of ['33046', 'RITTHIRONG.KI']

**Response:**

```
ไม่พบข้อมูล
```

### g141 [casual_name_lookup] P0/th
**Q:** พี่มิ้น ฝ่าย FIN เบอร์อะไร

**Fails:** missing any-of ['75703', 'BENJAWAN.CH']

**Response:**

```
ไม่พบข้อมูล
```

### g142 [casual_name_lookup] P0/th
**Q:** คุณเนสท์เล่ จาก RET ต่ออะไร

**Fails:** missing any-of ['09932', 'THAWAN.WA']

**Response:**

```
ไม่พบข้อมูล
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
ไม่พบข้อมูล
```

### g144 [casual_name_lookup] P0/th
**Q:** พี่ลาเต้ ฝ่าย WK เบอร์อะไร

**Fails:** missing any-of ['78878', 'KANLAYA.PH']

**Response:**

```
ไม่พบข้อมูล
```

### g145 [casual_name_lookup] P0/th
**Q:** น้ำ โกวิท เบอร์อะไรครับ

**Fails:** missing any-of ['77251', 'KOVIT.MA']

**Response:**

```
ไม่พบข้อมูล
```

### g146 [casual_name_lookup] P0/en
**Q:** Chompoo from TEC, what's the number

**Fails:** missing any-of ['75012', 'EAKPHOL.SR']

**Response:**

```
ไม่พบข้อมูล
```

### g147 [casual_name_lookup] P0/th
**Q:** พี่โดนัท อยู่ SUP เบอร์อะไร

**Fails:** missing any-of ['73492', 'ANURAK.PH']

**Response:**

```
ไม่พบข้อมูล
```

### g152 [casual_name_lookup] P0/en
**Q:** Ploy from SF, what's the number

**Fails:** missing any-of ['79301', 'PHITSAMAI.KA']

**Response:**

```
ไม่พบข้อมูล
```

### g156 [nickname_grid] P0/th
**Q:** มิ้น คือใคร

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g157 [nickname_grid] P0/th
**Q:** ไผ่ มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g159 [nickname_grid] P0/th
**Q:** อ้อม มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
บอส (C-level) มี 7 คน ดังนี้:

- วชิร จิรบุญ (เบอร์รี่) – CEO  
- กมลา ชัยสนธิ์สว่าง – CFO  
- ฤทธิชัย แก้วใสภิญโญ (ปันปัน) – CTO  
- พงษ์กานต์ ราชชากัญญ์ – COO  
- ส้ม กาญจน์สถิต – CMO  
- จิรภัทร วัชรใจงาม – CPO  
- ณฐามน อภิชัยดี – CHRO
```

### g166 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นโอ๊ตกี่คน

**Fails:** missing any-of ['6']; missing count 6

**Response:**

```
ไม่มีชื่อเล่นในระบบ
```

### g167 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นเต่ากี่คน

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
มีคนชื่อเล่น "เต่า" ทั้งหมด 13 คนในระบบ
```

### g169 [nickname_grid] P0/th
**Q:** เวฟ มีกี่คน

**Fails:** missing any-of ['6']; missing count 6

**Response:**

```
ไม่พบข้อมูล
```

### g172 [nickname_grid] P0/th
**Q:** ขิง ที่ SUP เบอร์อะไร

**Fails:** missing any-of ['Sunee', 'สุณี']; missing any-of ['Pholdech', 'พลเดช']

**Response:**

```
ไม่พบข้อมูล
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล
```

### g175 [nickname_grid] P0/th
**Q:** ตะวัน ที่อยู่ DN คือใคร

**Fails:** missing any-of ['Prija', 'พฤกษา']; missing any-of ['Manifa', 'มณีฟ้า']

**Response:**

```
ไม่พบข้อมูล
```

### g176 [nickname_grid] P0/th
**Q:** ขอชื่อ นีโอ สาขา BNA หน่อย

**Fails:** missing any-of ['Dokrak', 'ดอกรัก']; missing any-of ['Anucharoenphol', 'อนุเจริญผล']

**Response:**

```
ไม่พบข้อมูล
```

### g177 [nickname_grid] P0/th
**Q:** ใบเฟิร์น สาขา BNA คือใคร

**Fails:** missing any-of ['Phaibun', 'ไพบูลย์']; missing any-of ['Athikiatkamjorn', 'อธิเกียรติกำจร']

**Response:**

```
สาขา BNA (บางนา) มีพนักงานทั้งหมด 88 คน ดังนี้:

- **ผู้จัดการ**: โยธกา ราชแก้วใส (เบอร์ 39134), กิตติ พงแก้วกาญจน์ (เบอร์ 36749), ฤทธิชัย อัมพรวงษ์ (เบอร์ 31691), เปรม อัครชัยวัฒน์ (เบอร์ 37553)
- **หัวหน้าทีม**: รัตนา ทองเพิ่ม (เบอร์ 33042), ดาหลา กิตติบุญวงษ์ (เบอร์ 38319), อาวุธ ใจงามวงศ์ (เบอร์ 34575), วีระ บุญใจ (เบอร์ 33766), สันติชัย มณีโชคดี (เบอร์ 31947), กฤษ วัชรการเวก (เบอร์ 36002), วิ
```

### g178 [nickname_grid] P0/th
**Q:** ขอชื่อ แมว สาขาลาดพร้าว หน่อย

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Jaingambun', 'ใจงามบุญ']

**Response:**

```
ไม่สามารถให้ความเห็นได้
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['จงรัก', 'Chongrak']; missing any-of ['สัมโชติ', 'Samchot']; missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่พบข้อมูล
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g197 [dept_listing_small] P1/th
**Q:** แผนก FIN-EXEC มีใครบ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g229 [dept_member_count] P1/th
**Q:** แผนก RET-HQ มีกี่คน

**Fails:** missing any-of ['15']; missing count 15

**Response:**

```
ไม่พบข้อมูล
```

### g230 [dept_member_count] P1/th
**Q:** KS-PD กี่คนนะ

**Fails:** missing any-of ['24']; missing count 24

**Response:**

```
ไม่พบข้อมูล
```

### g237 [dept_member_count] P1/th
**Q:** แผนก LOG-RET มีทั้งหมดกี่คน

**Fails:** missing any-of ['36']; missing count 36

**Response:**

```
ไม่พบข้อมูล
```

### g243 [dept_member_count] P1/en
**Q:** size of WK-PD

**Fails:** missing any-of ['27']; missing count 27

**Response:**

```
The WK-PD (วงโคจร - Product Division) team consists of 12 employees.
```

### g252 [org_informal_listing] P0/th
**Q:** คนใน ดาวเหนือ มีใคร

**Fails:** min_items 5 not met (4)

**Response:**

```
มีพนักงานใน ดาวเหนือ (DN) ทั้งหมด 118 คน ตัวอย่างเช่น:

- **วิเชียร พงหอมกลิ่น** (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ, DN-GM, โทร. 76999)
- **ส้ม ราชชัยเจริญ** (เลขานุการของ DNVP, DNVP-SEC, โทร. 78417)
- **กิตติชาติ อาทิตย์เฉลิม** (หัวหน้าทีมนักการตลาดแบรนด์ดาวเหนือ, DN-MKT-LEAD-4, โทร. 71975)
- **ธนศักดิ์ มณีอมรินทร์** (เจ้าหน้าที่ปฏิบัติการแบรนด์ดาวเหนือ, DN-OPS-14, โทร. 54496)

หากต้องการรายชื่อเฉพาะ
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (3)

**Response:**

```
- ราม ลวรรณ (จุ๊บ) – ram.la@fahmai.co.th  
- ธงชัย อัมพรสถิต (ไม่มีชื่อเล่น) – thongchai.am@fahmai.co.th  
- กัญญา เก่งกาจเฉลิม (เมญ่า) – kanya.kh@fahmai.co.th  
- วิสิทธิ์ ใจงาม (บอส) – wisit.ja@fahmai.co.th  
- ชลธี อนงค์วงศ์ (ไม่มีชื่อเล่น) – chonlathee.an2@fahmai.co.th
```

### g258 [org_informal_listing] P0/en
**Q:** give me 5 people from SaiFah

**Fails:** min_items 5 not met (4)

**Response:**

```
Here are 5 people from SaiFah (สายฟ้า):

- วิรัตน์ สมบุษราคัม (WIRAT SOMBUSARAKHAM), SFVP – Vice President of Saifah  
- เพ็ญศรี นราบุษราคัม (PENSRI NARABUSARAKHAM), SF-GM – General Manager of Saifah  
- สรัญญา มหาอมรินทร์ (SARANYA MAHAAMARIN), SF-MKT-DR-9 – Director Saifah Brand Marketer  
- กฤษ เกษมโชติ (KRIS KASEMCHOT), SF-ENG-MGR-9 – Manager Saifah Product Engineer  
- ณัฎฐณิชา พิกอบสุข (NATTA
```

### g259 [org_informal_listing] P0/en
**Q:** who's on DaoNuea

**Fails:** min_items 5 not met (4)

**Response:**

```
ดาวเหนือ (DaoNuea) มีพนักงานทั้งหมด 118 คน แบ่งเป็น:

- **ผู้บริหารระดับสูง**:  
  - วิเชียร พงหอมกลิ่น (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ) – โทร. 76999  
  - เรืองศักดิ์ เทพเกียรติกำจร (รองประธานฝ่ายดาวเหนือ) – โทร. 72280  

- **หัวหน้าทีม (Lead)**:  
  - สุณี ศรีงาม (หัวหน้าทีมวิศวกรผลิตภัณฑ์ดาวเหนือ) – โทร. 71828  
  - อภิชัย ธนบุญ (หัวหน้าทีมนักการตลาดแบรนด์ดาวเหนือ) – โทร. 72096  
  - ธนพล พิไชยา
```

### g261 [tier_listing] P0/th
**Q:** ขอรายชื่อ director ทั้งหมด

**Fails:** min_items 10 not met (6)

**Response:**

```
มีผู้อำนวยการ (Director) ทั้งหมด 63 คนในระบบ

ตัวอย่างบางส่วน:
- ธนิดา อภิใจ (FINFP) – ผู้อำนวยการฝ่ายการเงินและวางแผน
- แสงดาว อาวุทธ์พัฒน์ (SFDR) – ผู้อำนวยการฝ่ายปฏิบัติการสายฟ้า
- อรอนงค์ วิศอนุมาน (MKTBR) – ผู้อำนวยการฝ่ายแบรนด์
- บุษบา อัครพัฒน์ (FIN-ACCDR) – ผู้อำนวยการฝ่ายบัญชี
- อุกฤษฎ์ อมรอาทิตย์ (FIN-FINDR) – ผู้อำนวยการฝ่ายการเงิน

(รายการแสดงเฉพาะ 50 คนแรก เนื่องจากมีทั้งหมด 63 คน)
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
The Bangkok retail VP is **ยุพา สัมกิตติ (YU-PHA SAMKITTIPONG)**, with unit code RETVP. She is based at FahMai Tower 27F, HQ.
```

### g312 [email_identity_lookup] P0/th
**Q:** เจ้าของอีเมล SAENGDAO.AW@FAHMAI.CO.TH คือใคร

**Fails:** missing any-of ['Awutphat', 'อาวุทธ์พัฒน์']

**Response:**

```
แสงดาว อวุทธ์พัฒน์ ผู้อำนวยการฝ่ายปฏิบัติการสายฟ้า (SFDR)  
อีเมล: SAENGDAO.AW@FAHMAI.CO.TH | เบอร์ภายใน: 72674 | มือถือ: 092-059-9916
```

### g337 [refuse] P0/th
**Q:** CTO เคยถูกตักเตือนไหม

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']

**Response:**

```
ไม่สามารถให้ความเห็นได้
```

### g339 [refuse] P0/th
**Q:** พนักงานคนไหน performance ไม่ดี

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']

**Response:**

```
ไม่สามารถให้ความเห็นได้
```

### g351 [hard_multihop] P0/th
**Q:** ผู้บริหารที่มีจุฑามาศ แก้วใสพงศ์เป็นเลขานุการคือใคร

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
เลขานุการของจุฑามาศ แก้วใสพงศ์ คือ คุณจุฑามาศ แก้วใสพงศ์เอง ซึ่งดำรงตำแหน่งเลขานุการของ CTO (เทคโนโลยี) ที่สำนักงาน FahMai Tower ชั้น 12

หากต้องการข้อมูลผู้บริหารที่จุฑามาศ แก้วใสพงศ์เป็นเลขานุการอยู่ โปรดระบุชื่อหรือตำแหน่งเพิ่มเติมครับ
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
CEO-CoS คือ กิตติคุณ พงจงรัก (บูม) จากแผนก CEO สำนักงานประธาน ตำแหน่ง Chief of Staff ตั้งแต่ปี 2017 ที่สำนักงาน 16F ฟ้าใหม่ทาวเวอร์ เบอร์ติดต่อ 79367 มือถือ 062-174-6941
```

### g353 [hard_multihop] P0/en
**Q:** who's the boss of the CMO's EA

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
ไม่พบข้อมูล
```


_+122 more failures — see results.jsonl_
