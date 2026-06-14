# Run: `opentyphoon_repl_L2_t4_repl_full`

**Overall: 375/626 pass (59.9%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| section_listing | 4/4 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| listing_count | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 87/90 | 96.7% |
| multi_entity_turn | 17/20 | 85.0% |
| tier_listing | 5/6 | 83.3% |
| email_identity_lookup | 5/6 | 83.3% |
| superlative | 8/10 | 80.0% |
| nickname_grid | 48/61 | 78.7% |
| evp_identity_by_code | 3/4 | 75.0% |
| name_lookup | 15/20 | 75.0% |
| surname_family | 18/24 | 75.0% |
| extension_reverse | 5/7 | 71.4% |
| email_mobile_lookup | 5/7 | 71.4% |
| hard_nickname_variant | 7/10 | 70.0% |
| vp_identity | 3/5 | 60.0% |
| thai_knowledge | 6/10 | 60.0% |
| multi_hop | 10/18 | 55.6% |
| bilingual | 21/40 | 52.5% |
| dept_listing_medium | 4/8 | 50.0% |
| retrieval | 7/14 | 50.0% |
| enterprise_shorthand | 10/20 | 50.0% |
| evp_vs_vp_disambig | 12/25 | 48.0% |
| hard_implicit_hierarchy | 9/19 | 47.4% |
| casual_name_lookup | 6/15 | 40.0% |
| dept_member_count | 6/15 | 40.0% |
| org_plus_person | 1/3 | 33.3% |
| evp_identity_by_description | 1/4 | 25.0% |
| ceo_president | 1/4 | 25.0% |
| subsidiary_routing | 3/12 | 25.0% |
| org_informal_listing | 1/6 | 16.7% |
| hard_multihop | 3/26 | 11.5% |
| evp_secretary | 0/5 | 0.0% |
| dept_listing_small | 0/7 | 0.0% |
| noisy_name_form | 0/20 | 0.0% |
| counterfactual | 0/25 | 0.0% |
| deep_multihop | 0/12 | 0.0% |

## By priority

- P0: 162/226 (71.7%)
- P1: 195/364 (53.6%)
- P2: 18/36 (50.0%)

## Failures (251)

### g006 [evp_identity_by_code] P0/en
**Q:** who's our SUPCX

**Fails:** missing any-of ['Boonchu', 'บุญชู']; missing any-of ['Kraiseesawang', 'ไกรศรีสว่าง']

**Response:**

```
ไม่พบข้อมูล
```

### g023 [evp_identity_by_description] P0/th
**Q:** ใครคุมการเงินของที่นี่

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
หัวหน้าฝ่ายการเงิน (CFO) คือ **เบญจวรรณ โชคดีกำจร**  
ตำแหน่ง: Executive Assistant to CFO  
อีเมล: BENJAWAN.CH@FAHMAI.CO.TH  

หากต้องการข้อมูลผู้บริหารระดับสูงกว่า เช่น รองประธานฝ่ายการเงิน หรือ CFO โดยตรง กรุณาสอบถามเพิ่มเติมครับ
```

### g029 [evp_identity_by_description] P0/en
**Q:** who heads finance

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
The Finance Department is led by several Directors. Key leaders include:

- อุกฤษฎ์ อมรอาทิตย์ (UKRIT.AM@FAHMAI.CO.TH) – Director Finance  
- ธนิดา อภิใจ (THANIDA.AP@FAHMAI.CO.TH) – Director Financial Planning  
- บุษบา อัครพัฒน์ (BUSABA.AK@FAHMAI.CO.TH) – Director Accounting  

For the highest leadership, the CFO is not explicitly listed in the directory under a single head role. However, the top
```

### g030 [evp_identity_by_description] P0/en
**Q:** who's in charge of tech

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
The head of the Technology (TEC) department at FahMai is **สมชาย ฟ้าสว่าง**, who serves as the **Chief Technology Officer (CTO)**.

Here are the key tech leadership roles:

- **CTO (Chief Technology Officer)** – สมชาย ฟ้าสว่าง  
  Email: SOMCHAI.FASWANG@FAHMAI.CO.TH  
  Office: FahMai Tower 8F  

- **TEC-Director** – ปวีณา แสงสุข  
  Email: PAWINA.SANGSUAN@FAHMAI.CO.TH  

- **TEC-MOB-3 Manager** –
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

### g048 [evp_secretary] P0/th
**Q:** ขอชื่อเลขา LOGFL หน่อย

**Fails:** missing any-of ['Sujira', 'สุจิรา']; missing any-of ['Apinyachaloem', 'อภิญญาเฉลิม']

**Response:**

```
ไม่มีชื่อเล่นในระบบ
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

**Fails:** missing any-of ['Saengdao', 'แสงดาว']; missing any-of ['Awutphat', 'อาวุทธ์พัฒน์']

**Response:**

```
ไม่พบข้อมูล
```

### g070 [evp_vs_vp_disambig] P0/th
**Q:** TECPM ใครนะ ไม่ใช่ TECVP

**Fails:** missing any-of ['Rachata', 'ราชตะ']; missing any-of ['Samchannarong', 'สัมชาญณรงค์']

**Response:**

```
ไม่พบข้อมูล
```

### g071 [evp_vs_vp_disambig] P0/en
**Q:** MKTDG not MKTVP, who is it

**Fails:** missing any-of ['Somphong', 'สมพงษ์']; missing any-of ['Kobsookprasert', 'กอบสุขประเสริฐ']

**Response:**

```
No record found.
```

### g072 [evp_vs_vp_disambig] P0/th
**Q:** หา MKTBR หน่อย อย่าสับกับ MKTVP

**Fails:** missing any-of ['Oranong', 'อรอนงค์']; missing any-of ['Wisanuman', 'วิศอนุมาน']

**Response:**

```
- สรพงษ์ อารีฟ้า | MANAGER BRAND SPECIALIST | SORAPONG.AR@FAHMAI.CO.TH  
- อาทิตย์ ประดี | LEAD BRAND SPECIALIST | ARTHIT.PR@FAHMAI.CO.TH  
- รัตพร มณีอนันต์ | LEAD BRAND SPECIALIST | RATAPON.MA@FAHMAI.CO.TH  
- ละไม เทพชัยสนธิ์ | BRAND SPECIALIST | LAMAI.TH@FAHMAI.CO.TH  
- ธเนศ อนุชากัญญ์ | BRAND SPECIALIST | TANET.AN@FAHMAI.CO.TH  

(16 total MKT-BR staff; shown top 5)
```

### g074 [evp_vs_vp_disambig] P0/th
**Q:** ขอชื่อ SUPCX (ไม่ใช่ SUPVP)

**Fails:** missing any-of ['Boonchu', 'บุญชู']; missing any-of ['Kraiseesawang', 'ไกรศรีสว่าง']

**Response:**

```
ไม่พบข้อมูล
```

### g075 [evp_vs_vp_disambig] P0/th
**Q:** OPSQA ใคร — ไม่ใช่ OPSVP

**Fails:** missing any-of ['Kanok', 'กนก']; missing any-of ['Khaengkadchai', 'เก่งกาจชัย']

**Response:**

```
ไม่พบข้อมูล
```

### g076 [evp_vs_vp_disambig] P0/en
**Q:** who's FINFP (not FINVP)

**Fails:** missing any-of ['Thanida', 'ธนิดา']; missing any-of ['Aphijai', 'อภิใจ']

**Response:**

```
ไม่พบข้อมูล
```

### g083 [vp_identity] P1/th
**Q:** VP คลื่นเสียง คือใคร

**Fails:** missing any-of ['Tanet', 'ธเนศ']; missing any-of ['Buathongprasert', 'บัวทองประเสริฐ']

**Response:**

```
ไม่พบข้อมูล
```

### g093 [vp_identity] P1/en
**Q:** who's VP of logistics

**Fails:** missing any-of ['Natthakan', 'ณัฐกานต์']; missing any-of ['Sriaromdee', 'ศรีอารมณ์ดี']

**Response:**

```
ไม่พบข้อมูล
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
The current CEO of FahMai is not listed in the directory.  
`ไม่สามารถให้ข้อมูลนี้ได้`
```

### g108 [ceo_president] P1/en
**Q:** who's the current CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
The current CEO of FahMai is **สมชาย ฟ้าสว่าง**, who also serves as Chairman.
```

### g112 [name_lookup] P1/en
**Q:** phone for Taksa-Orn Narawat

**Fails:** missing any-of ['73987', 'TAKSA-ORN.NA']

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

### g122 [name_lookup] P1/en
**Q:** phone for Sap Athianongkun

**Fails:** missing any-of ['18485', 'SAP.AT']

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

### g132 [name_lookup] P1/en
**Q:** ext for Boonruang Jaingamphong

**Fails:** missing any-of ['35442', 'BOONRUANG.JA', '088-563-7219']

**Response:**

```
ไม่มีชื่อเล่นในระบบ
```

### g134 [casual_name_lookup] P0/en
**Q:** Hook from SF, what's the number

**Fails:** missing any-of ['73096', 'YADTHIP.AN']

**Response:**

```
ถาวร บุญนำพงศ์ (SF-GM)  
เบอร์ภายใน: 79517
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

### g140 [casual_name_lookup] P0/en
**Q:** khun Jub in OPS — ext?

**Fails:** missing any-of ['33046', 'RITTHIRONG.KI']

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

### g152 [casual_name_lookup] P0/en
**Q:** Ploy from SF, what's the number

**Fails:** missing any-of ['79301', 'PHITSAMAI.KA']

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

### g170 [nickname_grid] P0/th
**Q:** นับคนชื่อปลื้มให้หน่อย

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
ไม่พบข้อมูล
```

### g173 [nickname_grid] P0/th
**Q:** กบ ที่อยู่ B2B คือใคร

**Fails:** missing any-of ['Oranong', 'อรอนงค์']; missing any-of ['Ratanakasemkit', 'รัตนเกษม']

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
ไม่พบข้อมูล
```

### g178 [nickname_grid] P0/th
**Q:** ขอชื่อ แมว สาขาลาดพร้าว หน่อย

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Jaingambun', 'ใจงามบุญ']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
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
ไม่มีเบอร์มือถือในระบบ
```

### g193 [nickname_grid] P0/th
**Q:** ใครคือปันปัน

**Fails:** missing any-of ['ปัน', 'ปัน', 'ไม่พบข้อมูล']

**Response:**

```
ฤทธิชัย แก้วใสภิญโญ  
Email: RITTICHAI.KA@FAHMAI.CO.TH  
เบอร์ภายใน: 75477
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

### g198 [dept_listing_small] P1/th
**Q:** ใครอยู่ TEC-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g199 [dept_listing_small] P1/th
**Q:** ใครอยู่ OPS-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```


_+201 more failures — see results.jsonl_
