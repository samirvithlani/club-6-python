def test(a,b,c):
    return a + b + c


def test1(a=0,b=0,c=0):
    return a + b + c

x = test(10,20,30)
y = test1(10,20,45)
print(x)
print(y)

