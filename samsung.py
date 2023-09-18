import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

URL = 'https://news.naver.com/main/list.naver'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


page= 100

for date in range(20230801, 20230832):
     
    while True:
        params = {
            'mode' : 'LPOD'
            ,'mid' : 'sec'
            ,'oid' : '001'
            ,'date' : str(date)
            ,'page' : str(page) 
        }
        res = requests.get(URL, headers=headers, params=params)
        bs = BeautifulSoup(res.text, 'html.parser')

    # 해당 페이지
        now_page = (int(bs.select_one('div.paging strong').text.strip()))

        if page != now_page:
            break
        else:
            print('date', date)
            print('page', page)
        
        page += 1
    dataframe = {'날짜':date, '본문':page}
    
    print(dataframe)
    
    page = 1 
print('크롤링 종료')