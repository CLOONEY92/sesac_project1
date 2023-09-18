import requests
from bs4 import BeautifulSoup
import re
import json

category = 'NEWS'
number = '0014200171'
URL = f'https://sports.like.naver.com/v1/search/contents?q={category}%5Bne_001_{number}%5D%7CJOURNALIST%5B56735(period)%5D%7C{category}_MAIN%5Bne_001_{number}%5D'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
res = requests.get(URL, headers=headers)
bs = (BeautifulSoup(res.text, 'html.parser'))



result = re.sub("\/\*\*\/jQuery111303191396601710963\_1695004276725\(","", bs.text)
result2 = re.sub("\)\;","", result)

result_dic = json.loads(result2)
print(result_dic)

# for data in result_dic['contents']:
#     for i in data['reactions']:
#         print(i['reactionType'])
#         print(i['count'])
