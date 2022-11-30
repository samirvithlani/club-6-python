#array is an group of similar kind of data types....

#how to define an array
from array import *


users = array('d',[10,20,30,40,50,45,78,63,56,45])
sum=0
#print(len(x))

for i in range(0,len(users)):
    #print(i)
    sum = sum + users[i]
    print(users[i])


'''
for i in users:
    sum = sum + i
    print(i)
'''
print("sum of all elements in array is ",sum)    