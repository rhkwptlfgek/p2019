#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CSE_USER
#
# Created:     30-05-2019
# Copyright:   (c) CSE_USER 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as nlp
import seaborn as sns
import os
import scipy as stats
#print(os.listdir("공공데이터"))
df = pd.read_excel("./공공데이터/부록03.2016년 월별 대기오염도(도시별).xls", sheetname='pm10')
#print(df.shape)
df = df.iloc[4:86, 1:15]

df.columns=['시군','1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월','연평균']

#print(type(df.ix[1:3,0:2]))
#print(df)

df1 = df[['시군','연평균']].sort_values(by='연평균',ascending=False).head(10)
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
plt.figure(figsize=(10,5))
plt.title("도시별 연평균 top 10")
#plt.figure(figsize=(10,6))
#plt.xlabel('시군')
#plt.ylabel('연평균')
#plt.bar(df1['시군'],df1['연평균'],c='b')
sns.barplot(x='시군',y='연평균',data=df1)
#plt.show()

df3 = df.sample(10)#무작위로 10개 가져왔다.
df3 = df3[['시군','연평균']]
plt.figure(figsize=(10,5))
plt.title("무작위")
plt.xlabel('시군')
plt.ylabel('연평균')
plt.plot(df3['시군'],df3['연평균'],'bo-')
#sns.barplot(x='시군',y='연평균',data=df3)
plt.show()

df2 = df.set_index('시군')
del df2['연평균']
df2=df2.head(2).T
x=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
plt.figure(figsize=(10,5))
plt.title('서울,부산 월별 미세먼지')
plt.xlabel('월')
plt.ylabel('미세먼지')
plt.plot(x,df2['서울'],c='r',lw=4,marker='o',label='서울')
plt.plot(x,df2['부산'],c='b',lw=2,marker='o',label='부산')
plt.show()


df4=df.set_index('시군')[['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']].mean(axis=0)
#df.loc['평균']=
plt.figure(figsize=(10,5))
plt.title('월별 평균')
plt.xlabel('월')
plt.ylabel('평균')
plt.bar(x,df4)
plt.show()






















