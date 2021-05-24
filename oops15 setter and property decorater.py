class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property                                                       # using property decorator, it makes the class a attribute. so, whenever we call the function we dont need to use () after its name
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@abcd.com"

    @email.setter                                                   # this is a setter. we cannot change the constructor attribute yetikai, so we use setter to do so
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]                            
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter                                                 # this is a deleter, to delete the set value
    def email(self):
        self.fname = None
        self.lname = None


Naame = Employee("Ashwin", "Khatiwada")


print(Naame.email)

Naame.fname = "US"

print(Naame.email)
Naame.email = "this.that@abcd.com"                                # this is done form setter 
print(Naame.fname)

del Naame.email
print(Naame.email)
Naame.email = "Ashwin.khatiwada@abcd.com"
print(Naame.email)

