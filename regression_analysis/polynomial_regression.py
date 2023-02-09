from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# income.txt 파일은 tab으로 구분되어있는 파일
# read_table()은 tab으로 구분해줌
df = pd.read_table('/Users/minsoo/Desktop/CS_practice/Coding Apple/PythonCrawler/regression_analysis/income.txt')

# 데이터에 어떤 값들이 빈칸(NaN)이나 오류값등이 있을 수 있음
df = df.dropna()

plt.scatter(df['age'], df['income'])
# plt.show()
# 그래프를 관찰해보면 직선으로 해결 불가해보임 대략 음의 이차함수 개형 -> 곡선은 어떻게?
# 이차함수로 시도 -> scipy 라이브러리 curve_fit(함수, x축데이터, y축데이터)
def func(x, a, b, c): # quadratic function
    return a*(x**2) + b*x + c

# curve_fit call하면 2가지 종류 데이터가 return
opt, cov = curve_fit(func, df['age'], df['income'])
# opt == a, b, c 값
# cov == 공분산(covariance)
print(opt, cov)

# 우리가 구한 그래프 그려보기
plt.plot([1,2,3,4,5,6], func(np.array([1,2,3,4,5,6]), opt[0], opt[1], opt[2]))
plt.show()