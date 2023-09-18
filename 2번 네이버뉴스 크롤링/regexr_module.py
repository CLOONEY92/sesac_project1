import requests
from bs4 import BeautifulSoup
import re

date= 20230801
page= 100

URL = 'https://news.naver.com/main/list.naver'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
params = {
        'mode' : 'LPOD'
        ,'mid' : 'sec'
        ,'oid' : '001'
        ,'date' : str(date)
        ,'page' : str(page) 
}
res = requests.get(URL, headers=headers, params=params)
bs = BeautifulSoup(res.text, 'html.parser')
for idx, data in enumerate(bs.select('div.list_body ul > li')):
    new_url = data.select_one('a').attrs['href']
    new_res = requests.get(new_url, headers=headers)
    new_bs = BeautifulSoup(new_res.text, 'html.parser')

def func(parameter: str) -> str:
    data1 = re.sub('<strong.*>.*<\/strong>',"", parameter)
    data2 = re.sub('<em.*>.*<\/em>',"", data1)
    data3 = re.sub('[가-힣]{2,3}\s?(?:인턴)?기자',"", data2)
    data4 = re.sub('\([가-힣]{2,3}=연합뉴스\)',"", data3)
    data5 = re.sub('[a-zA-Z]+@[a-zA-Z]+(\.[a-z]{2,4}){1,2}',"", data4)
    data_bs = BeautifulSoup(data5, 'html.parser')

    if new_bs.select_one('h2#title_area') != None:
        content = data_bs.select_one('article#dic_area').text.strip().replace("\n",'')
    elif new_bs.select_one('div.news_headline h4.title') != None:
        content = data_bs.select_one('div.news_end').text.strip().replace("\n",'')
    elif new_bs.select_one('h2.end_tit') != None:
        content = data_bs.select_one('div#articeBody').text.strip().replace("\n",'')
    return print(content)