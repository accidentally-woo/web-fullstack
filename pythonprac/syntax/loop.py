fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    if person['age'] > 20 :
        print(person)

fruits = ['사과', '배', '감', '귤','귤','수박','참외','감자','배','홍시','참외','오렌지']

for i, fruit in enumerate(fruits):
    print(i,fruit)

for i, fruit in enumerate(fruits):
    print(i, fruit)
    if i == 4:
        break