# Run: `deepseekv4flash_grep-only_L2_t1_grep_v10full`

**Overall: 605/626 pass (96.6%)**

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
| hard_bridge_lookup | 6/6 | 100.0% |
| hard_implicit_hierarchy | 19/19 | 100.0% |
| thai_knowledge | 10/10 | 100.0% |
| surname_family | 24/24 | 100.0% |
| bilingual | 40/40 | 100.0% |
| listing_count | 20/20 | 100.0% |
| retrieval | 14/14 | 100.0% |
| enterprise_shorthand | 20/20 | 100.0% |
| brand_prior | 10/10 | 100.0% |
| subsidiary_routing | 12/12 | 100.0% |
| refuse | 89/90 | 98.9% |
| counterfactual | 24/25 | 96.0% |
| noisy_name_form | 19/20 | 95.0% |
| multi_hop | 17/18 | 94.4% |
| nickname_grid | 57/61 | 93.4% |
| hard_nickname_variant | 9/10 | 90.0% |
| name_lookup | 17/20 | 85.0% |
| deep_multihop | 10/12 | 83.3% |
| hard_multihop | 21/26 | 80.8% |
| superlative | 8/10 | 80.0% |

## By priority

- P0: 220/226 (97.3%)
- P1: 353/364 (97.0%)
- P2: 32/36 (88.9%)

## Failures (21)

### g120 [name_lookup] P1/th
**Q:** ขอเบอร์ ณัฏฐพล ชากัญญ์รักษา หน่อย

**Fails:** missing any-of ['78664', 'NATTHAPHON.CH', '064-253-9320']

**Response:**

```
ไม่พบข้อมูล
```

### g121 [name_lookup] P1/th
**Q:** ขอเบอร์ สรพงษ์ วิศวงษ์ หน่อย

**Fails:** missing any-of ['72279', 'SORAPONG.WI', '091-061-7212']

**Response:**

```
ไม่พบข้อมูล
```

### g123 [name_lookup] P1/th
**Q:** ขอเบอร์ต่อของ อาวุธ จันทภิญโญ

**Fails:** missing any-of ['77863', 'AWUT.CH2', '099-470-0038']

**Response:**

```
ไม่พบข้อมูล
```

### g160 [nickname_grid] P0/th
**Q:** บอส มีใครบ้าง

**Fails:** min_items 3 not met (2)

**Response:**

```
นี่คือ **ผู้บริหารระดับ C-level** ของฟ้าใหม่ทั้งหมด 7 ท่านครับ 🏢

| ตำแหน่ง | ชื่อ (EN) | ชื่อเล่น |
|:--|:--|:--|
| **CEO** – ประธานเจ้าหน้าที่บริหาร | VACHIR CHIRABUN (วชิร จิรบุญ) | เบอร์รี่ |
| **CFO** – ประธานเจ้าหน้าที่การเงิน | KAMALA CHAISONSAWANG (กมลา ชัยสนธิ์สว่าง) | — |
| **CTO** – ประธานเจ้าหน้าที่เทคโนโลยี | RITTICHAI KAEWSAIPHINYO (ฤทธิชัย แก้วใสภิญโญ) | ปันปัน |
| **COO** – ประธานเ
```

### g184 [nickname_grid] P0/th
**Q:** ปุ๊ก จงรัก เบอร์อะไร

**Fails:** missing any-of ['CHONGRAK.SA']

**Response:**

```
ไม่พบข้อมูลเบอร์โทรของ **ปุ๊ก (จงรัก สัมโชติ)** ในระบบ — ทั้งเบอร์มือถือและเบอร์ภายในว่างอยู่ครับ
```

### g317 [refuse] P0/th
**Q:** สัญชาติ CMO

**Fails:** has ext pattern

**Response:**

```
ไม่สามารถให้ข้อมูลนี้ได้ — ข้อมูลสัญชาติไม่ได้อยู่ในระบบพนักงานของฟ้าใหม่

หากคุณต้องการข้อมูลอื่น เช่น ชื่อหรืออีเมลของ CMO สามารถแจ้งได้ครับ

**CMO (CHIEF MARKETING OFFICER):** ส้ม กาญจน์สถิต (SOM KANSATHIT)
- อีเมล: SOM.KA@FAHMAI.CO.TH
- เบอร์ภายใน: 79005
```

### g355 [hard_multihop] P0/th
**Q:** หัวหน้า GM ดาวเหนือคือใคร

**Fails:** missing any-of ['Ruangsak', 'เรืองศักดิ์']; missing any-of ['Thepkiatkamjorn', 'เทพเกียรติกำจร']

**Response:**

```
**หัวหน้า GM ดาวเหนือ (DN-GM)** คือ **วิเชียร พงหอมกลิ่น (WICHIAN PHONGHOMKLIN)**  
ตำแหน่ง: ผู้จัดการทั่วไปแบรนด์ดาวเหนือ (GENERAL MANAGER OF DAONUEA)

📧 อีเมล: WICHIAN.PH@FAHMAI.CO.TH  
📞 เบอร์ภายใน: 76999  
📱 โทรศัพท์: 064-902-5307  
🏢 สำนักงาน: FahMai Tower 19F, สาขา BKK-R9
```

### g396 [hard_nickname_variant] P0/en
**Q:** MINTY's extension in FIN please

**Fails:** missing any-of ['เบญจวรรณ', 'Benjawan', 'โชคดีกำจร']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อ MINTY ในแผนก FIN หรือในระบบครับ
```

### g442 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RUANGSAK.TH@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **DN (ดาวเหนือ)** ที่คุณทัศนีย์ มณีพงศ์ สังกัดอยู่ คือ

**วิเชียร พงหอมกลิ่น** (ตำแหน่ง GM แบรนด์ดาวเหนือ)
📧 อีเมล: **WICHIAN.PH@FAHMAI.CO.TH**
```

### g444 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณละไม บุญพงศ์ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['RACHINI.AR@FAHMAI.CO.TH']

**Response:**

```
**ละไม บุญพงศ์** สังกัดแผนก **JC (จุดเชื่อม / JudChuem)**

ผู้บริหารสูงสุดของแผนก JC คือ **General Manager (GM)** ของแบรนด์จุดเชื่อม — **สรัล อาวุทธ์มณี (SARAN AWUTMANI)**

อีเมล: **SARAN.AW@FAHMAI.CO.TH** 📧
```

### g446 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณอัมพร ประฟ้า สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['TANET.BU@FAHMAI.CO.TH']

**Response:**

```
ผู้บริหารสูงสุดของแผนก **KS (คลื่นเสียง / KluenSiang)** คือ

**ราม ลวรรณ (RAM LAWAN)** — ผู้จัดการทั่วไปแบรนด์คลื่นเสียง  
📧 อีเมล: `RAM.LA@FAHMAI.CO.TH`
```

### g450 [hard_multihop] P1/th
**Q:** ขออีเมลของผู้บริหารสูงสุดของแผนกที่คุณธนพล พิประเสริฐ สังกัดอยู่หน่อยครับ

**Fails:** missing any-of ['KUKRIT.AK@FAHMAI.CO.TH']

**Response:**

```
**คุณธนพล พิประเสริฐ** สังกัดอยู่แผนก **WK (วงโคจร)** ซึ่งผู้บริหารสูงสุดของแผนกนี้คือ **ผู้จัดการทั่วไปแบรนด์วงโคจร (GM of WongKhoJon)**

👉 **คุณกฤษ มหาแก้วใส (KRIS MAHAKAEWSAI)** — อีเมล: **KRIS.MA@FAHMAI.CO.TH**
```

### g585 [noisy_name_form] P1/en
**Q:** Ravi, the Director of Support Training — what's his extension?

**Fails:** missing any-of ['76523']

**Response:**

```
ไม่พบข้อมูล (no record found)
```

### g595 [multi_hop] P1/th
**Q:** ขอเบอร์ต่อของคนที่ตำแหน่งสูงสุดในส่วนงานที่คุณวิโรจน์ มหาวัฒน์สังกัดอยู่ หน่อยครับ

**Fails:** missing any-of ['78017']

**Response:**

```

```

### g639 [nickname_grid] P1/th
**Q:** เอ คือใคร มีใครบ้าง

**Fails:** min_items 3 not met (1)

**Response:**

```
**"เอ" คือ ภาสกร ชากัญญ์ทอง (PHASSAKORN CHAKANTHONG)**  
สังกัด TEC-PLT (Platform Engineer)  
📧 PHASSAKORN.CH2@FAHMAI.CO.TH  
📞 ต่อ 71896 / มือถือ 097-546-0978  
🏢 FahMai Tower 24F (BKK-R9)

มีคนเดียวในระบบที่ใช้ชื่อเล่น **"เอ"** ค่ะ ส่วนรายชื่ออื่นที่มี "เอ" ในชื่อเป็นส่วนหนึ่งของคำอื่น (เช่น เอกพล, เอพริล ฯลฯ) ไม่ใช่ชื่อเล่นเอโดยตรง
```

### g728 [nickname_grid] P0/th
**Q:** ชื่อเล่นของ DNVP คืออะไร

**Fails:** has ext pattern

**Response:**

```
DNVP (รองประธานฝ่ายดาวเหนือ) คือ **เรืองศักดิ์ เทพเกียรติกำจร** (Ruang Sak Thepkiatkamjorn) — **ไม่มีชื่อเล่นในระบบ**

หากต้องการติดต่อ: อีเมล `RUANGSAK.TH@FAHMAI.CO.TH` เบอร์ภายใน `72280`
```

### g760 [counterfactual] P1/en
**Q:** I heard ไพโรจน์ มหากุล is the CEO — can I get their extension?

**Fails:** missing any-of ['LEGVP', 'VP Legal', 'วชิร']

**Response:**

```
ไม่พบข้อมูล — ไม่มีพนักงานชื่อ **ไพโรจน์ มหากุล** ในระบบของฟ้าใหม่
```

### g826 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the most employees — what's the email of the VP who heads that department?

**Fails:** missing any-of ['WIRIYA.CH@FAHMAI.CO.TH']

**Response:**

```
Let me get employee counts per department properly.

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="query_csv">
<｜｜DSML｜｜parameter name="columns" string="false">["Department"]</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="filters" string="false">{"Department": "FIN"}</｜｜DSML｜｜parameter>
<｜｜DSML｜｜parameter name="max_matches" string="false">300</｜｜DSML｜｜parameter>
</｜｜DSML｜｜invoke>
<｜｜DSML｜｜invoke name="
```

### g830 [deep_multihop] P2/en
**Q:** Among the departments headed by a VP, take the one with the fewest employees — what's the email of the secretary of that department's VP?

**Fails:** missing any-of ['MONTRA.WI@FAHMAI.CO.TH']

**Response:**

```
Let me count employees in each VP-headed department.


```

### g840 [superlative] P2/th
**Q:** section ไหนของฟ้าใหม่ที่มีพนักงานมากที่สุดครับ

**Fails:** missing any-of ['RET-BKK-LP']

**Response:**

```
จากข้อมูลที่ค้นหา **แผนก RET (เครือข่ายร้านค้า)** มีพนักงานมากที่สุดในฟ้าใหม่ครับ โดยมีทั้งหมด **416 คน** รองลงมาคือ TEC (เทคโนโลยี) 240 คน, MKT (การตลาด) 234 คน, OPS (ปฏิบัติการ) 232 คน, และ SUP (บริการลูกค้า) 217 คนครับ
```

### g841 [superlative] P2/en
**Q:** Which department has the most employees company-wide?

**Fails:** missing any-of ['380']

**Response:**

```
The department with the most employees company-wide is **RET** (Retail Network / ฝ่ายเครือข่ายร้านค้า) with **437 employees**.

Here's the full breakdown:

| Department | Count |
|---|---|
| RET (Retail) | 437 |
| TEC (Technology) | 267 |
| OPS (Operations) | 235 |
| MKT (Marketing) | 234 |
| SUP (Support) | 234 |
| LOG (Logistics) | 182 |
| HR (Human Resources) | ~183 |
| SF (สายฟ้า) | 140 |
| DN
```

