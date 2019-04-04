import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/scores.csv")
df.index = df['name'].values # 학생의 이름을 키로 설정
del df['name']
print(df)
print('------------------------------------------')


# @@henry의 정보 출력
# print(df.loc['henry'])
# print(df.iloc[11].values)

# @@andrew 부터 paul 까지의 정보
# print(df.loc['andrew':'paul'])


# @@adam dan walter의 정보 출력
# print(df.loc[['adam','dan','walter']])

# @@ 앞에서 5번째 학생들 국어 점수
# print(df.iloc[:5]["kor"])

# @@ 앞에서 5번째 학생들 국어 수학
# print(df.iloc[:5][["kor","mat"]])


# @@ adam dan walter의 bio를 제외한 과목의 점수
# print(df.drop('bio',axis=1).loc[['adam','dan','walter']])
# print(df.loc[['adam','dan','walter'],:'mat'])
names = [0,4,7]
print(df.iloc[names,1:-1])













