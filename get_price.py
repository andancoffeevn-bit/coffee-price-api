import requests
from bs4 import BeautifulSoup
import json

def fetch_data():
    url = "https://giacaphe.com/gia-ca-phe-trong-nuoc/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm hàng có chứa "data-prev" bất kể id là gì
        # Đây là cách cào an toàn nhất
        all_rows = soup.find_all('tr')
        found = False
        
        for row in all_rows:
            if row.has_attr('data-prev'):
                data_json = row.get('data-prev')
                with open('data.json', 'w', encoding='utf-8') as f:
                    f.write(data_json)
                print("Tìm thấy dữ liệu và đã lưu vào data.json!")
                found = True
                break
        
        if not found:
            print("Không tìm thấy hàng nào có chứa dữ liệu giá!")
            exit(1) # Lỗi code 1 nếu không thấy dữ liệu
            
    except Exception as e:
        print(f"Lỗi: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_data()
