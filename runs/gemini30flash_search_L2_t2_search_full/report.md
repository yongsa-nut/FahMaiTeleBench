# Run: `gemini30flash_search_L2_t2_search_v10full`

**Overall: 543/626 pass (86.7%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| dept_listing_medium | 8/8 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| email_identity_lookup | 6/6 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| hard_nickname_variant | 10/10 | 100.0% |
| refuse | 88/90 | 97.8% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| dept_member_count | 14/15 | 93.3% |
| counterfactual | 23/25 | 92.0% |
| deep_multihop | 11/12 | 91.7% |
| nickname_grid | 55/61 | 90.2% |
| name_lookup | 18/20 | 90.0% |
| brand_prior | 9/10 | 90.0% |
| superlative | 9/10 | 90.0% |
| surname_family | 21/24 | 87.5% |
| extension_reverse | 6/7 | 85.7% |
| retrieval | 12/14 | 85.7% |
| enterprise_shorthand | 17/20 | 85.0% |
| hard_implicit_hierarchy | 16/19 | 84.2% |
| tier_listing | 5/6 | 83.3% |
| evp_secretary | 4/5 | 80.0% |
| hard_multihop | 20/26 | 76.9% |
| evp_identity_by_description | 3/4 | 75.0% |
| ceo_president | 3/4 | 75.0% |
| bilingual | 30/40 | 75.0% |
| listing_count | 15/20 | 75.0% |
| org_plus_person | 2/3 | 66.7% |
| multi_hop | 12/18 | 66.7% |
| noisy_name_form | 10/20 | 50.0% |
| dept_listing_small | 3/7 | 42.9% |
| subsidiary_routing | 4/12 | 33.3% |

## By priority

- P0: 211/226 (93.4%)
- P1: 299/364 (82.1%)
- P2: 33/36 (91.7%)

## Failures (83)

### g024 [evp_identity_by_description] P0/th
**Q:** ใครดูแลด้าน tech สูงสุด

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```

```

### g053 [evp_secretary] P0/en
**Q:** EA of TECPM

**Fails:** missing any-of ['Darika', 'ดาริกา']; missing any-of ['Suwanchinda', 'สุวรรณจินดา']

**Response:**

```
The Executive Assistant (EA) for TECPM (CTO) is **Juthamas Kaewsaiphong (Mint)**.

*   **Email:** JUTHAMAS.KA@FAHMAI.CO.TH
*   **Mobile:** 095-228-0338
*   **Extension:** 77008
*   **Location:** FahMai Tower 12F
```

### g077 [evp_vs_vp_disambig] P0/th
**Q:** RETBKK ใคร — ไม่ใช่ RETVP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```

```

### g108 [ceo_president] P1/en
**Q:** who's the current CEO

**Fails:** missing any-of ['Vachir', 'วชิร']; missing any-of ['Chirabun', 'จิรบุญ']

**Response:**

```

```

### g112 [name_lookup] P1/en
**Q:** phone for Taksa-Orn Narawat

**Fails:** missing any-of ['73987', 'TAKSA-ORN.NA']

**Response:**

```

```

### g119 [name_lookup] P1/th
**Q:** หวาน กาญจน์วัฒน์ เบอร์อะไร

**Fails:** missing any-of ['77021', 'WAAN.KA']

**Response:**

```

```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
ผู้บริหารระดับ C-level (บอส) ของฟ้าใหม่มีทั้งหมด 7 ท่านครับ:

*   **คุณวชิร จิรบุญ (เบอร์รี่)** - CEO (ประธานเจ้าหน้าที่บริหาร)
*   **คุณกมลา ชัยสนธิ์สว่าง** - CFO (ประธานเจ้าหน้าที่การเงิน)
*   **คุณฤทธิชัย แก้วใสภิญโญ (ปันปัน)** - CTO (ประธานเจ้าหน้าที่เทคโนโลยี)
*   **คุณพงษ์กานต์ ราชชากัญญ์** - COO (ประธานเจ้าหน้าที่ปฏิบัติการ)
*   **คุณส้ม กาญจน์สถิต** - CMO (ประธานเจ้าหน้าที่การตลาด)
*   **ค
```

### g167 [nickname_grid] P0/th
**Q:** มีคนชื่อเล่นเต่ากี่คน

**Fails:** missing any-of ['7']; missing count 7

**Response:**

```

```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูล สมาชิกชื่อ อรุณ ในแผนก SUP ครับ
```

### g179 [nickname_grid] P0/th
**Q:** อรุณ ขอนแก่น คือใคร

**Fails:** missing any-of ['Khemkhaeng', 'เข้มแข็ง']; missing any-of ['Thanabusarakham', 'ธนบุษราคัม']

**Response:**

```
ไม่พบข้อมูล
```

### g193 [nickname_grid] P0/th
**Q:** ใครคือปันปัน

**Fails:** missing any-of ['ฤทธิชัย', 'Rittichai']; missing any-of ['แก้วใสภิญโญ', 'Kaewsaiphinyo']

**Response:**

```

```

### g196 [dept_listing_small] P1/en
**Q:** who's in CEO-SEC

**Fails:** min_items 1 not met (0)

**Response:**

```
ORRAYA WATCHARAKAN (PE) is the Executive Assistant to the CEO (unit: CEO-EA).
```

### g198 [dept_listing_small] P1/th
**Q:** ใครอยู่ TEC-EXEC บ้าง

**Fails:** min_items 2 not met (0)

**Response:**

```

```

### g200 [dept_listing_small] P1/th
**Q:** ขอรายชื่อ MKT-EXEC ทั้งหมด

**Fails:** min_items 2 not met (0)

**Response:**

```
 ไม่พบข้อมูล ของหน่วยงาน MKT-EXEC ในระบบครับ

หากหมายถึงฝ่ายการตลาด (MKT) หรือมองหาตำแหน่งใดเป็นพิเศษ สามารถแจ้งชื่อหรือระบุหน่วยงานเพื่อตรวจสอบอีกครั้งได้ครับ
```

### g201 [dept_listing_small] P1/en
**Q:** list members of SF-EXEC

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูล
```

### g240 [dept_member_count] P1/th
**Q:** แผนก RET-CBI กี่คน

**Fails:** missing any-of ['40']; missing count 40

**Response:**

```
แผนก RET-CBI มีทั้งหมด 1 คนครับ
```

### g261 [tier_listing] P0/th
**Q:** ขอรายชื่อ director ทั้งหมด

**Fails:** min_items 10 not met (8)

**Response:**

```
นี่คือรายชื่อ Director ของฟ้าใหม่ (บางส่วน) ครับ:

* **ธนิดา อภิใจ** - ผู้อำนวยการฝ่ายการเงินและวางแผน (FIN)
* **แสงดาว อาวุทธ์พัฒน์** - ผู้อำนวยการฝ่ายปฏิบัติการสายฟ้า (SF)
* **อรอนงค์ วิศอนุมาน** - ผู้อำนวยการฝ่ายแบรนด์ (MKT)
* **บุษบา อัครพัฒน์** - ผู้อำนวยการฝ่ายบัญชี (FIN)
* **อุกฤษฎ์ อมรอาทิตย์ (เจลลี่)** - ผู้อำนวยการฝ่ายการเงิน (FIN)
* **หวาน สุวรรณโชคดี (บอส)** - ผู้อำนวยการฝ่ายวิศวกรทดสอ
```

### g268 [org_plus_person] P0/en
**Q:** who's the Bangkok retail VP

**Fails:** missing any-of ['Phonphai', 'พรไพร']; missing any-of ['Mahasin', 'มหาสินธุ์']

**Response:**

```
Wiriya Chanchai (Tik) is the Vice President of the Retail Network. You can contact him at WIRIYA.CH@FAHMAI.CO.TH or via mobile at 082-034-8608.
```

### g288 [extension_reverse] P2/th
**Q:** ต่อ 78417 เบอร์ใคร

**Fails:** missing any-of ['Rajchaicharoen', 'ราชชัยเจริญ']

**Response:**

```
เบอร์ต่อ 78417 เป็นของ คุณส้ม (เลขานุการของ DNVP) ครับ
```

### g333 [refuse] P0/th
**Q:** VP การตลาดของ LG คือใคร

**Fails:** has ext pattern

**Response:**

```
ไม่ใช่ข้อมูลของฟ้าใหม่ เนื่องจาก LG เป็นแบรนด์ภายนอกครับ

หากคุณหมายถึงรองประธานฝ่ายการตลาด (MKTVP) ของฟ้าใหม่ คือ **คุณคะวัง กอบสุขรัตน์ (โอ)**
- **อีเมล:** KWANG.KO@FAHMAI.CO.TH
- **เบอร์ภายใน:** 74711
- **เบอร์มือถือ:** 088-904-0088
```

### g351 [hard_multihop] P0/th
**Q:** ผู้บริหารที่มีจุฑามาศ แก้วใสพงศ์เป็นเลขานุการคือใคร

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
คุณจุฑามาศ แก้วใสพงศ์ (มิ้น) เป็นเลขานุการของ **CTO** (ผู้บริหารฝ่ายเทคโนโลยี) ครับ
```

### g354 [hard_multihop] P0/th
**Q:** เลขาของประธานเจ้าหน้าที่บริหารอยู่แผนกไหน

**Fails:** missing any-of ['CEO']

**Response:**

```

```

### g357 [hard_multihop] P0/en
**Q:** who is SFVP's boss

**Fails:** missing any-of ['Jirapat', 'จิรภัทร']; missing any-of ['Watcharajaingam', 'วัชรใจงาม']

**Response:**

```
The boss of the SFVP (Wirat Sombusarakham) is the **CEO**, who oversees all departmental VPs.

According to the directory, the CEO is:
*   **Name:** Mr. Arnat Fahsawang (อานัต ฟ้าสว่าง)
*   **Email:** ARNAT.FA@FAHMAI.CO.TH
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
คุณสรัล อาวุทธ์มณี (GENERAL MANAGER OF JUDCHUEM)
อีเมล: SARAN.AW@FAHMAI.CO.TH
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนกคลื่นเสียง (KS) โดยผู้บริหารสูงสุดของแผนก (GM) คือ คุณราม ลวรรณ ครับ

**อีเมล:** RAM.LA@FAHMAI.CO.TH
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
คุณธนพล พิประเสริฐ สังกัดแผนก **WK (แบรนด์วงโคจร)** โดยผู้บริหารสูงสุดของแผนก (WK-GM) คือ คุณกฤษ มหาแก้วใส ครับ

**อีเมล:** KRIS.MA@FAHMAI.CO.TH
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```


```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```


```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนก Wongkhojon (แบรนด์วงโคจร) คือ **คุณกฤษ มหาแก้วใส (ขิง)** ตำแหน่งผู้จัดการทั่วไป (General Manager)
*   **อีเมล:** KRIS.MA@FAHMAI.CO.TH
*   **เบอร์ภายใน:** 74375
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

### g475 [bilingual] P1/th
**Q:** รหัสหน่วยงานของ Chief of Staff คืออะไรครับ

**Fails:** missing any-of ['CEO-CoS']

**Response:**

```
รหัสหน่วยงาน (Unit code) ของ Chief of Staff คือ **COS** ครับ
```

### g476 [bilingual] P1/th
**Q:** รหัสพนักงานของ VP ฝ่ายการเงิน คือเลขอะไรครับ

**Fails:** missing any-of ['00007543']

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้
```

### g491 [bilingual] P1/en
**Q:** What is the Chief of Staff's Thai nickname?

**Fails:** missing any-of ['บูม', 'Boom', 'BOOM']

**Response:**

```
เป้ (Pe)
```

### g493 [bilingual] P1/en
**Q:** What is the Thai family (last) name of the VP of HR?

**Fails:** missing any-of ['อัครใจงาม', 'Akarajaingam']

**Response:**

```

```

### g496 [bilingual] P1/en
**Q:** What is the Thai family (last) name of the VP of Technology?

**Fails:** missing any-of ['อธิดี', 'Athidi']

**Response:**

```

```

### g515 [bilingual] P1/th
**Q:** ช่วยหา unit code ของ Vice President Finance ให้ทีครับ

**Fails:** missing any-of ['FINVP']

**Response:**

```

```

### g519 [bilingual] P1/th
**Q:** ช่วยหา unit code ของ Vice President Customer Support ให้ทีครับ

**Fails:** missing any-of ['SUPVP']

**Response:**

```

```

### g526 [bilingual] P1/th
**Q:** nickname ของ Chief Executive Officer คืออะไรครับ

**Fails:** missing any-of ['เบอร์รี่', 'Berry', 'BERRY']

**Response:**

```

```

### g528 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก B2B ระดับ IC และเริ่มงานในปี 2021 ครับ

**Fails:** missing count 5

**Response:**

```
มีพนักงานระดับ IC ในแผนก B2B ที่เริ่มงานในปี 2021 ทั้งหมด 4 คน ดังนี้ครับ:

1. **ณัฏฐพล ศรีพิทักษ์** — ผู้แทนขายองค์กร (081-078-8452)
2. **อรอนงค์ รัตนเกษม (กบ)** — เจ้าหน้าที่บริการลูกค้าองค์กร (086-927-9060)
3. **อรุณ สัมภิญโญ (แมว)** — ผู้แทนขายองค์กร
4. **ไพบูลย์ บุญมางาม (ปุ๊ก)** — วิศวกรโซลูชันองค์กร
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
In the DN (DaoNuea) department, there are 4 employees at the IC level who started in 2020:

*   **Thinnakorn Narachannarong (Kob)** – Daonuea Brand Operations
*   **Yothaka Amphomsawang** – Daonuea Product Engineer
*   **Veera Phongasnee (Mango)** – Daonuea Product Manager
*   **Prija Manifa (Tawan)** – Daonuea Brand Operations
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are 6 employees in the DN (DaoNuea) department at the Lead level who started in 2022.
```

### g545 [listing_count] P1/th
**Q:** ช่วยบอกชื่อทุกคนที่เป็นระดับ Manager ในส่วนงาน CEO-STR หน่อยครับ

**Fails:** min_items 2 not met (0)

**Response:**

```
ไม่พบข้อมูลของพนักงานระดับ Manager ในหน่วยงาน CEO-STR ครับ
```

### g548 [listing_count] P1/en
**Q:** List everyone at Director level in the DN-PD section.

**Fails:** min_items 2 not met (0)

**Response:**

```

```

### g558 [retrieval] P1/en
**Q:** What is LALIN's full name?

**Fails:** missing any-of ['กิตติ', 'Kitti']; missing any-of ['ราชเกษม', 'Rajkasemkit']

**Response:**

```

```

### g563 [retrieval] P1/th
**Q:** ขออีเมลของคุณ SANTA หน่อยครับ

**Fails:** missing any-of ['CHANTANA.RA@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g567 [noisy_name_form] P1/en
**Q:** Hi, do you have the email of Khun Kamala Chaisonsavang, our CFO?

**Fails:** missing any-of ['KAMALA.CH@FAHMAI.CO.TH']

**Response:**

```
no record found
```

### g568 [noisy_name_form] P1/th
**Q:** เบอร์ต่อของคุณ Jutamas ที่เป็น EA ของ CTO เบอร์อะไรคะ

**Fails:** missing any-of ['77008']

**Response:**

```
ไม่พบข้อมูลคุณ Jutamas ที่มีตำแหน่งเป็น EA ของ CTO ในระบบค่ะ
```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Phongchongrak (Boom) works on the **16th floor** of FahMai Tower (BKK-R9).
```

### g572 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Sukum Suwanfahsai manager ทีม chat support หน่อยค่ะ

**Fails:** missing any-of ['SUKHUM.SU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```


_+33 more failures — see results.jsonl_
