#() tuple
#[] list
#{} dictionary
#{set}

#if first param is args
def data(x,*values):
    print(values)
    print("x",x)
    for i in values:
        print(i)

data("ram","raj","ravi","rakesh")    