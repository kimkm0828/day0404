import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc,font_manager
import csv

f = open("./Data/2016_GDP.txt","r",encoding="UTF-8")
f.readline()
list = f.readlines()

names = []
money = []
for row in list:
    row = row.split(":")
    names.append(row[1])
    money.append(row[2].strip().replace(",",""))

rc('font', family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())
money = np.array(money,dtype=int)
plt.bar(range(10),money[:10])
plt.title("국가별 총생산량 순위")
plt.xticks(range(10),names[:10],rotation="90")
plt.show()

