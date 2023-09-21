import requests
from bs4 import BeautifulSoup

def get_blogs_list(URL) :
    blogId = URL.split('/')[-2]
    logNo = URL.split('/')[-1]
    new_url = f'https://blog.naver.com/PostView.naver?blogId={blogId}&logNo={logNo}&redirect=Dlog&widgetTypeCall=true&directAccess=false'
    # print(new_url)
    res = requests.get(new_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    category = print(soup.select_one("div.blog2_series a").text) #카테고리
    title = print(soup.select_one("div.se-module span").text) #제목
    name = print(soup.select_one("span.writer").text.strip()) #작성자
    date = soup.select("div.blog2_container").text #작성일시
    content = soup.select_one("div#newsct_article").text.replace("\n","") #원문
    
    
    return (title, category, name, date, content, URL)


# print(get_blogs_list('https://blog.naver.com/aaa4815926/223217855620'))