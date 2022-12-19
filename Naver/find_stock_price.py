import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.naver?code=005930')

def print_price(data):
    soup = BeautifulSoup(data.content, 'html.parser')
    companyName = soup.select('.wrap_company a')[0].text
    currentPrice = soup.select('#_nowVal')[0].text
    transactionQuantity = soup.select('#_quant')[0].text
    print('name of company is ' + companyName)
    print('current price is ' + currentPrice)
    print('transaction quantity is ' + transactionQuantity)

print_price(data)
