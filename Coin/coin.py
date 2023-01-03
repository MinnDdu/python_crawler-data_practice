import requests
import json
import time
from bs4 import BeautifulSoup

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinone&type=1h')

soup = BeautifulSoup(data.text, 'html.parser')

# JSON 자료형을 Dictionary 자료형으로 바꿔줌 -> 파이썬에서 조작 용이해짐
dict = json.loads(data.content)


# DT (date time) - epoch / UNIX 시간 -> 10자리 (1970년 1월 1일 이후로 몇초가 지났나), 
# 13자리 일시 뒤에 000은 밀리세컨드를 위해서
for i in range(200):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(dict['data'][i]['DT']/1000)) + ": " + dict['data'][i]['Close'])



