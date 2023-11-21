def isManager(func):
    manager = False
    def inner():
        if manager == True:
            print("Manager is calling")
            func() #allUsers()
        else:
            print("Not a manager")
            
    
    return inner


@isManager
def allUsers():
    print("All users called..")            


allUsers()        