import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=m_view&api_type=2&start=31&query=%EC%BD%94%ED%8A%B8&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22shopping_top%22%7D%2C%22sub%22%3A%5B%7B%22name%22%3A%22shopping%22%7D%5D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.m_view.view&ngn_country=KR&lgl_rcode=09410117&fgn_region=&fgn_city=&lgl_lat=37.5739083&lgl_long=126.9351754&abt=&_callback=jQuery224008183633387785272_1672650791480')

# print(data.content)

# 가끔 html class 나 id 에 '/' backslash가 있을 수 잇음 -> findall 이나 select로 못 찾음 -> replace() 로 백슬래쉬 제거
# data.content는 오브젝트 자료를 리턴해주기때문에 data.text를 사용해야 replace() 함수를 사용 가능!
soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')

a = soup.select('.api_txt_lines')

# 첫번째 글의 주소
print(a[0]['href'])