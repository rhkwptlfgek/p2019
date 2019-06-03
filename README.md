# 본인의 과제명 작성

학과 | 학번 | 성명
---- | ---- | ---- 
수학과 |201511113 |김원진


## 프로젝트 개요
1. 미세먼지 선형회귀분석
2. 도시별 연평균 미세먼지 top 10 그래프 
3. 무작위로 뽑은 도시 미세먼지 그래프
4. 서울,부산 미세먼지 비교 그래프
5. 월별 평균 미세먼지  

## 사용한 공공데이터 
[데이터보기](https://github.com/rhkwptlfgek/p2019/tree/master/%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0)

## 소스
* [링크로 소스 내용 보기](https://github.com/rhkwptlfgek/p2019/blob/master/module12.py)(https://github.com/rhkwptlfgek/p2019/blob/master/module1.py)

* 코드 삽입
~~~python
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
#result=stats.linregress(y,df3['서울'])
#result
#slope, intercept, r_value, stderr = stats.lin
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
-----------------------------------------------------
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
