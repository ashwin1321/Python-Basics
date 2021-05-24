# Multiple Inheritance:  

class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:                                           # another class
    var = 9
    no_of_games = 4
    _av = 56
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):              # in multiple inheritance, we can have multiple class as an argument to another new class
    # but when this class is mentioned or anything is done, it utilizes the methods and attributes of first class argument if there are same attributes in both of the functions. Else, it uses the called attibutes and method no matter in which class it is.

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])              
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
print(karan.printdetails())