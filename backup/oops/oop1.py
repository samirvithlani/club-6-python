#class class is a blueprint for creating new objects

class User:
    
    #instance variable or class variable
    uid = 100
    
    def passData(self):
        print("I am a function with pass data")
        
    def __init__(self,a):
        print("I am a constructor",a)
            
    
    #class object
    def getData(self,a,b):
        #local variable uid is not there
        uid = 200 #local variable...
        print("I am a function")
        print(self.uid) #accessing instance variable
        self.passData() #accessing instance function
        
    print("I am a class")
    print(id)    

#object
#u = User()
u = User(10)
#u.getData()
u.getData(10,23)

    
    