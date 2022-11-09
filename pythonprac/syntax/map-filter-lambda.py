people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 11},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]


def check_adult(person):
    if person['age'] > 20:
        return '성인'
    else:
        return '청소년'


result = map(check_adult, people)
print(list(result))


def check_adult2(person):
    return '성인' if person['age'] > 20 else '청소년'


result2 = map(check_adult2, people)
print(list(result2))


result3 = map(lambda x: ('성인' if x['age'] > 20 else '청소년'), people)
print(list(result3))