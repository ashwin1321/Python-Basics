# Multilevel Inheritance:

class Dad:                                              # this is the parent class for all the other classes below
    basketball =6

class Son(Dad):                                         # it has all the access to the attributes and methods of the class dad
    dance =1
    basketball = 9                                      # this is the overriding case as the varible is already defined in the class dad
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):                                   # it has all the access to the attributes and methods of the class dad and son
    dance =6
    guitar = 1                      

    def isdance(self):                                
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())                                  # this prints the return value in the function indance, as harry is the object of the class grandson, if the function isdance was not defined in this class the it would have returned value from its parent class son.