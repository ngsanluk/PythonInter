import requests
from bs4 import BeautifulSoup

url = "https://stock360.hkej.com/marketWatch/Top20/topGainers"
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

# print(soup.prettify())
top_stocks = soup.find(class_='dt640')
stocks = top_stocks.find_all("tr")
print(len(stocks))
for i in range(2, len(stocks)):
    stock = stocks[i]
    code = stock.find(class_='code')
    name = stock.find(class_='name')
    latest = stock.find(class_='latest')
    change = stock.find(class_='change')
    change_p = stock.find(class_='change_p')
    volumn = stock.find(class_='volumn')
    turnover = stock.find(class_='turnover')
    market_cap = stock.find(class_='marketCap')
    print(i-2, "\t", code.string.strip(), '\t', name.string.strip().ljust(30, ' '), '\t', latest.string, '\t', change_p.string)

# for link in soup.find_all('a'):
#     print(link.get('href'))
