data = [11,22,33,44,55,66,77,88,99,100]
dict1 ={}

    
# for i in range(1,len(data)):
#     if i % 2 == 0:
#         dict1[i] = data[i-1] **2
    
#dic = [i for i in range(1,len(data)) if i % 2 == 0] ] 
dict1 ={i:i **2 for i in data if i % 2 == 0}

print(dict1)
#{2:4,4:16,6:36,8:64,10:100}