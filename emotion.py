import requests
from bs4 import BeautifulSoup
import re
import json

URL = 'https://sports.like.naver.com/v1/search/contents?suppress_response_codes=true&callback=jQuery111303191396601710963_1695004276725&q=SPORTS%5Bne_001_0014106287%5D%7CJOURNALIST%5B56735(period)%5D%7CSPORTS_MAIN%5Bne_001_0014106287%5D&isDuplication=false&cssIds=MULTI_PC%2CSPORTS_PC&_=1695004276726'
# URL = 'https://sports.naver.com/news?oid=001&aid=0014106287'
# URL ='https://sports.like.naver.com/v1/services/SPORTS/contents/ne_001_0014106287?suppress_response_codes=true&_method=DELETE&callback=jQuery1113011101900582178059_1694948921890&displayId=SPORTS&reactionType=want&categoryId=&guestToken=336b79865532ea8fb6ca76ffe16f95bbd5563553b67c01ce78fa3af7493abd43f4dd1a1187c9b742b07e86c7a37c279ddebce3321b2e75ff082e901e93ebb142&timestamp=1694948921683&_ch=pcw&isDuplication=false&lang=ko&countType=default&count=1&history=&runtimeStatus=&_=1694948921892'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
res = requests.get(URL, headers=headers)
bs = (BeautifulSoup(res.text, 'html.parser'))



result = re.sub("\/\*\*\/jQuery111303191396601710963\_1695004276725\(","", bs.text)
result2 = re.sub("\)\;","", result)
# print(result2)
# results = re.finditer("\"reactionType\"\:\"fan\"\,\"count\"\:[0-9]", bs)
# print(results)

# for result in results:
#     print(result)

# print(bs)

result_dic = json.loads(result2)
# print(result_dic)

for data in result_dic['contents']:
    for i in data['reactions']:
        print(i['reactionType'])
        print(i['count'])
# for data in result2.json():

#     print(data)