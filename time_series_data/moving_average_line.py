#%% <----- 소스코드 맨위에 적으면 쥬피터 노트북으로 실행 가능
import pandas as pd
from pandas_datareader import data

# 시계열 데이터 - Time Series Data => 시간에 따라 기록되어있는 데이터
# 이 시계열 데이터의 추세, 흐름 파악 혹은 노이즈 제거를 위해 이동평균선 (moving average line)을 그려서 분석 많이함


# 보통 실시간 데이터는 웹크롤링을 통해 가져오지만 일별 데이터 같은 데이터는
# pandas_datareader로 쉽세 가져오기 가능 Ex) Yahoo Finance, Naver Finance
# DataReader('종목', '소스', start='시작날짜', end='종료날짜')
# df2 = data.DataReader('AAPL', 'yahoo', start='2019-01-01', end='2020-01-01')
df = data.DataReader('005930', 'naver', start='2019-01-01', end='2020-01-01')
df

# 데이터 자료형이 int/float 이 아닐경우 plot() 불가
print(df.dtypes) # 자료형 파악 가능
df['Close'] = df['Close'].astype(float) # Close == 종가 <- 가장 중요
print(df.dtypes)
print(df['Close'].plot())

# dataframe에는 index column 존재할 수 있음
print(df.index)


# %%
# Moving Average Line (이동평균선) - n일간 가격을 평균내서 그래프로 그린 것
# time series 데이터의 추세, 흐름 파악 혹은 노이즈 제거를 위해 이동평균선 분석을 할떄가 많음

df['rolling5'] = df['Close'].rolling(5).mean() # <- rolloing(n) == n개씩 싸잡아줌
df['rolling20'] = df['Close'].rolling(20).mean() 
df.plot()
df['rolling5'].plot() # <- 5일 이동평균선
df['rolling20'].plot() # <- 20일 이동평균선

# %%
# 실제로 데이터 분석을 할떄는 matplotlib 많이 사용 && 그래프 그릴떈 colab, jupyter notebook 좋음
import matplotlib.pyplot as plt
# line graph - plt.plot([x축데이터], [y축데이터]) / list 혹은 pandas의 series 데이터(리스트와 비슷)
plt.plot(df.index, df['Close'], color='crimson')
plt.xlabel('time') # x axis label
plt.ylabel('close price') # y axis label
plt.legend(['Samsung']) # legend 범례
plt.show() # 차트를 보여줌!!

# bar graph - plt.bar([x축데이터], [y축데이터]) - 보통 카데고리 데이터 빈출값 나타낼때
plt.bar(df.index, df['Close'])
plt.show()

# pie chart - plt.pie([data])
plt.pie([1,2,3], labels=['ramen', 'tuna', 'snack'])
plt.show()

# histogram - plt.hist() - 어떤 값이 빈출하는지, 분포가 어떻게 되는지
plt.hist([160, 170, 180, 170, 173, 175, 169])
plt.show()

# scatter plot - plt.scatter([x축데이터], [y축데이터]) - 분포도, 연관성 파악
math = [1,2,3,4,5,6,7,8]
eng = [31, 22, 81, 3, 56, 32, 76, 92]
plt.scatter(math, eng)
plt.show()

# stackplot - plt.stackplot([x축데이터], [y축데이터1], [y축데이터2], ...) - 누적되는 데이터 그래프
plt.stackplot([1, 2, 3], [10,20,30], [20,10,50])
plt.show()

# %%
# 여러 그래프 한번에 보여주기 - plot() 여러번 하고 그 다음에 plt.show()
# 사이즈 키우기 - plt.figure(figsize=(10, 10)) == 인치 - plot() 하기 전에 사용


# 직접 해보기
# Q1 -  아마존 (종목코드 AMZN) 주식의 2020년 01월01일~12월31일 주식가격을 yahoo에서 가져온 후 20일, 60일 이동평균선을 그려보십시오. 
import yfinance as yf

yf.pdr_override() # <== that's all it takes :-)

df_amazon = data.get_data_yahoo("AMZN", start="2020-01-01", end="2020-12-31")
df_amazon
df_rollings = pd.DataFrame({'rolling20': df_amazon['Close'].rolling(20).mean(), 'rolling60': df_amazon['Close'].rolling(60).mean()})
df_rollings

plt.plot(df_amazon.index, df_rollings['rolling20'])
plt.plot(df_amazon.index, df_rollings['rolling60'])
plt.show()

# %%
# Q2 - 두 기업의 연간 매출 데이터 그래프로 만들기
import numpy as np
df2 = pd.DataFrame({'': [2018, 2019, 2020, 2021], 
                    'Samsung': [50000, 60000, 75000, 70000],
                    'LG': [30000, 40000, 50000, 35000]})
df2
x_axis = np.array(df2[''])
w = 0.3
plt.bar(np.array([2018,2019,2020,2021]), df2['Samsung'], width=0.3)
x_axis = x_axis + w
plt.bar(np.array([2018,2019,2020,2021])+0.3, df2['LG'], width=0.3)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend(['Samsung', 'LG'])
plt.show()



# %%

# Q3 - 원하는 데이터만 보이게 그래프를 조작하기
# yahoo에서 2020년 01월01일~12월31일의 비트코인 가격을 가져오고 Close 가격을 그래프로 그리고 싶습니다. (종목코드 BTC-USD)
# 근데 Volume항목 2020년의 평균 Volume보다 높은 날의 가격만 그래프로 그려보고 싶다면?
btc_df = data.get_data_yahoo('BTC-USD', start='2020-01-01', end='2020-12-31')
# btc_df
avg_vol = btc_df['Volume'].mean()

btc_df['tf'] = btc_df['Volume'] > avg_vol
new_btc_df = btc_df[btc_df['tf'] == True]
new_btc_df
plt.bar(new_btc_df.index, new_btc_df['Close'])
plt.show()


# %%
