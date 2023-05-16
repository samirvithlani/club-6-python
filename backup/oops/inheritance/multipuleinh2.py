class Graph:
    
    xaxis = 0
    yaxis = 0
    
    def __init__(self):
        print("Graph class const")
    
    def setXaxis(self,xaxis):
        self.xaxis = xaxis
     
    def setYaxis(self,yaxis):
        self.yaxis = yaxis        
    
    def getXaxis(self):
        return self.xaxis
    
    def getYaxis(self):
        return self.yaxis
    
    def demo(self):
        print("Graph class demo")



class Model:
    row = 0
    col = 0
    
    def __init__(self):
        print("Model class const")
    
    def setRow(self,row):
        self.row = row
    
    def setCol(self,col):
        self.col = col    
    
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col    
    
    def demo(self):
        print("Model class demo")
        

class View(Model,Graph):
    
    
    def __init__(self):
        print("View class const")
     
    def generateTable(self):
        print("Table generated with ",self.row," rows and ",self.col," columns")
    
    def genTableWithFunction(self):
        rows = self.getRow()
        cols = self.getCol()
        print("Table generated with ",rows," rows and ",cols," columns")        
    
    
    def setRowsAndCols(self):
        self.setRow(10)
        self.setCol(5)
        
    def setXandY(self):
        self.setXaxis(5)
        self.setYaxis(5)
    
    def genGraph(self):
        xaxis = self.getXaxis()
        yaxis= self.getYaxis()
        print("Graph generated with ",xaxis," rows and ",yaxis," columns")            


view = View()
view.setRowsAndCols()
view.generateTable()
view.genTableWithFunction()     
view.setXandY()
view.genGraph()
view.demo()
   