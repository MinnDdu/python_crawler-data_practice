# 엑셀 자료가 너무 많아지면 (10만개 이상등등...) 보통 파이썬으로 많이 처리함
import pandas as pd

# 판다스에서 다루는 자료형은 Dataframe 자료형 (2차원 데이터 행렬) / Series (1차원 열 - 세로줄)
df = pd.read_csv('./pandas&SMTP/credit.csv')
# print(df)

# 원하는 열 가져오기 가능
# print(df['나이'])
# print(df['나이'].mean()) # mean() - 평균
# print(df['나이'].mode()) # mean() - 최빈값
# print(df['나이'].max()) # mean() - 최대값
# print(df['나이'].min()) # mean() - 최소값

# 빠른통계 describe()
print(df.describe())

# df.groupby('column) -> column안의 카테고리에 따라서 데이터를 다시 정렬
print(df.groupby('성별').mean())