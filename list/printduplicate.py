list = [10,20,10,20,30,10]
duplicate = []
unique =[]
for i in list:
    # 10 not in unique TRUE
    #20 not in unique TRUE
    #10 not in unique FALSE
    #20 not in unique FALSE
    #30 not in unique TRUE
    #10 not in unique FALSE
    if i not in unique:
        unique.append(i)
        # unique = [10,20,30]
        
    elif i not in duplicate:
        duplicate.append(i) 
        # duplicate = [10,20]   
        
print("duplicate list is: ",duplicate)