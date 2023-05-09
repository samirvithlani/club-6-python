# users = {1:("raj","raj@gmail.com"),2:("ram","ram@gmail.com")}

# for i, j in users.items():
#     print(i)
#     for x in j:
#         print(x)
        
sales = {1:[100,80,75],2:[80,56,90],3:[90,80,70],4:[100,90,80],5:[90,80,70],6:[100,90,80],7:[90,80,70]}
salessum=[]
sum =0

for i,j in sales.items():
    print(i)
    for x in j:
        sum = sum +x
        print(sum)
    salessum.append(sum)
    sum=0    

print(salessum)        

max =0
ind =0

for i in salessum:
    if i>max:
        max =i
        ind = salessum.index(i)

print("max sales is...",max,"for month...",ind+1)        
        