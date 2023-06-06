file =open("sum.txt","r")
data  = file.readlines()
for i in data:
    word = i.split()
    print(word)

#str to int
str = "100"
x = int(str)
print(x)
print(type(x))    