def test1(txt):
    print("test1 called",txt)

def test2(txt):
    print("test2 called",txt)
    
# def driver(a):
#     # a+100
#     # a.too

def sum(a,b):
    print(a+b)
    
# def driver(test1):
#     test1()

def driver(func):
    func("ok")

driver(test1)


#sum(10,20)