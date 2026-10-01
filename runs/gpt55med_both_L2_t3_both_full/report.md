# Run: `gpt55med_both_L2_t3_both_v10full`

**Overall: 599/626 pass (95.7%)**

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
| casual_name_lookup | 15/15 | 100.0% |
| nickname_grid | 61/61 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| refuse | 90/90 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| superlative | 10/10 | 100.0% |
| bilingual | 39/40 | 97.5% |
| listing_count | 19/20 | 95.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| dept_member_count | 14/15 | 93.3% |
| deep_multihop | 11/12 | 91.7% |
| dept_listing_small | 6/7 | 85.7% |
| subsidiary_routing | 10/12 | 83.3% |
| hard_nickname_variant | 8/10 | 80.0% |
| hard_multihop | 20/26 | 76.9% |
| hard_implicit_hierarchy | 14/19 | 73.7% |
| multi_hop | 12/18 | 66.7% |

## By priority

- P0: 222/226 (98.2%)
- P1: 342/364 (94.0%)
- P2: 35/36 (97.2%)

## Failures (27)

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
CEO-SEC not found, but CEO’s secretary/EA is Orraya Watcharakan — ext. 75665, ORRAYA.WA@FAHMAI.CO.TH.
```

### g239 [dept_member_count] P1/th
**Q:** แผนก CEO มีทั้งหมดกี่คน

**Fails:** missing any-of ['10']; missing count 10

**Response:**

```
แผนก CEO มีทั้งหมด 1 คน
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ทีม CEO-CoS มี 1 คน:

- กิตติคุณ พงจงรัก (บูม) — Chief of Staff, ext. 79367, 062-174-6941, KITTIKHUN.PH@FAHMAI.CO.TH
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น** — ext. **76999**, มือถือ **064-902-5307**
```

### g367 [hard_implicit_hierarchy] P0/en
**Q:** who reports to the COO

**Fails:** min_items 1 not met (0)

**Response:**

```
cannot provide this information — reporting lines aren’t tracked in the directory.
```

### g389 [hard_nickname_variant] P0/th
**Q:** พี่มุกกี้เบอร์อะไร

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอชื่อเล่น “มุก” หลายคนครับ ระบุชื่อจริงหรือแผนกหน่อยได้ไหม จะได้ให้เบอร์ถูกคนครับ
```

### g390 [hard_nickname_variant] P1/th
**Q:** ปุ๊กกี้อยู่ทีมไหน

**Fails:** missing any-of ['ลัดดาวรรณ', 'Laddawan', 'ประยุทธ์']

**Response:**

```
เจอชื่อเล่น “ปุ๊ก” หลายคน (13 คน) เลยครับ—ขอชื่อจริงหรือแผนกเพิ่มหน่อย จะเช็กทีมให้ตรงคนได้ครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์สังกัดแผนก DN (ดาวเหนือ) — ผู้บริหารสูงสุดคือ วิเชียร พงหอมกลิ่น  
อีเมล: WICHIAN.PH@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์อยู่แผนก JC (จุดเชื่อม) — ผู้บริหารสูงสุดคือ สรัล อาวุทธ์มณี, อีเมล SARAN.AW@FAHMAI.CO.TH
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพรอยู่แผนก KS (คลื่นเสียง) — ผู้บริหารสูงสุดคือ ราม ลวรรณ  
อีเมล: RAM.LA@FAHMAI.CO.TH
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพลอยู่แผนก WK (วงโคจร) — ผู้บริหารสูงสุดคือ กฤษ มหาแก้วใส  
อีเมล: KRIS.MA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของ Daonuea คือ **วิเชียร พงหอมกลิ่น** — General Manager of DaoNuea  
โทร: **76999** / **064-902-5307** | อีเมล: **WICHIAN.PH@FAHMAI.CO.TH**
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
Saran Awutmani — General Manager of JudChuem. Email: SARAN.AW@FAHMAI.CO.TH, ext. 78762, mobile 064-655-7513.
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของ KluenSiang คือ **ราม ลวรรณ** — GM แบรนด์คลื่นเสียง  
อีเมล: **RAM.LA@FAHMAI.CO.TH**, เบอร์ต่อ **75965**
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของ Wongkhojon คือ **กฤษ มหาแก้วใส** — General Manager of Wongkhojon  
อีเมล: **KRIS.MA@FAHMAI.CO.TH**, ต่อ **74375**
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g537 [listing_count] P1/en
**Q:** How many employees are in the DN department at Manager level who started in 2020?

**Fails:** missing count 2

**Response:**

```
Based on the lookup I ran: **0 employees**.
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์อยู่ส่วนงาน DN (ดาวเหนือ) — ผู้ที่ตำแหน่งสูงสุดคือคุณวิเชียร พงหอมกลิ่น (GM ดาวเหนือ) เบอร์ต่อ 76999
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
คุณอภิชัยอยู่ฝ่าย FIN — ผู้ตำแหน่งสูงสุดคือคุณกมลา ชัยสนธิ์สว่าง (CFO) เบอร์ต่อ 74921
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คุณมนตราอยู่ HR — คนตำแหน่งสูงสุดคือ ณฐามน อภิชัยดี (CHRO) เบอร์ต่อ 79303 ครับ
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์อยู่ส่วนงาน JC (จุดเชื่อม) — คนที่ตำแหน่งสูงสุดคือ **สรัล อาวุทธ์มณี** (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม), เบอร์ต่อ **78762**
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์อยู่ KS (คลื่นเสียง) — ผู้บริหารสูงสุดคือ **ราม ลวรรณ** (GM) เบอร์ต่อ **75965**
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
คุณคำรณอยู่ส่วนงาน OPS — คนตำแหน่งสูงสุดคือ พงษ์กานต์ ราชชากัญญ์ (COO) เบอร์ต่อ 75464
```

### g685 [enterprise_shorthand] P1/en
**Q:** Who is the head of the tech department?

**Fails:** missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
Rittichai Kaewsaiphiny (CTO) — ext. 75477, mobile 082-837-1298, RITTICHAI.KA@FAHMAI.CO.TH
```

### g771 [subsidiary_routing] P1/en
**Q:** Who heads the marketing unit of the DaoNuea brand?

**Fails:** missing any-of ['Phussadee', 'พุสดี']; missing any-of ['Chaisaidi', 'ชัยสัยดี']

**Response:**

```
Kovit Mahamani heads DaoNuea brand marketing — ext. 77251, KOVIT.MA@FAHMAI.CO.TH, mobile 094-711-0811.
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
Lalana Jaikieowsathit heads KluenSiang Brand Operations — ext. 73432, LALANA.JA@FAHMAI.CO.TH.
```

### g826 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the most employees — what's the email of the VP who heads that department?

**Fails:** missing any-of ['WIRIYA.CH@FAHMAI.CO.TH']

**Response:**

```
Based on what I found: **WIRAT.SO@FAHMAI.CO.TH** — Wirat Sombusarakham, VP of SaiFah (SF).
```

