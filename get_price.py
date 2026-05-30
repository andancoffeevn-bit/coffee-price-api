import requests
from bs4 import BeautifulSoup
import json
import sys

def fetch_data():
    url = "https://giacaphe.com/gia-ca-phe-truc-tuyen/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Thay vì tìm theo id="robusta", ta tìm theo thuộc tính data-exchange
        table = soup.find('table', {'data-exchange': 'coffee_liffe'})
        
        if not table:
            # Nếu vẫn không thấy, in ra tất cả các bảng có data-exchange để debug
            print("Không thấy bảng với data-exchange='coffee_liffe'.")
            print("Các bảng tìm thấy:")
            for t in soup.find_all('table'):
                print(f"Bảng: {t.get('data-exchange')}, id: {t.get('id')}")
            sys.exit(1)
            
        all_data = []
        rows = table.find_all('tr', {'data-prev': True})
        
        for row in rows:
            raw_json = row.get('data-prev')
            all_data.append(json.loads(raw_json))
            
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)
        print("Thành công! Đã ghi file data.json.")
            
    except Exception as e:
        print(f"Lỗi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_data()
