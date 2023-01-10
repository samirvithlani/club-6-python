username = {"amit","raj","jay","neha","shruti","parth","amita"}
username1 = {"amit","raj","jay","neha","shruti","parth","mmmm"}
removedelem = ""

# for i in username:
#     removedelem = username.pop()
#     print(removedelem)

# for i in range(len(username)):
#     removedelem = username.pop()
#     print(removedelem)
    
#usernamecopy = username.copy()    
#print(usernamecopy)
#username.difference_update(username1)
#diff = username1.difference(username)
#print(diff)
#ins = username.intersection(username1)
print("before",username)
username.intersection_update(username1)
print("after",username)

