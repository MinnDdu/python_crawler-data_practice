# 엑셀 자료가 너무 많아지면 (10만개 이상등등...) 보통 파이썬으로 많이 처리함
import pandas as pd

# 1. 판다스에서 다루는 자료형은 Dataframe 자료형 (2차원 데이터 행렬) / Series (1차원 열 - 세로줄)
df = pd.read_csv('./pandas&SMTP/credit.csv')
# print(df)

# 2. 원하는 열 가져오기 가능
# print(df['나이'])
# print(df['나이'].mean()) # mean() - 평균
# print(df['나이'].mode()) # mean() - 최빈값
# print(df['나이'].max()) # mean() - 최대값
# print(df['나이'].min()) # mean() - 최소값

# 3. 빠른통계 describe()
print(df.describe())

# 4. df.groupby('column) -> column안의 카테고리에 따라서 데이터를 다시 정렬
print(df.groupby('성별').mean())

# 5. correlation 값 구하기 - 두 column간의 관계도 - list안에다가 column들 넣기
print(df[['나이', '사용금액']].corr())
#             나이      사용금액
# 나이    1.000000  0.106826   -> 0.1만큼 관계있음 (거의 관계없음)
# 사용금액  0.106826  1.000000

# 6. 원하는 데이터만 필터주기 - df안에 조건십 입력
print(df[df['나이'] > 50])

# 7. query문 사용하기 - 여러가지 조건식 사용 (double quote 사용 and 문자자료는 single quote 사용해야함)
print(df.query(" 나이 > 50 and 기혼 == 'Married' "))

# 8. 파이썬의 기존 list 데이터를 판다스의 dataframe 자료로 바꾸기 가능 - (dictionary 자료형 이용)
shirts_sold = [15, 20, 35]
pants_sold = [150, 160, 170]
# 우선 dictionary 자료 필요 - key == column 이름, value == 각 row의 값들
dict = {
    'shirts': [15, 20, 35],
    'pants': [150, 160, 170]
}

df2 = pd.DataFrame(dict)
print(df2)

# 통계를 통해 명제 분석해보기
# '기혼남성은 싱글남성에 비해 사용금액이 평균적으로 높을것이다'
married_men = df.query("성별 == 'M' and 기혼 == 'Married'")
single_men = df.query("성별 == 'M' and 기혼 == 'Single'")

print(married_men['사용금액'].mean() > single_men['사용금액'].mean()) # 명제는 참!
# '연간소득이 높을수록 사용금액이 평균적으로 높을것이다'
# 안됨 - print(df[['소득', '사용금액']].corr()) -> 소득은 $40-$60 같이 string 자료형 즉, 바로 corr()불가
print(df.groupby('소득').describe())
