#["ram sita","lakshman","love kush"," amit"]

def sumofDigit(n):
    sum =0
    for i in str(n):
        sum+=int(i)
    
    if sum >10:
        return True
    
    else:
        return False    
    

data=[1234,5678,9087,56444,3222]

x = list(filter(lambda x : sumofDigit(x),data))
print(x)

