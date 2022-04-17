import requests
from bs4 import BeautifulSoup

url = "https://stock360.hkej.com/marketWatch/Top20/topGainers"
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
webpage_request = requests.get(url, headers)
soup = BeautifulSoup(webpage_request.content, 'html.parser')

# print(soup.prettify())
top_stocks_table = soup.find(class_='dt640')
stock_rows = top_stocks_table.find_all("tr")
# print(len(stock_rows))
for i in range(2, len(stock_rows)):
    stock = stock_rows[i]
    code = stock.find(class_='code')
    name = stock.find(class_='name')
    latest = stock.find(class_='latest')
    change = stock.find(class_='change')
    change_p = stock.find(class_='change_p')
    volumn = stock.find(class_='volumn')
    turnover = stock.find(class_='turnover')
    market_cap = stock.find(class_='marketCap')
    print(i-1, "\t", code.string.strip(), '\t', name.string.strip().ljust(15, ' '), '\t', latest.string.ljust(8, ' '),  change_p.string+"%")

# for link in soup.find_all('a'):
#     print(link.get('href'))
