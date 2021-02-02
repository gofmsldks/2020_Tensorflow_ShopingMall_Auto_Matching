import csv
from konlpy.tag import Okt
import re
import numpy as np
import pandas as pd

# 형태소 분석 및 품사 태깅, Data 사전을 만드는 과정

re_sc = re.compile('[\!@#$%\^&\*\(\)\-=_\[\]\{\}\.,/\?~\+\'"|]')



a = []


f = open('/Users/kimhyung-won/Downloads/내문서/2020_Tensorflow_ShopingMall_Auto_Matching/Translate_TestData.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    line = line[0].split("$")
    str = re_sc.sub(' ', line[2]).strip()
    if len(line) <= 3: a.append([str])
    else: a.append([str, line[3]])

f.close()

for i in a:
    print(i)


dd = []
twt = Okt()

for i in a:
    tagging = twt.pos(i[0], norm=True)
    print(tagging)


