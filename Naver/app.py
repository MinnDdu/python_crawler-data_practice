import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

# print(data.content)
# print(data.status_code)

soup = BeautifulSoup(data.content, 'html.parser')
print(soup.find_all('strong', id='_nowVal')[0].text)
print(soup.find_all('strong', class_='red01')[0].text)
print(soup.find_all('em', class_='no_down')[0].text)

# select() (CSS selector로 찾기 (.class, #id))
# 내가 찾는 태그가 id, class 모두 없을때 -> 부모 태그로 넘어가기 -> selector 띄어쓰기
print(soup.select('.f_down em')) # .f_down 클래스 태그 안에 있는 em 태그 찾기

print(soup.select('#img_chart_area')[0]['src'])