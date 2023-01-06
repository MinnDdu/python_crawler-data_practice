# Selenium 사용시 조금더 다이나믹 하고 어려운 사이트들도 크롤링 가능하게 해줌 (기존 requests로는 한계가 있음)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# 파이썬으로 웹 띄우기 - 크롬
driver = webdriver.Chrome('/Users/minsoo/Desktop/Coding Apple/PythonCrawler/Instagram_bot/chromedriver')

# 원하는 url 접속 
driver.get('http://instagram.com')
# driver 에 url에 담긴 모든 글/그림 정보가 담겨있음
driver.implicitly_wait(5) # driver가 알아서 기다려줌 (최대 10초)



# 흔한 selenium 에러 - no such element -> 페이지 로딩 시간 때문에 자주 발생
# time.sleep(n) 이용해서 로딩시간 n초 기다렸다가 크롤링하기
time.sleep(6) # 웹페이지 띄우고 10초간 코드 실행 멈춤 (로딩 시간 기다리기)
# driver.find_element_by_css_selector('.class명')
# driver.find_element_by_css_selector('#id명')
# driver.find_element_by_css_selector('태그명[속성이름="속성명"]') ex) ('input[name="username"]')
# 클래스명으로 찾는데 클래스 명이 띄어쓰기로 여러개? -> 클래스가 여러개인것 -> 그 중 하나로 검색
# e = driver.find_element_by_css_selector('.x1lliihq') -> html 다 가져옴

e = driver.find_element_by_css_selector('.x1lliihq').text # -> 태그안의 텍스트 영역만 가져옴
print(e)
# 인스타그램 자동로그인

name = driver.find_element_by_css_selector('input[name="username"]')
password = driver.find_element_by_css_selector('input[name="password"]')
# time.sleep(1)
name.send_keys('01037342988') # 파라미터를 name에 보내줌
password.send_keys('Irlaalstn12!')
# name.send_keys(Keys.ENTER) # 파라미터 안에 Keys.sth -> sth이 키보드 타자 의미 Keys.ENTER -> 키보드로 엔터 눌러줌
# time.sleep(1)
login = driver.find_element_by_css_selector('._acan._aiit._acap')
login.click()
# login.click() # login 이라는 요소룰 클릭함
time.sleep(5)



# chap 3 ~ 4 인스타 사진 자동저장
# 1. 로그인 후 검색 페이지 이동 (그냥 검색 url로 이동하는게 편함)
# 2. 첫사진 클릭 후 사진 저장 -> 다음 사진 이동 버튼 클릭 (검색 결과후 바로 나오는 창은 무한 스크롤이라 귀찮음) -> 반복
driver.get('https://www.instagram.com/explore/tags/%EA%B0%95%EC%95%84%EC%A7%80/') # 페이지 이동
driver.implicitly_wait(10) # driver가 알아서 기다려줌 (최대 10초)
time.sleep(5)
pic = driver.find_elements_by_css_selector('.x1i10hfl')[10].click()
# 클래스로 찾을때 dev tool 창에서 그 클래스를 검색해보는 것은 좋은 습관 -> 이 클래스를 가진 태그가 몇개인지 파악 가능 -> find_element's'_css_selector ?

img = driver.find_element_by_css_selector('.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3').get_attribute('src')
print(img)
urllib.request.urlretrieve(img, '1.jpg')