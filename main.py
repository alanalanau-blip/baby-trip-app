from nicegui import ui, app
import os

# ==========================================
# 1. 全新矩陣行程資料庫 (7日完整彈性版)
# ==========================================
ITINERARY = [
    {
        "day": 1, "title": "抵達基隆｜輕鬆適應日", "hotel": "基隆",
        "options": {
            "sunny": [
                {"time": "14:00-15:30", "activities": [
                    {"type": "⭐ 標準", "title": "包車直達酒店", "desc": "抵達台灣後，包車 / 的士直去基隆酒店；車程中讓小朋友小睡", "place": "基隆", "is_nap": True},
                    {"type": "🤩 活力", "title": "車上小遊戲", "desc": "包車去基隆，車上準備小食、貼紙書，避免悶", "place": "基隆", "is_nap": False},
                    {"type": "😴 休息", "title": "安靜補眠", "desc": "抵達後直接上車，盡量安靜讓小朋友睡", "place": "基隆", "is_nap": True},
                    {"type": "🛍️ 輕鬆", "title": "機場簡單補給", "desc": "機場先買麵包、水果、牛奶，再去基隆", "place": "桃園機場", "is_nap": False}
                ]},
                {"time": "15:30-16:30", "activities": [
                    {"type": "⭐ 標準", "title": "辦理入住休息", "desc": "酒店 check-in，換衫、飲水、休息", "place": "酒店", "is_nap": False},
                    {"type": "🤩 活力", "title": "房內小活動", "desc": "酒店放低行李後，讓小朋友在房內活動一下", "place": "酒店", "is_nap": False},
                    {"type": "😴 休息", "title": "酒店午睡", "desc": "酒店午睡，不急住出門", "place": "酒店", "is_nap": True},
                    {"type": "🛍️ 輕鬆", "title": "便利店補給", "desc": "酒店附近便利店補給尿片、水、小食", "place": "便利店", "is_nap": False}
                ]},
                {"time": "16:30-17:00", "activities": [
                    {"type": "⭐ 標準", "title": "出發廟口夜市", "desc": "出發去基隆廟口夜市早場", "place": "基隆廟口夜市", "is_nap": False},
                    {"type": "🤩 活力", "title": "前往海洋廣場", "desc": "去海洋廣場，先讓小朋友跑一跑", "place": "海洋廣場", "is_nap": False},
                    {"type": "😴 休息", "title": "留守酒店附近", "desc": "留在酒店附近，不搭車", "place": "酒店附近", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "附近搵食", "desc": "去便利店 / 麵包店 / 簡餐店", "place": "酒店附近", "is_nap": False}
                ]},
                {"time": "17:00-18:00", "activities": [
                    {"type": "⭐ 標準", "title": "廟口簡單晚餐", "desc": "廟口夜市簡單晚餐，選湯麵、魚丸湯、滷肉飯", "place": "基隆廟口夜市", "is_nap": False},
                    {"type": "🤩 活力", "title": "海景晚餐", "desc": "海洋廣場附近晚餐，食完再散步", "place": "海洋廣場", "is_nap": False},
                    {"type": "😴 休息", "title": "就近食飯", "desc": "酒店附近食飯，越近越好", "place": "酒店附近", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "外賣返房食", "desc": "外賣飯 / 麵 / 水果返酒店食", "place": "酒店", "is_nap": False}
                ]},
                {"time": "18:00-18:45", "activities": [
                    {"type": "⭐ 標準", "title": "散步睇船", "desc": "海洋廣場睇船、散步 30–40分鐘", "place": "海洋廣場", "is_nap": False},
                    {"type": "🤩 活力", "title": "盡情奔跑", "desc": "海洋廣場放電，睇船、睇海、跑一陣", "place": "海洋廣場", "is_nap": False},
                    {"type": "😴 休息", "title": "房內安靜準備", "desc": "房內玩玩具、沖涼、準備睡", "place": "酒店", "is_nap": True},
                    {"type": "🛍️ 輕鬆", "title": "房內休息", "desc": "酒店房內安靜活動", "place": "酒店", "is_nap": False}
                ]},
                {"time": "19:00", "activities": [
                    {"type": "⭐ 標準", "title": "沖涼休息", "desc": "返酒店沖涼休息", "place": "酒店", "is_nap": True},
                    {"type": "🤩 活力", "title": "提早回防", "desc": "返酒店，避免太夜太興奮", "place": "酒店", "is_nap": True},
                    {"type": "😴 休息", "title": "提早入睡", "desc": "早睡", "place": "酒店", "is_nap": True},
                    {"type": "🛍️ 輕鬆", "title": "提早入睡", "desc": "早睡", "place": "酒店", "is_nap": True}
                ]}
            ],
            "rainy": [
                {"time": "14:00-15:30", "activities": [{"type": "🌧️ 室內", "title": "直奔避雨", "desc": "抵達後不加任何景點，直接去酒店避雨", "place": "酒店", "is_nap": True}]},
                {"time": "15:30-16:30", "activities": [{"type": "🌧️ 室內", "title": "整理雨具", "desc": "酒店休息，整理雨具、後備衫", "place": "酒店", "is_nap": False}]},
                {"time": "16:30-17:00", "activities": [{"type": "🌧️ 室內", "title": "轉移室內商場", "desc": "去東岸廣場，有冷氣、有廁所", "place": "東岸廣場", "is_nap": False}]},
                {"time": "17:00-18:00", "activities": [{"type": "🌧️ 室內", "title": "商場晚餐", "desc": "東岸廣場晚餐，適合避雨和坐低", "place": "東岸廣場", "is_nap": False}]},
                {"time": "18:00-18:45", "activities": [{"type": "🌧️ 室內", "title": "室內行街", "desc": "東岸廣場室內行一圈，買飲品", "place": "東岸廣場", "is_nap": False}]},
                {"time": "19:00", "activities": [{"type": "🌧️ 室內", "title": "回房休息", "desc": "返酒店休息", "place": "酒店", "is_nap": True}]}
            ]
        }
    },
    {
        "day": 2, "title": "海科館 + i OCEAN｜冷氣親子日", "hotel": "基隆",
        "options": {
            "sunny": [
                {"time": "07:30-08:30", "activities": [
                    {"type": "⭐ 標準", "title": "早餐準備", "desc": "早餐、去廁所、帶水和小食", "place": "酒店附近", "is_nap": False},
                    {"type": "🤩 活力", "title": "防曬準備", "desc": "早餐後準備防曬、帽、後備衫", "place": "酒店附近", "is_nap": False},
                    {"type": "😴 休息", "title": "觀察狀態", "desc": "慢慢食早餐，觀察小朋友精神", "place": "酒店附近", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "慢慢出門", "desc": "早餐後先讓小朋友在酒店玩一陣", "place": "酒店附近", "is_nap": False}
                ]},
                {"time": "08:45-09:15", "activities": [
                    {"type": "⭐ 標準", "title": "搭車前往", "desc": "的士去海科館，車程約20–25分鐘", "place": "海科館", "is_nap": False},
                    {"type": "🤩 活力", "title": "提早出門", "desc": "早少少出發，避開人流", "place": "海科館", "is_nap": False},
                    {"type": "😴 休息", "title": "稍遲出門", "desc": "09:30左右才出發", "place": "海科館", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "更遲出門", "desc": "10:00左右才出發", "place": "海科館", "is_nap": False}
                ]},
                {"time": "09:30-11:30", "activities": [
                    {"type": "⭐ 標準", "title": "兒童廳放電", "desc": "海科館兒童廳 / 互動區，適合3歲摸摸看看", "place": "海科館", "is_nap": False},
                    {"type": "🤩 活力", "title": "加碼主題館", "desc": "兒童廳 + 主題館，多玩按鈕、模型、船舶展示", "place": "海科館", "is_nap": False},
                    {"type": "😴 休息", "title": "重點慢玩", "desc": "只玩小朋友最有興趣的展區，不趕場", "place": "海科館", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "短玩即走", "desc": "海科館玩 60–90分鐘即可", "place": "海科館", "is_nap": False}
                ]},
                {"time": "11:30-12:30", "activities": [
                    {"type": "⭐ 標準", "title": "館內午餐", "desc": "館內午餐，食麵、飯、簡餐", "place": "海科館", "is_nap": False},
                    {"type": "🤩 活力", "title": "外出用餐", "desc": "八斗子附近午餐，環境較開揚", "place": "八斗子", "is_nap": False},
                    {"type": "😴 休息", "title": "安靜補水", "desc": "館內坐低休息，補水、小食", "place": "海科館", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "回酒店食", "desc": "午餐後直接返酒店", "place": "酒店", "is_nap": False}
                ]},
                {"time": "12:30-12:45", "activities": [
                    {"type": "⭐ 標準", "title": "轉移水族館", "desc": "的士去 i OCEAN，短車程", "place": "潮境智能海洋館", "is_nap": False},
                    {"type": "🤩 活力", "title": "短看海景", "desc": "去 i OCEAN，若天氣好可短看海", "place": "潮境智能海洋館", "is_nap": False},
                    {"type": "😴 休息", "title": "視乎體力", "desc": "視乎小朋友狀態，決定去或不去", "place": "潮境智能海洋館", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "直接午睡", "desc": "返酒店午睡", "place": "酒店", "is_nap": True}
                ]},
                {"time": "12:45-14:00", "activities": [
                    {"type": "⭐ 標準", "title": "欣賞水族", "desc": "i OCEAN 睇魚、互動展，停留約1小時", "place": "潮境智能海洋館", "is_nap": False},
                    {"type": "🤩 活力", "title": "加碼散步", "desc": "i OCEAN + 潮境附近短散步", "place": "潮境公園", "is_nap": False},
                    {"type": "😴 休息", "title": "短玩即走", "desc": "i OCEAN 只短玩45分鐘", "place": "潮境智能海洋館", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "酒店休息", "desc": "酒店休息", "place": "酒店", "is_nap": True}
                ]},
                {"time": "14:00-14:30", "activities": [
                    {"type": "⭐ 標準", "title": "準備回程", "desc": "的士返基隆酒店", "place": "酒店", "is_nap": False},
                    {"type": "🤩 活力", "title": "車上午睡", "desc": "的士返酒店，車上午睡", "place": "酒店", "is_nap": True},
                    {"type": "😴 休息", "title": "不再加行程", "desc": "返酒店，不再加景點", "place": "酒店", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "持續午睡", "desc": "酒店午睡", "place": "酒店", "is_nap": True}
                ]},
                {"time": "14:30-16:15", "activities": [
                    {"type": "⭐ 標準", "title": "安靜休息", "desc": "酒店午睡 / 安靜休息", "place": "酒店", "is_nap": True},
                    {"type": "🤩 活力", "title": "恢復體力", "desc": "酒店午睡，恢復體力", "place": "酒店", "is_nap": True},
                    {"type": "😴 休息", "title": "自然睡醒", "desc": "長休息，讓小朋友自然醒", "place": "酒店", "is_nap": True},
                    {"type": "🛍️ 輕鬆", "title": "長休息", "desc": "酒店長休息", "place": "酒店", "is_nap": True}
                ]},
                {"time": "16:30-17:30", "activities": [
                    {"type": "⭐ 標準", "title": "廣場散步", "desc": "海洋廣場散步，睇船", "place": "海洋廣場", "is_nap": False},
                    {"type": "🤩 活力", "title": "加碼放電", "desc": "海洋廣場放電，再去東岸廣場", "place": "海洋廣場", "is_nap": False},
                    {"type": "😴 休息", "title": "短散步", "desc": "酒店附近散步15–30分鐘", "place": "酒店附近", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "不出門", "desc": "不再外出或只買晚餐", "place": "酒店", "is_nap": False}
                ]},
                {"time": "17:30-18:30", "activities": [
                    {"type": "⭐ 標準", "title": "商場晚餐", "desc": "東岸廣場晚餐，有座位、有廁所", "place": "東岸廣場", "is_nap": False},
                    {"type": "🤩 活力", "title": "夜市小食", "desc": "廟口夜市早場食少少小食", "place": "基隆廟口夜市", "is_nap": False},
                    {"type": "😴 休息", "title": "附近食飯", "desc": "酒店附近餐廳", "place": "酒店附近", "is_nap": False},
                    {"type": "🛍️ 輕鬆", "title": "外賣簡餐", "desc": "外賣 / 酒店附近簡餐", "place": "酒店", "is_nap": False}
                ]},
                {"time": "19:00", "activities": [
                    {"type": "⭐ 標準", "title": "回房休息", "desc": "返酒店", "place": "酒店", "is_nap": True},
                    {"type": "🤩 活力", "title": "回房休息", "desc": "返酒店", "place": "酒店", "is_nap": True},
                    {"type": "😴 休息", "title": "早睡", "desc": "早睡", "place": "酒店", "is_nap": True},
                    {"type": "🛍️ 輕鬆", "title": "早睡", "desc": "早睡", "place": "酒店", "is_nap": True}
                ]}
            ],
            "rainy": [
                {"time": "07:30-08:30", "activities": [{"type": "🌧️ 室內", "title": "帶妥雨具", "desc": "早餐後不急，帶雨具", "place": "酒店", "is_nap": False}]},
                {"time": "08:45-09:15", "activities": [{"type": "🌧️ 室內", "title": "的士直達", "desc": "的士直達海科館門口，減少淋雨", "place": "海科館", "is_nap": False}]},
                {"time": "09:30-11:30", "activities": [{"type": "🌧️ 室內", "title": "全程室內", "desc": "全程室內，玩兒童廳、海洋展示", "place": "海科館", "is_nap": False}]},
                {"time": "11:30-12:30", "activities": [{"type": "🌧️ 室內", "title": "避雨午餐", "desc": "館內午餐避雨，食完休息", "place": "海科館", "is_nap": False}]},
                {"time": "12:30-12:45", "activities": [{"type": "🌧️ 室內", "title": "室內轉場", "desc": "的士去 i OCEAN，繼續室內活動", "place": "潮境智能海洋館", "is_nap": False}]},
                {"time": "12:45-14:00", "activities": [{"type": "🌧️ 室內", "title": "慢玩水族", "desc": "i OCEAN 室內慢玩", "place": "潮境智能海洋館", "is_nap": False}]},
                {"time": "14:00-14:30", "activities": [{"type": "🌧️ 室內", "title": "搭車避雨", "desc": "的士返酒店", "place": "酒店", "is_nap": False}]},
                {"time": "14:30-16:15", "activities": [{"type": "🌧️ 室內", "title": "休息避雨", "desc": "酒店休息避雨", "place": "酒店", "is_nap": True}]},
                {"time": "16:30-17:30", "activities": [{"type": "🌧️ 室內", "title": "商場活動", "desc": "東岸廣場室內活動", "place": "東岸廣場", "is_nap": False}]},
                {"time": "17:30-18:30", "activities": [{"type": "🌧️ 室內", "title": "商場晚餐", "desc": "東岸廣場晚餐", "place": "東岸廣場", "is_nap": False}]},
                {"time": "19:00", "activities": [{"type": "🌧️ 室內", "title": "回房休息", "desc": "返酒店", "place": "酒店", "is_nap": True}]}
            ]
        }
    },
    {
        "day": 3, "title": "玩水消暑 ⇄ 彩虹屋", "hotel": "基隆",
        "options": {
            "sunny": [
                {"time": "09:00-11:30 (早晨放電)", "activities": [
                    {"type": "⭐ 標準", "title": "和平島親親水池", "desc": "趁早上還沒那麼熱，帶寶貝去玩天然海水和沙灘，盡情釋放體力！", "place": "和平島地質公園", "is_nap": False, "cost": "成人NT$120", "duration": "2.5 hrs", "age": "3歲+", "tips": ["👕 備更換衣物", "🚿 有沖洗區"]},
                    {"type": "🤩 活力", "title": "和平島公園短行", "desc": "如果寶貝不想下水，推車在園區步道看海景吹海風也很棒。", "place": "和平島公園步道", "is_nap": False, "cost": "成人NT$120", "duration": "1.5 hrs", "age": "全家", "tips": ["🧴 注意防曬"]}
                ]},
                {"time": "13:00-15:30 (正午休息)", "activities": [
                    {"type": "😴 休息", "title": "酒店充電時間", "desc": "玩水後寶貝一定非常睏，務必回酒店睡覺，避免過度疲勞鬧情緒。", "place": "基隆金華飯店", "is_nap": True, "cost": "免費", "duration": "2.5 hrs", "age": "全家", "tips": ["🚕 建議搭車"]},
                    {"type": "🛍️ 輕鬆", "title": "東岸廣場安靜休息", "desc": "如果不想回酒店，就去商場找間有沙發的 Cafe 讓孩子趴著睡一下。", "place": "東岸廣場", "is_nap": False, "cost": "依消費", "duration": "2 hrs", "age": "全家", "tips": ["☕ 爸媽喝咖啡"]}
                ]},
                {"time": "16:00-17:30 (黃昏活動)", "activities": [
                    {"type": "⭐ 標準", "title": "正濱漁港打卡", "desc": "下午陽光溫和，去彩虹屋拍拍照，找間 Cafe 吃點冰淇淋放鬆。", "place": "正濱漁港彩虹屋", "is_nap": False, "cost": "約NT$200", "duration": "1.5 hrs", "age": "全家", "tips": ["📷 拍照景點"]}
                ]}
            ],
            "rainy": [
                {"time": "09:30-13:00 (雨天備案)", "activities": [
                    {"type": "🌧️ 室內", "title": "野柳海洋世界", "desc": "若海邊封閉，改搭車去室內看可愛的海豚和海獅表演。", "place": "野柳海洋世界", "is_nap": False, "cost": "成人NT$450", "duration": "3 hrs", "age": "3歲+", "tips": ["❄️ 有遮蔽物"]},
                    {"type": "🌧️ 室內", "title": "陽明海洋文化藝術館", "desc": "留在基隆市區，去火車站旁邊的藝術館體驗開船樂趣。", "place": "陽明海洋文化藝術館", "is_nap": False, "cost": "約NT$100", "duration": "2 hrs", "age": "3歲+", "tips": ["🚢 互動體驗"]}
                ]}
            ]
        }
    },
    {
        "day": 4, "title": "基隆轉台北萬華 + 恐龍館", "hotel": "萬華",
        "options": {
            "sunny": [
                {"time": "09:30-10:30 (跨縣市轉移)", "activities": [
                    {"type": "⭐ 標準", "title": "包車輕鬆轉移", "desc": "推車又拿行李，建議直接包車前往台北酒店寄放行李，減少折騰。", "place": "禾順行旅", "is_nap": False, "cost": "~NT$1,000", "duration": "1 hr", "age": "全家", "tips": ["🚕 最推薦"]},
                    {"type": "🛍️ 輕鬆", "title": "台鐵慢慢搖", "desc": "行李少的話，可以搭乘台鐵區間車，寶貝可能會喜歡看火車。", "place": "基隆火車站", "is_nap": False, "cost": "NT$41/人", "duration": "1.5 hrs", "age": "全家", "tips": ["🚆 避開尖峰"]}
                ]},
                {"time": "13:00-14:30 (下午活動)", "activities": [
                    {"type": "⭐ 標準", "title": "土銀展示館(看恐龍)", "desc": "有巨大的恐龍骨架！室內平坦且冷氣強，非常適合推車與小童探索。", "place": "土銀展示館", "is_nap": False, "cost": "NT$30", "duration": "1.5 hrs", "age": "2歲+", "tips": ["🚸 推車極友善"]},
                    {"type": "🤩 活力", "title": "國立台灣博物館", "desc": "如果對恐龍沒興趣，去本館看動物標本和台灣原住民展覽。", "place": "國立台灣博物館", "is_nap": False, "cost": "NT$30", "duration": "1.5 hrs", "age": "全家", "tips": ["❄️ 冷氣強"]}
                ]},
                {"time": "17:30+ (晚餐時間)", "activities": [
                    {"type": "⭐ 標準", "title": "夜市早場晚餐", "desc": "傍晚出門去附近的夜市買點好吃的，早點回房休息。", "place": "艋舺夜市", "is_nap": False, "cost": "約NT$300", "duration": "1.5 hrs", "age": "全家", "tips": ["🚶 距離近"]},
                    {"type": "😴 休息", "title": "西門町室內晚餐", "desc": "想要坐得舒服點，就搭的士去西門町找間餐廳吃飯。", "place": "西門町", "is_nap": False, "cost": "約NT$600", "duration": "1.5 hrs", "age": "全家", "tips": ["❄️ 選擇多"]}
                ]}
            ],
            "rainy": [
                {"time": "11:30-14:30 (雨天備案)", "activities": [
                    {"type": "🌧️ 室內", "title": "台北地下街散步", "desc": "外面下雨就別去恐龍館了，在台北車站地下街吃飯、扭蛋，全室內。", "place": "台北地下街", "is_nap": False, "cost": "依消費", "duration": "3 hrs", "age": "全家", "tips": ["❄️ 全室內"]}
                ]}
            ]
        }
    },
    {
        "day": 5, "title": "兒童新樂園 + 科教館", "hotel": "萬華",
        "options": {
            "sunny": [
                {"time": "09:30-12:00 (上午主活動)", "activities": [
                    {"type": "⭐ 標準", "title": "兒童新樂園", "desc": "專為幼童設計的樂園！玩旋轉木馬，或在有遮蔭的沙坑區安靜玩耍。", "place": "台北兒童新樂園", "is_nap": False, "cost": "門票NT$30", "duration": "2.5 hrs", "age": "2-6歲", "tips": ["🎠 幼童設施多"]},
                    {"type": "🤩 活力", "title": "木柵動物園 (較曬)", "desc": "如果寶貝極度熱愛動物，可改去動物園，但記得做好防曬準備。", "place": "台北市立動物園", "is_nap": False, "cost": "NT$60", "duration": "3 hrs", "age": "全家", "tips": ["🧴 需嚴格防曬"]}
                ]},
                {"time": "13:30-15:00 (下午活動)", "activities": [
                    {"type": "⭐ 標準", "title": "科教館探索館", "desc": "走過對面就是科教館！有大型軟積木和攀爬網，大人可沙發休息。", "place": "國立臺灣科學教育館", "is_nap": False, "cost": "依展區收費", "duration": "1.5 hrs", "age": "3歲+", "tips": ["❄️ 室內冷氣"]},
                    {"type": "🤩 活力", "title": "天文館看星星", "desc": "如果喜歡太空，就去隔壁的天文館坐探險車。", "place": "台北市立天文館", "is_nap": False, "cost": "NT$40起", "duration": "1.5 hrs", "age": "3歲+", "tips": ["🚀 探險體驗"]}
                ]}
            ],
            "rainy": [
                {"time": "09:30-15:00 (雨天備案)", "activities": [
                    {"type": "🌧️ 室內", "title": "科教館全日室內", "desc": "下雨就放棄戶外樂園，直接在科教館待一整天，互動展區超豐富。", "place": "國立臺灣科學教育館", "is_nap": False, "cost": "約NT$200", "duration": "4-5 hrs", "age": "全家", "tips": ["❄️ 最佳避雨點"]}
                ]}
            ]
        }
    },
    {
        "day": 6, "title": "天文館 + 淡水", "hotel": "萬華",
        "options": {
            "sunny": [
                {"time": "09:30-12:30 (上午活動)", "activities": [
                    {"type": "⭐ 標準", "title": "天文館宇宙探險", "desc": "去坐室內軌道車！像溫和的機動遊戲，孩子覺得新鮮，大人也能涼快。", "place": "台北市立天文科學教育館", "is_nap": False, "cost": "成人NT$40起", "duration": "3 hrs", "age": "3歲+", "tips": ["🚸 推車友善"]},
                    {"type": "🤩 活力", "title": "補玩兒童新樂園", "desc": "如果 Day 5 沒去樂園，可以利用這個早上補去玩。", "place": "台北兒童新樂園", "is_nap": False, "cost": "依設施", "duration": "3 hrs", "age": "2-6歲", "tips": ["🎠 把握早晨"]}
                ]},
                {"time": "13:30-15:00 (午後補眠)", "activities": [
                    {"type": "😴 休息", "title": "🚇 搭捷運順便補眠", "desc": "搭捷運紅線直達淡水。在搖晃的冷氣車廂中讓寶貝安穩睡午覺！", "place": "捷運淡水線", "is_nap": True, "cost": "約NT$50", "duration": "1.5 hrs", "age": "全家", "tips": ["❄️ 冷氣車廂"]},
                    {"type": "🛍️ 輕鬆", "title": "轉移至美麗華", "desc": "不想跑太遠，就轉移到大直美麗華商場室內吹冷氣逛街。", "place": "美麗華百樂園", "is_nap": False, "cost": "免費", "duration": "1.5 hrs", "age": "全家", "tips": ["🛒 舒適好行"]}
                ]},
                {"time": "15:00-17:00 (黃昏散步)", "activities": [
                    {"type": "⭐ 標準", "title": "淡水河畔散步", "desc": "選擇寬闊的河邊平路推車散步，吹吹海風，還能搭渡輪去漁人碼頭。", "place": "淡水老街", "is_nap": False, "cost": "船票依規定", "duration": "2 hrs", "age": "全家", "tips": ["避開擁擠老街"]},
                    {"type": "🤩 活力", "title": "美麗華搭摩天輪", "desc": "如果選了商場備案，傍晚帶寶貝去坐摩天輪看市區風景。", "place": "美麗華摩天輪", "is_nap": False, "cost": "NT$150/人", "duration": "1 hr", "age": "全家", "tips": ["🎡 景色優美"]}
                ]}
            ],
            "rainy": [
                {"time": "15:00+ (雨天備案)", "activities": [
                    {"type": "🌧️ 室內", "title": "禮萊廣場室內備案", "desc": "如果淡水下雨，直接轉往全冷氣的室內廣場玩兒童球池，不看夕陽也開心。", "place": "滬尾藝文休閒園區", "is_nap": False, "cost": "依消費", "duration": "2-3 hrs", "age": "2-6歲", "tips": ["❄️ 避雨放電"]}
                ]}
            ]
        }
    },
    {
        "day": 7, "title": "萬華親子館 / 青年公園 + 機場", "hotel": "回程 ✈️",
        "options": {
            "sunny": [
                {"time": "09:15-12:00 (最後放電)", "activities": [
                    {"type": "⭐ 標準", "title": "萬華親子館", "desc": "趁早上還不熱玩戶外小車，變熱後立刻轉入室內冷氣區玩玩具！", "place": "萬華親子館", "is_nap": False, "cost": "免費", "duration": "2.5 hrs", "age": "2-6歲", "tips": ["🧦 必備襪子"]},
                    {"type": "🤩 活力", "title": "青年公園放電", "desc": "親子館沒預約到，就直接去旁邊的青年公園跑跳、溜滑梯。", "place": "青年公園", "is_nap": False, "cost": "免費", "duration": "2 hrs", "age": "全家", "tips": ["🌳 戶外空間"]}
                ]},
                {"time": "13:30-14:15 (前往機場)", "activities": [
                    {"type": "😴 休息", "title": "包車前往機場", "desc": "強烈建議包車直達！讓玩累的寶貝在車上深層補眠，免除搬行李痛苦。", "place": "桃園機場", "is_nap": True, "cost": "~NT$1,200", "duration": "45 mins", "age": "全家", "tips": ["🚕 最讚選擇"]},
                    {"type": "🛍️ 輕鬆", "title": "搭機場捷運", "desc": "行李不多的話，搭的士去台北車站換機捷直達機場。", "place": "機場捷運台北車站", "is_nap": False, "cost": "NT$160/人", "duration": "1 hr", "age": "全家", "tips": ["🚆 注意轉乘"]}
                ]},
                {"time": "14:30-17:00 (登機準備)", "activities": [
                    {"type": "⭐ 標準", "title": "機場兒童區放電", "desc": "慢慢辦理登機，有時間讓孩子在機場免費遊戲區做最後放電。", "place": "桃園機場第一航廈", "is_nap": False, "cost": "免費", "duration": "2.5 hrs", "age": "全家", "tips": ["🚼 設施齊全"]},
                    {"type": "🛍️ 輕鬆", "title": "免稅店與美食街", "desc": "大人做最後採買，順便在機場吃飽再上飛機。", "place": "桃園機場免稅店", "is_nap": False, "cost": "依消費", "duration": "2 hrs", "age": "大人", "tips": ["🛍️ 買伴手禮"]}
                ]}
            ],
            "rainy": [
                {"time": "09:15-12:00 (雨天備案)", "activities": [
                    {"type": "🌧️ 室內", "title": "台北地下街買手信", "desc": "下雨取消戶外活動，改到台北車站地下街散步、買伴手禮，全室內不用撐傘。", "place": "台北地下街", "is_nap": False, "cost": "依消費", "duration": "2.5 hrs", "age": "全家", "tips": ["🛍️ 室內避雨"]}
                ]}
            ]
        }
    }
]

CHECKLIST = [
    "🧦 襪子 (室內遊戲室必穿)",
    "🌧️ BB 車防雨罩 + 輕便雨傘",
    "🧴 防曬乳 + 遮陽帽 + 小風扇",
    "👕 兩套後備衣物 + 濕紙巾",
    "🥤 零食及保溫水樽",
    "🛂 全家護照正本"
]

# ==========================================
# 2. UI 元件與邏輯
# ==========================================
@ui.page('/')
def build_ui():
    ui.add_head_html('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">')
    ui.query('body').classes('bg-slate-200 m-0 p-0 overflow-x-hidden')

    state = {
        'weather': app.storage.user.get('weather', 'sunny')
    }

    with ui.column().classes('w-full max-w-[500px] mx-auto min-h-screen bg-slate-50 shadow-2xl relative pb-28 pt-6 px-4'):
        
        # === 頂部列：標題 & 收納工具按鈕 ===
        with ui.row().classes('w-full items-center justify-between mb-4'):
            with ui.column().classes('gap-0'):
                ui.label('💕 寶貝行程神隊友').classes('text-[22px] font-black text-slate-800 tracking-wider')
                ui.label('彈性調整 ⚡ 輕鬆陪伴 ❄️ 快樂回憶').classes('text-[12px] text-slate-500 font-bold mt-1')
            
            with ui.dialog() as dialog, ui.card().classes('w-full max-w-sm rounded-3xl p-6'):
                dialog_title = ui.label().classes('text-xl font-bold text-slate-800 border-b border-slate-100 pb-3 mb-3 w-full')
                dialog_desc = ui.label().classes('text-sm text-slate-600 mb-5 leading-relaxed')
                ui.label('👨‍👩‍👧 父母實用工具').classes('text-sm font-bold text-slate-400 mb-2 tracking-wide')
                
                with ui.row().classes('w-full gap-3 mb-4'):
                    map_btn = ui.button('📍 Google Maps', icon='map').classes('flex-grow bg-blue-50 text-blue-600 rounded-xl shadow-none text-[13px] font-bold py-2')
                    uber_btn = ui.button('🚗 叫 Uber', icon='local_taxi').classes('flex-grow bg-black text-white rounded-xl shadow-md text-[13px] font-bold py-2')
                
                ui.button('關閉', on_click=dialog.close).classes('w-full mt-2 bg-slate-200 text-slate-800 rounded-xl font-bold py-2 shadow-sm text-[14px]')

            def show_info(name, desc):
                dialog_title.set_text(name)
                dialog_desc.set_text(desc)
                map_btn.on_click(lambda: ui.navigate.to(f"https://www.google.com/maps/search/?api=1&query={name}", new_tab=True))
                uber_btn.on_click(lambda: ui.navigate.to("https://m.uber.com/ul/?action=setPickup&pickup=my_location", new_tab=True))
                dialog.open()

            ui.button(icon='build', on_click=lambda: show_info("目前位置", "點擊下方按鈕開啟地圖或叫車")).classes('bg-slate-100 text-slate-600 shadow-none px-3 py-2 rounded-full hover:bg-slate-200 transition-colors')

        # === 核心視覺：專屬每日行程 ===
        ui.label('📅 專屬每日行程').classes('text-[20px] font-black text-slate-800 mt-2 mb-4 tracking-widest pl-2 border-l-[5px] border-amber-400')

        for day_data in ITINERARY:
            is_first_day = (day_data["day"] == 1)
            with ui.expansion(f'Day {day_data["day"]}｜{day_data["title"]}', icon='event', value=is_first_day).classes('w-full bg-white rounded-2xl shadow-sm mb-4 font-black text-slate-800 border border-slate-100 text-[16px]').props('group="itinerary"'):
                ui.label(f'宿: {day_data["hotel"]}').classes('bg-amber-400 text-white text-[11px] px-2 py-0.5 rounded-md absolute right-10 top-4 shadow-sm tracking-wide')
                
                # 晴天行程容器 (動態綁定)
                with ui.column().classes('w-full bg-transparent p-0 mt-2').bind_visibility_from(state, 'weather', backward=lambda w: w == 'sunny'):
                    time_slots = day_data["options"].get('sunny', [])
                    for slot in time_slots:
                        ui.label(slot['time']).classes('text-[15px] font-black text-slate-500 mt-4 mb-1 border-b-2 border-slate-100 pb-1 w-full tracking-wider')
                        
                        is_multi = len(slot['activities']) > 1
                        
                        # [友善優化] 若有多個選項，加入橫向滑動提示
                        if is_multi:
                            ui.label('👉 左右滑動查看不同方案').classes('text-[11px] text-amber-600/70 font-bold mb-1 ml-1')

                        container_classes = 'w-full flex flex-nowrap overflow-x-auto snap-x snap-mandatory pb-4 gap-3 -mx-1 px-1' if is_multi else 'w-full flex flex-col gap-3'
                        
                        with ui.row().classes(container_classes):
                            for idx, event in enumerate(slot['activities']):
                                bg_color = 'bg-purple-50/80' if event.get('is_nap') else 'bg-white'
                                border_color = 'border-purple-400' if event.get('is_nap') else ('border-amber-400' if idx == 0 else 'border-emerald-400')
                                
                                # 動態決定 Tag 的顏色
                                badge_bg = 'bg-slate-400'
                                if '⭐' in event.get('type', ''): badge_bg = 'bg-amber-500'
                                elif '🤩' in event.get('type', ''): badge_bg = 'bg-orange-500'
                                elif '😴' in event.get('type', ''): badge_bg = 'bg-purple-400'
                                elif '🛍️' in event.get('type', ''): badge_bg = 'bg-emerald-500'
                                elif '🌧️' in event.get('type', ''): badge_bg = 'bg-blue-500'
                                
                                card_width = 'min-w-[85%] snap-center shrink-0' if is_multi else 'w-full'
                                card_p = 'p-3 mb-2' if is_multi else 'p-4 mb-3'
                                title_sz = 'text-[15px]' if is_multi else 'text-[16px]'
                                
                                with ui.card().classes(f'{card_width} {bg_color} border-l-[6px] {border_color} shadow-sm {card_p} cursor-pointer hover:shadow-md hover:-translate-y-0.5 transition-all').on('click', lambda e=event: show_info(e['place'], e['desc'])):
                                    with ui.row().classes('w-full items-center justify-between mb-2'):
                                        with ui.row().classes('items-center gap-2'):
                                            if is_multi or event.get('type'):
                                                ui.label(event.get('type', f"方案 {chr(65+idx)}")).classes(f'text-white {badge_bg} px-2 py-0.5 rounded text-[11px] font-black tracking-widest shadow-sm')
                                            ui.label(event['title']).classes(f'font-black text-slate-800 {title_sz}')

                                    ui.label(event['desc']).classes('text-[14px] text-slate-600 font-medium leading-relaxed mb-1')
                                    
                                    # [友善優化] 點擊提示
                                    ui.label('👆 點擊查看地圖與詳情').classes('text-[10px] text-slate-400 w-full text-right mt-1 border-t border-slate-100/50 pt-1')

                # 雨天備案容器 (動態綁定)
                with ui.column().classes('w-full bg-transparent p-0 mt-2').bind_visibility_from(state, 'weather', backward=lambda w: w == 'rainy'):
                    time_slots = day_data["options"].get('rainy', day_data["options"].get('sunny', []))
                    
                    if 'rainy' in day_data['options']:
                        ui.label('🌧️ 已啟用【暴雨/高熱避險】專屬路線').classes('text-[14px] text-blue-700 bg-blue-50 p-3 rounded-lg mb-3 w-full font-bold border border-blue-100')
                    else:
                        ui.label('☀️ 本日為全室內行程，無懼風雨！').classes('text-[14px] text-orange-700 bg-orange-50 p-3 rounded-lg mb-3 w-full font-bold border border-orange-100')

                    for slot in time_slots:
                        ui.label(slot['time']).classes('text-[15px] font-black text-slate-500 mt-4 mb-1 border-b-2 border-slate-100 pb-1 w-full tracking-wider')
                        
                        is_multi = len(slot['activities']) > 1
                        
                        if is_multi:
                            ui.label('👉 左右滑動切換不同方案').classes('text-[11px] text-amber-600/70 font-bold mb-1 ml-1')
                            
                        container_classes = 'w-full flex flex-nowrap overflow-x-auto snap-x snap-mandatory pb-4 gap-3 -mx-1 px-1' if is_multi else 'w-full flex flex-col gap-3'
                        
                        with ui.row().classes(container_classes):
                            for idx, event in enumerate(slot['activities']):
                                bg_color = 'bg-purple-50/80' if event.get('is_nap') else 'bg-white'
                                border_color = 'border-purple-400' if event.get('is_nap') else 'border-blue-500'
                                badge_bg = 'bg-blue-500'
                                
                                card_width = 'min-w-[85%] snap-center shrink-0' if is_multi else 'w-full'
                                card_p = 'p-3 mb-2' if is_multi else 'p-4 mb-3'
                                title_sz = 'text-[15px]' if is_multi else 'text-[16px]'
                                
                                with ui.card().classes(f'{card_width} {bg_color} border-l-[6px] {border_color} shadow-sm {card_p} cursor-pointer hover:shadow-md hover:-translate-y-0.5 transition-all').on('click', lambda e=event: show_info(e['place'], e['desc'])):
                                    with ui.row().classes('w-full items-center justify-between mb-2'):
                                        with ui.row().classes('items-center gap-2'):
                                            if is_multi or event.get('type'):
                                                ui.label(event.get('type', f"方案 {chr(65+idx)}")).classes(f'text-white {badge_bg} px-2 py-0.5 rounded text-[11px] font-black tracking-widest shadow-sm')
                                            ui.label(event['title']).classes(f'font-black text-slate-800 {title_sz}')

                                    ui.label(event['desc']).classes('text-[14px] text-slate-600 font-medium leading-relaxed mb-1')
                                    ui.label('👆 點擊查看地圖與詳情').classes('text-[10px] text-slate-400 w-full text-right mt-1 border-t border-slate-100/50 pt-1')

    # ==========================================
    # 底部天氣切換導航 & 回到頂部按鈕
    # ==========================================
    btn_sunny = None
    btn_rainy = None

    def set_w(w):
        state['weather'] = w
        app.storage.user['weather'] = w
        if w == 'sunny':
            btn_sunny.classes(replace='flex-1 bg-amber-500 text-white font-black rounded-xl shadow-md py-3 text-[15px] tracking-widest transition-all')
            btn_rainy.classes(replace='flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[15px] tracking-widest transition-all')
        else:
            btn_sunny.classes(replace='flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[15px] tracking-widest transition-all')
            btn_rainy.classes(replace='flex-1 bg-blue-500 text-white font-black rounded-xl shadow-md py-3 text-[15px] tracking-widest transition-all')

    # [友善優化] 回到頂端按鈕
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=100):
        ui.button(icon='arrow_upward', on_click=lambda: ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"})')).classes('bg-slate-800/60 hover:bg-slate-800 text-white rounded-full shadow-md backdrop-blur-sm transition-all').props('padding="12px"')

    with ui.row().classes('fixed bottom-6 left-1/2 -translate-x-1/2 w-[calc(100%-2rem)] max-w-[468px] bg-white/90 backdrop-blur-xl shadow-[0_8px_30px_rgba(0,0,0,0.12)] p-2 flex justify-center gap-2 z-50 rounded-2xl border border-slate-200/50'):
        init_sun_cls = 'flex-1 bg-amber-500 text-white font-black rounded-xl shadow-md py-3 text-[15px] tracking-widest transition-all' if state['weather'] == 'sunny' else 'flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[15px] tracking-widest transition-all'
        init_rain_cls = 'flex-1 bg-blue-500 text-white font-black rounded-xl shadow-md py-3 text-[15px] tracking-widest transition-all' if state['weather'] == 'rainy' else 'flex-1 bg-slate-100 text-slate-400 font-bold rounded-xl shadow-none py-3 text-[15px] tracking-widest transition-all'
        
        btn_sunny = ui.button('☀ 晴朗/預設', on_click=lambda: set_w('sunny')).classes(init_sun_cls)
        btn_rainy = ui.button('🌧 雷雨/太熱', on_click=lambda: set_w('rainy')).classes(init_rain_cls)

# ==========================================
# 3. 啟動伺服器
# ==========================================
PORT = int(os.environ.get('PORT', 8080))

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="寶貝行程神隊友", port=PORT, host='0.0.0.0', storage_secret='my_super_secret_key_123', show=False)