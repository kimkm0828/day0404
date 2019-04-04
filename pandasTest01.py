import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas의 자료 구조
# series            ==> 1차원 배열
# dataframe         ==> 2차원 배열

# a = [1,2,3,4,5]
# arr = pd.Series(a)
# print(a)
# print(arr)
# print(type(a))
# print(type(arr))


# arr = pd.Series(['홍길','강감','이순','유관'])
# print(arr)

# arr = pd.Series([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0])
# print(type(arr[0]))

# arr = pd.Series([['홍길','강감'],['홍길','강감']])
# print(arr)

# a = pd.Series([5,6,7,8], index=['김경','오상','이성','김도'])
# print(a.values)
# print(type(a.values))
# [5 6 7 8]
# <class 'numpy.ndarray'>
#  keys = a.index
#  for key in keys:
#      print(key,a[key])

a = {'김경':5,'오상':9,'이성':3}
arr = pd.Series(a)
print(arr)
























