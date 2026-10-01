# Run: `deepseekv4flash_search_L2_t2_search_v10full`

**Overall: 601/626 pass (96.0%)**

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
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| extension_reverse | 7/7 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| surname_family | 24/24 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| listing_count | 20/20 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| multi_hop | 18/18 | 100.0% |
| enterprise_shorthand | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| refuse | 88/90 | 97.8% |
| bilingual | 39/40 | 97.5% |
| casual_name_lookup | 14/15 | 93.3% |
| nickname_grid | 55/61 | 90.2% |
| thai_knowledge | 9/10 | 90.0% |
| hard_implicit_hierarchy | 17/19 | 89.5% |
| dept_listing_small | 6/7 | 85.7% |
| retrieval | 12/14 | 85.7% |
| hard_multihop | 21/26 | 80.8% |
| subsidiary_routing | 9/12 | 75.0% |
| org_plus_person | 2/3 | 66.7% |

## By priority

- P0: 215/226 (95.1%)
- P1: 350/364 (96.2%)
- P2: 36/36 (100.0%)

## Failures (25)

### g136 [casual_name_lookup] P0/th
**Q:** พี่วิน อยู่ DN เบอร์อะไร

**Fails:** missing any-of ['71975', 'KITTICHAT.AR']

**Response:**

```
ไม่มีคนชื่อ "วิน" ในแผนก DN (ดาวเหนือ) ในระบบครับ

คนชื่อ "วิน" ที่มีในระบบทั้งหมด 11 คน แต่อยู่แผนก TEC, RET, LOG, SF, OPS ไม่มีใครอยู่ใน DN เลยครับ

ไม่พบข้อมูล
```

### g166 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นโอ๊ตกี่คน

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

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
จากข้อมูลที่ค้นหา ไม่พบพนักงานชื่อ **อรุณ** ในแผนก SUP (Supply Chain) เลยครับ

มีอรุณทั้งหมด 14 คน แต่อยู่ในแผนกอื่น ๆ เช่น TEC, RET, LOG, MKT, SF, DN, OPS, WK, JC, B2B — ไม่มีใครสังกัด SUP เลย

**ไม่พบข้อมูล**
```

### g177 [nickname_grid] P0/th
**Q:** ใบเฟิร์น สาขา BNA คือใคร

**Fails:** missing any-of ['Phaibun', 'ไพบูลย์']; missing any-of ['Athikiatkamjorn', 'อธิเกียรติกำจร']

**Response:**

```
ไม่พบข้อมูล
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูลพนักงานที่ชื่อ **อรุณ** ที่สาขาขอนแก่น (KKN) ในระบบครับ
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
พบบุคคล **จงรัก สัมโชติ** (ชื่อเล่น ปุ๊ก) แผนก JC (จุดเชื่อม) แต่ไม่มีเบอร์โทรศัพท์ (ทั้งมือถือและสายภายใน) ในระบบครับ — `ไม่มีข้อมูล`
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
ไม่มี Unit `CEO-SEC` โดยตรง แต่เลขานุการของ CEO อยู่ใน Unit **CEO-EA** ซึ่งก็คือ

- **อรญา วัชรกาญจน์ (ORRAYA WATCHARAKAN)** — Nickname: เป้ / PE
- ตำแหน่ง: EXECUTIVE ASSISTANT TO CEO (เลขานุการของ CEO)
- เบอร์ภายใน: **75665**
- อีเมล: ORRAYA.WA@FAHMAI.CO.TH
- ที่ตั้ง: FahMai Tower 7F
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
**วิริยะ จันทชัย (WIRIYA CHANCHAI)** — รองประธานฝ่ายเครือข่ายร้านค้า  
📞 Phone Extension: **79141**  
📱 Mobile: **082-034-8608**  
📧 Email: **WIRIYA.CH@FAHMAI.CO.TH**  
📍 FahMai Tower 23F, HQ
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
หัวหน้า GM (ผู้จัดการทั่วไป) ของ **ดาวเหนือ (DaoNuea)** คือ **คุณวิเชียร พงหอมกลิ่น** (WICHIAN PHONGHOMKLIN)

- **ตำแหน่ง:** ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (GENERAL MANAGER OF DAONUEA)
- **เบอร์โทรศัพท์มือถือ:** 064-902-5307
- **อีเมล:** WICHIAN.PH@FAHMAI.CO.TH
- **สถานที่ทำงาน:** FahMai Tower ชั้น 19
- **สายต่อ:** 76999
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
**SFVP (วิรัตน์ สมบุษราคัม / Dokmai)** reports to the **CEO — วชิร จิรบุญ (เบอร์รี่ / Berry)**.

📞 CEO contact: Extension **73048** | Email: **VACHIR.CH@FAHMAI.CO.TH** | Office: FahMai Tower 12F
```

### g379 [thai_knowledge] P0/th
**Q:** ใครมีชื่อเล่นเป็นชื่อผลไม้บ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ เนื่องจากระบบของฟ้าใหม่ไม่มีฟังก์ชันสำหรับค้นหาหรือจัดหมวดหมู่ชื่อเล่นตามประเภท (เช่น ชื่อผลไม้) จึงไม่สามารถระบุรายชื่อพนักงานที่มีชื่อเล่นเป็นชื่อผลไม้ได้
```

### g404 [refuse] P1/th
**Q:** ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูล **ถาวร จิตรานนท์ฟ้า** ในระบบครับ

มีพนักงานชื่อคล้ายๆ กัน เช่น **อิสระ จิตรานนท์ฟ้า** (เบอร์ต่อ 72554) หรือ **สุจิรา จิตรานนท์ฟ้า** (เบอร์ต่อ 47209) แต่ไม่มีชื่อ "ถาวร" ที่ใช้นามสกุลนี้ครับ
```

### g414 [refuse] P1/th
**Q:** ขอเบอร์ต่อ อนุชา ทองแท้แน่นอน หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูลของ **อนุชา ทองแท้แน่นอน** ในระบบครับ 🙏

ชื่อ "อนุชา" ที่ใกล้เคียงที่สุดมี 2 คน แต่ไม่มีนามสกุลตรงกัน:
- **ธเนศ อนุชากัญญ์** (แผนก MKT) เบอร์ต่อ 71366
- **กิตติชาติ อนุชาญณรงค์** (แผนก SF) เบอร์ต่อ 77892

ถ้าต้องการเบอร์ต่อของคนใดคนหนึ่ง บอกเพิ่มเติมได้เลยครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **DN (ดาวเหนือ)** ที่คุณทัศนีย์สังกัดอยู่คือ **คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)** — General Manager of DaoNuea

📧 อีเมล: **WICHIAN.PH@FAHMAI.CO.TH**
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
อีเมลผู้จัดการใหญ่ (GM) ของฝ่าย **จุดเชื่อม (JC)** คือ **สรัล อาวุทธ์มณี** (SARAN AWUTMANI)  

📧 **SARAN.AW@FAHMAI.CO.TH**
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
อีเมลของผู้บริหารสูงสุดของแผนก **วงโคจร (WK)** ที่คุณธนพลสังกัดอยู่คือ **คุณกฤษ มหาแก้วใส** (KRIS MAHAKAEWSAI) — GM ของ WongKhojon ครับ

📧 **KRIS.MA@FAHMAI.CO.TH**
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนกดาวเหนือ (DN) คือ **วิเชียร พงหอมกลิ่น** (WICHIAN PHONGHOMKLIN) — ผู้จัดการทั่วไปแบรนด์ดาวเหนือ

📧 WICHIAN.PH@FAHMAI.CO.TH | ☎️ 76999 | 📱 064-902-5307
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The head of the Judchuem (จุดเชื่อม) brand is **สรัล อาวุทธ์มณี (SARAN AWUTMANI)** — General Manager of Judchuem.

- Email: SARAN.AW@FAHMAI.CO.TH
- Ext: 78762 | Mobile: 064-655-7513
- Office: FahMai Tower 24F (BKK-R9)
```

### g475 [bilingual] P1/th
**Q:** รหัสหน่วยงานของ Chief of Staff คืออะไรครับ

**Fails:** missing any-of ['CEO-CoS']

**Response:**

```
[agent error: JSONDecodeError: Unterminated string starting at: line 1 column 62 (char 61)]
```

### g562 [retrieval] P1/en
**Q:** What's DARIN's phone extension?

**Fails:** missing any-of ['54796']

**Response:**

```
ไม่พบข้อมูล
```

### g566 [retrieval] P1/en
**Q:** What is KHANOM's email address?

**Fails:** missing any-of ['KRITSADA.AN@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g771 [subsidiary_routing] P1/en
**Q:** Who heads the marketing unit of the DaoNuea brand?

**Fails:** missing any-of ['Phussadee', 'พุสดี']; missing any-of ['Chaisaidi', 'ชัยสัยดี']

**Response:**

```
The head of the DaoNuea (ดาวเหนือ) brand is **วิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)** — General Manager of DaoNuea (ผู้จัดการทั่วไปแบรนด์ดาวเหนือ).

📞 Ext: 76999 | Mobile: 064-902-5307 | ✉️ WICHIAN.PH@FAHMAI.CO.TH (FahMai Tower 19F, BKK-R9)
```

### g773 [subsidiary_routing] P1/en
**Q:** Who heads the marketing unit of the Judchuem brand?

**Fails:** missing any-of ['Phaibun', 'ไพบูลย์']; missing any-of ['Anujitranon', 'อนุจิตรานนท์']

**Response:**

```
The head of the Judchuem (จุดเชื่อม) brand is **สรัล อาวุทธ์มณี (SARAN AWUTMANI)** — General Manager of Judchuem (JC-GM).

Contact: 064-655-7513 · SARAN.AW@FAHMAI.CO.TH · FahMai Tower 24F
```

### g775 [subsidiary_routing] P1/en
**Q:** Who heads the operations unit of the Kluensiang brand?

**Fails:** missing any-of ['Vasin', 'วศิน']; missing any-of ['Rajchaidee', 'ราชชัยดี']

**Response:**

```
**ลลนา ใจเขียวสถิต** (LALANA JAIKIEOWSATHIT) — Manager, Kluensieng Brand Operations (KS-OPS).

- Email: LALANA.JA@FAHMAI.CO.TH
- Ext: 73432 · FahMai Tower 18F · BKK-R9
```

