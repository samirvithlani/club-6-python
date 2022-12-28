number = [1,2,3,4,5,6,7,8,9,10]
even_list =[]

'''
for i in number:
    if i %2 ==0:
        even_list.append(i)

print(even_list)        
'''

even_list = [i for i in number if i %2 ==0]
print(even_list)