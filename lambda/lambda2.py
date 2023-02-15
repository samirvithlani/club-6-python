def getData(name1):
    
    #lambda local variable....
    x = lambda name: name.upper()
    ans = x(name1)
    return ans

print(getData("raj"))

def getData1(name1):
    
    #lambda local variable....
    x = lambda name: name.upper()
    return x(name1)

print(getData1("raja"))    


    