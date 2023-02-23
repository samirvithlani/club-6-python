class Calc:
    
    no = 100
    def sum(self,a,b):
        self.no = self.no + a+b
        return self.no


c = Calc()
x = c.sum(15,25)    
print(x)
        
        
    
