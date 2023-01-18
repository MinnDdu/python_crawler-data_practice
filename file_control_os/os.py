import os # 파일 조작하는 파이썬 기본 라이브러리

files = os.listdir('./file_control_os/files') # 해당 경로에 있는 모든 파일들을 리스트로 반환

# 파이썬으로 원하는 파일의 파일명 바꾸기 (파라미터1경로가 파라미티2경로로 바뀜!)
# os.rename('./file_control_os/files/1.txt', './file_control_os/files/4.txt')
print(files)

# for file in os.listdir('./file_control_os/files'):
#     os.rename(f'./file_control_os/files/{file}', f'./file_control_os/files/modified{file}')
i = 1
for file in os.listdir('./file_control_os/files'):
    os.rename(f'./file_control_os/files/{file}', f'./file_control_os/files/{i}' + '.txt')
    i += 1

import shutil # 파이썬 이용해서 파일 복사할때 많이 사용하는 라이브러리
# (파라미터1경로를 파라미터2경로로 복사해줌)

# os.makedirs('./file_control_os/files2')

for file in os.listdir('./file_control_os/files'):
    shutil.copy(f'./file_control_os/files/{file}', f'./file_control_os/files2/{file}')

# 파일의 경로 문제
# 1. 절대경로 - 원하는 경로의 절대적인 위치
# 절대경로를 파이썬에서 사용할때는 백슬래쉬 \ 때문에 경로를 적은 스트링 앞에 r(raw)를 적어줘야함!
# r'C:\Users\Mark\Documents\GitHub\python_crawler_practice\file_control_os\files2'
# 2. 상대경로 - 원하는 경로의 내 위치에 따른 상대적인 위치

# os 경로관련 자주쓰이는 함수
# 경로 합치기 함수
# os.path.join('path1', 'path2') == 'path1' + '/path2'의 안정적인 방식
# 현재 파이썬파일의 절대경로 출력 함수
# os.get.getcwd() == current working directory

print(os.getcwd())