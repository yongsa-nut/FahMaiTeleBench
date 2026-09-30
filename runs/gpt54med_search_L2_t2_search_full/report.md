# Run: `gpt54med_search_L2_t2_search_v10full`

**Overall: 609/626 pass (97.3%)**

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
| refuse | 90/90 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| noisy_name_form | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| counterfactual | 25/25 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| deep_multihop | 12/12 | 100.0% |
| superlative | 10/10 | 100.0% |
| bilingual | 39/40 | 97.5% |
| nickname_grid | 59/61 | 96.7% |
| enterprise_shorthand | 19/20 | 95.0% |
| multi_hop | 17/18 | 94.4% |
| surname_family | 22/24 | 91.7% |
| dept_listing_small | 6/7 | 85.7% |
| hard_multihop | 22/26 | 84.6% |
| hard_implicit_hierarchy | 15/19 | 78.9% |
| org_plus_person | 2/3 | 66.7% |

## By priority

- P0: 219/226 (96.9%)
- P1: 354/364 (97.3%)
- P2: 36/36 (100.0%)

## Failures (17)

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
ถ้าหมายถึงผู้บริหารระดับ C-level มี 7 คนครับ

- วชิร จิรบุญ — CEO
- กมลา ชัยสนธิ์สว่าง — CFO
- ฤทธิชัย แก้วใสภิญโญ — CTO
- พงษ์กานต์ ราชชากัญญ์ — COO
- ส้ม กาญจน์สถิต — CMO
- จิรภัทร วัชรใจงาม — CPO
- ณฐามน อภิชัยดี — CHRO

ถ้าจะเอาระดับ VP ต่อด้วย บอกได้ครับ
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล อรุณ ขอนแก่น ในระบบพนักงานฟ้าใหม่
```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
no record found for `CEO-SEC`.

Closest listed unit is `CEO-EA`:
- ORRAYA WATCHARAKAN — Executive Assistant to CEO — ext. 75665 — ORRAYA.WA@FAHMAI.CO.TH
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
Bangkok Retail VP: **Wiriya Chanchai** — **WIRIYA.CH@FAHMAI.CO.TH**, ext. **79141**, mobile **082-034-8608**.
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
GM ของดาวเหนือคือ **วิเชียร พงหอมกลิ่น** — ต่อ **76999**, มือถือ **064-902-5307**, อีเมล **WICHIAN.PH@FAHMAI.CO.TH**
```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
cannot provide this information — reporting lines/boss relationships aren’t tracked in the directory.
```

### g364 [hard_implicit_hierarchy] P0/th
**Q:** ใต้ CFO มีใครรายงานตรงบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ — ระบบไดเรกทอรีไม่มีฟิลด์สายการบังคับบัญชาหรือผู้รายงานตรงของ CFO โดยตรง
```

### g367 [hard_implicit_hierarchy] P0/en
**Q:** who reports to the COO

**Fails:** min_items 1 not met (0)

**Response:**

```
cannot provide this information — the directory does not track reporting lines.
```

### g386 [surname_family] P1/en
**Q:** how many employees share the surname วัชรบุญ

**Fails:** missing any-of ['3']; missing count 3

**Response:**

```
6 employees have `วัชรบุญ` in their surname.
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณละไม บุญพงศ์ สังกัดแผนก JC โดยผู้บริหารสูงสุดของแผนกคือ **สรัล อาวุทธ์มณี** — **SARAN.AW@FAHMAI.CO.TH**
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก WK ครับ ผู้บริหารสูงสุดของแผนกนี้คือ กฤษ มหาแก้วใส (ผู้จัดการทั่วไปแบรนด์วงโคจร) — `KRIS.MA@FAHMAI.CO.TH`
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior head of the Judchuem department is **SARAN AWUTMANI** — **General Manager of Judchuem**.  
Contact: **78762** · **SARAN.AW@FAHMAI.CO.TH**
```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
กฤษ มหาแก้วใส (ขิง) — ผู้จัดการทั่วไปแบรนด์วงโคจร, อีเมล KRIS.MA@FAHMAI.CO.TH, ต่อ 74375
```

### g473 [bilingual] P1/th
**Q:** รหัสพนักงานของ CPO คือเลขอะไรครับ

**Fails:** missing any-of ['00001072']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ รหัสพนักงานเป็นข้อมูลภายในนอกเหนือจากชื่อและข้อมูลติดต่อ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณศักดิ์สิทธิ์ สัมชากัญญ์ สังกัดส่วนงาน KS ครับ — ตำแหน่งสูงสุดในส่วนงานนี้คือ **ธเนศ บัวทองประเสริฐ (รองประธานฝ่ายคลื่นเสียง)** เบอร์ต่อ **71215** ครับ
```

### g618 [surname_family] P1/en
**Q:** List everyone with the surname วัชรจงรัก (give all of them).

**Fails:** missing count 2

**Response:**

```
Here are all employees with the surname วัชรจงรัก:

- ปัญญา วัชรจงรัก (ไทเทิล) — Lead Technical Support Agent, ext. 72201, 093-616-9898, PANYA.WA@FAHMAI.CO.TH
- จรูญ วัชรจงรัก (ไผ่) — Learning & Development Specialist, ext. 71981, CHAROON.WA@FAHMAI.CO.TH
```

### g684 [enterprise_shorthand] P1/th
**Q:** ใครเป็นหัวหน้าทีมการตลาด

**Fails:** missing any-of ['Som', 'ส้ม']; missing any-of ['Kansathit', 'กาญจน์สถิต']

**Response:**

```
หัวหน้าทีมการตลาดคือ **คะวัง กอบสุขรัตน์ (โอ)** — **รองประธานฝ่ายการตลาด**  
ต่อ **74711** | มือถือ **088-904-0088** | **KWANG.KO@FAHMAI.CO.TH**

ถ้าหมายถึง **การตลาดดิจิทัล** คือ **สมพงษ์ กอบสุขประเสริฐ** — **รองประธานฝ่ายการตลาดดิจิทัล**
```

