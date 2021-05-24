# CLASS METHODS

class Employee:
    no_of_leaves = 8                                                     # variable in class, available for all objects


    def __init__(self,aname, asalary) :                                  # __init__ is a constructor. Using this we can take argument in a class

        self.name = aname                                                # here, aname and asalary are the arguments. AND name and salary are the object instances.
        self.salary = asalary


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}"           # using self keyword we can access the attributes and methods of the class 


# ----> Here, we cannot change the class variable from the object. So, we can use class method to update the variable through a object 

    @classmethod
    def change_leaves(cls,newleaves):                           # here, cls is the class   i.e Employee in this case      
        cls.no_of_leaves = newleaves


Ashwin = Employee("Ashwin Khatiwada",12345)                         # this works for __init__ function. if there's no __init__ it doesnt take argument and throws error
# Where self = Ashwin, aname = Ashwin Khatiwada, asalary = 12345
Harry = Employee("Harry Kafle",23452)


Ashwin.change_leaves(12)                                        # --> here we can change the value in variable in a class through a class method. here cls is reffered as instance Ashwin and argument newleaves is given

print(Ashwin.name)                     
                                       
print(Ashwin.no_of_leaves)