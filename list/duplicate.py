list = [10,20,30,10,20,40,45,63,96,10,20]
unique = []
duplicate = []

for i in list:
    # 10,20,30
    if i not in  unique:
        #10 not in [] = True
        #20 not in [10] = True
        #30 not in [10,20] = True
        #unique = []
        unique.append(i)
        #unique = [10]
        #unique = [10,20]
        #unique = [10,20,30]
        
print("Unique list is: ",unique)
