
class Employee:
    no_of_leaves = 8                                                     # variable in class, available for all objects

    def __init__(self,aname, asalary) :                                  # __init__ is a constructor. Using this we can take argument in a class

        self.name = aname                                                # here, aname and asalary are the arguments. AND name and salary are the object instances.
        self.salary = asalary


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}"           # using self keyword we can access the attributes and methods of the class 


Ashwin = Employee("Ashwin Khatiwada",12345)                         # this works for __init__ function. if there's no __init__ it doesnt take argument and throws error
# Where self = Ashwin, aname = Ashwin Khatiwada, asalary = 12345
print(Ashwin.name)

# Ashwin = Employee()
# Harry = Employee()

# Ashwin.name = "Ashwin"                              
# Ashwin.salary = 12346

# Harry.name = "Harry"
# Harry.salary = 20000
# print(Harry.printdetails())                                               # here Harry is used in the place of self in this function                           
                                            
