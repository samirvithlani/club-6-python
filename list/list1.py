users = ["John", "Paul", "George", "Ringo","John","John"]

users.append("Ravi")
users.insert(1,"hari")
users.extend(["mohan","sohan"])
#removedElm = users.pop(1)
#print("removing....",removedElm)
users.sort()
c = users.count("Johny")
ind = users.index("John")
print("index ->",ind)
print(c)
#users.clear()

users1 = users.copy()
print(users1)







l = len(users)
for i in range(0,l):
    print(users[i])

# for i in  users:
#     print(i)