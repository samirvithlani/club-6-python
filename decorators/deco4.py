def smartDiv(func):
    
    def inner(a,b):
        if b ==0:
            print("Can't divide by zero")
        else:
            print("Dividing",a,"and",b)
            func(a,b)
    
    return inner


@smartDiv
def calc(a,b):
    print("Result is",a/b)            

calc(10,0)    