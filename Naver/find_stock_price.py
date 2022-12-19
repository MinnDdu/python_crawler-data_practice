import requests
from bs4 import BeautifulSoup


categories = ['005930', '066575', '005380', '035720', '034220', '003490']

def print_price(code):
    # src = 'https://finance.naver.com/item/sise.naver?code={}'.format(code)
    src = f'https://finance.naver.com/item/sise.naver?code={code}'
    data = requests.get(src)
    soup = BeautifulSoup(data.content, 'html.parser')
    companyName = soup.select('.wrap_company a')[0].text
    currentPrice = soup.select('#_nowVal')[0].text
    transactionQuantity = soup.select('#_quant')[0].text
    print('name of company is ' + companyName)
    print('current price is ' + currentPrice)
    print('transaction quantity is ' + transactionQuantity)
    return companyName + ": " + currentPrice + " / " + transactionQuantity

# print_price('005930')
# print_price('066575')

f = open('a.txt', 'w')
for i in range(len(categories)):
    f.write(print_price(categories[i]) + "\n")

f.close()
