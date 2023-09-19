import re

samsung_cnt = 0
text = '에코프로 비엠이 주는 에코 엨코코ㅗ코코코 에코'

if re.match('에코프로', text) != None:
    samsung_cnt += 1

print(samsung_cnt)