import requests
from bs4 import BeautifulSoup

def get_news(URL):
    # URL = 'https://n.news.naver.com/mnews/article/215/0001126161?sid=101'
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select_one('h2#title_area span').text
    content = soup.select_one('div#newsct_article article').text.replace("\n","").strip()
    date = soup.select_one('span.media_end_head_info_datestamp_time')['data-date-time']
    media = soup.select_one('a.media_end_head_top_logo > img')['title']

    return (title, date, media, content, URL)

# get_news()