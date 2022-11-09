# if 삼항 연산자
num = 3

if num % 2 == 0:
    result = "짝수"
else:
    result = "홀수"

print(f"{num}은 {result}입니다.")

# 같은 결과
num = 3

result = "짝수" if num % 2 == 0 else "홀수"

print(f"{num}은 {result}입니다.")

# for 문의 단축표현 comprehention
a_list = [1, 3, 2, 5, 1, 2]

b_list = []
for a in a_list:
    b_list.append(a * 2)

print(b_list)
# 위 for문은 comprehention으로 짧게 만들기
a_list = [1, 3, 2, 5, 1, 2]

b_list = [a * 2 for a in a_list]

print(b_list)
