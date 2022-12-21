list = [10,20,10,20,30]
duplicate = []
unique =[]
for i in list:
    #10
    # 10 not in [] = True
    # 20 not in [10] = True
    # 10 not in [10,20] = False
    # 20 not in [10,20] = False
    # 30 not in [10,20] = True
    if i not in unique:
        #unique = []
        #unique = [10]
        #unique = [10,20]
        unique.append(i)
        #unique = [10]
        #unique = [10,20]
        #unique = [10,20]
        #unique = [10,20,30]
        
    elif i not in duplicate:
        #duplicate = []
        duplicate.append(i)    
        #duplicate = [10]
        #duplicate = [10,20]

print("duplicate list is: ",duplicate)