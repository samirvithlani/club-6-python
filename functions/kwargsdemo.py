#kwargs
#it will accept any number of keyword arguments
#it will accept any number of keyword arguments
#it will accept any number of keyword arguments and store it in dictionary

def getData(no,**kwargs):
    print(no)
    print(kwargs)
    

getData(15,name="raj",age=25,city="pune",mob=1234567890)