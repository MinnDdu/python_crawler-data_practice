import pandas as pd
import statsmodels.api as sm
import numpy as np

df = pd.read_csv('/Users/minsoo/Desktop/CS_practice/Coding Apple/PythonCrawler/regression_analysis/california_housing.csv')
print(df)

# 변수 3개로 회귀분석을 통해 집값을 알아보자  - year(연식), rooms, bedrooms
# 집값 = year * x1 + rooms * x2 + bedrooms * x3


# pandas series data도 가능
# [[year1, rooms1, bedrooms2], [year1, rooms1, bedrooms2], ...] 이런형태도 가능
model = sm.OLS(df['price'], df[['year', 'rooms', 'bedrooms']]).fit()
print(model.summary())

# 이제 추정도 가능함 - Ex) year=20, rooms=1000, bedrooms=200
# 1. 직접 결과값들 보고 식 만들기
y = 4886 * 20 + 48 * 1000 - 132 * 200
# 2. predict() 함수이용
a = model.predict([[20, 1000, 200]])
print(a)