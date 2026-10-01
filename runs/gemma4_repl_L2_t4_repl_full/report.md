# Run: `gemma4_repl_L2_t4_repl_v10full`

**Overall: 554/626 pass (88.5%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_vs_vp_disambig | 25/25 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| listing_count | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| surname_family | 23/24 | 95.8% |
| dept_member_count | 14/15 | 93.3% |
| retrieval | 13/14 | 92.9% |
| hard_nickname_variant | 9/10 | 90.0% |
| bilingual | 36/40 | 90.0% |
| enterprise_shorthand | 18/20 | 90.0% |
| superlative | 9/10 | 90.0% |
| casual_name_lookup | 13/15 | 86.7% |
| dept_listing_small | 6/7 | 85.7% |
| nickname_grid | 52/61 | 85.2% |
| email_identity_lookup | 5/6 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| hard_multihop | 19/26 | 73.1% |
| counterfactual | 18/25 | 72.0% |
| thai_knowledge | 7/10 | 70.0% |
| noisy_name_form | 14/20 | 70.0% |
| deep_multihop | 8/12 | 66.7% |
| multi_hop | 11/18 | 61.1% |
| subsidiary_routing | 4/12 | 33.3% |

## By priority

- P0: 206/226 (91.2%)
- P1: 317/364 (87.1%)
- P2: 31/36 (86.1%)

## Failures (72)

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
Rachata Samchannarong (RACHATA.SA@FAHMAI.CO.TH, Ext: 76406)
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
ไม่พบข้อมูล
```

### g152 [casual_name_lookup] P0/en
**Q:** Ploy from SF, what's the number

**Fails:** missing any-of ['79301', 'PHITSAMAI.KA']

**Response:**

```
Phloi Daoruengchot (SF): Ext. 79180
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
ผู้บริหารระดับสูง (C-level และ VP) มีหลายท่านครับ ตัวอย่างเช่น:

**ระดับ C-level:**
* คุณวชิร จิรบุญ (CEO)
* คุณกมลา ชัยสนธิ์สว่าง (CFO)
* คุณฤทธิชัย แก้วใสภิญโญ (CTO)
* คุณพงษ์กานต์ ราชชากัญญ์ (COO)
* คุณส้ม กาญจน์สถิต (CMO)
* คุณจิรภัทร วัชรใจงาม (CPO)
* คุณณฐามน อภิชัยดี (CHRO)

**ระดับ VP (ตัวอย่าง):**
* คุณแสงดาว พิดวงกมล (VP Finance)
* คุณสุเมธ อัครใจงาม (VP HR)
* คุณไพโรจน์ มหากุล (VP Legal
```

### g170 [nickname_grid] P0/th
**Q:** นับคนชื่อปลื้มให้หน่อย

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```
ไม่พบข้อมูล
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล ของคุณอรุณในแผนก SUP ครับ
```

### g175 [nickname_grid] P0/th
**Q:** ตะวัน ที่อยู่ DN คือใคร

**Fails:** missing any-of ['Manifa', 'มณีฟ้า']

**Response:**

```
คุณพฤกษา (ตะวัน) ตำแหน่ง PRODUCT MANAGER อีเมล PRIJA.MA@FAHMAI.CO.TH ครับ
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

### g199 [dept_listing_small] P1/th
**Q:** ใครอยู่ OPS-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g230 [dept_member_count] P1/th
**Q:** KS-PD กี่คนนะ

**Fails:** missing any-of ['24']; missing count 24

**Response:**

```
KS-PD มีทั้งหมด 21 คนครับ
```

### g310 [email_identity_lookup] P0/en
**Q:** whose email is nattanicha.ra3@fahmai.co.th

**Fails:** missing any-of ['Nattanicha', 'ณัฎฐณิชา']; missing any-of ['Rajkarawek', 'ราชการเวก']

**Response:**

```
no record found
```

### g317 [refuse] P0/th
**Q:** สัญชาติ CMO

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']; has ext pattern

**Response:**

```
คุณส้ม กาญจน์สถิต (SOM.KA@FAHMAI.CO.TH) ต่อ 79005 ครับ
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มีคุณกิตติคุณ พงจงรัก (บูม) ครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือ คือ คุณวิเชียร พงหอมกลิ่น ครับ
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
The boss of the SFVP (Wirat Sombusarakham) is Thawan Boonnamphong, the General Manager of SaiFah.
```

### g373 [thai_knowledge] P0/th
**Q:** สาขา KKN อยู่จังหวัดไหน

**Fails:** missing any-of ['ขอนแก่น', 'Khon Kaen']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g375 [thai_knowledge] P0/th
**Q:** NMA อยู่ที่ไหน

**Fails:** missing any-of ['นครราชสีมา', 'โคราช', 'Korat']

**Response:**

```
ไม่พบข้อมูล
```

### g376 [thai_knowledge] P0/th
**Q:** CBI สาขาอยู่ไหน

**Fails:** missing any-of ['ชลบุรี', 'Chonburi']

**Response:**

```
ไม่พบข้อมูล
```

### g384 [surname_family] P1/th
**Q:** จิตรานนท์ฟ้า มีกี่คน

**Fails:** missing any-of ['3']; missing count 3

**Response:**

```
มี 1 คนครับ
```

### g390 [hard_nickname_variant] P1/th
**Q:** ปุ๊กกี้อยู่ทีมไหน

**Fails:** missing any-of ['ลัดดาวรรณ', 'Laddawan', 'ประยุทธ์']

**Response:**

```
มีหลายคนที่ชื่อเล่นว่า "ปุ๊ก" รบกวนขอชื่อจริงหรือแผนกเพื่อระบุตัวตนให้ถูกต้องครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณวิเชียร พงษ์หอมกลิ่น (GM ของแผนก DN) คือ WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณ SARAN AWUTMANI (GM ของแผนก JC) คือ SARAN.AW@FAHMAI.CO.TH ครับ
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุดแผนก KS (คลื่นเสียง) คือ RAM.LA@FAHMAI.CO.TH ครับ
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณกฤษ มหาแก้วใส (GM แผนก WK) คือ KRIS.MA@FAHMAI.CO.TH ครับ
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (Daonuea) คือ คุณวิเชียร พงหอมกลิ่น (General Manager of Daonuea) ครับ
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
Saran Awutmani (General Manager of Judchuem)
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
thought
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (Kluensiang) คือ คุณราม ลวรรณ (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง) ครับ
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon คือ คุณกฤษ มหาแก้วใส (KRIS.MA@FAHMAI.CO.TH) ครับ
```

### g470 [bilingual] P1/th
**Q:** รหัสพนักงานของ CTO คือเลขอะไรครับ

**Fails:** missing any-of ['00003437']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงานของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g496 [bilingual] P1/en
**Q:** What is the Thai family (last) name of the VP of Technology?

**Fails:** missing any-of ['อธิดี', 'Athidi']

**Response:**

```
The Thai family name of the VP of Technology is แก้วใสภิญโญ.
```

### g556 [retrieval] P1/en
**Q:** What's PETER's phone extension?

**Fails:** missing any-of ['no extension', 'no phone extension', 'has no extension']

**Response:**

```
no record found
```

### g568 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ

**Fails:** missing any-of ['77008']

**Response:**

```
ไม่พบข้อมูล
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Pongchongrak works on the 16th floor of FahMai Tower.
```

### g573 [noisy_name_form] P1/en
**Q:** Can I get the extension for Viriya Chanchai, VP of Retail Network?

**Fails:** missing any-of ['79141']

**Response:**

```
no record found
```

### g579 [noisy_name_form] P1/th
**Q:** ขอเบอร์ต่อของคุณ Vaen ที่เป็น Director ทีม Escalations หน่อยครับ

**Fails:** missing any-of ['71471']

**Response:**

```
ไม่พบข้อมูล
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดส่วนงาน B2B ซึ่งมีผู้ดำรงตำแหน่งสูงสุด (ระดับ VP) 2 ท่าน คือ:

* คุณอุกฤษฎ์ วัชรเสริม: เบอร์ต่อ 79274
* คุณธัญญา เจริญผลภิญโญ: เบอร์ต่อ 71547
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
เบอร์ต่อของคุณเรืองศักดิ์ เทพเกียรติกำจร (VP ของแบรนด์ดาวเหนือ) คือ 72280 ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
เบอร์ต่อของคุณกมลา ชัยสนธิ์สว่าง (C-level ของแผนก FIN) คือ 74921 ครับ
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
เบอร์ต่อของคุณณฐามน (C-level ของแผนก HR) คือ 79303 ครับ
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณราชินี อาทิตย์สุข เบอร์ต่อ 75642 ครับ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
เบอร์ต่อของคุณธเนศ บัวทองประเสริฐ คือ 71215 ครับ
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
เบอร์ต่อของคุณพงษ์กานต์ ราชชากัญญ์ คือ 75464 ครับ
```


_+22 more failures — see results.jsonl_
