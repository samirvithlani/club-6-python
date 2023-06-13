sqr = lambda a: a*a
ans = lambda fn,x : fn(x)

x = ans(sqr,10)
print(x)


#royal enfield
#title case , upper case

name = lambda a: lambda b: a.title() + b.upper()

x = name("royal")("enfield")
print(x)

# pass a number if number is even return square of that number and odd return cube of that number

x = lambda a : a*a if  a %2 == 0 else a*a*a
print(x(10))

sqr = lambda a: a*a
cube = lambda a: a*a*a

x = lambda c: sqr(c) if c %2 == 0 else cube(c)
print(x(10))


