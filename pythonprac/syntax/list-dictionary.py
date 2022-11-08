# list : 순서가 있는 다양한 자료형들의 모임
a = [1, 5, 2]
print(len(a))

# 순서가 있기 때문에 슬라이싱, 인덱싱 사용가능
print(a[2])
print(a[-1])
print(a[1:2]) # -> [5] list가 반환됨
print(a)

# 리스트 붙이기
a.append(7)
print(a)

a.append([0, 0]) # append 파라미터는 바로 하나의 인자로 넘어감.
print(a)

a += [8, 1] # 연산은 리스트간 결합이 일어남.
print(a)

a.remove([0,0])
print(a)
# 정렬
print(a.sort()) # None 반환값없음. a 데이터를 직접 변경

print(a)

a.sort(reverse=True)
print(a)

# 요소가 리스트 안에 있는지 알아보기
b = [2, 1, 4, "2", 6]
print(1 in b) # True
print("1" in a) # False
print(0 not in a) # True

# Dictionary
person = {"name":"Bob", "age": 21}
print(person["name"])

# 딕셔너리를 만드는 다양한 방법
a = {"one": 1, "two": 2}

# 빈 딕셔너리 만들기
a = {}
a = dict()

# 딕셔너리의 요소에는 순서가 없기 때문에 인덱싱을 사용할 수 없다.
person = {"name":"Bob", "age": 21}
# print(person[0]) KeyError
print(person["name"])

# 딕셔너리 값 업데이트하거나 새로운 쌍의 자료를 넣을 수 있다.
person["name"] = "Woo"
print(person)

person["height"] = 163
print(person)

# 딕셔너리의 밸류로는 아무 자료형이나 넣을 수 있다.
person = {"name":"Alice", "age": 16, "scores": {"math": 81, "science": 92, "Korean": 84}}
print(person["scores"])             # {'math': 81, 'science': 92, 'Korean': 84}
print(person["scores"]["science"])  # 92

# 딕셔너리 안에 해당 키가 존재하는지 알고 싶을 때는 in 사용
print("name" in person)
print("email" in person)
print("phone" not in person)

# list 와 dictionary 의 조합
people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]

# people[0]['name']의 값은? 'bob'
print(people[0]["name"])
# people[1]['name']의 값은? 'carry'
print(people[1]["name"])

person = {'name': 'john', 'age': 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20}, {'name':'carry','age':38}, {'name':'john','age':7}]
print(people)
# people[2]['name']의 값은? 'john'
print(people[2]['name'])