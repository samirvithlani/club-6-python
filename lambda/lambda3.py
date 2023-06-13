res = lambda a: print(a)
res(10)

res1 = lambda a,b: a+b
print(res1(10,20))

ans = lambda a,b: lambda c: a+b+c

#ans1 it is a function
# ans1 = ans(100,200)
# ans2 = ans1(300)
# print(ans2)

x = ans(100,200)(400)
print(x)
