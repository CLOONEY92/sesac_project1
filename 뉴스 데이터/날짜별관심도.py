import pandas as pd
from glob import glob

# file_names = glob("./*.csv") 
# print(file_names)


df = pd.read_csv('./뉴스 데이터/news.csv', names=['날짜', '타이틀', '카테고리', '반응도(합산)', '기사본문'], sep=',')
print(df['반응도(합산)'])