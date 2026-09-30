# Run: `typhoon8b_search_L2_t2_search_v10full`

**Overall: 189/626 pass (30.2%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| email_identity_lookup | 6/6 | 100.0% |
| email_mobile_lookup | 6/7 | 85.7% |
| tier_listing | 5/6 | 83.3% |
| extension_reverse | 5/7 | 71.4% |
| dept_listing_medium | 5/8 | 62.5% |
| name_lookup | 12/20 | 60.0% |
| thai_knowledge | 6/10 | 60.0% |
| hard_nickname_variant | 6/10 | 60.0% |
| section_listing | 2/4 | 50.0% |
| surname_family | 11/24 | 45.8% |
| bilingual | 18/40 | 45.0% |
| enterprise_shorthand | 9/20 | 45.0% |
| evp_secretary | 2/5 | 40.0% |
| listing_count | 8/20 | 40.0% |
| superlative | 4/10 | 40.0% |
| evp_vs_vp_disambig | 9/25 | 36.0% |
| dept_member_count | 5/15 | 33.3% |
| org_informal_listing | 2/6 | 33.3% |
| org_plus_person | 1/3 | 33.3% |
| hard_bridge_lookup | 2/6 | 33.3% |
| nickname_grid | 20/61 | 32.8% |
| refuse | 29/90 | 32.2% |
| evp_identity_by_code | 1/4 | 25.0% |
| evp_identity_by_description | 1/4 | 25.0% |
| ceo_president | 1/4 | 25.0% |
| vp_identity | 1/5 | 20.0% |
| deep_multihop | 2/12 | 16.7% |
| dept_listing_small | 1/7 | 14.3% |
| hard_multihop | 3/26 | 11.5% |
| multi_entity_turn | 2/20 | 10.0% |
| subsidiary_routing | 1/12 | 8.3% |
| multi_hop | 1/18 | 5.6% |
| hard_implicit_hierarchy | 1/19 | 5.3% |
| noisy_name_form | 1/20 | 5.0% |
| casual_name_lookup | 0/15 | 0.0% |
| subsidiary_md | 0/8 | 0.0% |
| retrieval | 0/14 | 0.0% |
| brand_prior | 0/10 | 0.0% |
| counterfactual | 0/25 | 0.0% |

## By priority

- P0: 56/226 (24.8%)
- P1: 116/364 (31.9%)
- P2: 17/36 (47.2%)

## Failures (437)

### g002 [evp_identity_by_code] P0/th
**Q:** ใครเป็น OPSVP

**Fails:** missing any-of ['Kukrit', 'คึกฤทธิ์']; missing any-of ['Busarakhamwong', 'บุษราคัมวงศ์']

**Response:**

```
ไม่พบข้อมูล OPSVP ที่ตรงกับคำขอ. ขอปฏิเสธคำขอ.
```

### g003 [evp_identity_by_code] P0/th
**Q:** OPSQA ชื่ออะไร

**Fails:** missing any-of ['Kanok', 'กนก']; missing any-of ['Khaengkadchai', 'เก่งกาจชัย']

**Response:**

```
ไม่พบข้อมูล
```

### g006 [evp_identity_by_code] P0/en
**Q:** who's our SUPCX

**Fails:** missing any-of ['Boonchu', 'บุญชู']; missing any-of ['Kraiseesawang', 'ไกรศรีสว่าง']

**Response:**

```
กีวี่ ธันทิรา ไชยาเสริม (TANTHIRA CHAIYAWONGSOEM)  
ตำแหน่ง: เลขานุการของ SUPCX  
อีเมล: TANTHIRA.CH@FAHMAI.CO.TH  
โทรศัพท์: 76930 (ภายใน)  
สำนักงาน: ฟ้าใหม่ ทาวเวอร์ ชั้น 7
```

### g024 [evp_identity_by_description] P0/th
**Q:** ใครดูแลด้าน tech สูงสุด

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g029 [evp_identity_by_description] P0/en
**Q:** who heads finance

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
ไม่พบข้อมูล
```

### g030 [evp_identity_by_description] P0/en
**Q:** who's in charge of tech

**Fails:** missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
The person in charge of tech is **Rittichai Kaewsaphinyo (ปันปัน)**, CTO, at FahMai.  
Email: RITTICHAI.KA@FAHMAI.CO.TH  
Mobile: 082-837-1298  
Office: FahMai Tower 25F
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
ขอปฏิเสธคำขอ — ไม่พบข้อมูลของตำแหน่ง "TECPM" หรือ "Technical Product Manager" ในระบบของฟ้าใหม่. โปรดตรวจสอบว่าคุณต้องการค้นหาตำแหน่งใดในแผนก TEC หรือไม่.
```

### g071 [evp_vs_vp_disambig] P0/en
**Q:** MKTDG not MKTVP, who is it

**Fails:** missing any-of ['Somphong', 'สมพงษ์']; missing any-of ['Kobsookprasert', 'กอบสุขประเสริฐ']

**Response:**

```
รัตตนา เจริญใจ (RATTANA CHAROENJAI) — ตำแหน่งเลขานุการของ MKTDG, แผนก MKT, สำนักงานที่ FahMai Tower 21F, สาขา BKK-R9, โทรศัพท์: 75097, อีเมล: RATTANA.CH@FAHMAI.CO.TH
```

### g072 [evp_vs_vp_disambig] P0/th
**Q:** หา MKTBR หน่อย อย่าสับกับ MKTVP

**Fails:** missing any-of ['Oranong', 'อรอนงค์']; missing any-of ['Wisanuman', 'วิศอนุมาน']

**Response:**

```
ไม่พบข้อมูล
```

### g073 [evp_vs_vp_disambig] P0/th
**Q:** ขอ LOGFL หน่อย ไม่เอา LOGVP

**Fails:** missing any-of ['Malee', 'มาลี']; missing any-of ['Amonthong', 'อมรทอง']

**Response:**

```
ไม่พบข้อมูล
```

### g074 [evp_vs_vp_disambig] P0/th
**Q:** ขอชื่อ SUPCX (ไม่ใช่ SUPVP)

**Fails:** missing any-of ['Boonchu', 'บุญชู']; missing any-of ['Kraiseesawang', 'ไกรศรีสว่าง']

**Response:**

```
I need to clarify: you're asking for the name of someone in the SUPCX unit, which is a specific team within the SUP (Supply) department. However, the term "SUPCX" is not a standard unit code in the directory. Could you please confirm the correct unit code or provide more details about the role you're looking for? For example, is it SUP-PM, SUP-OPS, or another team within the Supply department?
```

### g076 [evp_vs_vp_disambig] P0/en
**Q:** who's FINFP (not FINVP)

**Fails:** missing any-of ['Thanida', 'ธนิดา']; missing any-of ['Aphijai', 'อภิใจ']

**Response:**

```
ไม่พบข้อมูล
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
ไม่พบข้อมูลของ RETBKK ที่ไม่ใช่ RETVP ตามที่คุณต้องการ  
มีเพียง 3 คนใน RET ที่ทำงานที่ BKK-R9 แต่ทั้งหมดเป็นเลขานุการของ RETVP หรือ RETUPC ไม่ใช่ตำแหน่งผู้จัดการทั่วไปของ RETBKK โดยตรง

ขอปฏิเสธคำขอ
```

### g078 [evp_vs_vp_disambig] P0/th
**Q:** ขอ RETUPC หน่อย ไม่เอา RETVP

**Fails:** missing any-of ['Santichai', 'สันติชัย']; missing any-of ['Boonmeephithak', 'บุญมีพิทักษ์']

**Response:**

```
I cannot provide the requested information. The system does not track or store personal contact details such as phone numbers or email addresses for employees. Please contact the HR department for official records.
```

### g080 [evp_vs_vp_disambig] P0/th
**Q:** หา FIN-ACCDR หน่อย อย่าสับกับ FINVP

**Fails:** missing any-of ['Busaba', 'บุษบา']; missing any-of ['Akaraphat', 'อัครพัฒน์']

**Response:**

```
ไม่พบข้อมูล
```

### g082 [vp_identity] P1/th
**Q:** VP วงโคจร คือใคร

**Fails:** missing any-of ['Kukrit', 'คึกฤทธิ์']; missing any-of ['Akaracharoen', 'อัครเจริญ']

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

### g084 [vp_identity] P1/th
**Q:** VP HR ใคร

**Fails:** missing any-of ['Sumate', 'สุเมธ']; missing any-of ['Akarajaingam', 'อัครใจงาม']

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

### g104 [ceo_president] P1/th
**Q:** CEO ตอนนี้ใคร

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
ไม่พบข้อมูล
```

### g107 [ceo_president] P1/en
**Q:** who is the CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
ไม่พบข้อมูล
```

### g108 [ceo_president] P1/en
**Q:** who's the current CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
ขอปฏิเสธคำขอ
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

### g122 [name_lookup] P1/en
**Q:** phone for Sap Athianongkun

**Fails:** missing any-of ['18485', 'SAP.AT']

**Response:**

```
I cannot provide personal contact information such as phone numbers. Please contact the HR department or use the official contact channels provided by FahMai.
```

### g123 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ อาวุธ จันทภิญโญ

**Fails:** missing any-of ['77863', 'AWUT.CH2', '099-470-0038']

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
I need to clarify your request. Could you please specify which person you're asking about? For example, are you looking for a specific employee in the SF department (e.g., a GM, VP, or manager)? If so, please provide their name or any identifying details (e.g., nickname, position, or email). I can only retrieve contact information if I have the exact details to search the directory.
```

### g135 [casual_name_lookup] P0/th
**Q:** พี่นัต ฝ่าย RET เบอร์อะไร

**Fails:** missing any-of ['54337', 'SUNEE.SU']

**Response:**

```
พี่นัต ฝ่าย RET เบอร์ 099-408-3592 (สุณี สุวรรณอนุมาน)
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
I need more information to help you. Could you please provide the full name (first and last name) of the person you're looking for? For example, "ยุ้ย สมใจ" or "Yui Somjai". I can then search the directory for you.
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
I need to clarify: "คุณเนสท์เล่" is not a real person in the FahMai directory. The name "เนสท์เล่" is a brand name, not an employee. Could you please provide the correct name of the person you're looking for?
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


_+387 more failures — see results.jsonl_
