# dunder methods are the special functions in Python

# --> dunderfunctions are used by using "__DunderMethod_name__"  inside a class 
# --> to know more about dunder method names, GOOGLE IT 

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):                                       # this is a dunder method
        return self.salary + other.salary

    def __truediv__(self, other):                           
        return self.salary / other.salary

    def __repr__(self):                                             # function returns a printable representational string of the given object. It executes first if it is present in the class and str is not present and method is not called in print statement

       return f"Employee('{self.name}', {self.salary})"

    def __str__(self):                                              #  if method is not called in the function and only object is called like below then this runs
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")

print(emp1)