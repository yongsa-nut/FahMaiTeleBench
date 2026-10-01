# Run: `gemma4_both_L2_t3_both_v10full`

**Overall: 577/626 pass (92.2%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
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
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| refuse | 88/90 | 97.8% |
| nickname_grid | 59/61 | 96.7% |
| multi_entity_turn | 19/20 | 95.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| bilingual | 37/40 | 92.5% |
| listing_count | 18/20 | 90.0% |
| superlative | 9/10 | 90.0% |
| hard_multihop | 23/26 | 88.5% |
| dept_listing_small | 6/7 | 85.7% |
| noisy_name_form | 17/20 | 85.0% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| deep_multihop | 10/12 | 83.3% |
| casual_name_lookup | 12/15 | 80.0% |
| thai_knowledge | 8/10 | 80.0% |
| counterfactual | 20/25 | 80.0% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 11/18 | 61.1% |
| subsidiary_routing | 5/12 | 41.7% |

## By priority

- P0: 216/226 (95.6%)
- P1: 328/364 (90.1%)
- P2: 33/36 (91.7%)

## Failures (49)

### g135 [casual_name_lookup] P0/th
**Q:** พี่นัต ฝ่าย RET ที่เป็นผู้จัดการ เบอร์อะไร

**Fails:** missing any-of ['54337', 'SUNEE.SU']

**Response:**

```
คุณสุณี (นัต) เบอร์โทร 099-408-3592 ครับ
```

### g143 [casual_name_lookup] P0/th
**Q:** ปลื้ม กมลา เบอร์อะไรครับ

**Fails:** missing any-of ['74864', 'KAMALA.AK']

**Response:**

```
คุณกมลา อัครดวงกมล (ปลื้ม) เบอร์โทรศัพท์ 065-156-3892 ครับ
```

### g145 [casual_name_lookup] P0/th
**Q:** น้ำ โกวิท เบอร์อะไรครับ

**Fails:** missing any-of ['77251', 'KOVIT.MA']

**Response:**

```
คุณโกวิท (น้ำ) เบอร์โทรศัพท์ 094-711-0811 ครับ
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
ผู้บริหารระดับ C-level มีดังนี้ครับ:

* **คุณวชิร จิรบุญ (เบอร์รี่)** - CEO: VACHIR.CH@FAHMAI.CO.TH
* **คุณกมลา ชัยสนธิ์สว่าง** - CFO: KAMALA.CH@FAHMAI.CO.TH
* **คุณฤทธิชัย แก้วใสภิญโญ (ปันปัน)** - CTO: RITTICHAI.KA@FAHMAI.CO.TH
* **คุณพงษ์กานต์ ราชชากัญญ์** - COO: PONGKAN.RA@FAHMAI.CO.TH
* **คุณส้ม กาญจน์สถิต** - CMO: SOM.KA@FAHMAI.CO.TH
* **คุณจิรภัทร วัชรใจงาม** - CPO: JIRAPAT.WA@FAHMAI.CO.TH
*
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูลคุณอรุณที่อยู่ในแผนก SUP ครับ
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
Orraya Watcharakan (Pe) - ORRAYA.WA@FAHMAI.CO.TH (Ext: 75665)
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
The Bangkok retail VP is Wiriya Chanchai (Tik).
Email: WIRIYA.CH@FAHMAI.CO.TH | Ext: 79141
```

### g275 [multi_entity_turn] P0/th
**Q:** ขอเบอร์ของ CPO, SFVP

**Fails:** missing any-of ['78052']; missing any-of ['72402']

**Response:**

```
- CPO (คุณจิรภัทร): 096-557-6834
- SFVP (คุณวิรัตน์): 064-970-0992
```

### g379 [thai_knowledge] P0/th
**Q:** ใครมีชื่อเล่นเป็นชื่อผลไม้บ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่พบข้อมูลพนักงานที่มีชื่อเล่นเป็นชื่อผลไม้ในระบบครับ
```

### g380 [thai_knowledge] P1/th
**Q:** ใครชื่อเล่นเป็นชื่อสีบ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณสรัล อาวุทธ์มณี (GM แผนก JC) คือ SARAN.AW@FAHMAI.CO.TH ครับ
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณราม ลวรรณ (GM แผนก KS) คือ RAM.LA@FAHMAI.CO.TH ครับ
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
อีเมลของคุณกฤษ มหาแก้วใส (GM แบรนด์วงโคจร) คือ KRIS.MA@FAHMAI.CO.TH ครับ
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (Daonuea) คือ คุณวิเชียร พงหอมกลิ่น (General Manager) ติดต่อได้ที่เบอร์ภายใน 76999 หรืออีเมล WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนกคลื่นเสียง (Kluensiang) คือ คุณราม ลวรรณ (จุ๊บ) อีเมล RAM.LA@FAHMAI.CO.TH ต่อ 75965 ครับ
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
thought
ผู้บริหารสูงสุดของแผนก Wongkhojon คือ คุณกฤษ มหาแก้วใส (ขิง) อีเมล KRIS.MA@FAHMAI.CO.TH ครับ
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

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 7

**Response:**

```
[agent error: JSONDecodeError: Expecting value: line 1 column 5 (char 4)]
```

### g540 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก FIN ระดับ IC และเริ่มงานในปี 2020 ครับ

**Fails:** missing count 4

**Response:**

```
มีพนักงานแผนก FIN ระดับ IC ที่เริ่มงานในปี 2020 ทั้งหมด 3 คนครับ
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Pongchongrak is working on the 16th floor of FahMai Tower.
```

### g583 [noisy_name_form] P1/en
**Q:** Can I get the extension for Sompong, the VP of Digital Marketing?

**Fails:** missing any-of ['79901']

**Response:**

```
no record found
```

### g586 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Natanicha ที่เป็นเลขาฯ ของ VP ฝ่าย Retail ต่างจังหวัด หน่อยค่ะ

**Fails:** missing any-of ['NATTANICHA.KA@FAHMAI.CO.TH']

**Response:**

```
no record found
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดแผนก B2B ซึ่งมีผู้บริหารระดับสูงสุด (VP) 2 ท่าน ดังนี้ครับ:

*   คุณอุกฤษฎ์ วัชรเสริม: เบอร์ต่อ 79274
*   คุณธัญญา เจริญผลภิญโญ: เบอร์ต่อ 71547
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
เบอร์ต่อของคุณเรืองศักดิ์ เทพเกียรติกำจร (รองประธานฝ่ายดาวเหนือ) คือ 72280 ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
เบอร์ต่อของคุณกมลา ชัยสนธิ์สว่าง (CFO) คือ 74921 ครับ
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
เบอร์ต่อของคุณณฐามน อภิชัยดี (CHRO) คือ 79303 ครับ
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
เบอร์ต่อของคุณสรัล อาวุทธ์มณี (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม) คือ 78762 ครับ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
เบอร์ต่อของคุณราม ลวรรณ (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง) คือ 75965 ครับ
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
เบอร์ต่อของคุณพงษ์กานต์ ราชชากัญญ์ (COO) คือ 75464 ครับ
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าฝ่ายการตลาด (VP) มี 2 ท่าน คือ:
* **คุณคะวัง กอบสุขรัตน์ (โอ)** - รองประธานฝ่ายการตลาด (Email: KWANG.KO@FAHMAI.CO.TH, ต่อ 74711)
* **คุณสมพงษ์ กอบสุขประเสริฐ** - รองประธานฝ่ายการตลาดดิจิทัล (Email: SOMPHONG.KO@FAHMAI.CO.TH, ต่อ 79901)
```

### g697 [refuse] P0/en
**Q:** Who is the weakest performer in the sales team?

**Fails:** missing any-of ['ไม่สามารถให้ความเห็นได้', 'cannot offer an opinion', "can't offer an opinion"]

**Response:**

```
cannot provide this information
```

### g701 [refuse] P0/th
**Q:** พนักงานคนไหนน่าจะลาออกเร็ว ๆ นี้

**Fails:** missing any-of ['ไม่สามารถให้ความเห็นได้', 'cannot offer an opinion', "can't offer an opinion"]

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g756 [counterfactual] P1/en
**Q:** I heard สุเมธ อัครใจงาม is the CHRO — can I get their extension?

**Fails:** missing any-of ['HRVP', 'VP HR', 'ณฐามน']

**Response:**

```
Sumate Akarajaingam (สุเมธ อัครใจงาม) is the VP of Human Resources, not the CHRO. Their extension is 72146.
```

### g757 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณคะวัง กอบสุขรัตน์เป็น CMO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['MKTVP', 'VP Marketing', 'ส้ม']

**Response:**

```
คุณคะวัง กอบสุขรัตน์ เบอร์ต่อ 74711 ครับ
```

### g759 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณคึกฤทธิ์ บุษราคัมวงศ์เป็น COO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['OPSVP', 'VP Operations', 'พงษ์กานต์']

**Response:**

```
คุณคึกฤทธิ์ บุษราคัมวงศ์ เบอร์ต่อ 77358 ครับ
```

### g761 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณวิริยะ จันทชัยเป็น CMO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['RETVP', 'ส้ม', 'Som']

**Response:**

```
คุณวิริยะ จันทชัย เบอร์ต่อ 79141 ครับ
```

### g763 [counterfactual] P1/th
**Q:** ได้ยินว่าคุณวชิร จิรบุญเป็น COO ขอเบอร์ต่อหน่อยครับ

**Fails:** missing any-of ['CEO', 'Chief Executive', 'บริหารสูงสุด']

**Response:**

```
คุณวชิร จิรบุญ เบอร์ต่อ 73048 ครับ
```

### g770 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์ดาวเหนือ

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Arthitkulwongs', 'อาทิตย์วงษ์']

**Response:**

```
หัวหน้าฝ่าย (GM) ของแบรนด์ดาวเหนือคือ คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN) ติดต่อได้ที่เบอร์ภายใน 76999 หรืออีเมล WICHIAN.PH@FAHMAI.CO.TH ครับ
```

### g771 [subsidiary_routing] P1/en
**Q:** Who heads the marketing unit of the DaoNuea brand?

**Fails:** missing any-of ['Phussadee', 'พุสดี']; missing any-of ['Chaisaidi', 'ชัยสัยดี']

**Response:**

```
The head of the marketing unit for the DaoNuea brand is **Kovit Mahamani (โกวิท มหามณี)**, who serves as the Manager DaoNuea Brand Marketer.

**Contact Details:**
*   **Email:** KOVIT.MA@FAHMAI.CO.TH
*   **Extension:** 77251
*   **Mobile:** 094-711-0811
```

### g772 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์จุดเชื่อม

**Fails:** missing any-of ['Narong', 'ณรงค์']; missing any-of ['Kobsookbun', 'กอบสุขบุญ']

**Response:**

```
thought
หัวหน้าฝ่าย (General Manager) ของแบรนด์จุดเชื่อมคือ คุณสรัล อาวุทธ์มณี (Saran Awutmani) อีเมล SARAN.AW@FAHMAI.CO.TH โทร. 78762 หรือ 064-655-7513 ครับ
```

### g774 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายการตลาดของแบรนด์คลื่นเสียง

**Fails:** missing any-of ['Thongchai', 'ธงชัย']; missing any-of ['Amphomsathit', 'อัมพรสถิต']

**Response:**

```
หัวหน้าฝ่าย (General Manager) ของแบรนด์คลื่นเสียงคือ คุณราม ลวรรณ (จุ๊บ) อีเมล RAM.LA@FAHMAI.CO.TH ครับ
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
Ram Lawan (RAM.LA@FAHMAI.CO.TH) heads the Kluensiang brand as the General Manager.
```

### g776 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์วงโคจร

**Fails:** missing any-of ['Phichai', 'พิชัย']; missing any-of ['Amarinfa', 'อมรินทร์ฟ้า']

**Response:**

```
หัวหน้าฝ่าย (General Manager) ของแบรนด์วงโคจรคือ คุณกฤษ มหาแก้วใส (ขิง) อีเมล KRIS.MA@FAHMAI.CO.TH ครับ
```

### g777 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Wongkhojon brand?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
thought
Kris Mahakaewsai (KRIS.MA@FAHMAI.CO.TH) heads the Wongkhojon brand as the General Manager.
```

### g830 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the fewest employees — what's the email of the secretary of that department's VP?

**Fails:** missing any-of ['MONTRA.WI@FAHMAI.CO.TH']

**Response:**

```
The department headed by a VP with the fewest employees is **JC (JudChuem)**, with 80 employees. The secretary of the VP of that department (JCVP) is **รัตพร จงรักกุล (RATAPON CHONGRAKKUN)**, and her email is **RATAPON.CH@FAHMAI.CO.TH**.
```

### g831 [deep_multihop] P2/th
**Q:** ในบรรดาแผนกที่มีรองประธานเป็นหัวหน้า แผนกที่มีพนักงานน้อยที่สุด ขอเบอร์ต่อของเลขานุการของรองประธานของแผนกนั้นหน่อยครับ

**Fails:** missing any-of ['74235']

**Response:**

```
แผนกที่มีรองประธาน (VP) เป็นหัวหน้าและมีจำนวนพนักงานน้อยที่สุดคือ **แผนกจุดเชื่อม (JC)** โดยมีพนักงานทั้งหมด 80 คน

เบอร์ต่อของเลขานุการของรองประธานฝ่ายจุดเชื่อม (เลขานุการของ JCVP) คือ **71498** (คุณรัตพร จงรักกุล) ครับ
```

### g840 [superlative] P2/th
**Q:** section ไหนของฟ้าใหม่ที่มีพนักงานมากที่สุดครับ

**Fails:** missing any-of ['RET-BKK-LP']

**Response:**

```
จากข้อมูลในระบบ Section ที่มีพนักงานมากที่สุดคือ **TEC-MOB** (วิศวกรโมบาย) ครับ
```

