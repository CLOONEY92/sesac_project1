import requests
from bs4 import BeautifulSoup
import pandas as pd
from get_news import get_news

def get_news_list(keyword, startdate, enddate) :
    li = []
    h = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Referer' : 'https://search.naver.com/search.naver?where=news&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&sort=2&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0'}
    page = 1
    # start = 1
    while True:
        start = (page-1)*10 + 1
        print(page)

        URL = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=2&photo=0&field=0&pd=3&ds={1}&de={2}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:from{3}to{4},a:all&start={5}".format(keyword, startdate, enddate, startdate.replace(".",""), enddate.replace(".",""), start)

        res = requests.get(URL,headers = h)
        soup = BeautifulSoup(res.text, "html.parser")

        if soup.select_one(".not_found02") :
            break
        news_list = soup.select("ul.list_news li")
            
        for item in news_list :
            if len(item.select("div.info_group a")) == 2 :
                li.append(get_news(item.select("div.info_group a")[1]['href']))
        page = page + 1
        # start += 10

    return pd.DataFrame(li, columns=['title','date','media','content','url'])


# print(get_news_list('테슬라','2023.08.21', '2023.08.21'))