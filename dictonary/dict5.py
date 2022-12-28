users ={1:("raj","jay","ajay"),2:("ram","man","ravi")}

# user = tuple
user = users.get(1)
#list
userList = list(user)
#list append
userList.append("sachin")
#user[1] ("raj","jay","ajay","sachin")
users[1] = tuple(userList)
print(users)

