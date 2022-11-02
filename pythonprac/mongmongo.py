from pymongo import MongoClient
import certifi

ca = certifi.where()

# mongodb 연결 실패하시는 분들 주목
client = MongoClient('mongodb+srv://비밀보안:비밀보안@cluster0.aauayqq.mongodb.net/woo?retryWrites=true&w=majority', tlsCAFile=ca)
# mongodb에서 애플리케이션 연결시 제공하는 주소 : mongodb+srv://계정:<password>@cluster0.aauayqq.mongodb.net/?retryWrites=true&w=majority
# ** 이 주소값에 계정, 비밀번호, 사용할 db이름이 들어가야합니다 **

# mongodb+srv://계정:<password>@cluster0.aauayqq.mongodb.net/만드는DB이름?retryWrites=true&w=majority
# -> 계정, <password> mongodb사이트에서 생성한 계정, 패스워드 값으로 변경
# url~ /만드는DB이름?retryWrites=true&w=majority -> 만들고자하는 db명을
# 작성 저는 'woo'로 만들었기떄문에 ~(생략)~mongodb.net/woo?retryWrites=true&w=majority
db = client.woo


# doc = {
#     "name":"bob",
#     "age":27
# }
#
# db.users.insert_one(doc)

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# 모든 데이터 뽑아보기
# all_users = list(db.users.find({},{'_id':False})) # id 속성 빼고 조회
all_users = list(db.users.find({})) # 전체 조회

print(db.users.find_one({"name":"bob"}))
print("~~~~")
print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

# 활용 뚜둘
all_ages = list(db.users.find({}, {'_id': False, 'name': False}))
[print(x) for x in all_ages] # python comprehension

print("~~~~")

for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(user)

print("~~~~")

user = db.users.find_one({'name':'bobby'})
print(user)

# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)

# db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user) # Node

# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})