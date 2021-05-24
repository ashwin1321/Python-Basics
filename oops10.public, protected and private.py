class Employee:
    no_of_leaves = 8                                                # This is a public variable having access for everybody inside a class
    var = 8
    _protec = 9                                                     # we write a protected variable by writing "_" before a variable name. Its accessible to all the child classses
    
    __pr = 98                                                       # this is a private  variable. we write this by writing "__" before a variable name

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("harry", 343, "Programmer")

print(emp._Employee__pr)                                    # to access the private class we use ( ._"Class_name"__"private variable")