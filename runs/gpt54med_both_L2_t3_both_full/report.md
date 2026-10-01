# Run: `gpt54med_both_L2_t3_both_v10full`

**Overall: 615/626 pass (98.2%)**

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
| dept_listing_small | 7/7 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| dept_member_count | 15/15 | 100.0% |
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
| hard_nickname_variant | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| nickname_grid | 60/61 | 98.4% |
| enterprise_shorthand | 19/20 | 95.0% |
| hard_multihop | 24/26 | 92.3% |
| multi_hop | 15/18 | 83.3% |
| hard_implicit_hierarchy | 15/19 | 78.9% |

## By priority

- P0: 223/226 (98.7%)
- P1: 356/364 (97.8%)
- P2: 36/36 (100.0%)

## Failures (11)

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่มีชื่อเล่นในระบบ — เบอร์โทรของ จงรัก สัมโชติ (ปุ๊ก) ไม่มีในระบบครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ของดาวเหนือคือ **วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ, ต่อ **76999**, อีเมล **WICHIAN.PH@FAHMAI.CO.TH**
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
cannot provide this information — the directory does not list reporting lines or “boss” relationships.
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Daonuea คือ **วิเชียร พงหอมกลิ่น** — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ  
อีเมล: **WICHIAN.PH@FAHMAI.CO.TH** | ต่อ **76999** | มือถือ **064-902-5307**
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading JudChuem is **Saran Awutmani (สรัล อาวุทธ์มณี)** — **General Manager of JudChuem**.  
Email: **SARAN.AW@fahmai.co.th** · Ext: **78762**
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ผู้บริหารสูงสุดของแผนก KluenSiang คือ **ราม ลวรรณ (จุ๊บ)** — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง, อีเมล **RAM.LA@FAHMAI.CO.TH**, ต่อ **75965**
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของ WongKhoJon คือ **กฤษ มหาแก้วใส (ขิง)** — ผู้จัดการทั่วไปแบรนด์วงโคจร, ต่อ **74375**, **KRIS.MA@FAHMAI.CO.TH**
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ สังกัด DN-MKT ในฝ่าย DN; ถ้าหมายถึงส่วนงาน DN คนตำแหน่งสูงสุดคือ **คุณเรืองศักดิ์ เทพเกียรติกำจร (รองประธานฝ่ายดาวเหนือ)** เบอร์ต่อ **72280** ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
คุณอภิชัย จิตรานนท์เจริญ อยู่ฝ่าย FIN ครับ  
ตำแหน่งสูงสุดในส่วนงานนี้คือ **กมลา ชัยสนธิ์สว่าง (ประธานเจ้าหน้าที่การเงิน / CFO)** เบอร์ต่อ **74921**
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ มหาวัฒน์สังกัดฝ่าย JC ครับ — คนที่ตำแหน่งสูงสุดในฝ่ายนี้คือ **ราชินี อาทิตย์สุข** (รองประธานฝ่ายจุดเชื่อม) **เบอร์ต่อ 75642**
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าทีมการตลาดคือ **คะวัง กอบสุขรัตน์** (รองประธานฝ่ายการตลาด) — ต่อ **74711**, อีเมล **KWANG.KO@FAHMAI.CO.TH**
```

