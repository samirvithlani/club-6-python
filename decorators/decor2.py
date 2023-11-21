def loginRequired(func):
    
    def inner(flag):
        print("Checking login")
        print("flag value",flag)
        if flag == True:
            print("Logged in")
            func(flag) #getData(True)
        else:
            print("Not logged in")
    
    return inner            
        


@loginRequired
def getData(flag):
    print("Getting data from DB")
    


getData(True)    
    