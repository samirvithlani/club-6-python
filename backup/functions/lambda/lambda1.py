name = "royal"
name = name[::-1]
name = name.upper()
print(name)


rv_up = lambda x: x[::-1].upper()
print(rv_up("royal"))


ans = lambda x,y : x+y
print(ans(10,20))

avg = lambda a,b,c : (a+b+c)/3
print(avg(10,20,30))

def findMax(*args):
    x =max(args)
    print(x)

def findMaxLen(*args):
    x = max(args,key=len)
    print(x)

findMax(10,20,30,40,50,60,70,80,90,100)
m = lambda *args : max(args)
print(m(10,20,30,40,50,60,70,80,90,100,99))

findMaxLen("sachin","rajata","rajesh","suresh","ramesh","raj","zara")

ml = lambda *args: max(args,key=len)
print(ml("sachin","rajata","rajesh","suresh","ramesh","raj","zara"))    
    
