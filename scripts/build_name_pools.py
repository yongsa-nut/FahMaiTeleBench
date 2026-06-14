"""Build curated Thai name pools + nickname variants from hand-collected source lists.

Sources (see provenance/name_sources.md):
- First names: ling-app.com "150+ Names In Thai" + Legit.ng "130+ Thai names" + Moonboon "110 cute Thai names"
- Surnames: Ling-app Medium "100 Common Thai Surnames" + Forebears.io frequency top
- Nicknames: elitenamecrew.com "501+ Thai Nicknames" + findnamez.com "120+ Thai Nicknames"

Output:
- name_pools/first_names_th.json
- name_pools/last_names_th.json
- name_pools/nicknames_th.json
- name_pools/nickname_variants.json

Determinism: pools are alphabetically sorted for byte-stable output.
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "name_pools"
OUT.mkdir(parents=True, exist_ok=True)

# ============================================================================
# FIRST NAMES (th, en, gender, meaning)
# Skewed toward uncommon / non-top-100 names to make first-name disambiguation
# harder. Includes all three ling-app + legit.ng + moonboon sources combined.
# ============================================================================
FIRST_NAMES = [
    # --- Male ---
    ("อาทิตย์",    "ARTHIT",      "m", "sun"),
    ("กิตติศักดิ์",  "KITTISAK",    "m", "renowned, powerful"),
    ("อาวุธ",      "AWUT",        "m", "weapon"),
    ("บดินทร์",    "BADIN",       "m", "king"),
    ("ไชยา",       "CHAIYA",      "m", "victory"),
    ("ชยพล",       "CHAYAPHON",   "m", "great fighter"),
    ("เกษม",       "KASEM",       "m", "happiness"),
    ("กิตติชัย",    "KITTICHAI",   "m", "famous victory"),
    ("กิตติชาติ",   "KITTICHAT",   "m", "famous clan"),
    ("กิตติพงศ์",   "KITTIPONG",   "m", "honorable clan"),
    ("กล้าหาญ",   "KLAHARN",     "m", "very brave"),
    ("ก้องภพ",     "KONGPHOP",    "m", "famous one"),
    ("ไพฑูรย์",    "PAITOON",     "m", "moonstone"),
    ("ไพบูลย์",    "PHAIBUN",     "m", "to prosper"),
    ("ภาสกร",     "PHASSAKORN",  "m", "sun"),
    ("พิชัย",       "PHICHAI",     "m", "triumphant"),
    ("ประยุทธ์",    "PRAYUT",      "m", "to fight"),
    ("ปัญญา",     "PANYA",       "m", "wisdom"),
    ("ปิยวัฒน์",    "PIYAWAT",     "m", "prosperous"),
    ("เรืองฤทธิ์",  "RUANGRIT",    "m", "mighty"),
    ("เรืองศักดิ์",  "RUANGSAK",    "m", "mighty, powerful"),
    ("สัจจะ",     "SATJA",       "m", "truth"),
    ("ศักดิ์ดา",    "SAKDA",       "m", "power"),
    ("ศักดิ์สิทธิ์",  "SAKSIT",      "m", "sacred"),
    ("ศุภเดช",     "SUPPADET",    "m", "powerful"),
    ("ธนชาติ",    "THANACHART",  "m", "wealthy family"),
    ("ธีรภพ",      "THEERAPHOP",  "m", "smart"),
    ("เอกลักษณ์",  "EKKALUCK",    "m", "distinctive"),
    ("ณัฐกานต์",   "NATTHAKAN",   "m", "wise and dear"),
    ("ณัฏฐพล",    "NATTHAPHON",  "m", "knowledgeable strength"),
    ("คำรณ",      "KHAMRON",     "m", "loud word"),
    ("อดิเทพ",    "ADITHEP",     "m", "excellent god"),
    ("อนันดา",    "ANANDA",      "m", "prosperous"),
    ("อนุรักษ์",   "ANURAK",      "m", "guardian"),
    ("อรุณ",      "AROON",       "m", "chariot driver"),
    ("ชาตรี",     "CHATRI",      "m", "brave knight"),
    ("เชษฐ์",      "CHET",        "m", "elder brother"),
    ("จงรัก",      "CHONGRAK",    "m", "faithful"),
    ("เดชา",      "DECHA",       "m", "powerful"),
    ("ดิเรก",      "DIREK",       "m", "smart ruler"),
    ("ก้อง",      "KONG",        "m", "resounding"),
    ("โกวิท",     "KOVIT",       "m", "expert"),
    ("ไกรสร",    "KRAISEE",     "m", "lion, brave"),
    ("กฤต",      "KRID",        "m", "ingenious"),
    ("คึกฤทธิ์",   "KUKRIT",      "m", "great authority"),
    ("ณรงค์",    "NARONG",      "m", "brave fighter"),
    ("นาวิน",    "NAVIN",       "m", "new"),
    ("นิรันดร์",   "NIRAN",       "m", "eternal"),
    ("ปกรณ์",    "PAKORN",      "m", "story"),
    ("พาณิช",    "PANIT",       "m", "beloved boy"),
    ("ฤทธิรงค์",  "RITTHIRONG",  "m", "good fighter"),
    ("วิริยะ",     "WIRIYA",      "m", "persistent"),
    ("วิสิทธิ์",    "WISIT",       "m", "glorious"),
    ("ยุทธ",      "YUT",         "m", "fearless"),
    ("เข้มแข็ง",  "KHEMKHAENG",  "m", "strong"),
    ("เกียรติ",   "KIET",        "m", "honorable"),
    ("ภูมิ",       "PHOOM",       "m", "earth"),
    ("ปิยบุตร",   "PIYABUTR",    "m", "father's son"),
    ("ประวัติ",   "PRAVAT",      "m", "historic"),
    ("ปรีดา",     "PREED",       "m", "joyful"),
    ("เปรม",     "PREM",        "m", "contentment"),
    # PUNYAA removed — duplicate Thai of PANYA with variant romanization
    ("ราม",      "RAM",         "m", "loud thunder"),
    ("สุเมธ",     "SUMATE",      "m", "intelligent"),
    ("ธนวัฒน์",  "TANAWAT",     "m", "knowledgeable"),
    ("ธเนศ",     "TANET",       "m", "rich"),
    ("ถวิน",     "TAWIN",       "m", "innocent"),
    ("ทนิน",     "THANIN",      "m", "big city"),
    ("ทินกร",    "THINNAKORN",  "m", "sun"),
    ("อุกฤษฎ์",  "UKRIT",       "m", "supreme"),
    ("วศิน",     "VASIN",       "m", "authoritarian"),
    ("วีระ",      "VEERA",       "m", "brave and daring"),
    ("วัฒน์",     "WAT",         "m", "army ruler"),
    ("สรพงษ์",  "SORAPONG",    "m", "virtuous lineage"),
    ("วิจิตร",    "VICHIT",      "m", "exquisite"),
    ("พรหมพงษ์", "PHROMPHONG",  "m", "descendant of Brahma"),
    ("ชลธี",      "CHONLATHEE",  "m", "river"),
    ("ถาวร",     "THAWAN",      "m", "permanent"),
    ("อิสระ",     "ISSARA",      "m", "freedom"),       # disambiguated from อิสรา/ISARA (f)
    ("ไกรฤกษ์",  "KRAIROEK",    "m", "auspicious and strong"),
    ("วิรัตน์",    "WIRAT",       "m", "brave"),
    ("ประเสริฐ",  "PRASERT",     "m", "excellent"),
    ("จรูญ",     "CHAROON",     "m", "flourishing"),
    ("ทรงพล",   "SONGPOL",     "m", "empowered"),
    ("บุญชู",     "BOONCHU",     "m", "merit-bringer"),
    ("มานิตย์",   "MANIT",       "m", "intelligence"),
    ("สมบัติ",    "SOMBAT",      "m", "treasure"),
    ("ธงชัย",    "THONGCHAI",   "m", "golden victory"),
    ("บุญมา",    "BUNMA",       "m", "merit has come"),
    ("ศักดิ์ชัย",  "SAKCHAI",     "m", "power and victory"),
    ("วิเชียร",   "WICHIAN",     "m", "diamond"),
    ("กิตติ",     "KITTI",       "m", "fame"),
    ("ไพโรจน์",  "PHAIROJ",     "m", "radiant"),
    ("สมพงษ์",   "SOMPHONG",    "m", "compatible"),
    ("มงคล",    "MONGKOL",     "m", "auspicious"),
    ("สนิท",     "SANIT",       "m", "close"),
    ("อภิชัย",    "APICHAI",     "m", "great success"),
    ("บุญเรือง",  "BOONRUANG",   "m", "light"),
    ("ชัยวัฒน์",   "CHAIWAT",     "m", "victory"),
    ("จักรี",     "CHAKRI",      "m", "wheel"),
    # DHANASAK removed — duplicate Thai of THANASAK with inconsistent romanization
    ("เอกพล",    "EAKPHOL",     "m", "good fortune"),
    ("จิรภัทร",   "JIRAPAT",     "m", "long-lasting"),
    ("กิตติคุณ",   "KITTIKHUN",   "m", "great fortune"),
    ("กฤษฎา",   "KRITSADA",    "m", "brilliant"),
    ("กฤติน",    "KRITTIN",     "m", "knowledgeable"),
    ("เมฆา",    "MEKHA",       "m", "moonlight"),
    ("นรินทร์",   "NARIN",       "m", "man of honor"),
    ("ณัฐพงษ์",  "NATTAPHONG",  "m", "gift of nature"),
    ("องอาจ",  "ONGART",      "m", "blessed"),
    ("พรไพร",  "PHONPHAI",    "m", "blessing"),
    ("ภูวดล",   "PHUWADON",    "m", "strong"),
    ("พงษ์กานต์","PONGKAN",     "m", "kindness"),
    ("พรกฤต",  "PONNAKRIT",   "m", "gift of God"),
    ("ราชตะ",   "RACHATA",     "m", "brave"),
    ("ฤทธิชัย",  "RITTICHAI",   "m", "brave"),
    ("ศศิปราภา","SASIPRAPA",   "m", "shining star"),
    ("สถาพร",  "SATHAPORN",   "m", "wise"),
    ("สมยศ",  "SOMYOT",      "m", "born to be happy"),
    ("สุจินดา", "SUJINDA",     "m", "beautiful"),
    ("สุขุม",    "SUKHUM",      "m", "happy"),
    ("สุกฤต",  "SUKRIT",      "m", "happiness"),
    ("ตะวัน",   "TAWAN",       "m", "sun"),
    ("ธีรพัฒน์", "TEERAPAT",    "m", "wise"),
    ("ธนกฤต",  "THANAKRIT",   "m", "prosperous"),
    ("ธนพล",  "THANAPHON",   "m", "prosperous"),
    ("ธนศักดิ์", "THANASAK",    "m", "strength"),
    ("วชิร",    "VACHIR",      "m", "diamond"),
    ("วิโรจน์",  "VIROJ",       "m", "to shine"),
    ("วิพันธ์", "WIPHAN",      "m", "bright"),
    ("ยศกร",  "YOTTHAKARN",  "m", "courageous"),
    ("ยุทธนา", "YUTHANA",     "m", "to win"),

    # --- Female ---
    ("มะลิ",     "MALI",        "f", "jasmine"),
    ("อนงค์",   "ANONG",       "f", "beautiful"),
    ("อัจฉรา",  "ATCHARA",     "f", "pretty angel"),
    ("อรจิรา",  "ORNCHIRA",    "f", "beautiful"),
    ("อัญชลี",  "ANCHALI",     "f", "greeting"),
    ("บุปผา",   "BUPPHA",      "f", "flower"),
    ("บุษบา",   "BUSABA",      "f", "floral"),
    ("ดารา",    "DARA",        "f", "star"),
    ("ดาหลา",  "DARHA",       "f", "flower"),
    ("กัลยา",    "KANLAYA",     "f", "good lady"),
    ("กมลา",   "KAMALA",      "f", "of the heart"),
    ("กาญจนา", "KANCHANA",    "f", "gold"),
    ("กัณณิกา", "KANNIKA",     "f", "flower"),
    ("กนก",    "KANOK",       "f", "design"),
    ("กัญญา",  "KANYA",       "f", "girl"),
    ("กานติมา", "KANTIMA",     "f", "beautiful girl"),
    ("ลัดดาวรรณ","LADDAWAN",   "f", "glorious"),
    ("มาลี",     "MALEE",       "f", "flower"),
    ("มนตรา",  "MONTRA",      "f", "spell caster"),
    ("งามจิตร", "NGAMCHIT",    "f", "good heart"),
    ("นงเยาว์", "NONGYAO",     "f", "young lady"),
    ("น้ำทิพย์",  "NAMTHIP",     "f", "nectar"),
    ("อรอนงค์", "ORANONG",     "f", "beautiful lady"),
    ("อรชร",   "ORACHON",     "f", "delicate"),
    ("อรญา",  "ORRAYA",      "f", "intelligent lady"),
    ("เพ็ญศรี", "PENSRI",      "f", "moon beauty"),
    ("พัชรี",    "PATCHAREE",   "f", "diamond"),
    ("ไพลิน",   "PHAILIN",     "f", "sapphire"),
    ("รัตนา",    "RATANA",      "f", "crystal"),
    ("รุ่งนภา",  "RUNGNAPA",    "f", "sky"),
    ("แสงดาว", "SAENGDAO",    "f", "starlight"),
    ("สุภาวดี",  "SUPHAWADEE",  "f", "beautiful girl"),
    ("สุจิรา",   "SUJIRA",      "f", "goodness"),
    ("สุดา",    "SUDA",        "f", "daughter"),
    ("สุณี",     "SUNEE",       "f", "good thing"),
    ("ทักษอร", "TAKSA-ORN",   "f", "clever girl"),
    ("ทัศนีย์",  "TASSANEE",    "f", "beautiful view"),
    ("หยาดทิพย์","YADTHIP",     "f", "beautiful"),
    ("อัปสร",   "APSARA",      "f", "celestial nymph"),
    ("เบญจวรรณ","BENJAWAN",   "f", "beautiful in every aspect"),
    ("ชฎา",   "CHADA",       "f", "crown"),
    ("จันทนา",  "CHANTANA",    "f", "thoughtful"),
    ("ชูใจ",    "CHUCHAI",     "f", "delightful"),
    ("ฟ้า",     "FAH",         "f", "sky"),
    ("อิสรา",   "ISARA",       "f", "freedom"),
    ("จุฑามาศ", "JUTHAMAS",    "f", "kind"),
    ("กนกวรรณ","KANOKWAN",    "f", "beautiful woman"),
    ("กัญญาลักษณ์","KANYALAK", "f", "beauty of the girl"),
    ("เกาะ",    "KOH",         "f", "island"),
    ("ลลนา",   "LALANA",      "f", "beautiful flower"),
    ("มาลัย",  "MALAI",       "f", "garland"),
    ("นางน้อย","NANGNOI",     "f", "little lady"),
    ("ณฐามน", "NATHAMON",    "f", "bringer of peace"),
    ("ณัฎฐณิชา","NATTANICHA",  "f", "beautiful name"),
    ("นิ่ม",      "NIM",         "f", "delicate"),
    ("ปัณณิกา", "PANNIKA",     "f", "lotus"),
    ("พรหมพร","PHROMPHUN",   "f", "golden flower"),
    ("พุสดี",    "PHUSSADEE",   "f", "prosperous"),
    ("พิมพ์ชนก","PIMCHANOK",   "f", "bright moon"),
    ("ปิยนันท์", "PIYANAN",     "f", "beloved"),
    ("ปิยธิดา", "PIYATHIDA",   "f", "lovely"),
    ("รัตนากร", "RATANAKORN",  "f", "gemstone"),
    ("รัตตนา",  "RATTANA",     "f", "gem"),
    ("ระวี",    "RAVEE",       "f", "sunshine"),
    ("สรัล",    "SARAN",       "f", "joyful"),
    ("สรัญญา",  "SARANYA",     "f", "defender"),
    ("ศศิ",     "SASI",        "f", "moonlight"),
    ("สุกัญญา", "SUKANYA",     "f", "good girl"),
    ("ทักษิณา", "TAKSIN",      "f", "sharp"),
    ("ธันทิรา", "TANTHIRA",    "f", "bright light"),
    ("ธัญญา",   "THANYA",      "f", "prosperous"),
    ("ธนิดา",   "THANIDA",     "f", "beautiful"),
    ("อัมพร",   "UMPORN",      "f", "blessings"),
    ("อุษณี",   "USANEE",      "f", "sun light"),
    ("วิภา",    "WIPHA",       "f", "calm"),
    ("ยาดา",   "YADA",        "f", "content"),
    ("โยธกา",  "YOTHAKA",     "f", "queen"),
    ("ดาริกา",  "DARIKA",      "f", "star"),
    ("ดวงเพ็ญ","DUANPHEN",    "f", "full moon"),
    ("ดุษฎี",    "DUSADI",      "f", "sensational"),
    ("จันทรา",  "CHANTARA",    "f", "moon and water"),
    ("ดอกรัก", "DOKRAK",      "f", "love"),
    ("กุหลาบ",  "KULAP",       "f", "rose"),
    ("พิชิต",    "PHICHIT",     "f", "to win"),
    ("พิศสมัย", "PHITSAMAI",   "f", "adorable"),
    ("พลอย",   "PHLOI",       "f", "precious stones"),
    ("ผึ้ง",     "PHUENG",      "f", "bee"),
    ("ปิติ",     "PITI",        "f", "joy"),
    ("พฤกษา",  "PRIJA",       "f", "intelligent"),
    ("ราชินี",  "RACHINI",     "f", "queen"),
    ("รัตพร",  "RATAPON",     "f", "blessing"),
    ("โรจนา",  "ROCHANA",     "f", "sweet-talker"),
    ("เสนาะ",  "SANOH",       "f", "pleasant sounding"),
    ("สนุก",    "SANOUK",      "f", "festival"),
    ("สันติชัย", "SANTICHAI",   "f", "peaceful"),
    ("ทรัพย์",   "SAP",         "f", "wealth"),
    ("หวาน",  "WAAN",        "f", "sweet"),
    ("แหวน",  "WAEN",        "f", "ring"),
    # WIPA removed — duplicate Thai of WIPHA (kept RTGS form)
    ("ยินดี",   "YINDEE",      "f", "pleasure"),
    ("หญิง",   "YING",        "f", "feminine"),
    ("ยุพา",    "YU-PHA",      "f", "innocent"),
    ("ส้ม",     "SOM",         "f", "orange"),
    ("สมตา",  "SOMTA",       "f", "juicy"),
    ("โสภา",  "SOPA",        "f", "pretty"),
    ("สุชาดา", "SUCHADA",     "f", "good sister"),
    ("แตง",   "TAENG",       "f", "melon"),
    ("อุมา",    "UMA",         "f", "light"),
    ("วนิดา",  "VANIDA",      "f", "girl"),
    ("คะวัง",  "KWANG",       "f", "deer"),
    ("ละไม",   "LAMAI",       "f", "caring"),
    ("ลาวัณย์",  "LAWANA",      "f", "graceful"),
    ("หอม",   "HOM",         "f", "fragrance"),

    # --- Unisex / Gender-neutral ---
    ("อนันต์",   "ANAN",        "u", "delightful"),
    ("กฤษ",    "KRIS",        "u", "crystal"),
    ("พิม",     "PIM",         "u", "to blossom"),
    ("เย็น",    "YEN",         "u", "cool"),
    ("ดาว",    "DAO",         "u", "star"),
    ("เต่า",    "TAO",         "u", "turtle"),
    ("รัศมี",   "RAI",         "u", "light"),
    ("ทาน",   "TARN",        "u", "to cross"),
]


# ============================================================================
# LAST NAMES (th, en, origin, meaning)
# Blend of Thai-origin (legally-unique surnames) and Sino-Thai (recurring
# across many families). For a 2,000-row company we expect ~40% Sino-Thai,
# ~60% Thai-origin, matching Thai urban demographics.
# ============================================================================
LAST_NAMES = [
    # --- Thai-origin (from ling-app.medium.com list) ---
    # ADULYADEJ removed — collision with late King Rama IX's royal name
    ("อนันต์",     "ANANT",        "thai", "eternal"),
    ("อนุมาน",    "ANUMAN",       "thai", "patience"),
    ("อนุรักษ์",   "ANURAK",       "thai", "angel"),
    ("อารมณ์ดี",  "AROMDEE",      "thai", "cheerful"),
    ("อัสนี",      "ASNEE",        "thai", "lightning"),
    # AYUTTHAYA removed — former royal capital, not a typical standalone surname
    ("อัญชลี",   "ANCHALI",      "thai", "greeting"),
    ("อมรินทร์", "AMARIN",       "thai", "undying"),
    ("อภิญญา",  "APINYA",       "thai", "magical power"),
    ("อนงค์",   "ANONGKUN",     "thai", "gorgeous woman"),
    ("อาทิตย์",   "ARTHITKUL",    "thai", "man of the sun"),
    ("อาวุทธ์",  "AWUT",         "thai", "weapon"),
    ("อัมพร",    "AMPHOM",       "thai", "sky"),
    ("อารี",      "AREE",         "thai", "hospitable"),
    ("บัวทอง",   "BUATHONG",     "thai", "gold lotus"),
    ("บุญมี",     "BOONMEE",      "thai", "have merit"),
    ("บุญเรือง",  "BOONRUENG",    "thai", "virtue with glory"),
    ("บุญญา",    "BOONYA",       "thai", "virtue"),
    ("บุญนำ",    "BOONNAM",      "thai", "born to good fortune"),
    ("บุญมา",    "BUNMAK",       "thai", "to have luck"),
    ("บุษราคัม",  "BUSARAKHAM",   "thai", "topaz"),
    ("แช้มช้อย", "CHAEMCHOI",    "thai", "gracefulness"),
    ("ชัยดี",     "CHAIDEE",      "thai", "kind"),
    ("ชัยเจริญ",  "CHAICHAROEN",  "thai", "triumphant"),
    ("ชัยสนธิ์",  "CHAISON",      "thai", "mischievous boy"),
    ("ไชยา",     "CHAIYAWONG",   "thai", "victory"),
    ("ชัยสัย",    "CHAISAI",      "thai", "victory"),
    ("ชาญณรงค์","CHANNARONG",   "thai", "experienced soldier"),
    ("ชากัญญ์",  "CHAKAN",       "thai", "able bodied"),
    ("จักรี",     "CHAKRII",      "thai", "king"),
    ("จินดา",    "CHINDA",       "thai", "precious stone"),
    ("ชาเรือนศักดิ์","CHAROENSUK","thai", "prosper with delight"),
    ("โชคดี",    "CHOKDEE",      "thai", "lucky"),
    ("จงรัก",    "CHONGRAK",     "thai", "loyal"),
    ("ดาวเรือง", "DAORUENG",     "thai", "calendula"),
    ("ดวงกมล",  "DUANGKAMOL",   "thai", "from the heart"),
    ("ใจเขียว",  "JAIKIEOW",     "thai", "green heart"),
    ("การเวก",   "KARAWEK",      "thai", "native bird"),
    ("เกษม",    "KASEMKIT",     "thai", "pure happiness"),
    ("เก่งกาจ",  "KHAENGKAD",    "thai", "brave"),
    ("กิตติบุญ",  "KITTIBUN",     "thai", "famous fortune"),
    ("กิตติชาติ", "KITTICHAT",    "thai", "famous clan"),
    ("กอบสุข",  "KOBSOOK",      "thai", "full happiness"),
    ("ไกรศรี",   "KRAISEE",      "thai", "brave lion"),
    ("ลวรรณ",   "LAWAN",        "thai", "beautiful"),
    ("มาลัย",    "MALAIKUL",     "thai", "garland"),
    ("มีบุญ",    "MEEBOON",      "thai", "have merit"),
    ("มงคล",   "MONGKHON",     "thai", "auspicious"),
    ("ณ เชียงใหม่","NACHIANGMAI","thai","descendants of rulers"),
    ("ณรงค์",   "NARONGKUL",    "thai", "ready for war"),
    ("งาม",     "NGAM",         "thai", "beautiful"),
    ("นิรันดร์",  "NIRAN",        "thai", "never-ending"),
    ("น้อย",    "NOI",          "thai", "little"),
    ("นกน้อย",  "NOKNOI",       "thai", "little bird"),
    ("อรศรี",    "ONSI",         "thai", "glory"),
    ("ไพทูล",   "PAITHOON",     "thai", "cat's eye"),
    ("ปัญญา",  "PANYA",        "thai", "intellect"),
    ("ผาสุก",   "PHASUK",       "thai", "joyfully"),
    ("ประวัติ",  "PRAVAT",       "thai", "historic"),
    ("ปรีดี",    "PREEDEE",      "thai", "joyful"),
    ("รัตนพร",  "RATANAPORN",   "thai", "crystal blessing"),
    # RATTANAKOSIN removed — collision with current Thai royal house
    ("ฤทธิรงค์", "RITTHIRONG",   "thai", "good fighter"),
    ("โรจนะ",  "ROCHANA",      "thai", "good with words"),
    ("รุ่ง",      "RUENG",        "thai", "glory"),
    ("แสงแก้ว",  "SAENGKAEW",   "thai", "crystal light"),
    ("ชินวรา",   "SHINWARA",     "thai", "does good routinely"),
    ("สร้อยคำ",  "SOIKHAM",      "thai", "gold necklace"),
    ("สมศรี",    "SOMSRI",       "thai", "suitable with honor"),
    ("สุวรรณรัตน์","SUWANNARAT", "thai", "gold with jewel"),
    ("สุวรรณ",  "SUWAN",        "thai", "gold"),
    ("ศักดิ์ดา",   "SAKDAKUL",    "thai", "powerful"),
    ("แสงทอง", "SANGTHONG",    "thai", "light of gold"),
    ("ศิริพร",   "SIRIPORN",     "thai", "gloriously blessed"),
    ("ทำบุญ",   "THAMBOON",     "thai", "merit-making"),
    ("ทองดี",   "THONGDI",      "thai", "good gold"),
    ("ตะวัน",   "THAWANKUL",    "thai", "the sun"),
    ("วันชัย",   "WANCHAI",      "thai", "victory day"),
    ("ทองใบ",  "THONGBAI",     "thai", "gold leaf"),
    ("ศรีสุข",    "SRISUK",       "thai", "happy glory"),
    ("ศรีจันทร์", "SRICHAN",      "thai", "moon glory"),
    ("ศรีทอง",  "SRITHONG",     "thai", "golden glory"),
    ("พงศ์ภัค",  "PHONGPHAK",    "thai", "fortunate lineage"),
    ("ภัทราภรณ์","PATTRAPORN",   "thai", "beautiful grace"),
    ("จิตรานนท์","JITRANON",     "thai", "mind of joy"),
    ("เจริญผล",  "CHAROENPHOL",  "thai", "prospering result"),
    ("แก้วใส",  "KAEWSAI",      "thai", "clear crystal"),
    ("แก้วกาญจน์","KAEWKAN",    "thai", "golden crystal"),
    ("อินทรีย์",  "INTHRI",       "thai", "majestic"),
    ("เทพมณี",  "THEPMANEE",    "thai", "divine gem"),
    ("พรหมสุข", "PHROMSUK",    "thai", "divine happiness"),
    ("สมหวัง", "SOMWANG",      "thai", "as wished"),
    ("ขวัญใจ", "KWANJAI",      "thai", "beloved spirit"),
    ("ใจดี",    "JAIDI",        "thai", "good-hearted"),
    ("ใจงาม", "JAINGAM",      "thai", "beautiful heart"),
    ("สุขสวัสดิ์","SUKSAWAT",    "thai", "happy fortune"),
    ("ทองอยู่", "THONGYU",      "thai", "gold remains"),
    ("ทองเพิ่ม","THONGPERM",    "thai", "increasing gold"),
    ("เขียวขจี","KIAOKAJI",     "thai", "lush green"),
    ("ฟ้าใส",   "FAHSAI",       "thai", "clear sky"),
    ("ดาวใส", "DAOSAI",       "thai", "bright star"),
    ("นพรัตน์", "NOPPARAT",     "thai", "nine gems"),
    ("กาญจน์","KAN",          "thai", "gold"),
    ("แก้วประเสริฐ","KAEWPRASERT","thai","precious crystal"),
    ("พลเดช",  "PHOLDECH",     "thai", "strong power"),
    ("ชัยวัฒน์", "CHAIWAT",      "thai", "victory growth"),
    ("เผือก",   "PHUEAK",       "thai", "white (albino)"),
    ("หอมกลิ่น","HOMKLIN",     "thai", "fragrant"),
    ("นิ่มนวล","NIMNUAL",      "thai", "gentle and soft"),
    ("พัฒนสมสิทธิ์","PHATTHANASOMSIT","thai","development and rights"),
    ("เรืองไชย","RUENGCHAI",   "thai", "glorious victory"),
    ("ไทรทอง","SAITHONG",     "thai", "golden banyan"),
    ("เกียรติกำจร","KIATKAMJORN","thai","spreading honor"),
    ("สุขสันต์","SUKSAN",       "thai", "peaceful happiness"),
    ("พรหมสิทธิ์","PHROMSIT",   "thai", "divine rights"),
    ("ทองคำ", "THONGKHAM",    "thai", "gold"),
    ("รัตนวงศ์","RATTANAWONG","thai", "crystal lineage"),

    # --- Sino-Thai origin (recurring across many families) ---
    ("แซ่ตั้ง",   "SAETANG",     "sino", "Chen (Chinese Chen)"),
    ("แซ่ลิ้ม",   "SAELIM",      "sino", "Lin (Chinese Lin)"),
    ("แซ่เล่า",  "SAELAU",      "sino", "Liu"),
    ("แซ่ลี้",    "SAELI",       "sino", "Li"),
    ("แซ่อึ้ง",   "SAEUENG",     "sino", "Huang"),
    ("แซ่โง้ว",  "SAENGO",      "sino", "Wu"),
    ("แซ่เตียว", "SAETIAOW",    "sino", "Zhang"),
    ("แซ่ฮวง",  "SAEHUANG",    "sino", "Huang"),
    ("แซ่หลิว",  "SAELIEW",     "sino", "Liu"),
    ("แซ่หลี",   "SAELEE",      "sino", "Li"),
    ("เจริญ",   "CHAROEN",     "sino", "advance"),
    ("กิตติ",    "KITTIPONG",   "sino", "undertaking"),
    ("กูล",     "KUL",         "sino", "family"),
    ("หลี",     "LE",          "sino", "joy"),
    ("เลิศ",    "LERT",        "sino", "brilliance"),
    ("พาณิชย์", "PANIT",       "sino", "commerce"),
    ("พัฒนา",  "PATANA",      "sino", "develop"),
    ("พิทักษ์",  "PITAK",       "sino", "protect"),
    ("พงศ์",    "PONG",        "sino", "family"),
    ("ศรีสุวรรณ","SRISUWAN",    "sino", "splendor with golden"),
    ("ตันเจริญ", "TANCHAROEN",  "sino", "advance"),
    ("วงศ์",     "WONG",        "sino", "family"),
    ("ตระกูล",  "TRAKUN",      "sino", "family lineage"),
    ("ตั้งธนวัฒน์","TANGTHANAWAT","sino", "established prosperity"),
    ("แซ่โค้ว",  "SAEKHOR",     "sino", "Guo"),
    ("เตชะตนานนท์","TECHATANANON","sino","power of dwelling"),
    ("พรหมจรรย์","PHROMCHAN",  "sino", "divine conduct"),
    ("ลิมปิสวัสดิ์","LIMPISAWAT","sino","Lin-blessed"),
    ("ลี้สกุล",  "LEESAKUL",    "sino", "Lee family"),
    ("ตันสุวรรณ","TANSUWAN",    "sino", "Tan gold"),
    ("เตชะสุวรรณ","TECHASUWAN","sino", "power of gold"),
    ("อึ้งตระกูล","UENGTRAKUN", "sino", "Huang lineage"),
]


# ============================================================================
# NICKNAMES (th, en, category)
# Heavy on modern / weird / Gen-Z / English-loan to make nickname-only lookup
# harder. Categories mirror elitenamecrew's sections but de-duplicated and
# grouped. "Common" ones like Boy/Nong/Fon deliberately trimmed to reduce
# real-person collision risk.
# ============================================================================
NICKNAMES = [
    # --- Classic Thai (short syllables) ---
    ("นัต",    "NUT",      "classic"),
    ("บี",     "BEE",      "classic"),
    ("ปิ๊ง",    "PING",     "classic"),
    ("ไผ่",     "PHAI",     "classic"),
    ("เบียร์",  "BEER",     "classic"),
    ("ติ๊ก",    "TIK",      "classic"),
    ("ตุ๊ก",    "TUK",      "classic"),
    ("เอ",     "AE",       "classic"),
    ("โอ",     "OH",       "classic"),
    ("ยุ้ย",     "YUI",      "classic"),
    ("ตูน",    "TOON",     "classic"),
    ("ต้อม",  "TUM",      "classic"),        # was TOM; renamed to avoid collision with ทอม/Tom (teen)
    ("แก้ว",  "KAEW",     "classic"),
    ("เปิ้ล",   "PLE",      "classic"),
    ("ปุ๊ก",    "PUK",      "classic"),
    # MOO, NOK, PLA, KAI, MHEE moved to animal — they ARE animals
    ("ไก่",   "KAI",      "classic"),       # keep here too as short-syllable name (chicken but used as generic nickname)
    ("ยุ้ง",    "YUNG",     "classic"),
    ("ติน",    "TIN",      "classic"),
    ("เป้",    "PE",       "classic"),
    ("จุ๊บ",    "JUB",      "classic"),
    ("เจี๊ยบ",  "JIAB",     "classic"),

    # --- Thai food / drink ---
    ("ไอซ์",  "ICE",      "food"),
    ("เค้ก",   "CAKE",     "food"),
    ("โกโก้",  "COCO",     "food"),       # cocoa/chocolate
    ("น้ำตาล","NAMTAN",   "food"),
    ("น้ำหวาน","NAMWAN", "food"),
    ("น้ำผึ้ง",  "NAMPHUENG","food"),     # RTGS fix
    ("ส้ม",   "SOM",      "food"),
    ("ส้มโอ", "SOMO",     "food"),
    ("ข้าว",   "KHAORICE", "food"),       # disambiguate from ขาว/white
    ("ขนม", "KHANOM",   "food"),
    ("โดนัท","DONUT",    "food"),
    ("คุกกี้",  "COOKIE",   "food"),
    ("มะม่วง","MANGO",   "food"),
    ("กีวี่",   "KIWI",     "food"),
    ("พีช",   "PEACH",    "food"),
    ("เบอร์รี่","BERRY",    "food"),
    ("วาฟเฟิล","WAFFLE", "food"),
    ("มัฟฟิน","MUFFIN",   "food"),
    ("ลาเต้",  "LATTE",    "food"),
    ("มอคค่า","MOCHA",   "food"),
    ("พุดดิ้ง","PUDDING",  "food"),
    ("โยเกิร์ต","YOGURT",  "food"),
    ("มิลค์",   "MILK",     "food"),
    ("เชอร์รี่","CHERRY",   "food"),
    ("ถั่ว",    "BEAN",     "food"),
    ("ขิง",    "KHING",    "food"),
    ("เจลลี่",  "JELLY",    "food"),
    ("โอริโอ้","OREO",     "food"),
    ("ซูชิ",    "SUSHI",    "food"),
    ("มาร์ช",  "MARSH",    "food"),
    ("ทาฟฟี่","TAFFY",     "food"),
    # moved to nature/body-part: MOOK(pearl), MALIE(jasmine), KAEM(cheek); removed KAPUK (not in source)

    # --- English loanwords (modern/trendy) ---
    ("มิ้น",    "MINT",     "modern"),
    ("เบนซ์",  "BENZ",     "modern"),
    ("บอส",   "BOSS",     "modern"),
    ("แบงค์",  "BANK",     "modern"),
    ("บีม",    "BEAM",     "modern"),
    ("ฟิล์ม",   "FILM",     "modern"),
    ("เฟิร์ส",  "FIRST",    "modern"),
    ("เกม",   "GAME",     "modern"),
    ("กอล์ฟ",  "GOLF",     "modern"),
    ("บอล",   "BALL",     "modern"),
    ("อาร์ต", "ART",      "modern"),
    ("นอร์ท", "NORTH",    "modern"),
    ("แชมป์","CHAMP",    "modern"),
    ("อิงค์",  "INK",      "modern"),
    ("โน้ต",  "NOTE",     "modern"),
    ("สกาย",  "SKY",      "modern"),
    ("เวฟ",   "WAVE",     "modern"),
    ("คลาวด์","CLOUD",   "modern"),
    ("เซน",  "ZEN",      "modern"),
    ("นีโอ",   "NEO",      "modern"),
    ("เรย์",   "RAY",      "modern"),
    ("ลีโอ",   "LEO",      "modern"),
    ("ไทเทิล","TITLE",    "modern"),
    ("เอซ",   "ACE",      "modern"),
    ("วิน",    "WIN",      "modern"),
    ("อาร์ม", "ARM",      "modern"),
    ("ปาล์ม", "PALM",     "modern"),
    ("โอ๊ต",   "OAT",      "modern"),
    ("ฟลุ๊ค",   "FLUKE",    "modern"),
    ("ปีเตอร์", "PETER",    "modern"),
    ("เชน",   "CHANE",    "modern"),
    ("เจน",   "JANE",     "modern"),
    ("เจย์",   "JAY",      "modern"),
    ("โจเอล", "JOEL",     "modern"),
    ("มาร์ค", "MARK",     "modern"),
    ("คิง",   "KING",     "modern"),
    ("ควีน", "QUEEN",    "modern"),
    # FLUCK removed — near-duplicate typo of FLUKE

    # --- Weird / Gen-Z / objects ---
    ("กาแฟ",  "KAFAE",    "weird"),
    ("คอฟฟี่เมต","COFFEEMATE","weird"),     # fix truncation bug
    ("โฟล์คซอง","FOLKSONG","weird"),
    ("คอตตอน","COTTON",  "weird"),
    ("ซานตา","SANTA",   "weird"),
    ("ปันปัน","PANPAN",  "weird"),
    ("ตังโอ๋", "TANGOH",   "weird"),
    ("โฟกัส",  "FOCUS",    "weird"),
    ("เจแปน","JAPAN",    "weird"),
    ("โอเค",  "OKAY",     "weird"),
    ("ไอโฟน","IPHONE",   "weird"),
    ("ปอร์เช่","PORSCHE", "weird"),
    ("เนสท์เล่","NESTLE", "weird"),
    ("ไอบีเอ็ม","IBM",     "weird"),
    ("ไทเกอร์","TIGER",   "weird"),
    ("ชาร์ค", "SHARK",    "weird"),
    ("จูปิเตอร์","JUPITER","weird"),

    # --- Nature / color / gems ---
    ("ฟ้า",    "FAH",      "nature"),
    ("ฝน",   "FON",      "nature"),
    ("ลม",   "LOM",      "nature"),
    ("ดาว",   "DAO",      "nature"),
    ("น้ำ",    "NAM",      "nature"),
    ("ทราย", "SAI",      "nature"),
    ("เมฆ",  "MEK",      "nature"),
    ("รุ้ง",    "RUNG",     "nature"),
    ("ใบเฟิร์น","BAIFERN", "nature"),
    ("บัว",    "BUA",      "nature"),
    ("ดอกไม้","DOKMAI",   "nature"),
    ("ใบเตย","BAITOEY",   "nature"),
    ("แดง",  "DAENG",    "nature"),
    ("ขาว",  "KHAOWHITE","nature"),      # disambiguate from ข้าว/rice
    ("ดำ",    "DUM",      "nature"),
    ("เขียว", "KIAW",     "nature"),
    ("ชมพู", "CHOMPOO",  "nature"),
    ("ทอง",  "THONG",    "nature"),
    ("เพชร", "PET",      "nature"),
    ("ตะวัน","TAWAN",    "nature"),
    ("มุก",   "MOOK",     "nature"),     # moved from food — pearl
    ("มะลิ",  "MALI",     "nature"),     # moved from food — jasmine; fixed typo
    ("พลอย", "PLOY",     "nature"),     # moved from soft — gem
    ("อรุณ",  "ARUN",     "nature"),     # moved from aesthetic — dawn
    # removed ใส (SAI2) — reading as "clear" conflicts with ทราย/sand

    # --- Animals (traditional Thai animal nicknames) ---
    ("กวาง", "KWANG",    "animal"),
    ("แมว",  "MAEW",     "animal"),
    ("กระต่าย","KRATAI",  "animal"),
    ("ช้าง",   "CHANG",    "animal"),
    ("เสือ",   "SUEA",     "animal"),
    ("หงส์",  "HONG",     "animal"),
    ("ฮูก",    "HOOK",     "animal"),     # fixed: นกฮูก→ฮูก; was HAO, now correct
    ("เต่า",   "TAO",      "animal"),
    ("กบ",   "KOB",      "animal"),
    ("ผึ้ง",    "PHEUNG",   "animal"),
    ("ปู",     "PU",       "animal"),
    ("กุ้ง",    "KUNG",     "animal"),
    ("ลิง",   "LING",     "animal"),
    ("หมู",   "MOO",      "animal"),     # canonical location for pig
    ("ปลา",  "PLA",      "animal"),     # canonical location for fish
    ("นก",   "NOK",      "animal"),     # canonical location for bird
    ("หมี",   "MHEE",     "animal"),     # canonical location for bear
    # removed PETE, PUI — not animals; moved elsewhere

    # --- Soft / short ---
    ("อ้อม",   "OM",       "soft"),
    ("ออม",  "AOM",      "soft"),        # was OM2; ออม is phonetically /ɔːm/ → AOM
    ("อุ่น",    "OON",      "soft"),
    ("อุ้ย",    "UI",       "soft"),
    ("มิว",   "MEW",      "soft"),
    ("นิว",   "NEW",      "soft"),
    ("บิ๋ม",    "BIM",      "soft"),
    ("ปริม",   "PRIM",     "soft"),
    ("พีม",   "PEEM",     "soft"),
    ("พันช์", "PUNCH",    "soft"),       # kept one spelling; removed near-dupe พั้นช์ PUNCH2
    ("ปุณณ์", "PUN",      "soft"),
    ("เปรียว","PREAW",   "soft"),
    ("แพร",  "PRAEW",    "soft"),
    ("ปุ้ย",    "PUI",      "soft"),       # moved from animal
    ("พีท",   "PETE",     "soft"),       # moved from animal
    # PLOY moved to nature (gem)

    # --- Aesthetic / feminine ---
    ("ลลิน",   "LALIN",    "aesthetic"),
    ("มิรา",   "MIRA",     "aesthetic"),
    ("อาญา", "ANYA",     "aesthetic"),
    ("ดาริน", "DARIN",    "aesthetic"),
    ("ณิชา",  "NISHA",    "aesthetic"),
    ("แอรีน", "AIREEN",   "aesthetic"),
    ("ริต้า",  "RITA",     "aesthetic"),
    ("เมญ่า","MAYA",     "aesthetic"),
    ("พิม",   "PIM",      "aesthetic"),
    ("พิมมาดา","PIMMADA","aesthetic"),
    ("ณิช",   "NISH",     "aesthetic"),
    ("ลิน่า", "LINA",     "aesthetic"),
    ("ริโอ",  "RIO",      "aesthetic"),

    # --- Masculine / teen ---
    ("บูม",   "BOOM",     "teen"),
    ("ปอนด์","POND",     "teen"),
    ("โฟล์ค","FOLK",     "teen"),
    ("ป๊อป",  "POP",      "teen"),
    ("ป๊อก",  "POK",      "teen"),
    ("ปลื้ม", "PLERM",    "teen"),
    ("ไท",    "TAI",      "teen"),
    ("ซัน",   "SUN",      "teen"),
    ("เคน",  "KEN",      "teen"),
    ("ต้น",   "TON",      "teen"),
    ("แท่น", "TAN",      "teen"),
    ("แทน", "THAEN",    "teen"),        # was TEN; แทน is /tʰɛːn/ → THAEN
    ("ทอม", "TOM",      "teen"),        # was TOMMY; ทอม = "Tom"
    ("คิม",   "KIM",      "teen"),
    ("ริต",   "RIT",      "teen"),
    ("ณัฐ",   "NAT",      "teen"),
    # removed POKE — ปอก doesn't match that English word

    # --- Doubled form (baby-talk style) ---
    ("บัมบัม","BAMBAM",   "doubled"),
    ("ฟ่อนฟ่อน","FONFON", "doubled"),
    ("ลาลา",  "LALA",     "doubled"),
    ("มิมิ",   "MIMI",     "doubled"),
    ("กีกี",   "GIGI",     "doubled"),
    ("ดีดี",    "DEEDEE",   "doubled"),
    ("ริริ",   "RIRI",     "doubled"),
    ("โอ้โอ้", "OHOH",     "doubled"),
    ("เป้เป้", "PEPE",     "doubled"),
    ("เน่อเน่อ","NERNER",  "doubled"),
    # removed ปันปัน (duplicate with weird category) and โกโก้ (duplicate with food)
    # removed เค้กเค้ก CAKECAKE (speculative, not in source)
]


# ============================================================================
# NICKNAME VARIANTS — how peers actually address the person
# Base nickname → list of variant forms used in natural speech.
# This pool is used ONLY by the question generator. CSV stores base form only.
# ============================================================================
NICKNAME_VARIANTS = {
    # Suffix-tee (most common diminutive pattern in modern Thai)
    "นัต":   ["นัตตี้", "นัตนัต", "น้องนัต", "พี่นัต", "นัตจัง"],
    "มิ้น":   ["มิ้นตี้", "มิ้นมิ้น", "น้องมิ้น", "พี่มิ้น"],
    "เก่ง":  ["เก่งกี้", "น้องเก่ง"],
    "มุก":   ["มุกกี้", "มุกนี่", "มุกมุก", "น้องมุก"],
    "บี":    ["บีบี", "พี่บี", "น้องบี"],
    "ปิ๊ง":   ["ปิ๊งปิ๊ง", "น้องปิ๊ง"],
    "ออม":  ["ออมออม", "ออมมี่", "น้องออม"],
    "อ้อม":  ["อ้อมอ้อม", "พี่อ้อม"],
    "ปัน":   ["ปันปัน", "ปันนี่"],
    "นก":   ["น้องนก", "นกนก", "นกน้อย"],
    "ไอซ์":  ["ไอซ์ไอซ์", "น้องไอซ์", "พี่ไอซ์"],
    "เค้ก":  ["เค้กเค้ก", "น้องเค้ก"],
    "มุกมุก":["พี่มุกมุก"],  # already-doubled base with honorific
    "แบงค์": ["แบงค์แบงค์", "น้องแบงค์"],
    "เบนซ์": ["เบนซ์ซี่", "น้องเบนซ์", "พี่เบนซ์"],
    "บอส":  ["น้องบอส", "พี่บอส"],
    "บีม":   ["บีมบีม", "น้องบีม"],
    "ฟิล์ม":  ["ฟิล์มมี่", "น้องฟิล์ม"],
    "พลอย":["พลอยพลอย", "น้องพลอย"],
    "ปุ๊ก":   ["ปุ๊กปุ๊ก", "ปุ๊กกี้"],
    "ตูน":   ["ตูนตูน", "น้องตูน", "พี่ตูน"],
    "เจี๊ยบ": ["เจี๊ยบเจี๊ยบ", "น้องเจี๊ยบ"],
    "ต้อม": ["ต้อมต้อม", "พี่ต้อม"],
    "แก้ม":  ["แก้มแก้ม", "น้องแก้ม"],
    "ฟ้า":   ["ฟ้าฟ้า", "น้องฟ้า", "พี่ฟ้า"],
    "ฝน":   ["ฟ่อนฟ่อน", "น้องฝน"],
    "แพร":  ["แพรแพร", "น้องแพร"],
    "ดาว":  ["น้องดาว", "ดาวดาว"],
    "พีช":   ["พีชพีช", "น้องพีช"],
    "นิว":   ["นิวนิว", "น้องนิว"],
    "มิว":   ["มิวมิว", "น้องมิว"],
    "เอ":    ["เอเอ", "น้องเอ"],
    "โอ":    ["โอโอ", "น้องโอ"],
    "เปิ้ล":  ["เปิ้ลเปิ้ล", "น้องเปิ้ล"],
    "ปาล์ม":["ปาล์มปาล์ม", "น้องปาล์ม"],
    "เบียร์":["เบียร์เบียร์", "น้องเบียร์"],
    "ไผ่":   ["ไผ่ไผ่", "น้องไผ่"],
    "ติ๊ก":   ["ติ๊กตี้", "ติ๊กติ๊ก"],
    "ตุ๊ก":   ["ตุ๊กตี้", "น้องตุ๊ก"],
    "จุ๊บ":   ["จุ๊บจุ๊บ", "น้องจุ๊บ"],
    "ปุ้ย":   ["ปุ้ยปุ้ย", "น้องปุ้ย"],
    "เจน":  ["เจนเจน", "น้องเจน"],
    "เจย์":  ["เจย์เจย์", "พี่เจย์"],
    "บูม":   ["บูมบูม", "น้องบูม"],
    "นอร์ท":["น้องนอร์ท"],
    "มาร์ค":["มาร์คมาร์ค", "พี่มาร์ค"],
    "คิง":   ["คิงคิง", "พี่คิง"],
    "ซัน":   ["ซันซัน", "น้องซัน"],
    "ไท":    ["ไทไท", "น้องไท"],
    "ปริม":  ["ปริมปริม", "น้องปริม"],
    "พีม":   ["พีมพีม", "พี่พีม"],
    "ต้น":   ["ต้นต้น", "น้องต้น"],
}


def main() -> None:
    # ---- first names ----
    first = [{"th": t, "en": e, "gender": g, "meaning": m} for (t, e, g, m) in FIRST_NAMES]
    first_sorted = sorted(first, key=lambda x: x["en"])
    (OUT / "first_names_th.json").write_text(
        json.dumps({"count": len(first_sorted), "items": first_sorted},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ---- last names ----
    last = [{"th": t, "en": e, "origin": o, "meaning": m} for (t, e, o, m) in LAST_NAMES]
    last_sorted = sorted(last, key=lambda x: x["en"])
    (OUT / "last_names_th.json").write_text(
        json.dumps({"count": len(last_sorted), "items": last_sorted},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ---- nicknames ----
    nicks = [{"th": t, "en": e, "category": c} for (t, e, c) in NICKNAMES]
    nicks_sorted = sorted(nicks, key=lambda x: x["en"])
    (OUT / "nicknames_th.json").write_text(
        json.dumps({"count": len(nicks_sorted), "items": nicks_sorted},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ---- variants ----
    (OUT / "nickname_variants.json").write_text(
        json.dumps({
            "note": "base → [variants]. Used ONLY by the question generator. CSV stores base form only.",
            "count": len(NICKNAME_VARIANTS),
            "variants": NICKNAME_VARIANTS,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ---- summary ----
    male = sum(1 for i in first if i["gender"] == "m")
    female = sum(1 for i in first if i["gender"] == "f")
    unisex = sum(1 for i in first if i["gender"] == "u")
    thai_origin = sum(1 for i in last if i["origin"] == "thai")
    sino = sum(1 for i in last if i["origin"] == "sino")

    print("=== Name pools built ===\n")
    print(f"first_names_th.json     {len(first):>4} entries  ({male} male · {female} female · {unisex} unisex)")
    print(f"last_names_th.json      {len(last):>4} entries  ({thai_origin} Thai-origin · {sino} Sino-Thai)")
    print(f"nicknames_th.json       {len(nicks):>4} entries  across {len(set(n['category'] for n in nicks))} categories")
    print(f"nickname_variants.json  {len(NICKNAME_VARIANTS):>4} base forms with variants\n")

    print("Category breakdown (nicknames):")
    from collections import Counter
    cat = Counter(n["category"] for n in nicks)
    for c, n in sorted(cat.items(), key=lambda x: -x[1]):
        print(f"  {c:<12} {n}")


if __name__ == "__main__":
    main()
