import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
file = open("삼성전자8월주가.csv", mode='w', encoding="utf-8", newline="")
writer = csv.writer(file)

URL = 'https://finance.naver.com/item/sise_day.naver?code=005930'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# res = requests.get(URL, headers=headers)
# bs = BeautifulSoup(res.text, 'html.parser')

# print(res.text)

datelist = []
pricelist = []
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
# print(pricelist)

dataframe = {'날짜' : datelist, '종가' : pricelist}
df = pd.DataFrame(dataframe)
# print(df)
# 날짜 종가
# 일별 시세(8월 한달간)

writer.writerow(df)
file.close()
