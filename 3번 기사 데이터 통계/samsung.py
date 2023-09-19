import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

URL = 'https://news.naver.com/main/list.naver'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


page= 53
article_sum = 0
samsung_cnt = 0
samsung_all_cnt = 0

for date in range(20230820, 20230832):

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
        # print(len(bs.select('div.list_body > ul.type06_headline > li')))
        # print(len(bs.select('div.list_body > ul.type06 > li')))

        if page != now_page:
            # article_sum += len(bs.select('div.list_body > ul.type06_headline > li'))+len(bs.select('div.list_body > ul.type06 > li'))-20
            break
        # else:
        #     print('date', date)
        #     print('page', page)
        print(date)
        print(page)

        
        for idx, data in enumerate(bs.select('div.list_body ul > li')):
            new_url = data.select_one('a').attrs['href']
            new_res = requests.get(new_url, headers=headers, params=params)
            new_bs = BeautifulSoup(new_res.text, 'html.parser')

            
            content = ''
            

            if new_bs.select_one('h2#title_area') != None:
                # print('일반기사')
                content = (new_bs.select_one('article#dic_area').text.strip().replace("\n",""))
                print(content)

                if re.match('윤석열', content) != None:
                    samsung_cnt += 1
                    # print(samsung_cnt)
                print({'윤석열 기사':samsung_cnt})
            # else:
            #     print('해당기사에는 없습니다.')        
        
        # samsung_all_cnt += samsung_cnt
        page += 1
        # article_sum += 20
        # print(article_sum)


    # dataframe = {'날짜':date, '본문':samsung_cnt, '본문%':samsung_cnt/samsung_all_cnt*100}
    
    # print(dataframe)
    # samsung_cnt = 0
    page = 1 
print('크롤링 종료')

# df = pd.DataFrame(dataframe)
# print(df)

# df.to_csv("stock(1).csv", encoding='utf-8-sig')


# 삼성전자주가% 를 다른 테이블에서 구하고,
# 두개의 테이블에서 INNER JOIN 날짜로 합친다음,
# 주가데이터가 없는 날짜 None은 날릴 것.
