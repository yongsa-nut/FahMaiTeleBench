# Run: `gpt55med_search_L2_t2_search_v10full`

**Overall: 460/626 pass (73.5%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| section_listing | 4/4 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| bilingual | 37/40 | 92.5% |
| surname_family | 22/24 | 91.7% |
| enterprise_shorthand | 18/20 | 90.0% |
| dept_listing_small | 6/7 | 85.7% |
| evp_secretary | 4/5 | 80.0% |
| evp_vs_vp_disambig | 20/25 | 80.0% |
| casual_name_lookup | 12/15 | 80.0% |
| superlative | 8/10 | 80.0% |
| evp_identity_by_code | 3/4 | 75.0% |
| evp_identity_by_description | 3/4 | 75.0% |
| dept_listing_medium | 6/8 | 75.0% |
| multi_entity_turn | 15/20 | 75.0% |
| hard_multihop | 19/26 | 73.1% |
| noisy_name_form | 14/20 | 70.0% |
| nickname_grid | 42/61 | 68.9% |
| counterfactual | 17/25 | 68.0% |
| dept_member_count | 10/15 | 66.7% |
| org_informal_listing | 4/6 | 66.7% |
| multi_hop | 11/18 | 61.1% |
| subsidiary_routing | 7/12 | 58.3% |
| deep_multihop | 7/12 | 58.3% |
| hard_implicit_hierarchy | 11/19 | 57.9% |
| extension_reverse | 4/7 | 57.1% |
| retrieval | 8/14 | 57.1% |
| ceo_president | 2/4 | 50.0% |
| subsidiary_md | 4/8 | 50.0% |
| hard_bridge_lookup | 3/6 | 50.0% |
| listing_count | 8/20 | 40.0% |
| brand_prior | 4/10 | 40.0% |
| org_plus_person | 1/3 | 33.3% |
| email_identity_lookup | 2/6 | 33.3% |
| name_lookup | 6/20 | 30.0% |
| email_mobile_lookup | 2/7 | 28.6% |
| vp_identity | 1/5 | 20.0% |

## By priority

- P0: 185/226 (81.9%)
- P1: 254/364 (69.8%)
- P2: 21/36 (58.3%)

## Failures (166)

### g002 [evp_identity_by_code] P0/th
**Q:** ใครเป็น OPSVP

**Fails:** missing any-of ['Kukrit', 'คึกฤทธิ์']; missing any-of ['Busarakhamwong', 'บุษราคัมวงศ์']

**Response:**

```
no record found
```

### g023 [evp_identity_by_description] P0/th
**Q:** ใครคุมการเงินของที่นี่

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
no record found
```

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
no record found
```

### g081 [vp_identity] P1/en
**Q:** who's VP of DaoNuea

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
no record found
```

### g082 [vp_identity] P1/th
**Q:** VP วงโคจร คือใคร

**Fails:** missing any-of ['Kukrit', 'คึกฤทธิ์']; missing any-of ['Akaracharoen', 'อัครเจริญ']

**Response:**

```
no record found under the search I ran, so I can’t confirm who the VP of WongKhoJon is right now.
```

### g083 [vp_identity] P1/th
**Q:** VP คลื่นเสียง คือใคร

**Fails:** missing any-of ['Tanet', 'ธเนศ']; missing any-of ['Buathongprasert', 'บัวทองประเสริฐ']

**Response:**

```
no record found
```

### g084 [vp_identity] P1/th
**Q:** VP HR ใคร

**Fails:** missing any-of ['Sumate', 'สุเมธ']; missing any-of ['Akarajaingam', 'อัครใจงาม']

**Response:**

```
no record found
```

### g105 [ceo_president] P1/th
**Q:** CEO คือใครนะ

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
no record found
```

### g108 [ceo_president] P1/en
**Q:** who's the current CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```
no record found
```

### g112 [name_lookup] P1/en
**Q:** phone for Taksa-Orn Narawat

**Fails:** missing any-of ['73987', 'TAKSA-ORN.NA']

**Response:**

```
no record found
```

### g114 [name_lookup] P1/th
**Q:** ขอเบอร์ สมพงษ์ อินทรีย์นาม หน่อย

**Fails:** missing any-of ['48530', 'SOMPHONG.IN', '085-412-9461']

**Response:**

```
no record found
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
no record found
```

### g118 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ จักรี วัชรอารมณ์ดี

**Fails:** missing any-of ['23496', 'CHAKRI.WA']

**Response:**

```
no record found
```

### g121 [name_lookup] P1/th
**Q:** ขอเบอร์ สรพงษ์ วิศวงษ์ หน่อย

**Fails:** missing any-of ['72279', 'SORAPONG.WI', '091-061-7212']

**Response:**

```
no record found
```

### g122 [name_lookup] P1/en
**Q:** phone for Sap Athianongkun

**Fails:** missing any-of ['18485', 'SAP.AT']

**Response:**

```
no record found
```

### g123 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ อาวุธ จันทภิญโญ

**Fails:** missing any-of ['77863', 'AWUT.CH2', '099-470-0038']

**Response:**

```
no record found
```

### g124 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ เมฆา ราชกำจร

**Fails:** missing any-of ['74887', 'MEKHA.RA']

**Response:**

```
no record found
```

### g125 [name_lookup] P1/th
**Q:** ขอเบอร์ติดต่อ วีระ อมรจงรัก

**Fails:** missing any-of ['12774', 'VEERA.AM']

**Response:**

```
no record found for วีระ อมรจงรัก.
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
no record found
```

### g128 [name_lookup] P1/th
**Q:** กานติมา การเวกประเสริฐ เบอร์อะไร

**Fails:** missing any-of ['78422', 'KANTIMA.KA', '095-932-5295']

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

### g135 [casual_name_lookup] P0/th
**Q:** พี่นัต ฝ่าย RET เบอร์อะไร

**Fails:** missing any-of ['54337', 'SUNEE.SU']

**Response:**

```
ไม่พบข้อมูล — จากผลที่ค้นหา ยังไม่เจอ “พี่นัต” ในฝ่าย RET ครับ
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
no record found
```

### g156 [nickname_grid] P0/th
**Q:** มิ้น คือใคร

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
ไม่พบข้อมูล — ไม่เจอพนักงานที่ตรงกับ “อ้อม” ในข้อมูลที่ค้นหาไว้ครับ
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
Based on what I found: no record found.
```

### g162 [nickname_grid] P0/th
**Q:** ภาสกร มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g163 [nickname_grid] P0/th
**Q:** ใครชื่อวิจิตร

**Fails:** min_items 3 not met (0)

**Response:**

```
no record found
```

### g164 [nickname_grid] P0/th
**Q:** กฤษฎา มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
no record found
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
no record found for “อรุณ” in SUP.
```

### g178 [nickname_grid] P0/th
**Q:** ขอชื่อ แมว สาขาลาดพร้าว หน่อย

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Jaingambun', 'ใจงามบุญ']

**Response:**

```
no record found
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล
```

### g180 [nickname_grid] P0/th
**Q:** ชื่อเล่น COO คืออะไร

**Fails:** missing any-of ['ไม่มีชื่อเล่นในระบบ', 'ไม่มีชื่อเล่น', 'ไม่ได้ระบุชื่อเล่น']

**Response:**

```
ไม่พบข้อมูล
```

### g182 [nickname_grid] P0/th
**Q:** ชื่อเล่น CPO คืออะไร

**Fails:** missing any-of ['ไม่มีชื่อเล่นในระบบ', 'ไม่มีชื่อเล่น', 'ไม่ได้ระบุชื่อเล่น']

**Response:**

```
no record found
```

### g193 [nickname_grid] P0/th
**Q:** ใครคือปันปัน

**Fails:** missing any-of ['ฤทธิชัย', 'Rittichai']; missing any-of ['แก้วใสภิญโญ', 'Kaewsaiphinyo']

**Response:**

```
no record found
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
no record found
```

### g210 [dept_listing_medium] P1/th
**Q:** แผนก WK-PD มีใครบ้าง

**Fails:** min_items 5 not met (0)

**Response:**

```
no record found — I found no entries for WK-PD.
```

### g215 [dept_listing_medium] P1/en
**Q:** list members of TEC-FE

**Fails:** min_items 5 not met (0)

**Response:**

```
no record found for TEC-FE.
```

### g231 [dept_member_count] P1/th
**Q:** แผนก MKT กี่คน

**Fails:** missing any-of ['110']; missing count 110

**Response:**

```
I can’t give a reliable MKT headcount from the result so far. The lookup found 0 records, but it was not a clean department-wide count.
```

### g235 [dept_member_count] P1/th
**Q:** แผนก SUP-CHAT กี่คน

**Fails:** missing any-of ['36']; missing count 36

**Response:**

```
SUP-CHAT: 0 คนในระบบที่ค้นพบ
```

### g238 [dept_member_count] P1/en
**Q:** size of RET

**Fails:** missing any-of ['380']; missing count 380

**Response:**

```
I can’t confirm the RET size from the results retrieved — the lookup returned 0 due to overly restrictive filters, so I don’t have a reliable count.
```

### g239 [dept_member_count] P1/th
**Q:** แผนก CEO มีทั้งหมดกี่คน

**Fails:** missing any-of ['10']; missing count 10

**Response:**

```
ขอโทษครับ ผลค้นหาที่ได้ก่อนหน้าไม่สามารถยืนยันจำนวนคนของแผนก CEO ได้อย่างถูกต้อง จึงยังตอบจำนวนที่แน่นอนไม่ได้ครับ
```

### g240 [dept_member_count] P1/th
**Q:** แผนก RET-CBI กี่คน

**Fails:** missing any-of ['40']; missing count 40

**Response:**

```
จากผลค้นหาที่มีอยู่ตอนนี้: RET-CBI พบ 0 คน
```

### g254 [org_informal_listing] P0/th
**Q:** ขอรายชื่อ คลื่นเสียง สัก 5 คน

**Fails:** min_items 5 not met (0)

**Response:**

```
จากการค้นหาที่ทำไป: **ไม่พบข้อมูล**
```

### g258 [org_informal_listing] P0/en
**Q:** give me 5 people from SaiFah

**Fails:** min_items 5 not met (0)

**Response:**

```
I couldn’t retrieve a usable SaiFah list from the lookup, so I can’t provide 5 verified people right now.
```

### g266 [org_plus_person] P0/th
**Q:** VP SUP ใคร

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Awutdi', 'อาวุทธ์ดี']

**Response:**

```
ไม่พบข้อมูล
```


_+116 more failures — see results.jsonl_
