from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 파이썬으로 웹 띄우기 - 크롬
driver = webdriver.Chrome('/Users/minsoo/Desktop/Coding Apple/PythonCrawler/Instagram_bot/chromedriver')

# 원하는 url 접속 
driver.get('http://instagram.com')

