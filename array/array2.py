#take input from user and add it to array
from array import *

users = array('i',[])


print("enter size of an array")
size = int(input())
'''
no1 = int(input("enter first number"))
users.append(no1)
no2 = int(input("enter first number"))
users.append(no2)
no3 = int(input("enter first number"))
users.append(no3)
no4 = int(input("enter first number"))
users.append(no4)
no5 = int(input("enter first number"))
users.append(no5)
'''
'''
for i in range(0,size):
    x = int(input("enter the number"))
    users.append(x)
'''


for i in range(0,size):
    # 120 x = 120
    # 450 x = 450
    x =int(input("enter number"))
    # users [0] = 120
    #users [1] = 450
    users.append(x)



print(users)


for i in users:
    print(i)

