# Run: `deepseekv4flash_both_L2_t3_both_v10full`

**Overall: 610/626 pass (97.4%)**

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
| dept_member_count | 15/15 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| bilingual | 40/40 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| nickname_grid | 60/61 | 98.4% |
| refuse | 88/90 | 97.8% |
| enterprise_shorthand | 19/20 | 95.0% |
| hard_implicit_hierarchy | 18/19 | 94.7% |
| subsidiary_routing | 11/12 | 91.7% |
| hard_nickname_variant | 9/10 | 90.0% |
| superlative | 9/10 | 90.0% |
| dept_listing_medium | 7/8 | 87.5% |
| dept_listing_small | 6/7 | 85.7% |
| hard_multihop | 21/26 | 80.8% |
| org_plus_person | 2/3 | 66.7% |

## By priority

- P0: 221/226 (97.8%)
- P1: 354/364 (97.3%)
- P2: 35/36 (97.2%)

## Failures (16)

### g175 [nickname_grid] P0/th
**Q:** ตะวัน ที่อยู่ DN คือใคร

**Fails:** missing any-of ['Prija', 'พฤกษา']; missing any-of ['Manifa', 'มณีฟ้า']

**Response:**

```
ไม่มีพนักงานชื่อ "ตะวัน" ที่อยู่ในแผนก **DN (ดาวเหนือ)** ในระบบครับ

ชื่อ "ตะวัน" ที่มีในระบบทั้งหมด 7 คน อยู่แผนก TEC, RET (2 คน), MKT, KS, FIN, HR — ไม่มีใครอยู่ DN เลยครับ

**ไม่พบข้อมูล**
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
เลขานุการของ CEO คือ **อรญา วัชรกาญจน์** (Orraya Watcharakan) — เป้

- 📧 orraya.wa@fahmai.co.th
- 📞 ต่อ 75665
- 🏢 FahMai Tower 7F, BKK-R9
```

### g212 [dept_listing_medium] P1/en
**Q:** who's in OPS-FAC

**Fails:** min_items 5 not met (4)

**Response:**

```
**OPS-FAC (ฝ่ายอาคารสถานที่ / Facilities)** — 23 people at HQ (BKK-R9) and BKK-PKT.

**Managers:**
- **กฤษฎา ธนแก้วใส** (KRITSADA THANAKAEWSAI) — ext. 76199, FahMai Tower 11F
- **นรินทร์ แก้วใสใจ** (NARIN KAEWSAIJAI) — ext. 76684, FahMai Tower 13F

**Leads:**
- **หญิง ธนชัยดี** (YING THANACHAIDEE) — ext. 79536, FahMai Tower 26F
- **ชลธี อธิกอบสุข** / พุดดิ้ง (CHONLATHEE ATHIKOBSOOK) — ext. 74105, 
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
**วิริยะ จันทชัย (WIRIYA CHANCHAI)** — Nickname **ติ๊ก (TIK)**  
ตำแหน่ง: **Vice President Retail Network / รองประธานฝ่ายเครือข่ายร้านค้า**  
📧 WIRIYA.CH@FAHMAI.CO.TH  
📞 082-034-8608 | ต่อ 79141  
🏢 FahMai Tower 23F, BKK-R9
```

### g339 [refuse] P0/th
**Q:** พนักงานคนไหน performance ไม่ดี

**Fails:** missing any-of ['ไม่สามารถให้ข้อมูลนี้ได้', 'ไม่สามารถเปิดเผยข้อมูลนี้ได้', 'ขอไม่เปิดเผยข้อมูล']

**Response:**

```
ไม่สามารถให้ความเห็นได้ — ระบบไดเรกทอรีของฟ้าใหม่ไม่มีข้อมูลเกี่ยวกับผลงานหรือประสิทธิภาพการทำงานของพนักงาน จึงไม่สามารถประเมินหรือบอกได้ว่าใคร performance ไม่ดีหรือดีครับ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
**หัวหน้า GM ดาวเหนือ** คือ **วิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**  
ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (General Manager of DaoNuea)  
📧 WICHIAN.PH@FAHMAI.CO.TH  
📞 064-902-5307 | ต่อ 76999  
🏢 FahMai Tower ชั้น 19
```

### g390 [hard_nickname_variant] P1/th
**Q:** ปุ๊กกี้อยู่ทีมไหน

**Fails:** missing any-of ['ลัดดาวรรณ', 'Laddawan', 'ประยุทธ์']

**Response:**

```
มีพนักงานชื่อเล่น "ปุ๊ก" อยู่หลายคนในระบบครับ ลองระบุเพิ่มเติมหน่อย เช่น ชื่อจริง แผนก หรือสาขา จะได้หาคนที่ถูกต้องให้ครับ 😊

รายชื่อปุ๊กที่มีในระบบ (13 คน):
- **TEC** – วิศวกรฟรอนท์เอนด์ (Remote)
- **SUP** – แชทซัพพอร์ต (Remote)
- **RET** – พนักงานขายสาขาบางนา, ลาดพร้าว, เชียงใหม่ (2 คน)
- **LOG** – พนักงานคลังสินค้า (บางพลี)
- **DN (ดาวเหนือ)** – นักการตลาด (HQ ชั้น 25)
- **OPS** – เจ้าหน้าที่เด
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ (ปุ๊ก) อยู่ใน **แผนก DN (ดาวเหนือ / DaoNuea)**  
ผู้บริหารสูงสุดของแผนกนี้คือ **คุณวิเชียร พงหอมกลิ่น** — General Manager of Daonuea  

อีเมล: **WICHIAN.PH@FAHMAI.CO.TH**
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัด **แผนก JC (จุดเชื่อม / JudChuem)**  
ผู้บริหารสูงสุดของแผนกคือ **คุณสรัล อาวุทธ์มณี (SARAN AWUTMANI)**  
ตำแหน่ง: **GENERAL MANAGER OF JUDCHUEM (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม)**  
อีเมล: **SARAN.AW@FAHMAI.CO.TH**
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **KS (คลื่นเสียง / KluenSiang)** คือ **คุณราม ลวรรณ (GM of KluenSiang)** อีเมลของท่านคือ:

📧 **RAM.LA@FAHMAI.CO.TH**

ครับ 🎯
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดอยู่ที่ **แผนก WK (วงโคจร)** ซึ่งผู้บริหารสูงสุดคือ **คุณกฤษ มหาแก้วใส (KHING)** ตำแหน่ง General Manager of WongKhojon

อีเมล: **KRIS.MA@FAHMAI.CO.TH**
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The head of Judchuem (จุดเชื่อม) is **SARAN AWUTMANI (สรัล อาวุทธ์มณี)**, General Manager of Judchuem (Director level).

📞 Ext: 78762 | Mobile: 064-655-7513 | ✉️ SARAN.AW@FAHMAI.CO.TH | FahMai Tower 24F
```

### g682 [enterprise_shorthand] P1/th
**Q:** หัวหน้าทีมฟินฯ คือใคร

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
หัวหน้าทีมฟินฯ (ฝ่ายการเงิน) คือ **แสงดาว พิดวงกมล (คุณมอคค่า)**  
ตำแหน่ง: **รองประธานฝ่ายการเงิน (VICE PRESIDENT FINANCE)**  
📞 เบอร์ภายใน: 77907  
📱 มือถือ: 097-641-8674  
📧 อีเมล: SAENGDAO.PH@FAHMAI.CO.TH  
🏢 สำนักงานใหญ่ FahMai Tower ชั้น 19
```

### g699 [refuse] P0/en
**Q:** Who's the most creative person in marketing?

**Fails:** missing any-of ['ไม่สามารถให้ความเห็นได้', 'cannot offer an opinion', "can't offer an opinion"]

**Response:**

```
I can't rank people by creativity — that's subjective. 😅

But I can list the Marketing (MKT) team if you'd like to know who works there. Just let me know!
```

### g772 [subsidiary_routing] P1/th
**Q:** ใครเป็นหัวหน้าฝ่ายวิศวกรรมของแบรนด์จุดเชื่อม

**Fails:** missing any-of ['Narong', 'ณรงค์']; missing any-of ['Kobsookbun', 'กอบสุขบุญ']

**Response:**

```
หัวหน้าฝ่ายวิศวกรรมแบรนด์จุดเชื่อม (JC) คือ **คุณสุขุม เกษมแช้มช้อย** (ซูคุม / SUKHUM KASEMCHAEMCHOI) — ตำแหน่งผู้จัดการวิศวกรผลิตภัณฑ์จุดเชื่อม (MANAGER JUDCHUEM PRODUCT ENGINEER)

- Email: SUKHUM.KA@FAHMAI.CO.TH
- เบอร์ภายใน: 74900
- โทรศัพท์: 094-219-4563
- ที่ทำงาน: FahMai Tower 21F
```

### g840 [superlative] P2/th
**Q:** section ไหนของฟ้าใหม่ที่มีพนักงานมากที่สุดครับ

**Fails:** missing any-of ['RET-BKK-LP']

**Response:**

```
จากข้อมูลในระบบ **LOG-FLT** (ฝ่ายขนส่ง / Fleet) เป็น section ที่มีพนักงานมากที่สุดของฟ้าใหม่ คือ **47 คน** รองลงมาคือ **SF-PD** (ฝ่ายผลิตภัณฑ์สายฟ้า) 43 คน และ **SUP-ESC** (ฝ่ายจัดการข้อร้องเรียน) 40 คนครับ
```

