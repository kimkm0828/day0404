import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

rc("font",family=font_manager.FontProperties(fname="C:\Windows\Fonts/H2GTRE.TTF").get_name())

data = pd.read_csv("./Data/scores.csv")
data.index = data['name']
del data['name']

print(data)
print("-"*100)


# @@ 모든학생 국어 점수
# print(data['kor'])


# @@ 모든과목의 점수
# print(data[['kor','eng','mat','bio']])


# @@ ben학생의 과목별 점수를 막대그래프로
# ben_sco = data.loc['ben'].values[1:]
# subject = data.columns
# plt.bar(range(len(ben_sco)),ben_sco)
# plt.xticks(range(len(ben_sco)),subject[1:])
# plt.show()

# @@ 모든 학생의 국어점수를 막대그래프로 ㄱㄱ
# kor_sco = data.loc[:,'kor']
# name = data.index
#
# plt.bar(range(len(kor_sco)),kor_sco)
# plt.title("국어점수")
# plt.xticks(range(len(kor_sco)),name,rotation="40")
# plt.show()

plt.subplot(211)
ben_sco = data.loc['ben'].values[1:]
subject = data.columns
plt.bar(range(len(ben_sco)),ben_sco)
plt.xticks(range(len(ben_sco)),subject[1:])


plt.subplot(212)
kor_sco = data.loc[:,'kor']
name = data.index
plt.bar(range(len(kor_sco)),kor_sco)
plt.title("국어점수")
plt.xticks(range(len(kor_sco)),name,rotation="40")
plt.savefig('templates/student.png')
print("차트만듬")


















