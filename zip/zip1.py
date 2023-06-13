list1 =[1,2,3,4,5]
list2 =[11,22,33,44,55]
dict1 ={}
for i,j in zip(list1,list2):
    dict1[i] = j
print(dict1)    

#royal
#r:R o:O y:Y a:A l:L

str = "royal"
dict2 ={}
for i in str:
    dict2[i] = i.upper()    
print(dict2)
    
    