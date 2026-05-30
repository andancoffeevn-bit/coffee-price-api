import requests
import json
import time

def fetch_data():
    url = "https://giacaphe.com/live-quotes/quotes-update-nOsjt.php?sid=&g=coffee"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": "https://giacaphe.com/gia-ca-phe-truc-tuyen/",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    try:
        s = requests.Session()
        s.headers.update(headers)
        s.get("https://giacaphe.com/gia-ca-phe-truc-tuyen/", timeout=15)
        time.sleep(2)
        response = s.get(url, timeout=15)
        
        if response.status_code == 200:
            full_data = response.json()
            
            # Lọc dữ liệu: Chỉ lấy kỳ hạn đầu tiên (thường là giá gần nhất)
            # Robusta là RMN26, Arabica là KCN26 (theo ví dụ bạn gửi)
            filtered_data = {
                "robusta": full_data["coffee_liffe"][0],
                "arabica": full_data["coffee_ice"][0],
                "updated": full_data["updated"]
            }
            
            # Lưu file gọn gàng
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(filtered_data, f, ensure_ascii=False, indent=4)
            print("Đã lưu dữ liệu Robusta & Arabica thành công!")
            
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    fetch_data()
