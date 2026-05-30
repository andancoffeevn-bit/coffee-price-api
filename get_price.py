import requests
from bs4 import BeautifulSoup
import json

def fetch_data():
    url = "https://giacaphe.com/gia-ca-phe-truc-tuyen/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm bảng có id="robusta"
        table = soup.find('table', {'id': 'robusta'})
        if not table:
            print("Không tìm thấy bảng id='robusta'")
            exit(1)
            
        all_data = []
        # Lấy tất cả các dòng có data-prev trong bảng này
        rows = table.find_all('tr', {'data-prev': True})
        
        for row in rows:
            # data-prev ở đây là một chuỗi JSON, ta giải mã nó
            raw_json = row.get('data-prev')
            all_data.append(json.loads(raw_json))
            
        # Lưu toàn bộ danh sách vào file data.json
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)
            
        print("Lấy dữ liệu thành công!")
            
    except Exception as e:
        print(f"Lỗi: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_data()
