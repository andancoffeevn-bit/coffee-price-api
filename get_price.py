import requests
from bs4 import BeautifulSoup
import json

def fetch_data():
    url = "https://giacaphe.com/gia-ca-phe-trong-nuoc/"
    # Thêm headers giả lập trình duyệt thật
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Kiểm tra lỗi mạng
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm tất cả các hàng, thay vì chỉ dựa vào id="0"
        # Đôi khi trang web đổi id, ta sẽ tìm theo cách an toàn hơn
        target = soup.find('tr', {'data-prev': True}) 
        
        if target:
            data_json = target.get('data-prev')
            with open('data.json', 'w', encoding='utf-8') as f:
                f.write(data_json)
            print("Đã tạo file data.json thành công!")
        else:
            print("Không tìm thấy dữ liệu! Kiểm tra lại cấu trúc web.")
            # In ra một chút nội dung HTML để debug nếu cần
            # print(soup.prettify()[:500]) 
            exit(1) # Dừng lại nếu không thấy dữ liệu
            
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_data()
