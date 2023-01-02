import requests
from bs4 import BeautifulSoup

def naver_blog_ranking(query, amount):
    src = f'https://s.search.naver.com/p/review/search.naver?rev=44&where=m_view&api_type=2&start=1&query={query}&nso=&nqx_theme=&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_jum&ssc=tab.m_view.view&ngn_country=KR&lgl_rcode=09410117&fgn_region=&fgn_city=&lgl_lat=37.5739083&lgl_long=126.9351754&abt=&_callback=jQuery22406394122066213355_1672652874251'
    data = requests.get(src)
    soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
    result = {}
    for i in range(amount):
        info = []
        piece = soup.select('.api_txt_lines.total_tit._cross_trigger')
        title = piece[i].text
        info.append(title)
        info.append(piece[i]['href'])
        result['Ranking ' + str(i+1)] = info



    return result

print(naver_blog_ranking('자낳대', 10))