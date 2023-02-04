# id: ZblfhAL1D5DgWB559Iqs
# pw: kiMmQEEdJJ

import json
import os
import sys
import urllib.request
client_id = "ZblfhAL1D5DgWB559Iqs" # 개발자센터에서 발급받은 Client ID 값
client_secret = "kiMmQEEdJJ" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("안녕하세요 저는 공부가 하기 싫지만 해야만 해요!")

# source && target
data = "source=ko&target=en&text=" + encText


url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    # JSON을 dictionary로 변환시켜줌
    dict = json.loads(response_body)
    print(dict['message']['result']['translatedText'])

    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)