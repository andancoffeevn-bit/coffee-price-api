import requests
import json

def fetch_data():
    # URL này bạn lấy từ tab Network khi nhấn vào request có tên giống như 'truc-tuyen'
    # URL dự đoán từ code của bạn:
    url = "https://giacaphe.com/wp-json/gia-ca-phe/v1/truc-tuyen/" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "X-Auth-Site": "giacaphe",  # BẮT BUỘC PHẢI CÓ DÒNG NÀY
        "Referer": "https://giacaphe.com/gia-ca-phe-truc-tuyen/"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() # Kiểm tra lỗi HTTP
        data = response.json()
        
        # Lưu toàn bộ dữ liệu (bạn có thể lọc theo key sau)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Đã lấy dữ liệu thành công!")
            
    except Exception as e:
        print(f"Lỗi kết nối: {e}")

if __name__ == "__main__":
    fetch_data()
