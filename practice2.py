import pandas as pd
import numpy as np
import os
from glob import glob

file_names = glob("./*.csv") 
print(file_names)

# forders = os.listdir('*.csv')
# print(forders)
total = pd.DataFrame()

df1 = pd.read_csv("연습용1.csv")
df2 = pd.read_csv("연습용2.csv")

total = pd.merge(df1, df2, how='inner', on=None)

# for file_name in file_names:
#     temp = pd.read_csv(file_name, sep=',', encoding='utf-8') #csv파일을 하나씩 열어 임시 데이터프레임으로 생성한다
#     # total = pd.concat([total, temp])
#     total = pd.merge(df1, df2, how='inner', on=None)

total.to_csv("./total2.csv")

# SELECT column_name(s)
# FROM table1
# INNER JOIN table2
# ON table1.column_name = table2.column_name;
