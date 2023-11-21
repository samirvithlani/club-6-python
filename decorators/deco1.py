'''
    decorators are used to modify the behavior of function or class without changing the source 
    code of the function or class itself.
    
    decorators are used to add functionality to an existing code.
    
    decorators can use with @ symbol.
    
    Points to remember:
    inside decorator function, we can define any number of inner functions.
    inside inner function, we can call the original function using function name.
    inside decoraor param function, we can pass any number of arguments.
'''

def order_pizza(func): #func - throw_party
    
    def inner():
        print("Ordering pizza")
        func() #throw_party()
    
    return inner    
        


@order_pizza
def throw_party():
    print("Throwing a party")
    


throw_party()    

