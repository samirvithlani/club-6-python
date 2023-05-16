class GenricView:
    
    def setView(self):
        print("setView(self) method called")


class View(GenricView):
    
    def setView(self):
        print("setView(self) method called view...")        
        super().setView()
        
        
view = View()
view.setView()        
        
        
# *g = GenricView()
# v = View()

# g = &v
        