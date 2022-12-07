from array import *

a = array('i',[])
size = int(input("enter size of an array"))

for i in range(0,size):
    x = int(input("enter number"))
    a.append(x)
    

for i in a:
    print(i)    
    
elem = int(input("enter element to search"))

flag =0
index =0
#[10,12,45,36,96]
#12
for i in range(0,len(a)):
    #0 10
    #1 12 True
    #75 false
    #12 false 
    if elem == a[i]:    
        index = i #index =4
        flag =1
        break


if flag ==1:
    print("element found at ",index+1)
else:
    print("element not found")    