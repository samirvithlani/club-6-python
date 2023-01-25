#args function
#variable length arguments
#only 1 param allowed while *args is used 
#if more param needs to add args should be last param

def sum(no,no1,*args):
    print(args)
    print("no1",no1)
    print("no",no)
    for i in args:
        print(i)


sum(12,25,63,96,78,52)    