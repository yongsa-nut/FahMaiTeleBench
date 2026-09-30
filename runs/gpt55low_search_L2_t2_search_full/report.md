# Run: `gpt55low_search_L2_t2_search_v10full`

**Overall: 412/626 pass (65.8%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| multi_entity_turn | 18/20 | 90.0% |
| bilingual | 36/40 | 90.0% |
| dept_listing_small | 6/7 | 85.7% |
| dept_member_count | 12/15 | 80.0% |
| hard_nickname_variant | 8/10 | 80.0% |
| ceo_president | 3/4 | 75.0% |
| dept_listing_medium | 6/8 | 75.0% |
| deep_multihop | 9/12 | 75.0% |
| noisy_name_form | 14/20 | 70.0% |
| enterprise_shorthand | 14/20 | 70.0% |
| hard_implicit_hierarchy | 13/19 | 68.4% |
| nickname_grid | 37/61 | 60.7% |
| casual_name_lookup | 9/15 | 60.0% |
| counterfactual | 15/25 | 60.0% |
| evp_vs_vp_disambig | 14/25 | 56.0% |
| listing_count | 11/20 | 55.0% |
| evp_identity_by_code | 2/4 | 50.0% |
| email_identity_lookup | 3/6 | 50.0% |
| multi_hop | 9/18 | 50.0% |
| brand_prior | 5/10 | 50.0% |
| superlative | 5/10 | 50.0% |
| surname_family | 11/24 | 45.8% |
| retrieval | 6/14 | 42.9% |
| hard_multihop | 11/26 | 42.3% |
| subsidiary_routing | 5/12 | 41.7% |
| name_lookup | 7/20 | 35.0% |
| org_informal_listing | 2/6 | 33.3% |
| extension_reverse | 2/7 | 28.6% |
| email_mobile_lookup | 2/7 | 28.6% |
| section_listing | 1/4 | 25.0% |
| subsidiary_md | 2/8 | 25.0% |
| vp_identity | 0/5 | 0.0% |
| org_plus_person | 0/3 | 0.0% |
| hard_bridge_lookup | 0/6 | 0.0% |

## By priority

- P0: 164/226 (72.6%)
- P1: 230/364 (63.2%)
- P2: 18/36 (50.0%)

## Failures (214)

### g001 [evp_identity_by_code] P0/en
**Q:** who is the RETVP

**Fails:** missing any-of ['Wiriya', 'วิริยะ']; missing any-of ['Chanchai', 'จันทชัย']

**Response:**

```
no record found
```

### g002 [evp_identity_by_code] P0/th
**Q:** ใครเป็น OPSVP

**Fails:** missing any-of ['Kukrit', 'คึกฤทธิ์']; missing any-of ['Busarakhamwong', 'บุษราคัมวงศ์']

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
no record found
```

### g075 [evp_vs_vp_disambig] P0/th
**Q:** OPSQA ใคร — ไม่ใช่ OPSVP

**Fails:** missing any-of ['Kanok', 'กนก']; missing any-of ['Khaengkadchai', 'เก่งกาจชัย']

**Response:**

```
ไม่พบข้อมูล
```

### g079 [evp_vs_vp_disambig] P0/th
**Q:** B2BACC ใคร — ไม่ใช่ B2BVP

**Fails:** missing any-of ['Thanya', 'ธัญญา']; missing any-of ['Charoenpholphinyo', 'เจริญผลภิญโญ']

**Response:**

```
ไม่พบข้อมูล
```

### g080 [evp_vs_vp_disambig] P0/th
**Q:** หา FIN-ACCDR หน่อย อย่าสับกับ FINVP

**Fails:** missing any-of ['Busaba', 'บุษบา']; missing any-of ['Akaraphat', 'อัครพัฒน์']

**Response:**

```
ไม่พบข้อมูล
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
no record found
```

### g093 [vp_identity] P1/en
**Q:** who's VP of logistics

**Fails:** missing any-of ['Natthakan', 'ณัฐกานต์']; missing any-of ['Sriaromdee', 'ศรีอารมณ์ดี']

**Response:**

```
no record found
```

### g105 [ceo_president] P1/th
**Q:** CEO คือใครนะ

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

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
no record found
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
no record found
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
no record found
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

### g129 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ ฤทธิรงค์ บุญอินทรีย์

**Fails:** missing any-of ['73128', 'RITTHIRONG.BU', '092-398-0784']

**Response:**

```
ไม่พบข้อมูล
```

### g132 [name_lookup] P1/en
**Q:** ext for Boonruang Jaingamphong

**Fails:** missing any-of ['35442', 'BOONRUANG.JA', '088-563-7219']

**Response:**

```
no record found
```

### g134 [casual_name_lookup] P0/en
**Q:** Hook from SF, what's the number

**Fails:** missing any-of ['73096', 'YADTHIP.AN']

**Response:**

```
no record found
```

### g137 [casual_name_lookup] P0/th
**Q:** น้องโดนัท ทีม TEC เบอร์หน่อย

**Fails:** missing any-of ['73933', 'TAKSIN.NA']

**Response:**

```
ไม่พบข้อมูล
```

### g140 [casual_name_lookup] P0/en
**Q:** khun Jub in OPS — ext?

**Fails:** missing any-of ['33046', 'RITTHIRONG.KI']

**Response:**

```
no record found
```

### g141 [casual_name_lookup] P0/th
**Q:** พี่มิ้น ฝ่าย FIN เบอร์อะไร

**Fails:** missing any-of ['75703', 'BENJAWAN.CH']

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

### g157 [nickname_grid] P0/th
**Q:** ไผ่ มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g158 [nickname_grid] P0/th
**Q:** พลอย คือใคร

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g161 [nickname_grid] P0/th
**Q:** ใครชื่อไพบูลย์

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
ไม่พบข้อมูล
```

### g164 [nickname_grid] P0/th
**Q:** กฤษฎา มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g165 [nickname_grid] P0/th
**Q:** ขอรายชื่อคนชื่อปิติ

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g168 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นไก่กี่คน

**Fails:** missing any-of ['12']; missing count 12

**Response:**

```
ไม่พบข้อมูล
```

### g169 [nickname_grid] P0/th
**Q:** เวฟ มีกี่คน

**Fails:** missing any-of ['6']; missing count 6

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

### g176 [nickname_grid] P0/th
**Q:** ขอชื่อ นีโอ สาขา BNA หน่อย

**Fails:** missing any-of ['Dokrak', 'ดอกรัก']; missing any-of ['Anucharoenphol', 'อนุเจริญผล']

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

### g197 [dept_listing_small] P1/th
**Q:** แผนก FIN-EXEC มีใครบ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล ในแผนก/ส่วนงาน FIN-EXEC
```

### g212 [dept_listing_medium] P1/en
**Q:** who's in OPS-FAC

**Fails:** min_items 5 not met (0)

**Response:**

```
no record found
```


_+164 more failures — see results.jsonl_
