class Model:
    
    
    
    def setRow(self, row):
        print("setRow(self) method called 1 param")

    def setRow(self, row, col):
        print("setRow(self) method called 2 param")
        
    def setRow(self):
        print("setRow() method called")        


model = Model()            
model.setRow()
