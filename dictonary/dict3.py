dict1 ={1:'sachin',2:'saurav',3:'rahul',4:'virat',5:'sachin'}
dict2 = {6:'Dhoni'}


dictlist = dict1.values()
print("....",dictlist)

dictItems = dict1.items()
print("....",dictItems)

dictKeys = dict1.keys()
print("....",dictKeys)


print("before update ")
print(dict1)
print(dict2)

dict1.update(dict2)
print("before update ")
print(dict1)
print(dict2)