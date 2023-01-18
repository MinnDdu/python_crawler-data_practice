
# class를 이용하여 object를 제작 (object 생성기계)
class Hero:
    # fields (members, attributes...) 모든 오브젝트들이 만들어질때 가지게되는 변수
    hidden = 'you found it!'

    # __init__ -> object를 만들때 init이 실행됨
    # self는 새로 생성될 object를 뜻함 (instance)
    def __init__(self, q, w, e, r):
        self.q = q
        self.w = w
        self.e = e
        self.r = r
    # 함수도 저장 가능함 -> 무조건 첫 파라미터는 self로 해야 에러가 나지 않음
    def hello(self):
        print('hi dude')



nunu = Hero('eat', 'snowball', 'throw', 'iceage')
garen = Hero('silence', 'courage', 'wheel', 'justice')

print(nunu.q)
print(nunu.hidden)
nunu.hidden = 'what'
print(nunu.hidden)
print(garen.hidden)


# *** '=' 등호로 값을 가져오는 것은 deepcopy가 아닌 shallowcopy ***
# Deep Copy - 실제 값을 '새로운 메모리 공간'을 할당하고 그 새로운 공간에 값을 복사
# Shallow Copy = 값이 아닌 복사되는 대상의 '주소값'을 복사함 (참조하고 있는 실제값은 동일!)
