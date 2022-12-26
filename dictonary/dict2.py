# languages ={}
# languages['python'] = 'a dynamic object-oriented programming language'
# languages['ruby'] = 'a dynamic, reflective, object-oriented, general-purpose programming language'
# languages['perl'] = 'a family of high-level, general-purpose, interpreted, dynamic programming languages'
# languages['java']= 'a general-purpose computer-programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible'

# for i,j in languages.items():
#     print(i,j)


languages ={}
size = int(input("Enter the size of dictonary:"))

for i in range(size):
    k = input("Enter the key:")
    v = input("Enter the value:")
    languages[k] = v
    
print(languages)    

#languages.clear()
#print(languages.get('c'))
#None

#pop
#poped_elem = languages.pop('c')
poped_item = languages.popitem()
print("removed element value...",poped_item)
print(languages) 
    
