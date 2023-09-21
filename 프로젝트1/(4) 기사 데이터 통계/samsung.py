import csv
import os
# print(os.listdir('./(3) 네이버뉴스 크롤링'))
import pandas as pd

# file = open(f"samsung.csv", mode="w", encoding="utf-8", newline="")
# writer = csv.writer(file)

f = open(f'./(3) 네이버뉴스 크롤링/naver.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

linelist = []

for line in rdr:
    if line[4].find('삼성전자') != -1:
        # writer.writerow(line)
        linelist.append(line[4])

dataframe = {'본문' : linelist}
df = pd.DataFrame(dataframe)

df.to_csv("samsung.csv", encoding='utf-8-sig')
