##[]
#()

#indexing [0]
data = ("java","python","c++","c#","java")

for i in  data:
    print(i)
    
#data[0] = "JAVA" error

cnt = data.count("java")
print("count of java is ",cnt)

ind = data.index("java")
print("index of java is ",ind)

#data.__add__(("php",".net")) error...tuple is immutable
cls1 = ("java","python","c++","c#")
cls2 = ("php",".net")


cls3 = cls1 + cls2
print(cls3)