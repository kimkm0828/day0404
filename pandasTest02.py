import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# df = pd.DataFrame([[1,2,3,],[4,5,6]])
# print(df)
# print(type(df))



df = pd.read_csv("Data/scores.csv")
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df['kor'])

# Pandas와 DataFrame에서 행접근 loc 이나 iloc함수를 이용
# 키값이 없을때는 둘다 가능
# 키값이 있을때 인덱스로 접근하려면 iloc

# values하면 넘파이 배열 줌 이거만 알면 다한다
print(df.iloc[2].values)




















