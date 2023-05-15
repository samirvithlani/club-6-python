
#1 parent class and many child class
#many parent 1 child...

#1 parent class 1 child class
class Cricket:
    
    overs =20  #class variable , instance variable
       
    def getMatch(self):
        print("Cricket Match")


class IPL(Cricket):        
    
    def getIPLMatch(self):
        print("IPL Match")
        print("IPL Match overs",self.overs)
  
class BBL(Cricket):
    
    def getBBLMatch(self):
        print("BBL Match")
        print("BBL Match overs",self.overs)
        


ipl = IPL()
ipl.getMatch() #child class object accesing paret class method
ipl.getIPLMatch() #child class object accesing child class method

#if we want call getMatch function need to create an object of Crieckt class or we can call with ipl class's object
#if we want call getIPLMatch function need to create an object of IPL class        

bbl = BBL()
bbl.getMatch() #child class object accesing paret class method
bbl.getBBLMatch() #child class object accesing child class method