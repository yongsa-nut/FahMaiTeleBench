# Run: `opentyphoon_search_L2_t2_search_full`

**Overall: 422/626 pass (67.4%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 84/90 | 93.3% |
| evp_vs_vp_disambig | 23/25 | 92.0% |
| tier_listing | 5/6 | 83.3% |
| vp_identity | 4/5 | 80.0% |
| thai_knowledge | 8/10 | 80.0% |
| evp_identity_by_description | 3/4 | 75.0% |
| ceo_president | 3/4 | 75.0% |
| dept_listing_medium | 6/8 | 75.0% |
| section_listing | 3/4 | 75.0% |
| multi_entity_turn | 15/20 | 75.0% |
| bilingual | 30/40 | 75.0% |
| hard_nickname_variant | 7/10 | 70.0% |
| nickname_grid | 41/61 | 67.2% |
| dept_member_count | 10/15 | 66.7% |
| org_plus_person | 2/3 | 66.7% |
| listing_count | 13/20 | 65.0% |
| multi_hop | 11/18 | 61.1% |
| enterprise_shorthand | 12/20 | 60.0% |
| hard_implicit_hierarchy | 11/19 | 57.9% |
| dept_listing_small | 4/7 | 57.1% |
| org_informal_listing | 3/6 | 50.0% |
| surname_family | 12/24 | 50.0% |
| superlative | 5/10 | 50.0% |
| counterfactual | 11/25 | 44.0% |
| subsidiary_routing | 4/12 | 33.3% |
| deep_multihop | 4/12 | 33.3% |
| hard_multihop | 8/26 | 30.8% |
| retrieval | 3/14 | 21.4% |
| noisy_name_form | 3/20 | 15.0% |
| casual_name_lookup | 1/15 | 6.7% |

## By priority

- P0: 169/226 (74.8%)
- P1: 230/364 (63.2%)
- P2: 23/36 (63.9%)

## Failures (204)

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

### g093 [vp_identity] P1/en
**Q:** who's VP of logistics

**Fails:** missing any-of ['Natthakan', 'ณัฐกานต์']; missing any-of ['Sriaromdee', 'ศรีอารมณ์ดี']

**Response:**

```
The VP of Logistics is **วิภา อนงค์กำจร** (Wipha Anongkunkamchon), LOGVP-SEC.  
Contact: wipha.an@fahmai.co.th | Mobile: 084-913-6866
```

### g107 [ceo_president] P1/en
**Q:** who is the CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
The CEO of FahMai is **สมชาย ฟ้าสว่าง**.
```

### g134 [casual_name_lookup] P0/en
**Q:** Hook from SF, what's the number

**Fails:** missing any-of ['73096', 'YADTHIP.AN']

**Response:**

```
Apologies, but I cannot provide this information.  
`ไม่สามารถให้ข้อมูลนี้ได้`
```

### g135 [casual_name_lookup] P0/th
**Q:** พี่นัต ฝ่าย RET เบอร์อะไร

**Fails:** missing any-of ['54337', 'SUNEE.SU']

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
ไม่สามารถให้ความเห็นได้
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
มีบอสทั้งหมด 7 คน ดังนี้:

- วชิร จิรบุญ (ประธานเจ้าหน้าที่บริหาร)
- กมลา ชัยสนธิ์สว่าง (ประธานเจ้าหน้าที่การเงิน)
- ฤทธิชัย แก้วใสภิญโญ (ประธานเจ้าหน้าที่เทคโนโลยี)
- พงษ์กานต์ ราชชากัญญ์ (ประธานเจ้าหน้าที่ปฏิบัติการ)
- ส้ม กาญจน์สถิต (ประธานเจ้าหน้าที่การตลาด)
- จิรภัทร วัชรใจงาม (ประธานเจ้าหน้าที่ฝ่ายผลิตภัณฑ์)
- ณฐามน อภิชัยดี (ประธานเจ้าหน้าที่ฝ่ายทรัพยากรบุคคล)
```

### g169 [nickname_grid] P0/th
**Q:** เวฟ มีกี่คน

**Fails:** missing any-of ['6']; missing count 6

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
ไม่พบข้อมูล
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

### g206 [dept_listing_small] P1/en
**Q:** who's in HR-OPS

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g211 [dept_listing_medium] P1/en
**Q:** who's in WK-ENG

**Fails:** min_items 5 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g217 [dept_listing_medium] P1/th
**Q:** JC-PD มีใครบ้าง

**Fails:** min_items 5 not met (4)

**Response:**

```
JC-PD มีทั้งหมด 74 คน ตัวอย่าง:

- ราชินี อาทิตย์สุข (RACHINI ARTHITKUL) – JCVP  
- รัตพร จงรักกุล (RATAPON CHONGRAKKUN) – JCVP-SEC  
- สรัล อาวุทธ์มณี (SARAN AWUTMANI) – JC-GM  
- สนุก อนุอาวุทธ์ (SANOUK ANUAWUT) – JC-PD-DR-4  
- ณรงค์ กอบสุขบุญ (NARONG KOBSOOKBUN) – JC-ENG-DR-6  

(แสดงเฉพาะ 10 คนแรกจากผลลัพธ์ 74 คน)
```

### g228 [dept_member_count] P1/en
**Q:** how many in B2B-SUP

**Fails:** missing any-of ['17']; missing count 17

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
KS-PD มีทั้งหมด 100 คน
```

### g234 [dept_member_count] P1/th
**Q:** แผนก TEC-INF มีทั้งหมดกี่คน

**Fails:** missing any-of ['29']; missing count 29

**Response:**

```
ไม่พบข้อมูล
```

### g243 [dept_member_count] P1/en
**Q:** size of WK-PD

**Fails:** missing any-of ['27']; missing count 27

**Response:**

```
The size of the WK-PD unit is not available in the directory.  
`ไม่สามารถให้ข้อมูลนี้ได้`
```

### g247 [section_listing] P0/th
**Q:** ขอรายชื่อ MKT-EVT

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g252 [org_informal_listing] P0/th
**Q:** คนใน ดาวเหนือ มีใคร

**Fails:** min_items 5 not met (3)

**Response:**

```
มีพนักงานในแบรนด์ ดาวเหนือ (DN) ทั้งหมด 118 คน ตัวอย่างเช่น:

- **วิเชียร พงหอมกลิ่น** (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ) – โทร: 76999, อีเมล: WICHIAN.PH@FAHMAI.CO.TH  
- **ส้ม ราชชัยเจริญ** (เลขานุการของ DNVP) – โทร: 78417, อีเมล: SOM.RA@FAHMAI.CO.TH  
- **กิตติชาติ อาทิตย์เฉลิม** (หัวหน้าทีมผู้จัดการผลิตภัณฑ์ดาวเหนือ) – โทร: 71975, มือถือ: 068-463-2877  

(รายการแสดงเฉพาะ 50 คนแรกเนื่องจากมีทั้งหมด
```

### g255 [org_informal_listing] P0/th
**Q:** วงโคจร มีใครบ้าง

**Fails:** min_items 5 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g259 [org_informal_listing] P0/en
**Q:** who's on DaoNuea

**Fails:** min_items 5 not met (0)

**Response:**

```
ไม่พบข้อมูล
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

(รายการครบ 63 คน แสดงเฉพาะ 50 คนแรกเนื่อง
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
The Bangkok retail VP is **Yupa Samkittipong** (ยุพา สัมกิตติ), with Employee ID 08991405.  
Contact: yu-pha.sa@fahmai.co.th | Mobile: 082-885-4387  

(Note: The search returned a secretary, not the VP. No VP was found under RET department.)
```

### g274 [multi_entity_turn] P0/th
**Q:** ขอ ext ของ CMO กับ MKTVP

**Fails:** missing any-of ['79005']; min_items 2 not met (1)

**Response:**

```
CMO ไม่มีข้อมูลในระบบ  
MKTVP: คะวัง กอบสุขรัตน์ (โอ) – เบอร์ภายใน: 74711
```

### g275 [multi_entity_turn] P0/th
**Q:** ขอเบอร์ของ CPO, SFVP

**Fails:** missing any-of ['78052']; min_items 2 not met (1)

**Response:**

```
ไม่พบข้อมูล  
CPO ไม่มีในระบบ  

SFVP: วิรัตน์ สมบุษราคัม (ดอกไม้)  
เบอร์ภายใน: 72402 | มือถือ: 064-970-0992 | อีเมล: WIRAT.SO@FAHMAI.CO.TH
```

### g317 [refuse] P0/th
**Q:** สัญชาติ CMO

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']

**Response:**

```
ไม่สามารถให้ความเห็นได้
```


_+154 more failures — see results.jsonl_
