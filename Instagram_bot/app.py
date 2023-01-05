# Selenium 사용시 조금더 다이나믹 하고 어려운 사이트들도 크롤링 가능하게 해줌 (기존 requests로는 한계가 있음)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 파이썬으로 웹 띄우기 - 크롬
driver = webdriver.Chrome('/Users/minsoo/Desktop/Coding Apple/PythonCrawler/Instagram_bot/chromedriver')

# 원하는 url 접속 
driver.get('http://instagram.com')
# driver 에 url에 담긴 모든 글/그림 정보가 담겨있음

time.sleep(10) # 웹페이지 띄우고 10초간 코드 실행 멈춤 (로딩 시간 기다리기)
# e = driver.find_element_by_css_selector('.x1lliihq') -> html 다 가져옴
e = driver.find_element_by_css_selector('.x1lliihq').text # -> 태그안의 텍스트 영역만 가져옴

# driver.find_element_by_css_selector('.class명')
# driver.find_element_by_css_selector('#id명')
# driver.find_element_by_css_selector('태그명[속성이름="속성명"]')

print(e)

# 흔한 selenium 에러 - no such element -> 페이지 로딩 시간 때문에 자주 발생
# time.sleep(n) 이용해서 로딩시간 n초 기다렸다가 크롤링하기