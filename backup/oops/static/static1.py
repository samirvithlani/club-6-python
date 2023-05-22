class Student:
    #static variable
    stream = 'cse'  # class variable
    
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

a = Student('Rahul',2)
b = Student('Rohit',3)

print(a.stream)        
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

print(Student.stream) # class variable can be accessed using class name also
print(Student.name) # instance variable can not be accessed using class name

