class Gov:

    tax = 18
    
    def __init__(self):
        print("Gov class const")
        
    print("Gov class")
    

class State(Gov):
    
    grant =12000
    
    def __init__(self):
        print("tax = ",self.tax)
        print("State class const")
        
    print("State class")
    

class City(State):
    
    def __init__(self):
        print("grant = ",self.grant)
        print("City class const")
        
    print("City class")
    


city = City()

            