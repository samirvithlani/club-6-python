sqaureList =[]

'''
for i in range(1,11):
    sqaureList.append(i**2)

print(sqaureList)    
'''

sqaureList = [i**2 for i in range(1,11)]
print(sqaureList)

charlist =[]

name = "royal"
'''
for i in name:
    charlist.append(i)
    
print(charlist)    
'''

charlist = [i for i in name]
print(charlist)



oddNumlist = [i for i in range(1,20) if i % 2!=0 or i % 3 ==0]
print(oddNumlist)
