import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

rc("font",family=font_manager.FontProperties(fname="C:\Windows\Fonts/H2GTRE.TTF").get_name())

data = pd.read_csv("./Data/scores.csv")
data.index = data['name']
del data['name']

checkName = data.index.values
cnt = 0
for i in range(len(checkName)):
    if 'dan' == checkName[i]:
        cnt += 1