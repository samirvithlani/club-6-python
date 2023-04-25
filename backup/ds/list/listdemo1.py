#blank list
#list allows duplicate values
#list allows different data types
#list allows indexing
#list allows slicing
#list allows negative indexing
#list allows negative slicing
#list allows nested list
#list is mutable
#list is ordered
#list is dynamic
#list is iterable

#users = []
users = [12,22,34,56,78,12,3,4]
print(users)
users.append(100)
print(users)
users.extend([200,300,400])
print(users)
users.insert(0,1000)
print(users)
users[0]=1001
print(users)
users.sort()
print(users)
#users.remove(1011) error
ind = users.index(200)
print(ind)
pops = users.pop() #last element
pops = users.pop(1) #index 1
print(pops)
users.reverse()
print(users)
cnt = users.count(122)
print(cnt)
usercopy = users.copy()
print(usercopy)
