#@classMethod decorator
#class method is bound to class only not to object
#this method can be called by class name or object name
#class method can access class variable only not instance variable
class Employee:
    
    def getemp(self):
        print('Employee  method')
    
    @classmethod
    def empSalary(self,salary):
        print('Employee salary is',salary)
        print('Employee class is',self)

    @staticmethod
    def empAge():
        print("static")
        #print('Employee age is',age)
        #print('Employee class is',cls)

e = Employee()
e.getemp()
e.empSalary(10000)
Employee.empSalary(20000)
#Employee.empAge(25)        
#e.empAge(30)
            