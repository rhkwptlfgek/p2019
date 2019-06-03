# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:39:39 2019

@author: SAMSUNG
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as nlp
import scipy as stats
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
#print(os.listdir("공공데이터"))
df = pd.read_excel("./공공데이터/부록01.연도별 대기오염도 (도시별 '89~'17).xls", sheetname='미세먼지(PM10)')
#print(df.shape)

df = df.iloc[2:86,1:25]
x=['시도','95년','96년','97년','98년','99년','00년','01년','02년','03년','04년','05년','06년','07년','08년','09년','10년','11년','12년','13년','14년','15년','16년','17년']
df.columns=x
df1=df.head(1)																					
df2= df1.dropna(axis=1)

y=['01년','02년','03년','04년','05년','06년','07년','08년','09년','10년','11년','12년','13년','14년','15년','16년','17년']
df3.columns=['서울']
#result=stats.linregress(df3['서울'],y)
#result
#slope, intercept, r_value, stderr = stats.linregress(df3['서울'],y)
x1 = np.array(df3['서울'])
slope = -5/13
intercept = 32
plt.figure(figsize=(10,6))
plt.scatter(df3['서울'],y)
plt.plot(x1,slope*x1+intercept,c="red")
plt.title('서울')
plt.xlabel('미세먼지(PM10)')
plt.ylabel('연도')
plt.show


#result = stats.linregress()