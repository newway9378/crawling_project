
!pip install beautifulsoup4
!pip install requests

from google.colab import drive
drive.mount('/content/drive')
# %cd /content/drive/MyDrive/Crawling
!pwd
!ls

import requests
from bs4 import BeautifulSoup
import csv
import time

def to_eng():
  while True:
    keyword = input('스포츠, 사회, 정치, 문화, 경제 중 하나를 선택해주시오: ')
    if keyword == '스포츠':
      eng = 'sports'
      return eng
    elif keyword == '사회':
      eng = 'society'
      return eng
    elif keyword == '정치':
      eng = 'politics'
      return eng
    elif keyword == '문화':
      eng = 'culture'
      return eng
    elif keyword == '경제':
      eng = 'economy'
      return eng
    else:
      print('스포츠, 사회, 정치, 문화, 경제 중 하나를 입력해주시오.')
      continue

f = open("data.csv", "w", encoding='utf-8')
writer = csv.writer(f) 
data = [['한겨레', '중앙일보', '한국일보', '동아일보']]
writer.writerows(data)

eng = to_eng()

for i in data[0]:

  #한겨레 기사
  if i == '한겨레':

    한겨레 = []

    url = f'https://www.hani.co.kr/arti/{eng}/home01.html'
    response = requests.get(url)

    if response.status_code == 200:
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
      
      title = soup.find_all('h4', {'class': 'article-title'}, 'a')
      for item in title:
        한겨레.append(item.get_text().strip('\n'))

      print(한겨레)

    else:
      print('연결되지않음')
      print(response.status_code)

    time.sleep(2)



  #중앙일보 기사
  if i == '중앙일보':

    중앙일보 = []

    url = f'https://www.joongang.co.kr/{eng}'
    response = requests.get(url)

    if response.status_code == 200:
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
          
      
      title = soup.find_all('h2', {'class': 'headline'}, 'a')
      for item in title:
        중앙일보.append(item.get_text().replace('&apos', '').strip('\n'))

      print(중앙일보)

    else:
      print('연결되지않음')
      print(response.status_code)

    time.sleep(2)

  #한국일보 기사
  if i == '한국일보':
    eng = eng[0].upper() + eng[1::]

    한국일보 = []

    url = f'https://www.hankookilbo.com/{eng}'
    response = requests.get(url)

    if response.status_code == 200:
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
          
      
      title = soup.find_all('h4')
      for item in title:
        한국일보.append(item.get_text().strip('\n').replace('\'', '"'))

      print(한국일보)

    else:
      print('연결되지않음')
      print(response.status_code)

    time.sleep(2)



  #동아일보 기사
  if i == '동아일보':
    eng = eng[0].upper() + eng[1::]

    동아일보 = []

    url = f'https://www.donga.com/news/{eng}'
    response = requests.get(url)

    if response.status_code == 200:
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
          
      title = soup.find_all('span', {'class': 'tit'}, 'a')
      for item in title:
        동아일보.append(item.get_text().strip('\n'))

      동아일보.pop(0)
      print(동아일보)

    else:
      print('연결되지않음')
      print(response.status_code)

    time.sleep(2)

num = min(len(한겨레), len(중앙일보), len(한국일보), len(동아일보))

for i in range(num):
    row = [[한겨레[i], 중앙일보[i], 한국일보[i], 동아일보[i]]]
    writer.writerows(row)

f.close()
