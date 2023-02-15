

def check1():
    print("check1")
    return True

def check2():
    print("check2")
    return False


def isValid(func):
    return func()

age = int(input("Enter age: "))

if age>18:
    flag =isValid(check1)
    if(flag == True):
        print("Eligible")
    
else:
    flag1 = isValid(check2)
    print(flag1)
    if flag1 == False:
        print("Not eligible")
    