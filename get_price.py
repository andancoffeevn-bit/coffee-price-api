import requests
import json
import time

def fetch_data():
    url = "https://giacaphe.com/live-quotes/quotes-update-nOsjt.php?sid=&g=coffee"
    
    # Header này bắt chước trình duyệt thật mạnh mẽ hơn
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "X-Requested-With": "XMLHttpRequest",
        "X-Auth-Site": "giacaphe",
        "Referer": "https://giacaphe.com/gia-ca-phe-truc-tuyen/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    
    try:
        # Dùng session để duy trì cookie từ lần request đầu
        s = requests.Session()
        s.headers.update(headers)
        
        # Bước 1: Ghé thăm trang chủ trước (giống như user thật mở tab web)
        s.get("https://giacaphe.com/gia-ca-phe-truc-tuyen/", timeout=15)
        
        # Bước 2: Đợi 2 giây để giả lập thời gian load trang
        time.sleep(2)
        
        # Bước 3: Gọi API lấy giá
        response = s.get(url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("Lấy dữ liệu thành công!")
        else:
            print(f"Server từ chối, mã lỗi: {response.status_code}")
            print(f"Nội dung phản hồi: {response.text[:200]}")

    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    fetch_data()
