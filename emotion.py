import requests
from bs4 import BeautifulSoup
import json

# URL = 'https://sports.naver.com/news?oid=001&aid=0014106287'
URL ='https://sports.like.naver.com/v1/services/SPORTS/contents/ne_001_0014106287?suppress_response_codes=true&_method=DELETE&callback=jQuery1113011101900582178059_1694948921890&displayId=SPORTS&reactionType=want&categoryId=&guestToken=336b79865532ea8fb6ca76ffe16f95bbd5563553b67c01ce78fa3af7493abd43f4dd1a1187c9b742b07e86c7a37c279ddebce3321b2e75ff082e901e93ebb142&timestamp=1694948921683&_ch=pcw&isDuplication=false&lang=ko&countType=default&count=1&history=&runtimeStatus=&_=1694948921892'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    ,'Referer':
        'https://sports.naver.com/news?oid=001&aid=0014106287'
    ,'Cookie':
        'NNB=IG4QYHLXUBIGI; ASID=d3d1375700000187dd33fe4100000048; recent_card_list=1692,1292; nx_ssl=2; nid_inf=-1497059888; NID_AUT=gvshSHjRYGgM94tdTuAlICbMgPrFZolr2W6SOt4PbVkgrSvjE6Sufn/rJNo1y+uR; NID_JKL=qebO90VbT2R+kyKMxUqLv97fa3BZVKLd37XYhOMDpa4=; NID_SES=AAABp4eF+yQaTCCLkasqnQixzVAVUuLKXjDn9gB+FdbG0QieXonbr90cL8wDuDHFe6msJ8LgDJOdW0QQ64KQAup6I6mG6Ohuc1UllJiB1BRyCvcgm69Wk7eMdApuigtstVjnmsdj0GtMw8ibIwk+LSAhsZdyKTsh59VW+NsSdiTXYsqVljEFWmx4885e5rKsyc4nhO7XkcJWSqidVAP4V+2lqhMEIA0Bkx7c+73bnFZQ4xJU++9OSj8BYFSO5C3BeH4/+/kvI3hsErfXl7+6F8fUdZRP+G3h3KbBCtu53sbu0A2NtFzepQfa8ZPdYMrYeAw4mDevWyW8w/RzgTAszTa6CkXLRKf2k+/Jg1so6hkpsZVh+JrQE3TyItM+kEjtKMYP/TlKn+JaNvCo4v9ivYf0I15hPb7BWMI1Kut+b9vesw85lz+KOL0cEYEQEFPhGf1ztqa7k0CzV7A0mrxIZ8IMfQNbynYU3HM1lbayw5mQ71ADu0995yV95CbIA+EnUWlwUWvyRC63ZJOOobMT6AVhwO5B8oyc9U5DfzM1yia4f/Jsdpct0YCir2emDsXC1pOvaQ=='
}
res = requests.get(URL, headers=headers)
bs = BeautifulSoup(res.text, 'html.parser')

# print(bs.select('div._reactionModule'))

for data in res.json():

    print(data)