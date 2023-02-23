class Employee:
    
    name = "Ravi" #class variable  instance variable
    salary = 50000 #class variable  instance variable
    #self is nothing but a reference variable of class
    def display(self,no):
        #local variable....
        salary = 10000
        #print(name) error
        print(self.name)
        print("Hello",no)
        print("Salary is",salary)
        print("Salary is",self.salary)


#need to create an object  class

emp = Employee()
emp.display(10)