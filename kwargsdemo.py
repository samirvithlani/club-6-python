def getData(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)

getData(name="Ravi", age=23, city="Pune", salary=10000)

def printData(*args):
    print(args)

printData(12,45,78,96,"rajesh", "ravi", "suresh")    
