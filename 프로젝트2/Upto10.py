import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_news(URL) :
  res = requests.get(URL)
  soup = BeautifulSoup(res.text, "html.parser")

  title = soup.select_one("h2#title_area span").text #제목
  date = soup.select_one("span.media_end_head_info_datestamp_time")['data-date-time'] #기사작성일시
  media = soup.select_one("a.media_end_head_top_logo img")['title'] #매체명 (예.한국경제)
  content = soup.select_one("div#newsct_article").text.replace("\n","") #기사원문

  return (title, date, media, content, URL)

# get_news("https://n.news.naver.com/mnews/article/014/0005075348?sid=101")


# keyword = "테슬라"
# startdate="2023.08.21"
# enddate="2023.09.21"


def get_pages_list(keyword, startdate, enddate, allstart):

    pageli = []
    for page in range(1, allstart*10, 10):
        page_url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=1&photo=0&field=0&pd=3&ds={1}&de={2}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:dd,p:from{3}to{4},a:all&start={5}'.format(keyword, startdate, enddate, startdate.replace(".",""), enddate.replace(".",""), page)
        
        res = requests.get(page_url)
        soup = BeautifulSoup(res.text, "html.parser")
        news_list = soup.select("ul.list_news li")


        pageli.append(page_url)
    return pageli
    # return pd.DataFrame(pageli)

print(get_pages_list('테슬라','2023.08.21', '2023.09.21', 10))
