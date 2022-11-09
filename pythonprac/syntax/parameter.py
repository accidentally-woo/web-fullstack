def cal(a, b):
    return a + 2 * b


print(cal(3, 5))
print(cal(5, 3))
# 매개변수(parameter)를 지정하지 않고, 인자(argument)값을 줄땐 순서가 중요

print(cal(a=3, b=5))  # 좋은 IDE를 사용하면 parameter 변수명을 알 수있어서 활용할 수 있음
print(cal(b=5, a=3))


def cal2(a, b=3):  # 기본(default) 값을 지정해도, 덮어쓰기 0
    return a + 2 * b


print(cal2(4))
print(cal2(4, 2))
print(cal2(a=6))
print(cal2(a=1, b=7))


def call_names(*args):  # 매개변수(parameter)를 자유롭게 받는 방법
    for name in args:
        print(f'{name}야 밥먹어라~')


call_names('철수', '영수', '희재')


def get_kwargs(**kwargs):
    print(kwargs)


get_kwargs(name='bob')
get_kwargs(name='john', age='27')


# Parameter 혼용 가능
#   단! **가변 키워드 인자는 파라미터의 가장 마지막 요소여야 한다.
def get_kwargs(*args, **kwargs):
    print(kwargs)


get_kwargs('철수', '영수', '희재')
get_kwargs(name='bob')
get_kwargs(name='john', age='27')
get_kwargs('철수', '영수', '희재', name='bob')
