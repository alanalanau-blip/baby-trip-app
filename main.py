import os
import traceback
os.environ['NICEGUI_STORAGE_SECRET'] = 'my_super_secret_key_123'

from nicegui import ui, app

# ==========================================
# 1. 終極行程表資料庫 (加入交通與 3歲 BB Caution)
# ==========================================
ITINERARY = [
    {
        "day": 1, "title": "抵達基隆｜適應與安頓", "hotel": "基隆",
        "options": {
            "sunny": [
                {
                    "time": "14:00–16:00｜抵達台灣 → 前往基隆酒店",
                    "transport": [
                        "首選：包車 / 的士 (約 60–80 分鐘) - 有行李、有 BB 車、想點對點最舒服",
                        "高性價比：機捷 + 國光客運 1813 (約 90–120 分鐘) - 行李不多、想慳錢",
                        "不建議：全程轉乘大眾交通 - 轉車多，對 3歲 BB 較辛苦"
                    ],
                    "caution": [
                        "包車需提早要求 3歲兒童安全座椅。",
                        "客運 / 車內冷氣可能較凍，要準備薄外套。",
                        "抵達日不要安排景點，讓小朋友先適應環境。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "標準安頓", "desc": "抵達台灣後，直接前往基隆酒店 check-in，入房休息、換衫、飲水"},
                        {"type": "🤩 方案 B", "title": "未有房備案", "desc": "如果未能 check-in，先寄存行李，再去東岸廣場涼冷氣"},
                        {"type": "😴 方案 C", "title": "車上睡覺", "desc": "上車後安排安靜環境，讓 BB 車程中補眠", "is_nap": True},
                        {"type": "🛍️ 方案 D", "title": "機場補給", "desc": "出發前在機場買水、麵包、水果、牛奶、小食"},
                        {"type": "🛏️ 方案 E", "title": "超攰版本", "desc": "不安排任何活動，直去酒店，入房後休息到晚餐", "is_nap": True}
                    ]
                },
                {
                    "time": "16:30–17:30｜早晚餐",
                    "transport": ["酒店近市中心：步行約 5–15 分鐘", "酒店較遠：的士約 5–10 分鐘"],
                    "caution": [
                        "夜市只建議早場短食，不要夜晚黑迫人潮。",
                        "3歲小朋友食夜市食物要剪細，湯類要放涼。",
                        "避免太辣、太油、太大粒丸類食物。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "廟口早場", "desc": "基隆廟口夜市早場，食湯麵、魚丸湯、滷肉飯"},
                        {"type": "🤩 方案 B", "title": "冷氣餐廳", "desc": "東岸廣場餐廳，有冷氣、有廁所、有座位"},
                        {"type": "😴 方案 C", "title": "酒店附近食", "desc": "酒店附近簡餐，減少移動"},
                        {"type": "🛍️ 方案 D", "title": "外賣返酒店", "desc": "買飯 / 麵 / 水果返酒店食"},
                        {"type": "🛏️ 方案 E", "title": "便利店簡餐", "desc": "便利店買飯糰、麵包、牛奶、水果，最簡單"}
                    ]
                },
                {
                    "time": "17:45–18:30｜基隆港邊輕鬆活動",
                    "transport": ["廟口 → 海洋廣場：步行約 8–12 分鐘", "東岸廣場 / 酒店附近：步行或的士"],
                    "caution": [
                        "不要排太滿，第一日重點係早睡。",
                        "港邊風可能大，要帶薄外套。",
                        "如果 BB 已經開始扭計，立即返酒店。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "海洋廣場", "desc": "睇船、散步、讓 BB 跑一陣"},
                        {"type": "🤩 方案 B", "title": "東岸廣場", "desc": "室內行一圈，買飲品，避雨 / 避熱"},
                        {"type": "🛍️ 方案 C", "title": "買水果", "desc": "去附近買水果、牛奶、小食"},
                        {"type": "😴 方案 D", "title": "附近散步", "desc": "不走遠，只在酒店附近行 15–20 分鐘"},
                        {"type": "🛏️ 方案 E", "title": "直接返酒店", "desc": "如果小朋友攰，取消活動，返酒店沖涼睡覺", "is_nap": True}
                    ]
                }
            ],
            "rainy": [
                {"time": "14:00–16:00｜抵達台灣 → 前往基隆酒店", "activities": [{"type": "🌧️ 雨天版", "title": "直奔酒店避雨", "desc": "抵達後不加任何景點，直接去酒店避雨", "is_nap": True}]},
                {"time": "16:30–17:30｜早晚餐", "activities": [{"type": "🌧️ 雨天版", "title": "冷氣餐廳", "desc": "東岸廣場餐廳，有冷氣、有廁所、有座位"}]},
                {"time": "17:45–18:30｜室內輕鬆活動", "activities": [{"type": "🌧️ 雨天版", "title": "東岸廣場", "desc": "室內行一圈，買飲品，避雨避熱"}]}
            ]
        }
    },
    {
        "day": 2, "title": "室內冷氣親子日｜海科館 + i OCEAN", "hotel": "基隆",
        "options": {
            "sunny": [
                {
                    "time": "08:45–11:30｜海科館",
                    "transport": ["基隆市中心 → 海科館：的士約 20–25 分鐘"],
                    "caution": [
                        "館內冷氣較大，帶薄外套。",
                        "出發前查官方開放時間，博物館常見 星期一休館。",
                        "3歲小朋友注意力有限，建議每 45–60 分鐘休息一次。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "兒童廳主攻", "desc": "海科館兒童廳，最適合3歲放電"},
                        {"type": "🤩 方案 B", "title": "主題館", "desc": "海洋、船舶、互動展區，適合慢慢看"},
                        {"type": "🌧️ 方案 C", "title": "室內避雨", "desc": "全程留海科館室內，避雨避熱"},
                        {"type": "😴 方案 D", "title": "慢玩版", "desc": "只玩小朋友有興趣嘅展區，不追求行晒"},
                        {"type": "🛍️ 方案 E", "title": "半日版", "desc": "玩 60–90 分鐘，午餐後直接返酒店"}
                    ]
                },
                {
                    "time": "11:30–12:30｜午餐休息",
                    "caution": [
                        "午餐要選有座位、有冷氣、有廁所地方。",
                        "不建議排隊名店。",
                        "BB 午餐後容易眼瞓，預留彈性。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "館內餐飲", "desc": "最方便，食完可直接繼續行程"},
                        {"type": "🤩 方案 B", "title": "八斗子簡餐", "desc": "附近簡餐 / 小餐廳"},
                        {"type": "😴 方案 C", "title": "輕食休息", "desc": "只食麵包、水果、飲品，讓 BB 放慢節奏"},
                        {"type": "🛏️ 方案 D", "title": "早返酒店", "desc": "如果 BB 已攰，午餐後直接返酒店", "is_nap": True},
                        {"type": "🛍️ 方案 E", "title": "外帶簡餐", "desc": "外帶食物，方便之後上車 / 回酒店"}
                    ]
                },
                {
                    "time": "12:45–14:00｜i OCEAN / 潮境",
                    "transport": ["海科館 → i OCEAN：的士約 5 分鐘", "海科館 → 潮境公園：短車程 / 視位置短步行"],
                    "caution": [
                        "由海科館去 i OCEAN 雖近，但有3歲小朋友建議搭車。",
                        "潮境公園風大、日曬，要留意帽、防曬、水。",
                        "如果中午開始扭計，不要硬去第二個景點。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "i OCEAN", "desc": "潮境智能海洋館，睇魚、互動展"},
                        {"type": "🤩 方案 B", "title": "潮境公園", "desc": "天氣好可去大草地跑 20–30 分鐘"},
                        {"type": "😴 方案 C", "title": "短玩版", "desc": "i OCEAN 只玩 45 分鐘"},
                        {"type": "🛏️ 方案 D", "title": "取消景點", "desc": "如果 BB 攰，直接返酒店", "is_nap": True},
                        {"type": "📷 方案 E", "title": "拍照版", "desc": "潮境附近簡單影相，唔長留"}
                    ]
                },
                {
                    "time": "14:30–16:30｜酒店午睡",
                    "transport": ["i OCEAN / 海科館 → 基隆酒店：的士約 20–25 分鐘"],
                    "caution": [
                        "14:30–16:30 盡量保留為午睡。",
                        "3歲小朋友如果無午睡，晚上容易崩潰。",
                        "回酒店先洗手、換衫、補水。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "正式午睡", "desc": "回酒店睡 1.5–2 小時", "is_nap": True},
                        {"type": "😴 方案 B", "title": "安靜休息", "desc": "不一定睡，但房內玩貼紙書 / 積木"},
                        {"type": "🤩 方案 C", "title": "車上午睡", "desc": "如已在車上睡著，到酒店後延續休息", "is_nap": True},
                        {"type": "🛍️ 方案 D", "title": "輪流休息", "desc": "一位陪 BB 睡，一位買補給"},
                        {"type": "🛏️ 方案 E", "title": "不外出", "desc": "如果上午玩太多，下午取消所有活動", "is_nap": True}
                    ]
                },
                {
                    "time": "16:30–18:30｜短活動 + 晚餐",
                    "transport": ["市中心範圍：步行或的士 5–10 分鐘"],
                    "caution": [
                        "晚餐後不要再加景點。",
                        "夜市最多 45–60 分鐘。",
                        "小朋友開始揉眼、扭抱，就即刻返酒店。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "東岸廣場", "desc": "室內行一圈 + 冷氣晚餐"},
                        {"type": "🤩 方案 B", "title": "海洋廣場", "desc": "睇船、散步，再去晚餐"},
                        {"type": "🛍️ 方案 C", "title": "廟口早場", "desc": "如精神好，可去廟口早場短食"},
                        {"type": "😴 方案 D", "title": "酒店附近", "desc": "酒店附近簡單晚餐"},
                        {"type": "🛏️ 方案 E", "title": "外賣返酒店", "desc": "太攰就外賣 / 便利店返酒店"}
                    ]
                }
            ],
            "rainy": [
                {"time": "08:45–11:30｜海科館", "activities": [{"type": "🌧️ 雨天版", "title": "全程室內", "desc": "全程留海科館室內，避雨避熱"}]},
                {"time": "11:30–12:30｜午餐", "activities": [{"type": "🌧️ 雨天版", "title": "館內餐飲", "desc": "最方便，食完可直接繼續行程"}]},
                {"time": "12:45–14:00｜i OCEAN", "activities": [{"type": "🌧️ 雨天版", "title": "i OCEAN", "desc": "潮境智能海洋館，睇魚、互動展"}]},
                {"time": "14:30–16:30｜回房休息", "activities": [{"type": "🌧️ 雨天版", "title": "正式午睡", "desc": "回酒店睡避雨", "is_nap": True}]},
                {"time": "16:30–18:30｜室內晚餐", "activities": [{"type": "🌧️ 雨天版", "title": "東岸廣場", "desc": "室內行一圈 + 冷氣晚餐"}]}
            ]
        }
    },
    {
        "day": 3, "title": "玩水放電與彩色屋", "hotel": "基隆",
        "options": {
            "sunny": [
                {
                    "time": "08:30–10:30｜和平島玩水",
                    "transport": ["基隆酒店 → 和平島：的士約 15–20 分鐘"],
                    "caution": [
                        "親親水池受天氣及海況影響，出發前一晚查開放情況。",
                        "出門前先塗防曬，帶帽、防滑水鞋、毛巾、後備衫。",
                        "玩水時每 30–45 分鐘補水。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "親親水池", "desc": "和平島親親水池玩水，約 60–90 分鐘"},
                        {"type": "😴 方案 B", "title": "短玩版", "desc": "只玩 45–60 分鐘，避免過攰"},
                        {"type": "🤩 方案 C", "title": "公園短行", "desc": "玩水後只在和平島公園短行"},
                        {"type": "🌧️ 方案 D", "title": "雨天備案", "desc": "改去海科館 / i OCEAN / 東岸廣場"},
                        {"type": "🛍️ 方案 E", "title": "不玩水", "desc": "改去正濱彩色屋 + Cafe"}
                    ]
                },
                {
                    "time": "10:30–12:15｜沖身 + 午餐",
                    "caution": [
                        "玩水後要盡快換乾衫，避免著涼。",
                        "小朋友玩水後可能突然眼瞓，午餐不要排隊。",
                        "濕衫要用膠袋分開裝好。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "遊客中心休息", "desc": "沖身、換衫、補水、小食"},
                        {"type": "🤩 方案 B", "title": "和平島簡餐", "desc": "在和平島附近簡餐，減少移動"},
                        {"type": "🛍️ 方案 C", "title": "正濱午餐", "desc": "去正濱附近 Cafe / 簡餐"},
                        {"type": "🛏️ 方案 D", "title": "市區午餐", "desc": "直接返市區食飯"},
                        {"type": "😴 方案 E", "title": "外帶午餐", "desc": "買簡單食物返酒店"}
                    ]
                },
                {
                    "time": "12:15–15:30｜酒店長午睡",
                    "transport": ["和平島 / 正濱 → 基隆酒店：的士約 15–20 分鐘"],
                    "caution": [
                        "玩水後體力消耗大，必須安排長休息。",
                        "不建議午睡後立即安排太遠景點。",
                        "若 BB 午睡超過時間，可直接取消黃昏活動。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "長午睡", "desc": "回酒店睡 2 小時左右", "is_nap": True},
                        {"type": "🤩 方案 B", "title": "洗澡休息", "desc": "回酒店沖涼，再午睡", "is_nap": True},
                        {"type": "😴 方案 C", "title": "安靜玩", "desc": "如果不睡，房內安靜玩"},
                        {"type": "🛏️ 方案 D", "title": "完全休息", "desc": "下午取消正濱，只休息", "is_nap": True},
                        {"type": "🛍️ 方案 E", "title": "輪流買補給", "desc": "BB 留酒店休息，大人輪流買水/水果"}
                    ]
                },
                {
                    "time": "16:30–18:30｜正濱彩色屋 / 晚餐",
                    "transport": ["基隆酒店 → 正濱：的士約 10–15 分鐘", "正濱 → 基隆市區：的士約 10–15 分鐘"],
                    "caution": [
                        "正濱主要係影相，不宜安排太長。",
                        "如風大、落雨或 BB 未醒透，直接取消。",
                        "晚餐可於正濱附近 Cafe，或回基隆市區食更穩陣。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "正濱彩色屋", "desc": "影相、食雪糕、短散步"},
                        {"type": "🤩 方案 B", "title": "正濱 Cafe", "desc": "找 Cafe 坐低，適合大人休息"},
                        {"type": "📷 方案 C", "title": "阿根納外圍", "desc": "精神好可順路外圍短看，不深入停留太久"},
                        {"type": "🛏️ 方案 D", "title": "取消活動", "desc": "超攰就留酒店，不出門", "is_nap": True},
                        {"type": "🛍️ 方案 E", "title": "市區晚餐", "desc": "只去基隆市中心 / 東岸廣場食晚餐"}
                    ]
                }
            ],
            "rainy": [
                {"time": "08:30–13:00｜雨天替代", "activities": [{"type": "🌧️ 雨天版", "title": "海洋世界/海科館", "desc": "改搭車去室內看海豚表演或回海科館"}]},
                {"time": "13:00–15:30｜午睡", "activities": [{"type": "🌧️ 雨天版", "title": "回房長休息", "desc": "酒店長午睡", "is_nap": True}]},
                {"time": "16:30–18:30｜晚餐", "activities": [{"type": "🌧️ 雨天版", "title": "市區晚餐", "desc": "直接去東岸廣場室內晚餐"}]}
            ]
        }
    },
    {
        "day": 4, "title": "搬酒店與恐龍迷之日｜基隆 → 台北", "hotel": "萬華 / 西門",
        "options": {
            "sunny": [
                {
                    "time": "09:30–11:00｜基隆 → 台北萬華 / 西門酒店",
                    "transport": [
                        "首選：包車 / 的士 (約 45–60 分鐘) - 有行李、BB 車",
                        "高性價比：台鐵基隆 → 萬華 (約 50–60 分鐘) - 想慳錢，行李不太多",
                        "轉乘版：視班次而定 - 需台北車站轉乘，較辛苦"
                    ],
                    "caution": [
                        "搭台鐵要避開 07:30–09:00 上班繁忙時間。",
                        "有 BB 車 + 行李時，包車最穩陣。",
                        "搬酒店日不要排太多活動。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "標準搬酒店", "desc": "早餐後包車到台北酒店，寄存行李"},
                        {"type": "🛍️ 方案 B", "title": "台鐵慳錢版", "desc": "基隆站搭台鐵到萬華站"},
                        {"type": "😴 方案 C", "title": "慢出發", "desc": "稍遲出發，避免趕時間"},
                        {"type": "🤩 方案 D", "title": "車上午睡", "desc": "安排車程俾 BB 補眠", "is_nap": True},
                        {"type": "🛏️ 方案 E", "title": "完全休息日", "desc": "到台北後不安排景點，只休息", "is_nap": True}
                    ]
                },
                {
                    "time": "11:00–12:45｜寄存行李 + 午餐",
                    "caution": [
                        "午餐後要安排去廁所、換片、補水。",
                        "不要排長隊餐廳。",
                        "酒店未有房時，先找冷氣地方等。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "龍山寺附近", "desc": "麵店 / 飯店 / 湯類餐廳"},
                        {"type": "🤩 方案 B", "title": "西門町午餐", "desc": "選有冷氣、有座位餐廳"},
                        {"type": "🛍️ 方案 C", "title": "酒店附近", "desc": "最穩陣，減少移動"},
                        {"type": "😴 方案 D", "title": "Cafe 休息", "desc": "如未能 check-in，先在 Cafe 坐低"},
                        {"type": "🛏️ 方案 E", "title": "便利店輕食", "desc": "BB 太攰時，簡單食完等入房"}
                    ]
                },
                {
                    "time": "13:00–14:30｜恐龍館 / 台博館",
                    "transport": [
                        "萬華 / 西門 → 恐龍館：的士約 10–15 分鐘",
                        "恐龍館 → 228公園：步行可達"
                    ],
                    "caution": [
                        "博物館常見星期一休館，出發前查開放時間。",
                        "恐龍館 60–90 分鐘已足夠。",
                        "3歲 BB 若怕暗、怕大型標本，可縮短停留。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "土地銀行展示館", "desc": "睇恐龍骨架，大型標本，適合恐龍迷"},
                        {"type": "🌧️ 方案 B", "title": "國立台灣博物館", "desc": "雨天室內替代，展品較安靜"},
                        {"type": "😴 方案 C", "title": "短玩版", "desc": "只玩 60 分鐘，然後返酒店"},
                        {"type": "🤩 方案 D", "title": "228公園", "desc": "如精神好，之後去公園跑 20 分鐘"},
                        {"type": "🛏️ 方案 E", "title": "取消景點", "desc": "若搬酒店太攰，直接返酒店休息", "is_nap": True}
                    ]
                },
                {
                    "time": "15:30–17:00｜酒店 Check-in + 午睡",
                    "transport": ["恐龍館 → 酒店：的士約 10–20 分鐘"],
                    "caution": [
                        "搬酒店日容易過度刺激，下午一定要回房。",
                        "Check-in 後不要立即再出遠門。",
                        "晚餐以近酒店為主。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "正式 check-in", "desc": "入房整理、午睡", "is_nap": True},
                        {"type": "🛏️ 方案 B", "title": "長休息", "desc": "小朋友如已攰，直接睡到晚餐", "is_nap": True},
                        {"type": "😴 方案 C", "title": "安靜玩", "desc": "不睡就玩貼紙書 / 小玩具"},
                        {"type": "🛍️ 方案 D", "title": "整理行李", "desc": "BB 休息，大人整理衣物"},
                        {"type": "🤩 方案 E", "title": "取消外出", "desc": "如狀態差，晚餐外賣解決"}
                    ]
                },
                {
                    "time": "17:30–18:30｜早晚餐",
                    "transport": ["酒店附近：步行或的士"],
                    "caution": [
                        "搬酒店日不要逛夜市。",
                        "食完簡單晚餐就返房。",
                        "晚上避免再搭長途車。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "龍山寺晚餐", "desc": "簡單麵食、飯類"},
                        {"type": "🤩 方案 B", "title": "西門町餐廳", "desc": "選冷氣、有廁所、有兒童椅更好"},
                        {"type": "🛍️ 方案 C", "title": "酒店附近", "desc": "最穩陣，不走遠"},
                        {"type": "🛏️ 方案 D", "title": "外賣返酒店", "desc": "BB 太攰時最佳"},
                        {"type": "😴 方案 E", "title": "短行西門", "desc": "若精神好，飯後只行 30 分鐘"}
                    ]
                }
            ],
            "rainy": [
                {"time": "09:30–11:00｜基隆 → 台北", "activities": [{"type": "🌧️ 雨天版", "title": "包車直達", "desc": "包車到台北酒店，避免淋雨搬行李"}]},
                {"time": "11:00–12:45｜午餐", "activities": [{"type": "🌧️ 雨天版", "title": "室內餐廳", "desc": "選有冷氣、有座位餐廳"}]},
                {"time": "13:00–14:30｜室內展覽", "activities": [{"type": "🌧️ 雨天版", "title": "台博館本館", "desc": "雨天室內替代，展品較安靜"}]},
                {"time": "15:30–17:00｜回房", "activities": [{"type": "🌧️ 雨天版", "title": "正式午睡", "desc": "入房整理、避雨午睡", "is_nap": True}]},
                {"time": "17:30–18:30｜晚餐", "activities": [{"type": "🌧️ 雨天版", "title": "酒店附近", "desc": "外賣或極近距離晚餐"}]}
            ]
        }
    },
    {
        "day": 5, "title": "高能樂園大放電｜兒童新樂園 + 科教館", "hotel": "萬華 / 西門",
        "options": {
            "sunny": [
                {
                    "time": "08:40–11:30｜台北兒童新樂園",
                    "transport": ["萬華 / 西門 → 士林兒童新樂園：的士約 25–35 分鐘"],
                    "caution": [
                        "3歲主攻溫和設施，不要排太刺激項目。",
                        "排隊超過 20 分鐘就換項目。",
                        "如改去動物園，要注意非常曬、非常耗體力，要補水防中暑。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "標準版", "desc": "玩 4–5 個適合3歲設施"},
                        {"type": "😴 方案 B", "title": "溫和設施", "desc": "旋轉木馬、小火車、慢速設施"},
                        {"type": "🛍️ 方案 C", "title": "短玩版", "desc": "玩 90 分鐘，避開中午日曬"},
                        {"type": "🤩 方案 D", "title": "木柵動物園", "desc": "如果想看動物，但體力消耗更大"},
                        {"type": "🌧️ 方案 E", "title": "雨天改室內", "desc": "下雨直接去科教館室內玩"}
                    ]
                },
                {
                    "time": "11:30–12:30｜午餐",
                    "caution": [
                        "午餐時間要讓 BB 坐低休息，不要邊行邊食。",
                        "補水、去廁所、換片。",
                        "不建議排隊餐廳。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "樂園內美食", "desc": "最省力，不用轉場"},
                        {"type": "🤩 方案 B", "title": "科教館美食", "desc": "食完直接去科教館"},
                        {"type": "🛍️ 方案 C", "title": "附近簡餐", "desc": "找冷氣餐廳坐低"},
                        {"type": "😴 方案 D", "title": "輕食休息", "desc": "麵包、水果、飲品，簡單補充"},
                        {"type": "🛏️ 方案 E", "title": "早返酒店", "desc": "如果上午已玩爆，午餐後返酒店", "is_nap": True}
                    ]
                },
                {
                    "time": "12:30–14:45｜科教館",
                    "transport": ["兒童新樂園 → 科教館：步行約 5–10 分鐘"],
                    "caution": [
                        "不需要勉強行晒全館。",
                        "2–3 個互動區已足夠。",
                        "若 BB 開始失控，立即返酒店，不要硬撐。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "互動區", "desc": "玩 2–3 個互動展區"},
                        {"type": "🤩 方案 B", "title": "特展版", "desc": "如有合適兒童特展，可加玩"},
                        {"type": "😴 方案 C", "title": "慢玩版", "desc": "只玩一層，讓 BB 自由探索"},
                        {"type": "🛏️ 方案 D", "title": "超攰備案", "desc": "直接返酒店午睡", "is_nap": True},
                        {"type": "🌧️ 方案 E", "title": "雨天主行程", "desc": "如天氣差，科教館可延長停留"}
                    ]
                },
                {
                    "time": "15:15–17:30｜回酒店午睡",
                    "transport": ["士林 → 萬華 / 西門酒店：的士約 25–35 分鐘"],
                    "caution": [
                        "樂園日放電量很大，下午必須休息。",
                        "不要安排夜市。",
                        "晚餐一定要近酒店。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "車上+房內", "desc": "的士返酒店，讓 BB 補眠", "is_nap": True},
                        {"type": "🛏️ 方案 B", "title": "長午睡", "desc": "直接睡到晚餐", "is_nap": True},
                        {"type": "😴 方案 C", "title": "安靜玩", "desc": "不睡就房內安靜活動"},
                        {"type": "🛍️ 方案 D", "title": "輪流休息", "desc": "一位陪 BB，一位整理 / 買東西"},
                        {"type": "🤩 方案 E", "title": "取消散步", "desc": "如果上午活動量大，晚餐後不再外出"}
                    ]
                },
                {
                    "time": "17:45–19:15｜酒店附近晚餐",
                    "caution": [
                        "避免再去人多夜市。",
                        "19:30 前返酒店較理想。",
                        "小朋友若過度興奮，睡前要留安靜時間。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "西門町餐廳", "desc": "選有冷氣、有座位餐廳"},
                        {"type": "🤩 方案 B", "title": "萬華 / 龍山寺", "desc": "麵、飯、湯類最穩陣"},
                        {"type": "🛍️ 方案 C", "title": "附近簡餐", "desc": "最少移動"},
                        {"type": "🛏️ 方案 D", "title": "外賣", "desc": "BB 已攰時最佳"},
                        {"type": "😴 方案 E", "title": "飯後短行", "desc": "精神好才行 20–30 分鐘"}
                    ]
                }
            ],
            "rainy": [
                {"time": "08:40–14:45｜全日室內", "activities": [{"type": "🌧️ 雨天版", "title": "科教館", "desc": "下雨直接去科教館室內玩，可延長停留"}]},
                {"time": "15:15–17:30｜回房", "activities": [{"type": "🌧️ 雨天版", "title": "午睡", "desc": "直接睡到晚餐", "is_nap": True}]},
                {"time": "17:45–19:15｜晚餐", "activities": [{"type": "🌧️ 雨天版", "title": "附近簡餐", "desc": "最少移動避雨"}]}
            ]
        }
    },
    {
        "day": 6, "title": "室內天文與河畔黃昏｜天文館 + 淡水", "hotel": "萬華 / 西門",
        "options": {
            "sunny": [
                {
                    "time": "08:45–11:30｜台北市立天文館",
                    "transport": ["萬華 / 西門 → 士林天文館：的士約 25–35 分鐘"],
                    "caution": [
                        "天文劇場視乎 BB 是否坐得定再決定。",
                        "如果怕黑、怕大聲，不建議硬看劇場。",
                        "天文館同科教館位置近，可彈性替換。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "標準版", "desc": "宇宙展、星球、互動區"},
                        {"type": "🤩 方案 B", "title": "劇場版", "desc": "BB 坐得定、不怕黑才買劇場票"},
                        {"type": "😴 方案 C", "title": "短玩版", "desc": "玩 60–90 分鐘即可"},
                        {"type": "🛏️ 方案 D", "title": "超攰備案", "desc": "留酒店慢早餐，取消早上景點"},
                        {"type": "🌧️ 方案 E", "title": "雨天加強", "desc": "如下雨，天文館 / 科教館室內活動延長"}
                    ]
                },
                {
                    "time": "11:30–13:00｜午餐 + 前往捷運站",
                    "transport": ["天文館 / 科教館 → 捷運士林或劍潭站：的士約 5–10 分鐘"],
                    "caution": [
                        "午餐後先去廁所、補水。",
                        "去淡水前要確認 BB 狀態。",
                        "如果已經打瞌睡，可利用捷運午睡。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "科教館美食", "desc": "冷氣、有座位、廁所方便"},
                        {"type": "🛍️ 方案 B", "title": "天文館簡餐", "desc": "快食快走"},
                        {"type": "🤩 方案 C", "title": "士林餐廳", "desc": "找適合小朋友嘅餐廳"},
                        {"type": "🛏️ 方案 D", "title": "返酒店", "desc": "如 BB 已攰，取消淡水", "is_nap": True},
                        {"type": "😴 方案 E", "title": "買輕食", "desc": "準備水、小食，去淡水途中用"}
                    ]
                },
                {
                    "time": "13:00–15:30｜前往淡水 / 備選活動",
                    "transport": [
                        "士林 / 劍潭 → 淡水：捷運紅線約 30–40 分鐘",
                        "士林 → 美麗華：的士或捷運轉乘"
                    ],
                    "caution": [
                        "淡水來回車程較長，要保留體力。",
                        "捷運上注意 BB 車煞車、扶穩。",
                        "如果天氣太熱或落雨，寧願改室內。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "河畔散步", "desc": "捷運到淡水，河邊慢行"},
                        {"type": "🤩 方案 B", "title": "老街輕食", "desc": "買雪糕、小食，但不深入迫人路段"},
                        {"type": "🌧️ 方案 C", "title": "美麗華商場", "desc": "室內冷氣備選，適合雨天 / 太熱"},
                        {"type": "🛏️ 方案 D", "title": "返酒店", "desc": "若 BB 太攰，直接返酒店", "is_nap": True},
                        {"type": "😴 方案 E", "title": "捷運午睡", "desc": "利用紅線車程讓 BB 睡一段", "is_nap": True}
                    ]
                },
                {
                    "time": "15:30–17:30｜淡水黃昏",
                    "caution": [
                        "河邊風大，要帶外套。",
                        "老街人多，要拖實小朋友。",
                        "不要為了日落硬撐到太晚。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "河邊睇船", "desc": "慢行、睇船、吹風"},
                        {"type": "😴 方案 B", "title": "河邊 Cafe", "desc": "坐低休息，飲品 / 小食"},
                        {"type": "🤩 方案 C", "title": "老街小食", "desc": "雪糕、簡單小吃"},
                        {"type": "📷 方案 D", "title": "日落版", "desc": "天氣好就等日落"},
                        {"type": "🛏️ 方案 E", "title": "提早晚餐", "desc": "如果 BB 攰，16:30–17:00 先食早晚餐"}
                    ]
                },
                {
                    "time": "17:30–18:30｜淡水晚餐",
                    "transport": ["淡水 → 台北市區 / 萬華：捷運約 60 分鐘左右", "淡水 → 酒店：的士較貴且可能塞車"],
                    "caution": [
                        "去完淡水，絕對不要再加夜市。",
                        "晚餐後直接回酒店。",
                        "回程 BB 很可能睡著，準備外套 / 小被。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "老街晚餐", "desc": "選有座位餐廳"},
                        {"type": "🤩 方案 B", "title": "河邊餐廳", "desc": "景觀好，但不建議排長隊"},
                        {"type": "🛍️ 方案 C", "title": "簡單麵飯", "desc": "快食快走"},
                        {"type": "😴 方案 D", "title": "外帶上車", "desc": "BB 太攰可買簡單食物"},
                        {"type": "🛏️ 方案 E", "title": "回台北食", "desc": "如淡水太多人，可先搭車回酒店附近"}
                    ]
                }
            ],
            "rainy": [
                {"time": "08:45–13:00｜天文館", "activities": [{"type": "🌧️ 雨天版", "title": "室內活動延長", "desc": "天文館 / 科教館室內活動延長"}]},
                {"time": "13:00–15:30｜商場備案", "activities": [{"type": "🌧️ 雨天版", "title": "美麗華商場", "desc": "室內冷氣備選，適合雨天 / 太熱"}]},
                {"time": "17:30–18:30｜晚餐", "activities": [{"type": "🌧️ 雨天版", "title": "商場晚餐", "desc": "在商場解決晚餐再回酒店"}]}
            ]
        }
    },
    {
        "day": 7, "title": "輕鬆活動與機場回程", "hotel": "回程 ✈️",
        "options": {
            "sunny": [
                {
                    "time": "08:30–09:15｜Check-out + 早餐",
                    "caution": [
                        "行李先整理好，避免最後一刻混亂。",
                        "手提袋要放尿片、濕紙巾、水、小食、後備衫。",
                        "不要安排遠景點。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "酒店早餐", "desc": "最穩陣，食完收行李"},
                        {"type": "🤩 方案 B", "title": "附近早餐", "desc": "簡單食飯糰、蛋餅、豆漿"},
                        {"type": "🛍️ 方案 C", "title": "便利店", "desc": "飯糰、麵包、牛奶"},
                        {"type": "😴 方案 D", "title": "慢慢 check-out", "desc": "留時間俾 BB 玩一下"},
                        {"type": "🛏️ 方案 E", "title": "延遲退房", "desc": "如酒店可安排 late check-out，最舒服"}
                    ]
                },
                {
                    "time": "09:30–10:45｜早上短活動",
                    "transport": ["酒店 → 親子館 / 青年公園：的士約 5–15 分鐘", "酒店附近：步行"],
                    "caution": [
                        "親子館通常要預約，出發前查閱及登記。",
                        "如遇雨天，不建議青年公園。",
                        "活動時間一定要控制，不可玩過鐘。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "萬華親子館", "desc": "室內放電，最適合3歲"},
                        {"type": "🤩 方案 B", "title": "青年公園", "desc": "天氣好可跑跳"},
                        {"type": "😴 方案 C", "title": "附近散步", "desc": "最輕鬆，不搭車"},
                        {"type": "🛍️ 方案 D", "title": "西門町短行", "desc": "買手信 / 飲品"},
                        {"type": "🛏️ 方案 E", "title": "直接去機場", "desc": "如果大人想穩陣，早點去機場"}
                    ]
                },
                {
                    "time": "11:15–12:45｜午餐 + 取行李",
                    "caution": [
                        "上車前為 BB 換好尿片、去廁所。",
                        "預先買定水及小食。",
                        "不要午餐後再加行程。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "附近午餐", "desc": "最安全，食完即取行李"},
                        {"type": "🤩 方案 B", "title": "西門町", "desc": "選近酒店、有冷氣餐廳"},
                        {"type": "🛍️ 方案 C", "title": "龍山寺", "desc": "簡單飯麵"},
                        {"type": "😴 方案 D", "title": "外帶", "desc": "如時間緊，買外帶"},
                        {"type": "🛏️ 方案 E", "title": "機場午餐", "desc": "如果早出發，到機場食"}
                    ]
                },
                {
                    "time": "13:00–14:15｜前往桃園機場",
                    "transport": [
                        "首選：包車 / 的士 (約 45–70 分鐘) - 有行李、BB 車、最穩陣",
                        "高性價比：的士去 A1 + 機捷直達車 (總計約 50–60 分鐘)",
                        "不建議：全程公車 / 多次轉車 - 時間不穩"
                    ],
                    "caution": [
                        "17:00 航班，最遲 13:00 必須起行。",
                        "包車仍要提早預約兒童安全座椅。",
                        "預留塞車、排隊、BB 突然要廁所等突發狀況。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "包車直達", "desc": "最舒服，點對點"},
                        {"type": "🛍️ 方案 B", "title": "機捷版", "desc": "的士去台北車站 A1，再搭機捷直達車"},
                        {"type": "🤩 方案 C", "title": "早出發", "desc": "12:30 出發，預留更多時間"},
                        {"type": "😴 方案 D", "title": "車上午睡", "desc": "安排安靜環境，讓 BB 睡", "is_nap": True},
                        {"type": "🛏️ 方案 E", "title": "早到機場", "desc": "早到機場後去兒童區 / 輕食"}
                    ]
                },
                {
                    "time": "14:15–17:00｜機場 Check-in + 登機",
                    "caution": [
                        "入閘前後都要安排去廁所。",
                        "機場兒童區不要玩到滿頭汗才上機。",
                        "登機前準備水、小食、貼紙書 / 小玩具。"
                    ],
                    "activities": [
                        {"type": "⭐ 方案 A", "title": "處理行李", "desc": "到機場先處理行李"},
                        {"type": "🤩 方案 B", "title": "兒童區", "desc": "辦妥手續後去兒童區玩"},
                        {"type": "🛍️ 方案 C", "title": "輕食", "desc": "食少少麵包、飯、飲品"},
                        {"type": "😴 方案 D", "title": "安靜等待", "desc": "找座位休息，避免太興奮"},
                        {"type": "🛏️ 方案 E", "title": "提早去閘口", "desc": "預留時間行去登機閘口"}
                    ]
                }
            ],
            "rainy": [
                {"time": "09:30–10:45｜室內活動", "activities": [{"type": "🌧️ 雨天版", "title": "萬華親子館", "desc": "室內放電，最適合3歲"}]},
                {"time": "13:00–14:15｜前往機場", "activities": [{"type": "🌧️ 雨天版", "title": "包車直達", "desc": "最舒服避雨，點對點"}]}
            ]
        }
    }
]

# ==========================================
# 2. UI 渲染 (結合交通與 Cautions)
# ==========================================
@ui.page('/')
def safe_build_ui():
    try:
        build_ui()
    except Exception as e:
        ui.label('⚠️ 系統在啟動時遇到小問題').classes('text-[20px] font-black text-red-600 px-4 pt-8')
        ui.label(str(e)).classes('text-[13px] text-red-500 px-4 mt-4 font-mono')
        ui.label(traceback.format_exc()).classes('text-[11px] text-slate-400 p-4 whitespace-pre-wrap font-mono bg-slate-100 rounded-xl m-4 overflow-x-auto')

def build_ui():
    ui.add_head_html('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">')
    ui.query('body').classes('bg-slate-200 m-0 p-0 overflow-x-hidden')

    state = {
        'weather': app.storage.user.get('weather', 'sunny')
    }

    with ui.column().classes('w-full max-w-[500px] mx-auto min-h-screen bg-slate-50 shadow-2xl relative pb-28 pt-6 px-4'):
        
        # 標題與工具箱
        with ui.row().classes('w-full items-center justify-between mb-4'):
            with ui.column().classes('gap-0'):
                ui.label('💕 寶貝行程神隊友').classes('text-[20px] font-black text-slate-800 tracking-wider')
                ui.label('彈性調整 ⚡ 輕鬆陪伴 ❄️ 快樂回憶').classes('text-[11px] text-slate-500 font-bold mt-1')
            
            with ui.dialog() as dialog, ui.card().classes('w-full max-w-sm rounded-3xl p-6'):
                dialog_title = ui.label().classes('text-[18px] font-bold text-slate-800 border-b border-slate-100 pb-3 mb-3 w-full')
                dialog_desc = ui.label().classes('text-[14px] text-slate-600 mb-5 leading-relaxed')
                ui.label('👨‍👩‍👧 父母實用工具').classes('text-[13px] font-bold text-slate-400 mb-2 tracking-wide')
                
                with ui.row().classes('w-full gap-3 mb-4'):
                    map_btn = ui.button('📍 Google Maps').classes('flex-grow bg-blue-50 text-blue-600 rounded-xl shadow-none text-[13px] font-bold py-2')
                    uber_btn = ui.button('🚗 叫 Uber').classes('flex-grow bg-black text-white rounded-xl shadow-md text-[13px] font-bold py-2')
                
                ui.button('關閉', on_click=dialog.close).classes('w-full mt-2 bg-slate-200 text-slate-800 rounded-xl font-bold py-2 shadow-sm text-[14px]')

            def show_info(name, desc):
                dialog_title.set_text(name)
                dialog_desc.set_text(desc)
                map_btn.on_click(lambda: ui.navigate.to(f"https://www.google.com/maps/search/?api=1&query={name}", new_tab=True))
                uber_btn.on_click(lambda: ui.navigate.to("https://m.uber.com/ul/?action=setPickup&pickup=my_location", new_tab=True))
                dialog.open()

            ui.button('🛠️ 工具箱', on_click=lambda: show_info("目前位置", "點擊下方按鈕開啟地圖或叫車")).classes('bg-slate-100 text-slate-700 shadow-none px-3 py-2 rounded-full font-bold text-[13px] hover:bg-slate-200 transition-colors')

        # === 每日行程主體 ===
        ui.label('📅 專屬每日行程').classes('text-[18px] font-black text-slate-800 mt-2 mb-4 tracking-widest pl-2 border-l-[5px] border-amber-400')

        for day_data in ITINERARY:
            is_first_day = (day_data["day"] == 1)
            with ui.expansion(f'📍 Day {day_data["day"]}｜{day_data["title"]}', value=is_first_day).classes('w-full bg-white rounded-2xl shadow-sm mb-4 font-black text-slate-800 border border-slate-100 text-[15px] leading-tight').props('group="itinerary"'):
                ui.label(f'宿: {day_data["hotel"]}').classes('bg-amber-400 text-white text-[10px] px-2 py-0.5 rounded-md absolute right-10 top-4 shadow-sm tracking-wide')
                
                # --- 晴天 / 標準行程 ---
                with ui.column().classes('w-full bg-transparent p-0 mt-2').bind_visibility_from(state, 'weather', backward=lambda w: w == 'sunny'):
                    time_slots = day_data["options"].get('sunny', [])
                    for slot in time_slots:
                        ui.label(f"⏰ {slot['time']}").classes('text-[14px] font-black text-slate-500 mt-4 mb-2 border-b-2 border-slate-100 pb-1 w-full tracking-wider leading-relaxed')
                        
                        # [新增] 交通建議區塊
                        if slot.get('transport'):
                            with ui.column().classes('w-full bg-blue-50/60 p-3 rounded-xl mb-2 border border-blue-100/50 gap-1 shadow-sm'):
                                ui.label('🚖 交通安排').classes('font-black text-blue-800 text-[13px] mb-1')
                                for t in slot['transport']:
                                    ui.label(f"• {t}").classes('text-[12px] text-slate-600 leading-snug ml-1')

                        # [新增] 3歲 BB Caution 區塊
                        if slot.get('caution'):
                            with ui.column().classes('w-full bg-red-50/60 p-3 rounded-xl mb-3 border border-red-100/50 gap-1 shadow-sm'):
                                ui.label('⚠️ 3歲 BB Caution').classes('font-black text-red-800 text-[13px] mb-1')
                                for c in slot['caution']:
                                    ui.label(f"• {c}").classes('text-[12px] text-slate-600 leading-snug ml-1')

                        is_multi = len(slot['activities']) > 1
                        if is_multi:
                            ui.label('👉 左右滑動揀選不同方案').classes('text-[11px] text-amber-600/70 font-bold mb-1 ml-1')

                        container_classes = 'w-full flex flex-nowrap overflow-x-auto snap-x snap-mandatory pb-4 gap-3 -mx-1 px-1' if is_multi else 'w-full flex flex-col gap-3'
                        
                        with ui.row().classes(container_classes):
                            for idx, event in enumerate(slot['activities']):
                                bg_color = 'bg-purple-50/80' if event.get('is_nap') else 'bg-white'
                                border_color = 'border-purple-400' if event.get('is_nap') else ('border-amber-400' if idx == 0 else 'border-emerald-400')
                                
                                # 動態決定 Tag 顏色
                                badge_bg = 'bg-slate-400'
                                if '⭐' in event.get('type', ''): badge_bg = 'bg-amber-500'
                                elif '🤩' in event.get('type', ''): badge_bg = 'bg-orange-500'
                                elif '😴' in event.get('type', ''): badge_bg = 'bg-purple-400'
                                elif '🛍️' in event.get('type', ''): badge_bg = 'bg-emerald-500'
                                elif '🛏️' in event.get('type', ''): badge_bg = 'bg-slate-500'
                                elif '🌧️' in event.get('type', ''): badge_bg = 'bg-blue-500'
                                
                                card_width = 'min-w-[85%] snap-center shrink-0' if is_multi else 'w-full'
                                card_p = 'p-3 mb-2' if is_multi else 'p-4 mb-3'
                                title_sz = 'text-[14px]' if is_multi else 'text-[15px]'
                                
                                with ui.card().classes(f'{card_width} {bg_color} border-l-[6px] {border_color} shadow-sm {card_p} cursor-pointer hover:shadow-md hover:-translate-y-0.5 transition-all').on('click', lambda e=event: show_info(e['title'], e['desc'])):
                                    with ui.column().classes('w-full gap-1 mb-2'):
                                        if is_multi or event.get('type'):
                                            ui.label(event.get('type', f"方案 {chr(65+idx)}")).classes(f'text-white {badge_bg} px-2 py-0.5 rounded text-[10px] font-black tracking-widest shadow-sm self-start')
                                        ui.label(event['title']).classes(f'font-black text-slate-800 {title_sz} mt-1')

                                    ui.label(event['desc']).classes('text-[13px] text-slate-600 font-medium leading-relaxed mb-1')

                # --- 雨天備案 ---
                with ui.column().classes('w-full bg-transparent p-0 mt-2').bind_visibility_from(state, 'weather', backward=lambda w: w == 'rainy'):
                    time_slots = day_data["options"].get('rainy', [])
                    
                    if time_slots:
                        ui.label('🌧️ 已啟用【雨天避險】專屬路線').classes('text-[13px] text-blue-700 bg-blue-50 p-3 rounded-lg mb-3 w-full font-bold border border-blue-100')
                    else:
                        ui.label('☀️ 本日預設為全室內行程，無懼風雨！').classes('text-[13px] text-orange-700 bg-orange-50 p-3 rounded-lg mb-3 w-full font-bold border border-orange-100')

                    for slot in time_slots:
                        ui.label(f"⏰ {slot['time']}").classes('text-[14px] font-black text-slate-500 mt-4 mb-2 border-b-2 border-slate-100 pb-1 w-full tracking-wider leading-relaxed')
                        
                        is_multi = len(slot['activities']) > 1
                        container_classes = 'w-full flex flex-nowrap overflow-x-auto snap-x snap-mandatory pb-4 gap-3 -mx-1 px-1' if is_multi else 'w-full flex flex-col gap-3'
                        
                        with ui.row().classes(container_classes):
                            for idx, event in enumerate(slot['activities']):
                                bg_color = 'bg-purple-50/80' if event.get('is_nap') else 'bg-white'
                                border_color = 'border-blue-500'
                                badge_bg = 'bg-blue-500'
                                
                                card_width = 'min-w-[85%] snap-center shrink-0' if is_multi else 'w-full'
                                card_p = 'p-3 mb-2' if is_multi else 'p-4 mb-3'
                                title_sz = 'text-[14px]' if is_multi else 'text-[15px]'
                                
                                with ui.card().classes(f'{card_width} {bg_color} border-l-[6px] {border_color} shadow-sm {card_p} cursor-pointer hover:shadow-md hover:-translate-y-0.5 transition-all').on('click', lambda e=event: show_info(e['title'], e['desc'])):
                                    with ui.column().classes('w-full gap-1 mb-2'):
                                        if is_multi or event.get('type'):
                                            ui.label(event.get('type', f"方案 {chr(65+idx)}")).classes(f'text-white {badge_bg} px-2 py-0.5 rounded text-[10px] font-black tracking-widest shadow-sm self-start')
                                        ui.label(event['title']).classes(f'font-black text-slate-800 {title_sz} mt-1')

                                    ui.label(event['desc']).classes('text-[13px] text-slate-600 font-medium leading-relaxed mb-1')

    # 回到頂端按鈕
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=100):
        ui.button('⬆️', on_click=lambda: ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"})')).classes('bg-slate-800/60 hover:bg-slate-800 text-white rounded-full shadow-md backdrop-blur-sm transition-all font-bold text-lg').props('padding="12px"')

    btn_sunny = None
    btn_rainy = None

    def set_w(w):
        state['weather'] = w
        app.storage.user['weather'] = w
        if w == 'sunny':
            btn_sunny.classes(replace='flex-1 bg-amber-500 text-white font-black rounded-xl shadow-md py-3 text-[14px] tracking-widest transition-all')
            btn_rainy.classes(replace='flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[14px] tracking-widest transition-all')
        else:
            btn_sunny.classes(replace='flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[14px] tracking-widest transition-all')
            btn_rainy.classes(replace='flex-1 bg-blue-500 text-white font-black rounded-xl shadow-md py-3 text-[14px] tracking-widest transition-all')

    with ui.row().classes('fixed bottom-6 left-1/2 -translate-x-1/2 w-[calc(100%-2rem)] max-w-[468px] bg-white/90 backdrop-blur-xl shadow-[0_8px_30px_rgba(0,0,0,0.12)] p-2 flex justify-center gap-2 z-50 rounded-2xl border border-slate-200/50'):
        init_sun_cls = 'flex-1 bg-amber-500 text-white font-black rounded-xl shadow-md py-3 text-[14px] tracking-widest transition-all' if state['weather'] == 'sunny' else 'flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[14px] tracking-widest transition-all'
        init_rain_cls = 'flex-1 bg-blue-500 text-white font-black rounded-xl shadow-md py-3 text-[14px] tracking-widest transition-all' if state['weather'] == 'rainy' else 'flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[14px] tracking-widest transition-all'
        
        btn_sunny = ui.button('☀ 晴朗/預設', on_click=lambda: set_w('sunny')).classes(init_sun_cls)
        btn_rainy = ui.button('🌧 雷雨/室內', on_click=lambda: set_w('rainy')).classes(init_rain_cls)

PORT = int(os.environ.get('PORT', 8080))

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="寶貝行程神隊友", port=PORT, host='0.0.0.0', storage_secret='my_super_secret_key_123', show=False)