import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
file = open("stock.csv", mode='w', encoding="utf-8", newline="")
writer = csv.writer(file)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

datelist = []
pricelist = []
pops = []
for page in range(2, 5):
    page_url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={page}'
    page_res = requests.get(page_url, headers=headers)
    page_bs = BeautifulSoup(page_res.text, 'html.parser')

    for data in page_bs.select("tr[onmouseover = 'mouseOver(this)']"):
        date = (data.select('td')[0].text)
        stock_price = (data.select('td')[1].text)

        if re.match('^2023.08', date):
            # print(date)
            datelist.append(date)
            pricelist.append(stock_price)

            pops.append(date)
            pops.append(stock_price)
# print(pops)
writer.writerow(['날짜', '종가'])
writer.writerow(pops)
file.close()

dataframe = {'날짜' : datelist, '종가' : pricelist}
df = pd.DataFrame(dataframe)
# print(df)

df.to_csv("stock(1).csv", encoding='utf-8-sig')
