import requests
from bs4 import BeautifulSoup

def get_blog(URL) :
    blogId = URL.split('/')[-2]
    logNo = URL.split('/')[-1]
    new_url = f'https://blog.naver.com/PostView.naver?blogId={blogId}&logNo={logNo}&redirect=Dlog&widgetTypeCall=true&directAccess=false'
    # print(new_url)
    res = requests.get(new_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    if soup.select_one(".se-title-text") :
        category = print(soup.select_one("div.blog2_series a").text) #카테고리
        title = print(soup.select_one("div.se-module span").text) #제목
        name = print(soup.select_one("span.writer").text.strip()) #작성자
        date = soup.select("div.blog2_container").text #작성일시
        content = soup.select_one("div#newsct_article").text.replace("\n","") #원문
    elif soup.select_one("h3.se_textarea") :
        title = soup.select_one("h3.se_textarea").text
        category = soup.select_one(".blog2_series > a").text
        nick = soup.select_one(".nick > a").text
        date = soup.select_one(".se_publishDate").text
        content = soup.select_one(".se_doc_viewer").text.replace("\n","")
    else:
        return None
    
    return (title, category, name, date, content, URL)


# print(get_blogs_list('https://blog.naver.com/aaa4815926/223217855620'))