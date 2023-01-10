users = [("usa","uk"),("india","china"),("japan","korea")]
print(users)
#users.append(("russia","france"))
data = users[0] 
data = data + ("russia","france")
users[0] = data
print(users)


emp = (("abc","xyz"),("pqr","lmn"),("stu","vwx"))
print(emp)


for e in emp:
    for x in e:
        print(x)


students = (["amit","raj"],["parth","jay"],["amita","rani"])

#students[0].insert(1,"amita")
#tuple modified....
students[0] = ["amit","raj","amita"]

for i in students:
    for j in i:
        print(j)