data = [[12,2],[23,32],[12,42],[7,26],[12,22,22],[12,22,45,78,96]]

#data.insert(0,[14,55])
data[1].insert(1,15)

#i = 0
for i in range(0,len(data)):
    # i = 0
    # i = 1
    for j in range(0,len(data[i])):
        # j =0
        # j =1
        print(data[i][j],end=" ")
        #[0][0]
        #[0][1]
        #[1][0]
        #[1][1]
    
    print("\n")    