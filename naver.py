import requests
from bs4 import BeautifulSoup
import re

URL = 'https://news.naver.com/main/list.naver'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

date= 20230801
page= 100

def func(parameter: str) -> str:
    data1 = re.sub('<strong.*>.*<\/strong>',"", parameter)
    data2 = re.sub('<em.*>.*<\/em>',"", data1)
    data3 = re.sub('[가-힣]{2,3}\s?(?:인턴)?기자',"", data2)
    data4 = re.sub('\([가-힣]{2,3}=연합뉴스\)',"", data3)
    data5 = re.sub('[a-zA-Z]+@[a-zA-Z]+(\.[a-z]{2,4}){1,2}',"", data4)
    data_bs = BeautifulSoup(data5, 'html.parser')
    content = data_bs.select_one('article#dic_area').text.strip().replace("\n",'')

    return print(content)

while True:
    print('date', date)
    

    params = {
        'mode' : 'LPOD'
        ,'mid' : 'sec'
        ,'oid' : '001'
        ,'date' : str(date)
        ,'page' : str(page) 
    }
    res = requests.get(URL, headers=headers, params=params)
    bs = BeautifulSoup(res.text, 'html.parser')


# 해당 날짜 및 요일
    now_date = print(bs.select_one('div.pagenavi_day > span.viewday').text)
# 해당 페이지
    now_page = (int(bs.select_one('div.paging strong').text.strip()))

    # print(type(page))
    # print(type(now_page))
    if page != now_page:
        break
    else:
        print('page', page)
    
    for idx, data in enumerate(bs.select('div.list_body ul > li')):
        new_url = data.select_one('a').attrs['href']
        new_res = requests.get(new_url, headers=headers)
        new_bs = BeautifulSoup(new_res.text, 'html.parser')

        title = ''
        content = ''
        category = ''

        if new_bs.select_one('h2#title_area') != None:
            print('일반기사')
            title = (new_bs.select_one('h2#title_area').text.strip())

            article = str(new_bs.select('article#dic_area'))
            func(article)
            # # print(type(article))
            # data1 = re.sub('<strong.*>.*<\/strong>',"", article)
            # data2 = re.sub('<em.*>.*<\/em>',"", data1)
            # data3 = re.sub('[가-힣]{2,3}\s?(?:인턴)?기자',"", data2)
            # data4 = re.sub('\([가-힣]{2,3}=연합뉴스\)',"", data3)
            # data5 = re.sub('[a-zA-Z]+@[a-zA-Z]+(\.[a-z]{2,4}){1,2}',"", data4)
            # # print(data5)        
            # data_bs = BeautifulSoup(data5, 'html.parser')
            
            # content = print(data_bs.select_one('article#dic_area').text.strip().replace("\n",''))
            if new_bs.select_one('em.media_end_categorize_item') != None:
                category = (new_bs.select_one('em.media_end_categorize_item').text)                
            else:
                print('이 기사는 언론사에서 섹션분류를 하지 않았습니다.')
            feelings = (new_bs.select('ul.u_likeit_layer'))
            # for mood in feelings:
            #     useful = (mood.select('span')[1].text)
            #     wow = (mood.select('span')[3].text)
            #     touched = (mood.select('span')[5].text)
            #     label = (mood.select('span')[7].text)
            #     recommend = (mood.select('span')[9].text)

        elif new_bs.select_one('div.news_headline h4.title') != None:
            print('스포츠기사')
            title = (new_bs.select_one('div.news_headline h4.title').text.strip())

            article = str(new_bs.select('div.news_end'))
            data1 = re.sub('<strong.*>.*<\/strong>',"", article)
            data2 = re.sub('<em.*>.*<\/em>',"", data1)
            data3 = re.sub('[가-힣]{2,3}\s?(?:인턴)?기자',"", data2)
            data4 = re.sub('\([가-힣]{2,3}=연합뉴스\)',"", data3)
            data5 = re.sub('[a-zA-Z]+@[a-zA-Z]+(\.[a-z]{2,4}){1,2}',"", data4)

            data_bs = BeautifulSoup(data5, 'html.parser')
            
            # content = print(data_bs.select_one('div.news_end').text.strip().replace("\n",''))
            category = '스포츠'

        elif new_bs.select_one('h2.end_tit') != None:
            print('연예기사')
            title = (new_bs.select_one('h2.end_tit').text.strip())
            content = (new_bs.select_one('div#articeBody').text.strip().replace("\n",''))
            category = '연예'

        else:
            print('!!!!!!!!!!!!!!!!!!!!')
            print(new_url)
            
        # print(title)
        # print(content)
        # print(category)
        # print()

    page += 1

print('크롤링 종료')


# 기사별 링크, 분기
# for idx, data in enumerate(bs.select('ul.type06_headline > li')):
#     print(data.select_one('a').attrs['href'])
# for idx, data in enumerate(bs.select('ul.type06 > li')):
#     print(data.select_one('a').attrs['href'])

# 8월 한달동안 날짜, 타이틀, 기사본문, 기사반응, 카테고리
# 기사내용은 전처리 진행(strong, 이메일, em.img_desc, (서울=연합뉴스), (인턴)기자)
