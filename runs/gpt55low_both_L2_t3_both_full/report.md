# Run: `gpt55low_both_L2_t3_both_full`

**Overall: 587/626 pass (93.8%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| evp_vs_vp_disambig | 25/25 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| nickname_grid | 61/61 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_member_count | 15/15 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| bilingual | 40/40 | 100.0% |
| retrieval | 14/14 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| superlative | 10/10 | 100.0% |
| refuse | 89/90 | 98.9% |
| counterfactual | 24/25 | 96.0% |
| enterprise_shorthand | 19/20 | 95.0% |
| surname_family | 22/24 | 91.7% |
| name_lookup | 18/20 | 90.0% |
| listing_count | 18/20 | 90.0% |
| noisy_name_form | 18/20 | 90.0% |
| dept_listing_medium | 7/8 | 87.5% |
| extension_reverse | 6/7 | 85.7% |
| subsidiary_routing | 10/12 | 83.3% |
| deep_multihop | 10/12 | 83.3% |
| hard_nickname_variant | 8/10 | 80.0% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| hard_multihop | 20/26 | 76.9% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 12/18 | 66.7% |
| email_mobile_lookup | 4/7 | 57.1% |

## By priority

- P0: 221/226 (97.8%)
- P1: 336/364 (92.3%)
- P2: 30/36 (83.3%)

## Failures (39)

### g114 [name_lookup] P1/th
**Q:** ขอเบอร์ สมพงษ์ อินทรีย์นาม หน่อย

**Fails:** missing any-of ['48530', 'SOMPHONG.IN', '085-412-9461']

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

### g212 [dept_listing_medium] P1/en
**Q:** who's in OPS-FAC

**Fails:** min_items 5 not met (4)

**Response:**

```
OPS-FAC has 23 people. Key contacts:

- KRITSADA THANAKAEWSAI — Manager Facilities Officer — ext. 76199 — KRITSADA.TH2@FAHMAI.CO.TH
- NARIN KAEWSAIJAI — Manager Facilities Officer — ext. 76684 — NARIN.KA@FAHMAI.CO.TH
- YING THANACHAIDEE — Lead Facilities Officer — ext. 79536 — YING.TH@FAHMAI.CO.TH
- CHONLATHEE ATHIKOBSOOK — Lead Facilities Officer — ext. 74105 — CHONLATHEE.AT@FAHMAI.CO.TH

There a
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
Wiriya Chanchai — VP Retail Network  
Ext. 79141, 082-034-8608, WIRIYA.CH@FAHMAI.CO.TH
```

### g288 [extension_reverse] P2/th
**Q:** ต่อ 78417 เบอร์ใคร

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Rajchaicharoen', 'ราชชัยเจริญ']

**Response:**

```
ไม่พบข้อมูล
```

### g300 [email_mobile_lookup] P2/th
**Q:** 093-978-9586 ใคร

**Fails:** missing any-of ['Rattana', 'รัตตนา']; missing any-of ['Charoenfa', 'เจริญฟ้า']

**Response:**

```
ไม่พบข้อมูล
```

### g302 [email_mobile_lookup] P2/th
**Q:** 091-523-9087 เบอร์ใครคะ

**Fails:** missing any-of ['Chayaphon', 'ชยพล']; missing any-of ['Anukraisee', 'อนุไกรศรี']

**Response:**

```
ไม่พบข้อมูล
```

### g305 [email_mobile_lookup] P2/en
**Q:** whose mobile is 083-026-8696

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Areeprasert', 'อารีประเสริฐ']

**Response:**

```
no record found
```

### g333 [refuse] P0/th
**Q:** VP การตลาดของ LG คือใคร

**Fails:** missing any-of ['ไม่ใช่ข้อมูลของฟ้าใหม่', 'ไม่ใช่พนักงานฟ้าใหม่', 'ไม่ใช่ข้อมูลฟ้าใหม่']; has ext pattern

**Response:**

```
VP การตลาดของฟ้าใหม่คือ คะวัง กอบสุขรัตน์ (โอ) — ext. 74711, 088-904-0088, KWANG.KO@FAHMAI.CO.TH
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
CEO-CoS มี 1 คน:

- กิตติคุณ พงจงรัก (บูม) — Chief of Staff, ext. 79367, 062-174-6941, KITTIKHUN.PH@FAHMAI.CO.TH
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ดาวเหนือคือ **วิเชียร พงหอมกลิ่น**  
โทร. **76999** / มือถือ **064-902-5307** / **WICHIAN.PH@FAHMAI.CO.TH**
```

### g389 [hard_nickname_variant] P0/th
**Q:** พี่มุกกี้เบอร์อะไร

**Fails:** missing any-of ['ยุพา', 'Yu-Pha', 'งามจิตร']

**Response:**

```
เจอชื่อเล่น “มุก” หลายคนครับ ขอชื่อจริง/แผนกเพิ่มนิดนึงว่าเป็นมุกไหน?
```

### g390 [hard_nickname_variant] P1/th
**Q:** ปุ๊กกี้อยู่ทีมไหน

**Fails:** missing any-of ['ลัดดาวรรณ', 'Laddawan', 'ประยุทธ์']

**Response:**

```
มีหลายคนชื่อเล่น “ปุ๊ก” ครับ รบกวนขอชื่อจริง/นามสกุล หรือทีม/สาขาเพิ่มเติมหน่อยครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์อยู่แผนก DN (ดาวเหนือ) — ผู้บริหารสูงสุดคือคุณวิเชียร พงหอมกลิ่น  
อีเมล: WICHIAN.PH@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์สังกัดอยู่ (JC) คือ **SARAN.AW@FAHMAI.CO.TH** — สรัล อาวุทธ์มณี, ผู้จัดการทั่วไปแบรนด์จุดเชื่อม.
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
อัมพร ประฟ้า สังกัดแผนก KS (คลื่นเสียง) — ผู้บริหารสูงสุดของแผนกคือ ราม ลวรรณ (GM) อีเมล: RAM.LA@FAHMAI.CO.TH
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก WK คือ กฤษ มหาแก้วใส — KRIS.MA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea (DN)

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของ Daonuea (DN) คือ **วิเชียร พงหอมกลิ่น** — General Manager of Daonuea  
โทร. **76999**, มือถือ **064-902-5307**, อีเมล **WICHIAN.PH@FAHMAI.CO.TH**
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem (JC) department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
Saran Awutmani — General Manager of JudChuem (JC)  
Email: SARAN.AW@FAHMAI.CO.TH | Ext: 78762 | Mobile: 064-655-7513
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
ราม ลวรรณ — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง (KS)  
อีเมล: RAM.LA@FAHMAI.CO.TH, ต่อ 75965
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon (WK)

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของ Wongkhojon (WK) คือ **กฤษ มหาแก้วใส** — General Manager of WongKhoJon  
อีเมล: **KRIS.MA@FAHMAI.CO.TH**, ต่อ **74375**
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
7 employees.
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
6 employees.
```

### g568 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ

**Fails:** missing any-of ['77008']

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

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณทัศนีย์สังกัด DN (ดาวเหนือ) — คนที่ตำแหน่งสูงสุดคือ **วิเชียร พงหอมกลิ่น** (GM ดาวเหนือ) เบอร์ต่อ **76999**
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
คุณอภิชัยสังกัด FIN — ตำแหน่งสูงสุดคือคุณกมลา ชัยสนธิ์สว่าง (CFO) เบอร์ต่อ 74921
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
คุณมนตรา บุญเรืองโชติ สังกัด HR — ตำแหน่งสูงสุดคือคุณณฐามน อภิชัยดี (CHRO) เบอร์ต่อ 79303
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์อยู่ฝ่าย JC (จุดเชื่อม) — ตำแหน่งสูงสุดคือคุณราชินี อาทิตย์สุข (รองประธานฝ่ายจุดเชื่อม) เบอร์ต่อ 75642 ครับ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์อยู่สายงาน KS (คลื่นเสียง) — ตำแหน่งสูงสุดคือ ราม ลวรรณ (ผู้จัดการทั่วไปแบรนด์คลื่นเสียง) เบอร์ต่อ 75965
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
คุณคำรณ ศรีอัญชลีสังกัด OPS ครับ  
คนที่ตำแหน่งสูงสุดคือ **พงษ์กานต์ ราชชากัญญ์ (COO)** เบอร์ต่อ **75464**
```

### g607 [surname_family] P1/th
**Q:** พนักงานที่นามสกุล แสงทอง มีใครบ้าง ขอชื่อทุกคน

**Fails:** missing any-of ['Ravee', 'ระวี']; missing any-of ['Dao', 'ดาว']; missing any-of ['Anurak', 'อนุรักษ์']; missing count 3

**Response:**

```
ไม่พบข้อมูล
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
- วีระ อภิญญาเสริม — VEERA.AP@FAHMAI.CO.TH
- ดาหลา อภิญญาเสริม — DARHA.AP@FAHMAI.CO.TH, ext. 75781
```

### g666 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Rama IX (R9) HQ branch?

**Fails:** missing any-of ['1255']

**Response:**

```
1,255 staff work at the Rama IX (R9) HQ branch.
```

### g758 [counterfactual] P1/en
**Q:** I heard ณัฐพงษ์ อธิดี is the CTO — can I get their extension?

**Fails:** missing any-of ['TECVP', 'VP Technology', 'ฤทธิชัย']

**Response:**

```
no record found for ณัฐพงษ์ อธิดี as CTO.
```

### g772 [subsidiary_routing] P1/th
**Q:** แบรนด์จุดเชื่อมเป็นแบรนด์ในเครือฟ้าใหม่ ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์นี้

**Fails:** missing any-of ['Narong', 'ณรงค์']; missing any-of ['Kobsookbun', 'กอบสุขบุญ']

**Response:**

```
หัวหน้าทีมวิศวกรผลิตภัณฑ์จุดเชื่อมคือ **สุชาดา วัชรอาวุทธ์**  
อีเมล: **SUCHADA.WA@FAHMAI.CO.TH** | ต่อ: **74383**
```

### g777 [subsidiary_routing] P1/en
**Q:** The Wongkhojon brand is an in-house FahMai division — who heads its operations unit?

**Fails:** missing any-of ['Nangnoi', 'นางน้อย']; missing any-of ['Kanchai', 'กาญจน์ชัย']

**Response:**

```
WongKhoJon is headed by **Kris Mahakaewsai** — General Manager of WongKhoJon.  
Email: **KRIS.MA@FAHMAI.CO.TH**, ext. **74375**
```

### g821 [deep_multihop] P2/en
**Q:** What's the email of the secretary of the VP who heads the department that ภูมิ กาญจน์เจริญ works in?

**Fails:** missing any-of ['BUPPHA.AP@FAHMAI.CO.TH']

**Response:**

```
ภูมิ works in FIN. The head is the CFO, and the secretary/EA email is **BENJAWAN.CH@FAHMAI.CO.TH**.
```

### g825 [deep_multihop] P2/en
**Q:** What's the phone extension of the secretary of the VP who heads the department that ละไม บุญพงศ์ works in?

**Fails:** missing any-of ['71498']

**Response:**

```
ละไม บุญพงศ์ อยู่แผนก JC แต่จากข้อมูลที่ค้นได้ตอนนี้ยังไม่พบเบอร์ต่อของเลขา JCVP — no record found
```

