import requests
from bs4 import BeautifulSoup
import pandas as pd
from get_blog import get_blog
from tqdm.notebook import tqdm as tqdm
import re
import json

# 30개씩 무한 스크롤링
def get_blog_list(keyword, startdate, enddate) :
    start = 1
    URL = 'https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={0}&rev=44&start={1}&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Cp%3Afrom{2}to{3}&nlu_query=%7B%22r_category%22%3A%2233+25%22%7D&dkey=0&source_query=&nx_search_query={0}&spq=0&_callback=viewMoreContents'.format(keyword, start, startdate, enddate)
    h = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Referer' : 'https://search.naver.com/search.naver?where=news&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&sort=2&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0', 'cookie':'NNB=KXDWSALR5HLWE; ASID=afc28e77000001821bee653700000062; _ga=GA1.2.852833469.1658355403; _ga_7VKFYR6RV1=GS1.1.1663030713.12.1.1663030726.47.0.0; NFS=2; m_loc=8e6c6458de8107ce6b301a2fdcaac47c270f10d32641f9fdfed1b5b1faac3e2c; NV_WETR_LAST_ACCESS_RGN_M="MDIxMzU1NTA="; NV_WETR_LOCATION_RGN_M="MDIxMzU1NTA="; recent_card_list=2936,3397,2717,3977; nx_ssl=2; nid_inf=-1453188587; NID_AUT=3O547E30xwR+LSPJWBh1H0BeJZ8z7w5GcYoFiB1oouz7XPFXgUYyapi0YaIPu/ed; NID_JKL=G/s4QbAdJVVTz69y/dBkR/9g00VQhbM8nxg71ZvVgyE=; NID_SES=AAABoKkgglCWz6aloghoOZ3uiyN2Gx8Ya6M3siOaeQCtWMn7TXgrPkganW/YVI931ONSrWmpB6IIM3p/mCMfueM9ekkTAuzM2mj8PfOoUbrV7BrzerfHGStcNmmb0QkiSuOy8AH1MwneQ7sJCTZBpPEfIbn9HUQ6S62sMy5oLJ0xqXedXxwQ4TsBa4+6Z6FWpVTIfmTzWMFt/M4pfpxYEbYAVBsfhLIsNPCjHLCrkoDdQPeUS949dDM9Xf8zpucBTRJrB6GwKaQDSeVWs+OgXngp1iusiktNnHZ7hEWDO5gyZCXkA7jV9njHKBDw6b58JD2La4eTPDBjq6xzUHaCAt+L7rGlpQ5FWHh1UF8XcyHGLdi2zQRHHSs9giWGIdbJ61akjlPZM/N8vL9zJZcw8qFmko0EY8RNmF1aUNE7qEcfaEyQNu/tlmIsUeYl5kPbZgL8fUiKMssPunn4ciffRsstEIcRbvtkVUdDKvr5QdQdf5J0o167t5vXBvctqzggQXUYOOBv8Cb9G9W5NcGibg9J3OCd7JMZTNGPV6gFAtga/WJL; page_uid=idY26sprvTVssudbzPwssssssI4-486433; _naver_usersession_=SXc2E3wZ6W9q/0SVHj+cMQ=='}
    
    res = requests.get(URL, headers = h)
    result = re.finditer("\{([^}]+)\}", res.text)
    for each in result :
        r = json.loads(each.group())
    
    total_page = int(r['total'])
    # total_page = int(res.text[28:].split('\"')[0])//30+1

    li = []
    for page in tqdm(range(1, total_page+1), desc="get_blog_list"):
        start = 30*(page-1)+1 #1, 31, 61, 91, 121 
        URL = "https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={0}&rev=44&start={1}&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Cp%3Afrom{2}to{3}&nlu_query=%7B%22r_category%22%3A%2233+25%22%7D&dkey=0&source_query=&nx_search_query={4}&spq=0&_callback=viewMoreContents".format(keyword, start, enddate.replace(".",""), startdate.replace(".",""), keyword)

        res = requests.get(URL,headers = h)
        result = re.finditer("\{([^}]+)\}", res.text)
        for each in result :
            r = json.loads(each.group())

        soup = BeautifulSoup(r['html'], 'html.parser')
        # soup = BeautifulSoup(res.text.replace("\\",""), "html.parser")

        blog_list = soup.select("li div.total_area > a")
        for item in blog_list :     
            try :
                li.append(get_blog(item['href']))
            except :
                print(item['href'])

    return pd.DataFrame(li, columns=['title','category','name','date','content', 'url'])


# print(get_blog_list('삼부토건', '2023.08.31', '2023.09.21'))