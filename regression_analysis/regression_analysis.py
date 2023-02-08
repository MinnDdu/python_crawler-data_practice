import matplotlib.pyplot as plt
import numpy as np

height = [170, 180, 160, 165, 158, 176, 182, 172]
weight = [75, 81, 59, 70, 55, 78, 84, 72]

# Regression Analysis (회귀분석) - 하는 이유?
# 1. 데이터간 비례/반비례 여부 파악 가능
# 2. 비례/반비례할 경우 예측 가능

plt.scatter(height, weight)
plt.show()

# 점들을 대충 선으로 그어보면 경향성 파악가능
# 회귀분석 선 제대로 그리는 법: OLS(Ordinary Least Squares)를 충족하는 선!
# 1. 선을 그림 (1차 방정식)
# 2. 각각 점들이 그 선으로부터의 거리(오차)들의 합이 최소가 되는 선이 중요
# 3. 총 오차를 구할 땐 각각의 오차들을 제곱해서 더함 (음수제거 및 오차 뻥튀기)

# 파이썬에서 선형회귀분석 하는 법
from sklearn.linear_model import LinearRegression

# fit(x_data, y_data)
# model = LinearRegression().fit(height, weight)
# 이때 그냥 list로 돌리면 shape가 맞지 않음
# Error: Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
height = np.array(height).reshape(-1, 1)
# reshape()에서 '-1'의 의미는 너가 알아서 남은 배열 길이랑 남은 차원보고 정해라 이런소리
model = LinearRegression().fit(height, weight)
# 이제 model 이라는 변수에 우리가 원하는 정보들이 모두 저장됨


# model 분석 -> y = ax + b
print(model.score(height, weight)) # R값 해석 - 0~1 나옴 : 1에 가까우면 두 데이터간 연관성 높음
print(model.intercept_) # b값
print(model.coef_) # coefficient - a값

# 0.9361426318808448
# -118.03578708946773
# [1.11392978]
# 따라서 1차 방정식을 구하고, 그를 이용해 추정도 가능!
def f(x):
    return 1.1 * x - 118
print(f(180))

# model.predict() 로도 가능
print(model.predict([[175], [183]]))

# scatter에 선도 그려보기
plt.scatter(height, weight)
plt.plot(height, model.predict(height))
plt.show()


# statsmodels 라이브러리 이용해서 통계 이쁘게 내기
import statsmodels.api as sm

# sm.OLS(y, x).fit()
model2 = sm.OLS(weight, height).fit()
print(model2.summary())

# 회귀분석할 땐 특히 a(계수)가 0일 것이다라는 가설을 세우고 그걸 확률로 증명함
# y = ax + b
# R-squared (uncentered): 두 데이터가 얼마나 관련이 있는지
# Prob (F-statistic): a 값이 0일 확률 == x와 y가 관련 없을 확률


