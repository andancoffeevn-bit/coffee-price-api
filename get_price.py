import requests
from bs4 import BeautifulSoup
import json

def fetch_data():
    # Thay link bằng trang web thực tế bạn muốn lấy dữ liệu
    url = "https://giacaphe.com/gia-ca-phe-trong-nuoc/" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm thẻ tr có id="0" như bạn đã cung cấp
        target = soup.find('tr', {'id': '0'})
        if target:
            data_json = target.get('data-prev')
            # Lưu vào file data.json
            with open('data.json', 'w', encoding='utf-8') as f:
                f.write(data_json)
            print("Cập nhật dữ liệu thành công!")
        else:
            print("Không tìm thấy dữ liệu trên trang web.")
            
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    fetch_data()
