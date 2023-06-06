
file = open("filehandling.txt","r")
# for i in file:
#     print(i)

print(file.read())

cnt=0
file1 = open("sum.txt","r")
for i in file1:
    cnt+=1
    print(i)

print("Total lines in file:",cnt)    