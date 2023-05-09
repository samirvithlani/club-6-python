data ={1:"java",2:"python",3:"c",4:"c++",5:"c#"}

print(data)
print(data[1])
print(data.items())

x = data.get(1)
print(x)

#you have to pass key
removevalue = data.pop(3)
print("remove value...",removevalue)

remitem = data.popitem()
print("remove item...",remitem)

print(data.keys())
print(data.values())

data.update({11:"JAVA"})

copydic = data.copy()
print("copy dic...",copydic)

list =[1,2,3,4,5,1]
newdic = data.fromkeys(list,"python")
print("new dic...",newdic)

for i,j in data.items():
    print(i,"-",j)
    
    
    
    