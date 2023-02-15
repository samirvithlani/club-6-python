#lambda: lambda is function without name
# def printing():
#     print("hello")

# printing()    
    
x = lambda:print("hello")
x()

y = lambda name: print(name)
y("raj")
convname = lambda name: name.upper()
p = convname("raj")
print(p)

sum = lambda a,b: a+b
print(sum(10,20))

data = lambda a,b :print("a is greated") if a>b else print("b is greater")
data(10,2)

#data1 = lambda a,b : a if a>b else b

#loop with lambda


