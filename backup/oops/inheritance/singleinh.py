#1 parent class 1 child class
class Cricket:
    
    overs =20  #class variable , instance variable
    
    def __init__(self):
        print("Cricket class constructor")
       
    def getMatch(self):
        print("Cricket Match")


class IPL(Cricket):        
    
    # def __init__(self):
    #     print("IPL class constructor")
    
    #call parent class constructor explicitly
    
    def __init__(self):
        super().__init__() #it will call parent class constructor explicitly
        print("IPL class constructor")
            
    def getIPLMatch(self):
        print("IPL Match")
        print("IPL Match overs",self.overs)
        


#object of child class
ipl = IPL()
ipl.getMatch() #child class object accesing paret class method
ipl.getIPLMatch() #child class object accesing child class method

#if we want call getMatch function need to create an object of Crieckt class or we can call with ipl class's object
#if we want call getIPLMatch function need to create an object of IPL class        