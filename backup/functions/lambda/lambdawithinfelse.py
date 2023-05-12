a = 10
b = 10

result = lambda x,y : f"{x} is smaller than {y}" \
    if x < y else (f"{x} is greater than {y}" if x > y \
               else f"{x} is equal to {y}")


res = lambda x,y : x if (x>y)\
    else(y if x<y else "both are equal")

print(result(a,b))    