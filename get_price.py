import requests
import json
import os
import firebase_admin
from firebase_admin import credentials, db

# 1. Cấu hình Firebase
# Lấy key từ GitHub Secret mà bạn đã đặt tên là FIREBASE_KEY
key_dict = json.loads(os.environ['FIREBASE_KEY'])
cred = credentials.Certificate(key_dict)

# Khởi tạo Firebase với Database URL của bạn
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://coffee-price-api-default-rtdb.firebaseio.com/'
})

def fetch_and_update():
    url = "https://giacaphe.com/live-quotes/quotes-update-nOsjt.php?sid=&g=coffee"
    # Header để giả lập trình duyệt, giúp vượt qua lớp bảo vệ của trang gốc
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": "https://giacaphe.com/gia-ca-phe-truc-tuyen/",
        "X-Requested-With": "XMLHttpRequest",
        "X-Auth-Site": "giacaphe"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            full_data = response.json()
            
            # Lọc dữ liệu: Chỉ lấy kỳ hạn đầu tiên (thường là giá gần nhất)
            # Dữ liệu từ giacaphe.com trả về danh sách, ta lấy index [0]
            filtered_data = {
                "robusta": full_data["coffee_liffe"][0],
                "arabica": full_data["coffee_ice"][0],
                "updated": full_data["updated"]
            }
            
            # Đẩy dữ liệu đã lọc lên Firebase tại node 'coffee_prices'
            ref = db.reference('coffee_prices')
            ref.set(filtered_data)
            print("Đã cập nhật lên Firebase thành công!")
            
        else:
            print(f"Lỗi khi lấy dữ liệu từ giacaphe.com, mã lỗi: {response.status_code}")
            
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    fetch_and_update()
