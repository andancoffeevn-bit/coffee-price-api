import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://giacaphe.com/gia-ca-phe-trong-nuoc/"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Tìm phần tử có id="0"
target = soup.find('tr', {'id': '0'})

if target:
    data_json = target.get('data-prev')
    # Ghi file
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(data_json)
    print("Đã tạo file data.json thành công")
else:
    print("Không tìm thấy dữ liệu!")
    exit(1) # Báo lỗi nếu không thấy dữ liệu
