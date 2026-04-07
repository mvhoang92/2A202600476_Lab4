from langchain_core.tools import tool
from typing import Optional

# --- MOCK DATA ---
FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1450000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2800000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1200000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1350000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1100000, "class": "economy"},
    ],
    ("TP.HCM", "Hà Nội"): [
        {"airline": "Vietnam Airlines", "departure": "05:00", "arrival": "07:10", "price": 1850000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "09:30", "arrival": "11:40", "price": 950000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "13:00", "arrival": "15:10", "price": 1300000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3500000, "class": "business"},
    ],
    ("TP.HCM", "Đà Lạt"): [
        {"airline": "VietJet Air", "departure": "07:15", "arrival": "08:05", "price": 650000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "11:30", "arrival": "12:30", "price": 1150000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "17:45", "arrival": "18:35", "price": 580000, "class": "economy"},
    ],
    ("Đà Nẵng", "TP.HCM"): [
        {"airline": "Bamboo Airways", "departure": "08:20", "arrival": "09:45", "price": 1050000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "15:10", "arrival": "16:40", "price": 2200000, "class": "business"},
        {"airline": "VietJet Air", "departure": "21:00", "arrival": "22:25", "price": 720000, "class": "economy"},
    ],
    ("Hà Nội", "Nha Trang"): [
        {"airline": "Vietnam Airlines", "departure": "06:30", "arrival": "08:20", "price": 1950000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "12:45", "arrival": "14:35", "price": 1250000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "19:15", "arrival": "21:05", "price": 1500000, "class": "economy"},
    ]
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1800000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1200000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250000, "area": "Hải Châu", "rating": 4.6},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3500000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1500000, "area": "Bãi Trường", "rating": 4.2},
    ],
    "Hà Nội": [
        {"name": "Sofitel Legend Metropole", "stars": 5, "price_per_night": 6500000, "area": "Hoàn Kiếm", "rating": 4.9},
        {"name": "La Siesta Classic", "stars": 4, "price_per_night": 1800000, "area": "Mã Mây", "rating": 4.6},
    ],
    "TP.HCM": [
        {"name": "The Reverie Saigon", "stars": 5, "price_per_night": 7200000, "area": "Quận 1", "rating": 4.8},
        {"name": "Common Inn", "stars": 2, "price_per_night": 550000, "area": "Thảo Điền", "rating": 4.5},
    ],
    "Đà Lạt": [
        {"name": "Ana Mandara Villas", "stars": 5, "price_per_night": 2800000, "area": "Phường 5", "rating": 4.6},
        {"name": "The Kupid Homestay", "stars": 2, "price_per_night": 400000, "area": "Đặng Thái Thân", "rating": 4.7},
    ],
    "Nha Trang": [
        {"name": "Amiana Resort", "stars": 5, "price_per_night": 4200000, "area": "Vĩnh Hòa", "rating": 4.8},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1100000, "area": "Lộc Thọ", "rating": 4.4},
    ]
}

# --- UTILS ---

def format_vn_currency(amount: int) -> str:
    return "{:,.0f}đ".format(amount).replace(",", ".")

def normalize_city_name(city: str) -> str:
    city_lower = city.lower().strip()
    mapping = {
        "hồ chí minh": "TP.HCM", "hcm": "TP.HCM", "sài gòn": "TP.HCM", "saigon": "TP.HCM",
        "hà nội": "Hà Nội", "hn": "Hà Nội",
        "đà nẵng": "Đà Nẵng", "đn": "Đà Nẵng",
        "phú quốc": "Phú Quốc", "pq": "Phú Quốc",
        "nha trang": "Nha Trang", "nt": "Nha Trang",
        "đà lạt": "Đà Lạt", "dl": "Đà Lạt"
    }
    for key, value in mapping.items():
        if key in city_lower:
            return value
    return city.title()

# --- TOOLS ---

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm chuyến bay trực tiếp hoặc nối chuyến giữa hai thành phố.
    Tham số:
    - origin: Thành phố đi (ví dụ: Hà Nội, Sài Gòn).
    - destination: Thành phố đến (ví dụ: Đà Nẵng, Nha Trang).
    """
    org = normalize_city_name(origin)
    dest = normalize_city_name(destination)

    # 1. Tìm chuyến bay THẲNG
    direct_flights = FLIGHTS_DB.get((org, dest))
    if direct_flights:
        result = [f"✈️ Chuyến bay THẲNG từ {org} đến {dest}:"]
        for f in direct_flights:
            result.append(f"- {f['airline']} ({f['class']}): {f['departure']} -> {f['arrival']} | Giá: {format_vn_currency(f['price'])}")
        return "\n".join(result)

    # 2. Tìm chuyến bay NỐI CHUYẾN
    all_cities = set([c for route in FLIGHTS_DB.keys() for c in route])
    connecting_routes = []
    
    for transit in all_cities:
        if transit in [org, dest]: continue
        leg1 = FLIGHTS_DB.get((org, transit))
        leg2 = FLIGHTS_DB.get((transit, dest))
        
        if leg1 and leg2:
            for f1 in leg1:
                for f2 in leg2:
                    h1, m1 = map(int, f1['arrival'].split(':'))
                    h2, m2 = map(int, f2['departure'].split(':'))
                    t1_arr = h1 * 60 + m1
                    t2_dep = h2 * 60 + m2
                    
                    # Xử lý nối chuyến qua ngày nếu t2_dep < t1_arr
                    wait_time = t2_dep - t1_arr
                    if wait_time < 0: wait_time += 1440 
                    
                    if 60 <= wait_time <= 720: # Chờ từ 1h đến 12h
                        connecting_routes.append({
                            "transit": transit, "f1": f1, "f2": f2,
                            "total": f1['price'] + f2['price'], "wait": wait_time
                        })

    if connecting_routes:
        connecting_routes.sort(key=lambda x: x['total'])
        best = connecting_routes[0]
        return (f"Không có chuyến thẳng. Gợi ý nối chuyến qua {best['transit']}:\n"
                f"1. {best['f1']['airline']}: {org} ({best['f1']['departure']}) -> {best['transit']}\n"
                f"2. {best['f2']['airline']}: {best['transit']} ({best['f2']['departure']}) -> {dest}\n"
                f"💰 Tổng chi phí: {format_vn_currency(best['total'])} | ⏱️ Chờ: {best['wait']} phút")

    return f"Rất tiếc, TravelBuddy không tìm thấy đường bay nào từ {org} đến {dest}."

@tool
def search_hotels(city: str, max_price: Optional[int] = None) -> str:
    """
    Tìm khách sạn tại một thành phố.
    Tham số:
    - city: Tên thành phố.
    - max_price: Ngân sách tối đa mỗi đêm (VNĐ), ví dụ: 2000000.
    """
    normalized_city = normalize_city_name(city)
    hotels = HOTELS_DB.get(normalized_city)
    
    if not hotels:
        return f"Hiện tại chưa có dữ liệu khách sạn tại {normalized_city}."
    
    filtered = [h for h in hotels if max_price is None or h['price_per_night'] <= max_price]
    if not filtered:
        return f"Không có khách sạn nào tại {normalized_city} dưới {format_vn_currency(max_price or 0)}."
    
    filtered.sort(key=lambda x: x['rating'], reverse=True)
    res = [f"🏨 Khách sạn tại {normalized_city} (Theo đánh giá):"]
    for h in filtered:
        res.append(f"- {h['name']} ({'⭐'*h['stars']}) | {h['area']} | Giá: {format_vn_currency(h['price_per_night'])} | Đánh giá: {h['rating']}")
    return "\n".join(res)

@tool
def calculate_budget(total_budget: int, expenses_str: str) -> str:
    """
    Tính toán ngân sách còn lại.
    Tham số:
    - total_budget: Tổng ngân sách (số nguyên, ví dụ: 5000000).
    - expenses_str: Các khoản chi theo dạng 'tên:số_tiền, tên:số_tiền'.
    """
    try:
        total_expense = 0
        detail = []
        parts = expenses_str.split(',')
        for p in parts:
            if ':' not in p: continue
            name, amt = p.rsplit(':', 1)
            amt_val = int(amt.strip())
            total_expense += amt_val
            detail.append(f"- {name.strip().capitalize()}: {format_vn_currency(amt_val)}")
        
        remaining = total_budget - total_expense
        status = "✅ Ổn định" if remaining >= 0 else "⚠️ Vượt ngân sách!"
        
        return (f"📊 Báo cáo ngân sách ({status}):\n" + "\n".join(detail) + 
                f"\n---\nTổng chi: {format_vn_currency(total_expense)}\n"
                f"Còn lại: {format_vn_currency(remaining)}")
    except Exception:
        return "Lỗi: Vui lòng nhập chi phí theo định dạng 'tên:số_tiền, tên:số_tiền'."

if __name__ == "__main__":
    # Test thử
    print(search_flights.invoke({"origin": "Hà Nội", "destination": "Sài Gòn"}))