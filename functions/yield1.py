def test():
    yield 100,500 # checkpoint
    yield 200 # checkpoint
    yield 300 # checkpoint
    yield 400 # checkpoint
    
    
x = test() 
for i in x:
    print(i)
    