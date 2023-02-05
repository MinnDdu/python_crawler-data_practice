from papago import translator_practice
# from 파일명(서브폴더면 서브폴더.파일명) import 함수명
# import * 하면 모든 함수 가져옴
# 파일명을 잘 지어야 하는 이유 - 자주쓰이는 라이브러리 (ex - pandas, mtplotlib, math ...) 등으로 파일이름 지으면?
# import 할때 곤란

import pandas as pd
df = pd.read_excel('/Users/minsoo/Desktop/Coding Apple/PythonCrawler/papago_API/english.xlsx', engine='openpyxl')
# print(df)
# print(df.dtypes)
# df['english'] = df['english'].astype(str)
# print(df.dtypes)

# 기존 반복문
# for i in range(len(df)):
#     df['korean'][i] = translator_practice(df['english'][i], 'en', 'ko')

# pandas dataframe 반복문
# 하나씩 꺼낼 행이 굉장히 많다? - df.itertuples() 사용이 유리
for i, row in df.iterrows():
    # i는 행번호, row는 행 내용
    # df.loc[행번호, 열]
    df.loc[i, 'korean'] = translator_practice(row['english'], 'en', 'ko')

print(df)

# 결과를 저장하기 - df.to_excel('path')
df.to_excel('./papago_API/eng2kor.xlsx')
df.to_csv('./papago_API/eng2kor.csv')
