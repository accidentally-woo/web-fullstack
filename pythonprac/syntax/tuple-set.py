a = (1, 2, 3) # 튜플은 리스트와 비슷하지만 불변인 자료형 (추가 공부 : mutable / immutable 차이점 알아보기)
print(a[0])

# a[0] = 99 -> Error! : TypeError: 'tuple' object does not support item assignment

# 형식이 고정된 자료형에 사용하기 좋음.
#       딕셔너리 대신 리스트와 튜플로 활용
a_dict = [('bob','24'),('john','29'),('smith','30')]
print(a_dict)

a = [1,2,3,4,5,3,4,2,1,2,4,2,3,1,4,1,5,1]

a_set = set(a)

print(a_set) # -> 중복 제

a = ['사과','감','수박','참외','딸기']
b = ['사과','멜론','청포도','토마토','참외']

print(set(a) & set(b))  # 교집합
print(set(a) | set(b))  # 합집합