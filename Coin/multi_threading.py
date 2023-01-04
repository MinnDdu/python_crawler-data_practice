import requests
import json
import time

# 수집하고 싶은 url이 매우 많을때 (1000개 10000개 ... 100만개 등등)
# loop 문을 돌려도 한개씩 순차적으로 돌아가게됨 -> 상당히 느림
# 병렬작업 - multi-threading/multi-processing 을 하자! (multi-processing 은 창 여러개 띄워서 돌리기) (multi-threading 은 CPU 여러개 threading)
# Caution! - multi-processing 할때 변수가 있으면 여러 process에서 동시 변경 불가 -> (병목현상 bottleneck) 한 프로세스가 lock시키고 변경하고 lock 풀고 다음 프로세스로... -> loop 랑 차이 x

url = [
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
    'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

def close_price(url):
    data = requests.get(url)
    dict = json.loads(data.content)
    return dict['data'][0]['Close']

print(close_price(url[1]))

# multi-processing 라이브러리
# multiprocessing -> multi-processing 사용 / multiprocessing.dummy -> multi-threading 사용가능
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
pool.map()
#보통 close(), join() 세트로 많이 다님
pool.close() # pool 작업 그만
pool.join() # pool 결과 나올때까지 기다리기