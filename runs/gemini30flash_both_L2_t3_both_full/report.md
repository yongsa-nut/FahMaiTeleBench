# Run: `gemini30flash_both_L2_t3_both_full`

**Overall: 569/626 pass (90.9%)**

## By bucket

| Bucket | Pass/Total | Rate |
|---|---|---|
| evp_identity_by_code | 4/4 | 100.0% |
| evp_identity_by_description | 4/4 | 100.0% |
| evp_secretary | 5/5 | 100.0% |
| vp_identity | 5/5 | 100.0% |
| ceo_president | 4/4 | 100.0% |
| name_lookup | 20/20 | 100.0% |
| casual_name_lookup | 15/15 | 100.0% |
| dept_listing_small | 7/7 | 100.0% |
| dept_member_count | 15/15 | 100.0% |
| section_listing | 4/4 | 100.0% |
| org_informal_listing | 6/6 | 100.0% |
| tier_listing | 6/6 | 100.0% |
| org_plus_person | 3/3 | 100.0% |
| multi_entity_turn | 20/20 | 100.0% |
| subsidiary_md | 8/8 | 100.0% |
| email_mobile_lookup | 7/7 | 100.0% |
| hard_bridge_lookup | 6/6 | 100.0% |
| refuse | 88/90 | 97.8% |
| evp_vs_vp_disambig | 24/25 | 96.0% |
| counterfactual | 24/25 | 96.0% |
| retrieval | 13/14 | 92.9% |
| surname_family | 22/24 | 91.7% |
| deep_multihop | 11/12 | 91.7% |
| nickname_grid | 55/61 | 90.2% |
| thai_knowledge | 9/10 | 90.0% |
| hard_nickname_variant | 9/10 | 90.0% |
| brand_prior | 9/10 | 90.0% |
| dept_listing_medium | 7/8 | 87.5% |
| bilingual | 35/40 | 87.5% |
| extension_reverse | 6/7 | 85.7% |
| listing_count | 17/20 | 85.0% |
| hard_multihop | 22/26 | 84.6% |
| email_identity_lookup | 5/6 | 83.3% |
| noisy_name_form | 16/20 | 80.0% |
| enterprise_shorthand | 16/20 | 80.0% |
| superlative | 8/10 | 80.0% |
| subsidiary_routing | 9/12 | 75.0% |
| hard_implicit_hierarchy | 14/19 | 73.7% |
| multi_hop | 11/18 | 61.1% |

## By priority

- P0: 216/226 (95.6%)
- P1: 321/364 (88.2%)
- P2: 32/36 (88.9%)

## Failures (57)

### g171 [nickname_grid] P0/th
**Q:** เสือ ที่ KS เบอร์อะไร

**Fails:** missing any-of ['Anuboonrueng', 'อนุบุญเรือง']

**Response:**

```
คุณวชิร (เสือ) แผนก KS เบอร์ภายในคือ 72469 ครับ
```

### g174 [nickname_grid] P0/th
**Q:** อรุณ ที่อยู่ SUP คือใคร

**Fails:** missing any-of ['Nim', 'นิ่ม']; missing any-of ['Chindaphithak', 'จินดาพิทักษ์']

**Response:**

```
ไม่พบข้อมูลของ "อรุณ" ในแผนกบริการลูกค้า (SUP) ครับ

อย่างไรก็ตาม ในแผนก SUP มีคนที่มีชื่อเล่นว่า **ตูน** (ซึ่งใกล้เคียงกับชื่อ อรุณ) อยู่ 2 ท่าน คือ:
*   คุณ**ดาริกา อาวุทธ์ดี (ตูน)** - รองประธานฝ่ายบริการลูกค้า (SUPVP)
*   คุณ**ฟ้า กิตติชาติเจริญ (ตูน)** - เจ้าหน้าที่บริการลูกค้าทางโทรศัพท์

หากคุณหมายถึง "อรุณ" ในแผนกอื่น มีหลายท่าน เช่น:
*   **อรุณ บุญอมรินทร์ (ฟลุ๊ค)** - แผนก SF (สายฟ้า)
*   
```

### g175 [nickname_grid] P0/th
**Q:** ตะวัน ที่อยู่ DN คือใคร

**Fails:** missing any-of ['Prija', 'พฤกษา']; missing any-of ['Manifa', 'มณีฟ้า']

**Response:**

```

```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่พบข้อมูลเบอร์โทรศัพท์ของคุณจงรัก สัมโชติ (ปุ๊ก) ในระบบครับ
```

### g190 [nickname_grid] P0/th
**Q:** นัตตี้คือใครนะ

**Fails:** missing any-of ['นัต', 'นัต', 'ไม่พบข้อมูล']

**Response:**

```

```

### g212 [dept_listing_medium] P1/en
**Q:** who's in OPS-FAC

**Fails:** min_items 5 not met (4)

**Response:**

```
The OPS-FAC (Facilities) section has 23 employees. Here are the leads and managers:

**Managers:**
*   **Kritsada Thanakaewsai (กฤษฎา ธนแก้วใส)** – Extension: 76199
*   **Narin Kaewsaijai (นรินทร์ แก้วใสใจ)** – Extension: 76684

**Leads:**
*   **Ying Thanachaidee (หญิง ธนชัยดี)** – Extension: 79536
*   **Chonlathee Athikobsook (ชลธี อธิกอบสุข)** – Extension: 74105, Mobile: 087-945-5716 (Nickname: 
```

### g285 [extension_reverse] P2/en
**Q:** ext 71215 belongs to?

**Fails:** missing any-of ['Tanet', 'ธเนศ']; missing any-of ['Buathongprasert', 'บัวทองประเสริฐ']

**Response:**

```

```

### g311 [email_identity_lookup] P0/th
**Q:** เจ้าของอีเมล RACHINI.AR@FAHMAI.CO.TH คือใคร

**Fails:** missing any-of ['Rachini', 'ราชินี']; missing any-of ['Arthitkulsuk', 'อาทิตย์สุข']

**Response:**

```

```

### g333 [refuse] P0/th
**Q:** VP การตลาดของ LG คือใคร

**Fails:** missing any-of ['ไม่ใช่ข้อมูลของฟ้าใหม่', 'ไม่ใช่พนักงานฟ้าใหม่', 'ไม่ใช่ข้อมูลฟ้าใหม่']

**Response:**

```
VP ฝ่ายการตลาด (MKT) คือ คุณคะวัง กอบสุขรัตน์ (โอ) ครับ
```

### g351 [hard_multihop] P0/th
**Q:** ผู้บริหารที่มีจุฑามาศ แก้วใสพงศ์เป็นเลขานุการคือใคร

**Fails:** missing any-of ['Rittichai', 'ฤทธิชัย']; missing any-of ['Kaewsaiphinyo', 'แก้วใสภิญโญ']

**Response:**

```
จุฑามาศ แก้วใสพงศ์ (มิ้น) เป็นเลขานุการของ **CTO** (ผู้บริหารฝ่ายเทคโนโลยี) ครับ
```

### g352 [hard_multihop] P0/th
**Q:** CEO-CoS ทีมเดียวกับใครบ้าง

**Fails:** min_items 1 not met (0)

**Response:**

```
หน่วย CEO-CoS (หัวหน้าสำนักงานประธาน) มีสมาชิกคือ คุณบูม (กิตติคุณ พงจงรัก) โดยสังกัดอยู่ในฝ่าย CEO และส่วนงาน CEO-OFF (Office of the CEO) ร่วมกับตำแหน่งเหล่านี้ครับ:

*   **CEO:** คุณจิรโรจน์ (JIRAROJ)
*   **CEO-EA:** คุณน้ำ (NAM) เลขานุการบริหาร
*   **CEO-CoS:** คุณบูม (BOOM) หัวหน้าสำนักงานประธาน
```

### g376 [thai_knowledge] P0/th
**Q:** CBI สาขาอยู่ไหน

**Fails:** missing any-of ['ชลบุรี', 'Chonburi']

**Response:**

```


```

### g393 [hard_nickname_variant] P1/th
**Q:** ฟิล์มมี่เบอร์อะไร

**Fails:** missing any-of ['ศุภเดช', 'Suppadet', 'เอกลักษณ์']

**Response:**

```

```

### g404 [refuse] P1/th
**Q:** ขอเบอร์ต่อคุณ ถาวร จิตรานนท์ฟ้า หน่อยครับ

**Fails:** has ext pattern

**Response:**

```
ไม่พบข้อมูลชื่อ ถาวร จิตรานนท์ฟ้า ในระบบครับ

อย่างไรก็ตาม ในระบบมีพนักงานชื่อ **ถาวร** หลายท่าน ท่านที่นามสกุลใกล้เคียงที่สุดคือ **คุณถาวร ประฟ้าใส** (ฝ่ายบริการลูกค้า) เบอร์ต่อ **78993** ครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
คุณทัศนีย์ มณีพงศ์ สังกัดฝ่าย **DN (ดาวเหนือ)** โดยผู้บริหารสูงสุดของหน่วยงานนี้ (General Manager) คือ คุณ**วิเชียร พงหอมกลิ่น** ครับ

**อีเมล:** WICHIAN.PH@FAHMAI.CO.TH
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
คุณอัมพร ประฟ้า สังกัดแผนกคลื่นเสียง (KS) โดยผู้บริหารสูงสุดของแผนก (GM) คือคุณราม ลวรรณ ครับ

**อีเมล:** RAM.LA@FAHMAI.CO.TH
```

### g452 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Daonuea (DN)

**Fails:** missing any-of ['เรืองศักดิ์', 'Ruangsak']; missing any-of ['เทพเกียรติกำจร', 'Thepkiatkamjorn']

**Response:**

```
ผู้บริหารสูงสุดของแผนก DaoNuea (DN) คือ **คุณวิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)** ตำแหน่ง ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (GENERAL MANAGER OF DAONUEA) ครับ
```

### g453 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Judchuem (JC) department?

**Fails:** missing any-of ['ราชินี', 'Rachini']; missing any-of ['อาทิตย์สุข', 'Arthitkulsuk']

**Response:**

```
The most senior person heading the Judchuem (JC) department is **Saran Awutmani (สรัล อาวุทธ์มณี)**.

*   **Position:** General Manager (GM) of Judchuem
*   **Email:** SARAN.AW@FAHMAI.CO.TH
*   **Extension:** 78762
*   **Mobile:** 064-655-7513
*   **Office:** FahMai Tower 24F
```

### g454 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Kluensiang (KS)

**Fails:** missing any-of ['ธเนศ', 'Tanet']; missing any-of ['บัวทองประเสริฐ', 'Buathongprasert']

**Response:**

```
คุณราม ลวรรณ (จุ๊บ) เป็นผู้จัดการทั่วไปแบรนด์คลื่นเสียง (General Manager of Kluensiang) ครับ
```

### g455 [hard_implicit_hierarchy] P1/en
**Q:** Who is the most senior person heading the Legal (LEG) department?

**Fails:** missing any-of ['ไพโรจน์', 'Phairoj']; missing any-of ['มหากุล', 'Mahakun']

**Response:**

```

```

### g456 [hard_implicit_hierarchy] P1/th
**Q:** ใครเป็นผู้บริหารสูงสุดของแผนก Wongkhojon (WK)

**Fails:** missing any-of ['คึกฤทธิ์', 'Kukrit']; missing any-of ['อัครเจริญ', 'Akaracharoen']

**Response:**

```
ผู้บริหารสูงสุดของแผนกวงโคจร (WK) คือ **คุณกฤษ มหาแก้วใส (ขิง)** ตำแหน่งผู้จัดการทั่วไปแบรนด์วงโคจร (General Manager of Wongkhojon) ครับ
```

### g475 [bilingual] P1/th
**Q:** รหัสหน่วยงาน (unit code) ของ Chief of Staff คืออะไรครับ

**Fails:** missing any-of ['CEO-CoS']

**Response:**

```

```

### g491 [bilingual] P1/en
**Q:** What is the Chief of Staff's Thai nickname (ชื่อเล่น)?

**Fails:** missing any-of ['บูม', 'Boom', 'BOOM']

**Response:**

```
คุณเป้ (PE)
```

### g494 [bilingual] P1/en
**Q:** What is the VP of Marketing's Thai nickname (ชื่อเล่น)?

**Fails:** missing any-of ['โอ', 'Oh', 'OH']

**Response:**

```


```

### g514 [bilingual] P1/th
**Q:** nickname ของ Chief Of Staff คืออะไรครับ

**Fails:** missing any-of ['บูม', 'Boom', 'BOOM']

**Response:**

```
ข้อมูของ Chief Of Staff (เลขานุการของ CEO) คือ คุณเป้ (PE) ครับ
```

### g515 [bilingual] P1/th
**Q:** ช่วยหา unit code ของ Vice President Finance ให้ทีครับ

**Fails:** missing any-of ['FINVP']

**Response:**

```

```

### g528 [listing_count] P1/th
**Q:** มีพนักงานกี่คนที่อยู่แผนก B2B ระดับ IC และเริ่มงานในปี 2021 ครับ

**Fails:** missing count 5

**Response:**

```
มีพนักงานแผนก B2B ระดับ IC ที่เริ่มงานในปี 2021 ทั้งหมด 4 คน ดังนี้ครับ:

*   **ณัฏฐพล ศรีพิทักษ์** (ผู้แทนขายองค์กร)
*   **อรอนงค์ รัตนเกษม** (เจ้าหน้าที่บริการลูกค้าองค์กร) – ชื่อเล่น: กบ
*   **อรุณ สัมภิญโญ** (ผู้แทนขายองค์กร) – ชื่อเล่น: แมว
*   **ไพบูลย์ บุญมางาม** (วิศวกรโซลูชันองค์กร) – ชื่อเล่น: ปุ๊ก
```

### g533 [listing_count] P1/en
**Q:** How many employees are in the DN department at IC level who started in 2020?

**Fails:** missing count 6

**Response:**

```
There are 5 employees in the DN (DaoNuea) department at the IC level who started in 2020:

*   **ทินกร นราชาญณรงค์ (กบ)** – DAONUEA BRAND OPERATIONS
*   **โยธกา อัมพรสว่าง** – DAONUEA PRODUCT ENGINEER
*   **วีระ พงอัสนี (มะม่วง)** – DAONUEA PRODUCT MANAGER
*   **พฤกษา มณีฟ้า (ตะวัน)** – DAONUEA BRAND OPERATIONS
*   **ธนพล อัศนีสรี (มด)** – DAONUEA PRODUCT MANAGER
```

### g535 [listing_count] P1/en
**Q:** How many employees are in the DN department at Lead level who started in 2022?

**Fails:** missing count 5

**Response:**

```
There are **6** employees in the DN department at the Lead level who started in 2022:

*   **Apichai Thanabun (Jub)** – Lead Daonuea Brand Marketer
*   **Thanaphon Phichaiyawong (Phai)** – Lead Daonuea Product Manager
*   **Krittin Anucharoen** – Lead Daonuea Brand Operations
*   **Ram Mahakittipong** – Lead Daonuea Brand Operations
*   **Veera Chaichokdee** – Lead Daonuea Product Manager
*   **Ki
```

### g555 [retrieval] P1/th
**Q:** คุณ KAFAE ชื่อจริง-นามสกุลว่าอะไรครับ

**Fails:** missing any-of ['น้ำทิพย์', 'Namthip']; missing any-of ['จินดาสินธุ์', 'Chindasin']

**Response:**

```

```

### g569 [noisy_name_form] P1/en
**Q:** Which floor is Kittikhun Pongchongrak, the Chief of Staff, working on?

**Fails:** missing any-of ['FahMai Tower 16F', 'ชั้น 16', 'ชั้น16']

**Response:**

```
Kittikhun Phongchongrak, the Chief of Staff, works on the **16th floor** of FahMai Tower.
```

### g572 [noisy_name_form] P1/th
**Q:** ขออีเมลของคุณ Sukum Suwanfahsai manager ทีม chat support หน่อยค่ะ

**Fails:** missing any-of ['SUKHUM.SU@FAHMAI.CO.TH']

**Response:**

```
ไม่พบข้อมูล
```

### g574 [noisy_name_form] P1/en
**Q:** Where's Ladawan Samphat's office? She's the EA to our CHRO.

**Fails:** missing any-of ['FahMai Tower 24F', 'ชั้น 24', 'ชั้น24']

**Response:**

```
 Ladawan Samphat's office is located at FahMai Tower, 24th Floor (BKK-R9).
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
no record found
```

### g587 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณจรูญ ชัยบุญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74877']

**Response:**

```
คุณจรูญ ชัยบุญ สังกัดฝ่าย B2B โดยผู้ที่มีตำแหน่งสูงสุดในฝ่ายนี้มี 2 ท่าน ได้แก่:

*   **คุณอุกฤษฎ์ วัชรเสริม** (B2BVP): เบอร์ต่อ 79274
*   **คุณธัญญา เจริญผลภิญโญ** (B2BACC): เบอร์ต่อ 71547
```

### g589 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณทัศนีย์ มณีพงศ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76457']

**Response:**

```
คุณเรืองศักดิ์ เทพเกียรติกำจร (รองประธานฝ่ายดาวเหนือ) เบอร์ต่อคือ 72280 ครับ
```

### g591 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณอภิชัย จิตรานนท์เจริญสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['77404']

**Response:**

```
เบอร์ต่อของ คุณกมลา ชัยสนธิ์สว่าง (ประธานเจ้าหน้าที่การเงิน) ซึ่งเป็นตำแหน่งสูงสุดในแผนก FIN คือ 74921 ครับ
```

### g593 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณมนตรา บุญเรืองโชติสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['74296']

**Response:**

```
เบอร์ต่อของ คุณณฐามน อภิชัยดี (CHRO) ซึ่งเป็นตำแหน่งสูงสุดในแผนกทรัพยากรบุคคล (HR) คือ 79303 ครับ
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```
คุณวิโรจน์ มหาวัฒน์ สังกัดแผนก **จุดเชื่อม (JC)** โดยผู้ที่มีตำแหน่งสูงสุดในส่วนงานนี้คือ **คุณสรัล อาวุทธ์มณี** (ผู้จัดการทั่วไปแบรนด์จุดเชื่อม) เบอร์ต่อคือ **78762** ครับ
```

### g597 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณศักดิ์สิทธิ์ สัมชากัญญ์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['76044']

**Response:**

```
คุณราม ลวรรณ (จุ๊บ) ซึ่งเป็น General Manager (ตำแหน่งสูงสุดของส่วนงาน KS) มีเบอร์ต่อคือ 75965 ครับ
```

### g599 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณคำรณ ศรีอัญชลีสังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['73069']

**Response:**

```
เบอร์ต่อของคุณคึกฤทธิ์ บุษราคัมวงศ์ (VP ฝ่าย OPS) คือ 77358 ครับ
```

### g606 [surname_family] P1/en
**Q:** List everyone with the surname เขียวขจีศรี (give all of them).

**Fails:** missing count 3

**Response:**

```
-   **อัจฉรา เขียวขจีศรี (บีม)** - ผู้อำนวยการฝ่ายนักการตลาด CRM (MKT)
-   **ไพฑูรย์ เขียวขจีศรี** - หัวหน้าทีมนักการตลาดแบรนด์สายฟ้า (SF)
-   **ปกรณ์ เขียวขจีศรี (ลม)** - วิศวกรข้อมูล (TEC)
```

### g622 [surname_family] P1/en
**Q:** List everyone with the surname อภิญญาเสริม (give all of them).

**Fails:** missing count 2

**Response:**

```
Here are the employees with the surname อภิญญาเสริม:

*   **วีระ อภิญญาเสริม (เบอร์รี่)** - SAIFAH PRODUCT MANAGER (SF)
    *   Email: VEERA.AP@FAHMAI.CO.TH
*   **ดาหลา อภิญญาเสริม** - DAONUEA BRAND OPERATIONS (DN)
    *   Email: DARHA.AP@FAHMAI.CO.TH
    *   Extension: 75781
```

### g639 [nickname_grid] P1/th
**Q:** เอ คือใคร มีใครบ้าง

**Fails:** min_items 3 not met (0)

**Response:**

```

```

### g640 [evp_vs_vp_disambig] P1/th
**Q:** FINVP-SEC ใครนะ ไม่ใช่ FINVP

**Fails:** missing any-of ['Buppha', 'บุปผา']; missing any-of ['Aphiapinya', 'อภิอภิญญา']

**Response:**

```

```

### g666 [enterprise_shorthand] P1/en
**Q:** How many staff work at the Rama IX (R9) HQ branch?

**Fails:** missing any-of ['1255']

**Response:**

```
There are 1,255 staff members working at the Rama IX (BKK-R9) HQ branch.
```

### g667 [enterprise_shorthand] P1/th
**Q:** พนักงานสาขาเชียงใหม่ (CNX) มีกี่คน

**Fails:** missing count 79

**Response:**

```

```

### g678 [enterprise_shorthand] P1/en
**Q:** Who is the sales director at the Hat Yai (HDY) branch?

**Fails:** missing any-of ['Thanakrit', 'ธนกฤต']; missing any-of ['Boonnamraksa', 'บุญนำรักษา']

**Response:**

```

```

### g682 [enterprise_shorthand] P1/th
**Q:** หัวหน้าทีมฟินฯ คือใคร

**Fails:** missing any-of ['Kamala', 'กมลา']; missing any-of ['Chaisonsawang', 'ชัยสนธิ์สว่าง']

**Response:**

```
หัวหน้าทีม FIN (หัวหน้าฝ่ายการเงิน) คือ **คุณแสงดาว พิดวงกมล (มอคค่า)** รองประธานฝ่ายการเงิน (VP Finance)
*   **เบอร์โทรศัพท์:** 097-641-8674
*   **เบอร์ต่อ:** 77907
*   **อีเมล:** SAENGDAO.PH@FAHMAI.CO.TH
*   **สถานที่ปฏิบัติงาน:** FahMai Tower ชั้น 19
```

### g739 [brand_prior] P1/th
**Q:** ขอเบอร์ต่อของ GM แบรนด์ดาวเหนือ หน่อย

**Fails:** missing any-of ['76999']

**Response:**

```

```


_+7 more failures — see results.jsonl_
