def display():
    print("Hello World")


def value():
    return 150

def sum(a,b):
    return a + b

display()
x = value()
print(x)

ans = sum(15,25)
print(ans)
print(sum(100,200))
    
    
def convert(name):
    if len(name)> 3 and name.lower():
        name = name.upper()
        return name
    
    return name
    

print(convert("SAC"))