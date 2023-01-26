import pandas as pd
import re # regular expression

raw = pd.read_excel('./pandas&SMTP/product.xlsx', engine='openpyxl')

# 새로운 column을 만드는 방법 dataframe['column name'] = 무언가
raw['부가세포함'] = raw['판매가'] * 1.1


def func(data):
    return data * 1.1
# column 조작을 쉽게해주는 apply 함수 - 특정 컬럼에 있는 모든 데이터를 함수에 적용
raw['부가세포함'] = raw['판매가'].apply(func)


def func2(category):
    if 'Chair' in str(category):
    # pandas로 string을 읽을때 가끔 object로 변환됨 (string으로 캐스팅 필요)
        return 'Chair'
    elif 'Table' in str(category):
        return 'Table'


# 데이터를 수집한 후 데이터전처리를 해줄때 보통 더러운 데이터, 빵꾸난 데이터등을 쉽게 처리가능

# 1. re.search(정규식표현, 타겟) - 정규식을 이용해 특정 문자열이 존재하는지 판단 
def func2re(category):
    if re.search('Chair', str(category)):
        return 'Chair'
    if re.search('Mirror|Sofa', str(category)):
        return 'furniture'
    if re.search('\D', str(category)):
        return category
    else:
        return 'error'

# 기존 컬럼에다가 적용시 덮어쓰기 해줌
raw['카테고리'] = raw['상품목록'].apply(func2re)

print(raw)

# 2. re.findall(정규식표현, 타겟) - 표현이 타겟에 존재시 전부 리스트에 담아줌
a = re.findall('a', 'sdasda', re.IGNORECASE) # re.IGNORECASE == case sensitive 하지 않게 해줌
b = re.findall('^a', 'sdadas') # ^exp == exp로 시작하는 문자열?
c = re.findall('b$', 'asdb') # exp$ == exp로 끝나는 문자열?
d = re.findall('\$', '$@#$@#') # '\특수문자' == 특수문자 찾기
e = re.findall('[abcx]', 'asdasdas') # 'a' OR 'b' == '[ab]'
f = re.findall('[a-z가-힣ㄱ-ㅎ]', 'asdㅇㄴㅁㅁㄴds안녕') # '-' == 어디서부터 어디까지
h = re.findall('[^가-힣]', '크크안녕123') # '[^]' == []안에 ^은 NOT
i = re.findall('\d', '1234') # '\d' == 모든 숫자하나 (digit) == '[0-9]' *//* '\D' == 숫자가 아닌 모든것
# *** 정규식 스캔 방식 ***
# 정규식은 앞에서부터 선형적으로 하나씩 검사 후 제거 즉, '\d\d\d'로 '1234' 를 찾을시
# '123', '234'가 나오는게 아닌 처음에 나온 '123'만 나오게됨 ('1234'가 '4'만 남게 되고 스캔을 다시시작)
j = re.findall('\d{3}', '12345') # {n} == n만큼 (곱셈이라 생각하면 편함)
k = re.findall('\s', 'ds ds ds') # '\s' == 공백 (white space) *//* '\S' == 공백이 아닌 모든것
l = re.findall('a+', 'aaavab') # 'a+' == a 연속으로 한개 이상인 것 찾아줌 (greedy하다)
print(a, b, c, d, e, f, h, i, j, k, l)

# 3. re.sub('이걸찾아서', '이걸로바꾸기', '타겟') (substitute)
print(re.sub('\-', '.', '2022-1-1'))
print(re.sub('[0-9]', '', 'asda123awsd123'))


# 문제 - 1. 이메일 형식
결과 = re.findall('[a-zA-Z0-9]+@[a-zA-Z]+\.com', 'abc@example.com')
print(결과)