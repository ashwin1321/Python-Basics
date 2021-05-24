# CLASS METHOD AS ALTERNTIVE CONSTRUCTOR

class Employee:
    no_of_leaves = 8                                 # variable in class, available for all objects

    def __init__(self, aname, asalary):              # # __init__ is a constructor. Using this we can take argument in a class

        self.name = aname                            # # here, aname and asalary are the arguments. AND name and salary are the object instances.
        self.salary = asalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}"          # using self keyword we can access the attributes and methods of the class


# ----> Here, we cannot change the class variable from the object. So, we can use class method to update the variable through a object


    @classmethod
    def change_leaves(cls, newleaves):              #  # here, cls is the class   i.e Employee in this case
        cls.no_of_leaves = newleaves

    @classmethod                                    # USING AS A ALTERNATIVE CONSTRUCTOR
    def abc(cls,string):
        para = string.split("-")                    # - aayo bhane string lai split handinxa
        return cls(para[0], para[1])

        # return cls(*string.split("-"))            # works same as above two line does       

    
Ashwin = Employee("Ashwin Khatiwada",12345)         # works from __init__ function

Ashwin.change_leaves(12)                            # we can change the class variable through a instance using classmethod        

Harry = Employee.abc("Harry-24513")                             

# print(Harry.salary)