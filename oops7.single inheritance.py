# We can access all the function in the parent class and also add the needed function in the child class 

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = languages

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

class Programmer(Employee):                                     # Programmer class inherit all the property of class Employee

    def __init__(self, aname, asalary, arole,languages):
        super().__init__(aname, asalary, arole,languages)       # super() le mathi ko inherited class ma bhako constructor ko sabai kura linxa
       

    def printprog(self):                                        # we can create other function inside a inherited class as well

        return f"The Programmer Name is {self.name}. Salary is {self.salary} and role is {self.role}. The languages are {self.language}."
    pass

harry = Employee("Harry", 255, "Instructor","Python")
rohan = Employee("Rohan", 455, "Student",'python')

subham = Programmer("Subham", 553543, "programmer",['python'])
Ashwin = Programmer("Ashwin", 4345543, "programmer", ['python'])

print(Ashwin.printprog())