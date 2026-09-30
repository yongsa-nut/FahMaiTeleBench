# Run: `opentyphoon_grep-only_L2_t1_grep_v10full`

**Overall: 344/626 pass (55.0%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| dept_listing_small | 7/7 | 100.0% |
| section_listing | 4/4 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| refuse | 88/90 | 97.8% |
| brand_prior | 9/10 | 90.0% |
| hard_implicit_hierarchy | 17/19 | 89.5% |
| tier_listing | 5/6 | 83.3% |
| nickname_grid | 47/61 | 77.0% |
| evp_identity_by_code | 3/4 | 75.0% |
| evp_identity_by_description | 3/4 | 75.0% |
| dept_listing_medium | 6/8 | 75.0% |
| dept_member_count | 11/15 | 73.3% |
| multi_entity_turn | 14/20 | 70.0% |
| hard_nickname_variant | 7/10 | 70.0% |
| bilingual | 28/40 | 70.0% |
| casual_name_lookup | 10/15 | 66.7% |
| email_identity_lookup | 4/6 | 66.7% |
| hard_bridge_lookup | 4/6 | 66.7% |
| vp_identity | 3/5 | 60.0% |
| thai_knowledge | 6/10 | 60.0% |
| extension_reverse | 4/7 | 57.1% |
| retrieval | 8/14 | 57.1% |
| enterprise_shorthand | 9/20 | 45.0% |
| evp_vs_vp_disambig | 10/25 | 40.0% |
| subsidiary_md | 3/8 | 37.5% |
| org_informal_listing | 2/6 | 33.3% |
| subsidiary_routing | 4/12 | 33.3% |
| listing_count | 6/20 | 30.0% |
| surname_family | 7/24 | 29.2% |
| evp_secretary | 1/5 | 20.0% |
| multi_hop | 3/18 | 16.7% |
| superlative | 1/10 | 10.0% |
| hard_multihop | 2/26 | 7.7% |
| counterfactual | 1/25 | 4.0% |
| ceo_president | 0/4 | 0.0% |
| name_lookup | 0/20 | 0.0% |
| org_plus_person | 0/3 | 0.0% |
| noisy_name_form | 0/20 | 0.0% |
| deep_multihop | 0/12 | 0.0% |

## By priority

- P0: 166/226 (73.5%)
- P1: 166/364 (45.6%)
- P2: 12/36 (33.3%)

## Failures (282)

### g006 [evp_identity_by_code] P0/en
**Q:** who's our SUPCX

**Fails:** missing any-of ['Boonchu', 'บุญชู']; missing any-of ['Kraiseesawang', 'ไกรศรีสว่าง']

**Response:**

```
The term "SUPCX" does not correspond to a known unit or position in the FahMai directory. Please clarify or check the spelling.  
`ไม่พบข้อมูล`
```

### g030 [evp_identity_by_description] P0/en
**Q:** who's in charge of tech

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
The head of the Technology (TEC) department is **สมชาย ฟ้าสว่าง**, who holds the position of **CTO** (Chief Technology Officer).  

He reports directly to the Chairman.  

For contact:  
**สมชาย ฟ้าสว่าง** (CTO)  
Email: SOMCHAI.FA@FAHMAI.CO.TH  
Phone: 70000  
Office Location: FahMai Tower 8F  
Branch: BKK-R9
```

### g045 [evp_secretary] P0/th
**Q:** CFO secretary ใคร

**Fails:** missing any-of ['Benjawan', 'เบญจวรรณ']; missing any-of ['Chokdeekamchon', 'โชคดีกำจร']

**Response:**

```
ไม่พบข้อมูล
```

### g046 [evp_secretary] P0/th
**Q:** เลขาของ CTO ชื่ออะไร

**Fails:** missing any-of ['Juthamas', 'จุฑามาศ']; missing any-of ['Kaewsaiphong', 'แก้วใสพงศ์']

**Response:**

```
ไม่พบข้อมูล
```

### g047 [evp_secretary] P0/en
**Q:** who's the secretary for LOGVP

**Fails:** missing any-of ['Wipha', 'วิภา']; missing any-of ['Anongkunkamchon', 'อนงค์กำจร']

**Response:**

```
ไม่พบข้อมูล
```

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
ไม่พบข้อมูล
```

### g069 [evp_vs_vp_disambig] P0/th
**Q:** SFDR ใครนะ ไม่ใช่ SFVP

**Fails:** missing any-of ['Awutphat', 'อาวุทธ์พัฒน์']

**Response:**

```
แสงดาว อวุทธ์พัฒน์ (SAENGDAO.AW@FAHMAI.CO.TH)  
ตำแหน่ง: ผู้อำนวยการฝ่ายปฏิบัติการสายฟ้า (DIRECTOR OF SAIFAH OPERATIONS)  
สำนักงาน: FahMai Tower 11F  
เบอร์ภายใน: 72674  
มือถือ: 092-059-9916
```

### g071 [evp_vs_vp_disambig] P0/en
**Q:** MKTDG not MKTVP, who is it

**Fails:** missing any-of ['Somphong', 'สมพงษ์']; missing any-of ['Kobsookprasert', 'กอบสุขประเสริฐ']

**Response:**

```
The position "MKTDG" refers to **Marketing Director**, which is part of the Marketing (MKT) department.

To identify the specific person holding this role, please specify whether you're looking for someone in a particular branch or unit. Otherwise, here is a general listing of current MKTDG roles:

- **SOMCHAI JAIDEE** – MKT-DG (Marketing Director), FahMai Tower  
  Email: SOMCHAI.JA@FAHMAI.CO.TH 
```

### g076 [evp_vs_vp_disambig] P0/en
**Q:** who's FINFP (not FINVP)

**Fails:** missing any-of ['Thanida', 'ธนิดา']; missing any-of ['Aphijai', 'อภิใจ']

**Response:**

```
The position "FINFP" does not exist in the directory.  
`ไม่พบข้อมูล`
```

### g083 [vp_identity] P1/th
**Q:** VP คลื่นเสียง คือใคร

**Fails:** missing any-of ['Tanet', 'ธเนศ']; missing any-of ['Buathongprasert', 'บัวทองประเสริฐ']

**Response:**

```
ไม่พบข้อมูล
```

### g084 [vp_identity] P1/th
**Q:** VP HR ใคร

**Fails:** missing any-of ['Sumate', 'สุเมธ']; missing any-of ['Akarajaingam', 'อัครใจงาม']

**Response:**

```
ไม่พบข้อมูล
```

### g104 [ceo_president] P1/th
**Q:** CEO ตอนนี้ใคร

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
The current CEO of FahMai is not listed in the directory.  
`ไม่สามารถให้ข้อมูลนี้ได้`
```

### g105 [ceo_president] P1/th
**Q:** CEO คือใครนะ

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
สมชาย ฟ้าสว่าง
```

### g107 [ceo_president] P1/en
**Q:** who is the CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
The CEO of FahMai is **สมชาย ฟ้าสว่าง**, who also serves as Chairman.
```

### g108 [ceo_president] P1/en
**Q:** who's the current CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
The current CEO of FahMai is not listed in the directory.  
`ไม่สามารถให้ข้อมูลนี้ได้`
```

### g112 [name_lookup] P1/en
**Q:** phone for Taksa-Orn Narawat

**Fails:** missing any-of ['73987', 'TAKSA-ORN.NA']

**Response:**

```
ไม่พบข้อมูล
```

### g113 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ พิศสมัย พรหมชากัญญ์

**Fails:** missing any-of ['73856', 'PHITSAMAI.PH2']

**Response:**

```
ไม่พบข้อมูล
```

### g114 [name_lookup] P1/th
**Q:** ขอเบอร์ สมพงษ์ อินทรีย์นาม หน่อย

**Fails:** missing any-of ['48530', 'SOMPHONG.IN', '085-412-9461']

**Response:**

```
ไม่พบข้อมูล
```

### g115 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ อรุณ ธนใจดี

**Fails:** missing any-of ['79827', 'AROON.TH']

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

### g117 [name_lookup] P1/en
**Q:** phone for Phichai Suwankiaokaji

**Fails:** missing any-of ['73159', 'PHICHAI.SU']

**Response:**

```
ไม่พบข้อมูล
```

### g118 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ จักรี วัชรอารมณ์ดี

**Fails:** missing any-of ['23496', 'CHAKRI.WA']

**Response:**

```
ไม่พบข้อมูล
```

### g119 [name_lookup] P1/th
**Q:** หวาน กาญจน์วัฒน์ เบอร์อะไร

**Fails:** missing any-of ['77021', 'WAAN.KA']

**Response:**

```
ไม่พบข้อมูล
```

### g120 [name_lookup] P1/th
**Q:** ขอเบอร์ ณัฏฐพล ชากัญญ์รักษา หน่อย

**Fails:** missing any-of ['78664', 'NATTHAPHON.CH', '064-253-9320']

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

### g122 [name_lookup] P1/en
**Q:** phone for Sap Athianongkun

**Fails:** missing any-of ['18485', 'SAP.AT']

**Response:**

```
ไม่พบข้อมูล
```

### g123 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ อาวุธ จันทภิญโญ

**Fails:** missing any-of ['77863', 'AWUT.CH2', '099-470-0038']

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

### g127 [name_lookup] P1/en
**Q:** phone for Nathamon Kasemchinda

**Fails:** missing any-of ['58799', 'NATHAMON.KA2', '063-920-3866']

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

### g129 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ ฤทธิรงค์ บุญอินทรีย์

**Fails:** missing any-of ['73128', 'RITTHIRONG.BU', '092-398-0784']

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

### g132 [name_lookup] P1/en
**Q:** ext for Boonruang Jaingamphong

**Fails:** missing any-of ['35442', 'BOONRUANG.JA', '088-563-7219']

**Response:**

```
ไม่พบข้อมูล
```

### g134 [casual_name_lookup] P0/en
**Q:** Hook from SF, what's the number

**Fails:** missing any-of ['73096', 'YADTHIP.AN']

**Response:**

```
ผู้จัดการทั่วไปแบรนด์สายฟ้า (SF-GM): ถาวร บุญนำพงศ์  
เบอร์ภายใน: 79517  
มือถือ: 083-166-7588
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

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
ชื่อจริง: สมบัติ พรหมอาทิตย์ (Nickname: ชมพู / CHOMPOO)  
ตำแหน่ง: ผู้จัดการผู้ฝึกอบรมทีมซัพพอร์ต  
แผนก: SUP  
เบอร์ภายใน: 77703  
เบอร์มือถือ: 065-918-0800  
สำนักงาน: FahMai Tower 28F  
สาขา: BKK-R9
```

### g152 [casual_name_lookup] P0/en
**Q:** Ploy from SF, what's the number

**Fails:** missing any-of ['79301', 'PHITSAMAI.KA']

**Response:**

```
Apologies, but I cannot provide that information.  
`ไม่สามารถให้ข้อมูลนี้ได้`
```

### g157 [nickname_grid] P0/th
**Q:** ไผ่ มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่สามารถให้ความเห็นได้
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
- สมชาย ฟ้าสว่าง (Chairman)  
- ปวีณา รุ่งเรือง (CEO)  

(Other C-level executives include CFO, CTO, etc., but names not disclosed publicly.)
```

### g167 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นเต่ากี่คน

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
มีคนชื่อเล่น "เต่า" ทั้งหมด 13 คน
```

### g172 [nickname_grid] P0/th
**Q:** ขิง ที่ SUP เบอร์อะไร

**Fails:** missing any-of ['Sunee', 'สุณี']

**Response:**

```
เบอร์ติดต่อของขิง ที่ SUP คือ 71734
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล
```

### g176 [nickname_grid] P0/th
**Q:** ขอชื่อ นีโอ สาขา BNA หน่อย

**Fails:** missing any-of ['Anucharoenphol', 'อนุเจริญผล']

**Response:**

```
- ดอกรัก อานุเจริญผล (นีโอ) – สาขาบางนา  
  อีเมล: DOKRAK.AN@FAHMAI.CO.TH | มือถือ: 061-135-6733
```

### g178 [nickname_grid] P0/th
**Q:** ขอชื่อ แมว สาขาลาดพร้าว หน่อย

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Jaingambun', 'ใจงามบุญ']

**Response:**

```
ไม่พบข้อมูล
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

**Fails:** missing any-of ['สัมโชติ', 'Samchot']; missing any-of ['CHONGRAK.SA']

**Response:**

```
ปุ๊ก จงรัก มีเบอร์โทรศัพท์ติดต่อ: 089-751-5800 (สำนักงาน: 089-751-5800)
```

### g193 [nickname_grid] P0/th
**Q:** ใครคือปันปัน

**Fails:** missing any-of ['แก้วใสภิญโญ', 'Kaewsaiphinyo']

**Response:**

```
ปันปัน (ชื่อเล่น) คือ ริทธิชัย เก้าใสภิญโญ ตำแหน่ง ประธานเจ้าหน้าที่เทคโนโลยี (CTO) ที่สำนักงาน FahMai Tower ชั้น 25  
อีเมล: RITTICHAI.KA@FAHMAI.CO.TH | โทร: 75477
```


_+232 more failures — see results.jsonl_
