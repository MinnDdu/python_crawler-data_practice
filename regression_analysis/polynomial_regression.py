from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import statsmodels.api as sm

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

# statsmodel로 최소제곱법 - 1차방정식 때는 OLS(y, x), x -> [[x1], [x2], ...] / 2차방정식은 [[x1^2, x1, 상수], [x2^2, x2, 상수], ...]
# 대략 방정식 항 하나당 변수 넣어준다는 느낌
x = np.column_stack([df['age']**2, df['age'], np.ones(79)]) # 상수항은 그냥 1로함
model = sm.OLS(df['income'], x).fit()
print(model.summary())

# overfitting 현상 - 과적합 현상
# 우리는 직선에(1차함수)에 curve를 줄 수 있다고 했음 -> 커브 1개 (2차함수)/ 커브 2개 (3차함수) ...
# scatter 함수를 이어줄때 그럼 매우많은 커브르 주면 더욱더 좋은 예측결과함수를 만들지 않을까?
# -> 과적합 (overfitting) 현상이 일어남 -> 기존데이터에게만 너무나도 적합한 모델이 되는 것! (새로운 데이터 적용의미 x)
# 어느정도 적합할정도만 커브를 주는 것이 중요함
