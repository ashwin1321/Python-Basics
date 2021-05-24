
class A:
    classvar1 = "This is the variable in class A."
    v =23
    def __init__(self):
        self.var1 = "This is inside a class A constructor"
        self.classvar1 = 'Instance variable in class A'
        self.s = 123


class B(A):                                                     # B is inherited class of A
    classvar2 = "This is the variable in class B."
    v =4                                                        # this is the overriding case for class B. when v is accessed by the methods or instances in B, it uses this value instead of the value in the parent class.

    def __init__(self):

        super().__init__()                                      # using this we can access the not mentioned attibute in the overriden function
        # --> If it is written at last of the function, then all the overriden get cancelled or it prints the above function attributes,  if there is same attributes in both functions

        self.var1 = "This is inside a class B constructor"
        self.classvar1 = 'Instance variable in class B'


a= A()
b = B()

print(b.classvar1)                                          # this prints the instance variable inside the constructor. If there is no instance varible in the constructor it checks in the class variables.

print(b.c)                                                  # this throws an ERROR, as the init function is already override in class B so , if there is no attribute in the overriden function, it doesnot check the overrided function in the base class.

# --> But, if super().__init__() is used inside the override function, it can access all the attribute if the called attribute is not in  the function that is overriden.