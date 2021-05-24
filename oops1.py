# CLASSES --> Template, blueprint, premade
# OBJECT -->  Instance of the class 

# OOP uses DRY (Do not Repeat Yourself) concept 

#making  a class
'''
class student:
    pass

#object
Ashwin = student()
Harry = student()

Ashwin.name = "Ashwin"
Ashwin.std = 12
Ashwin.sec = "A"
print(Ashwin.std)
'''


class Employee:
    no_of_leaves = 8                                    # variable in class, available for all objects
    pass

Ashwin = Employee()
Harry = Employee()

# variable in objects, accessible only for respective objective

Ashwin.name = "Ashwin"                              
Ashwin.sal = 12346

Harry.name = "Harry"
Harry.salary = 20000

print (Ashwin.sal)                                     # .name is a object variable, so it prints element in object
print(Ashwin.no_of_leaves)                              # .no_of_object is a class variable 
# print(Harry.sal)                                        # sal is not a variable of object Harry, so it doesnot print
print(Harry.no_of_leaves)                               # class variable is accessible for all the objects 

print(Harry.__dict__)                                   # Prints all the attributes of harry in dictionary

print(Employee.no_of_leaves)                             # we can print elements using same class name as well


Employee.no_of_leaves = 9                               # to update the value, we have to use the (class_name.variable_name)

print(Employee.no_of_leaves)