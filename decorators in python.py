#                                                       DECORATORS IN PYTHON           

# --> modify the functionality of a function 
'''

def func():
    print("hello")

func2 =func                                 # assigning func in func2
func2()                                     # executes the content in func 

del func                                    # deleting the func
func2()                                     # even though we deleted func, as we already assigned func in func2, func2 already contains the content in func. So, it executes



# function inside a function

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = funcret(1)
print(a)



# returning a function through a function . Using a function as a argument

def abc(func):
    func('this')

abc(print)
'''


# Example:

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1                                               # @dec1 works same as  who_is_who = dec1(who_is_who)

def who_is_who():
    print("He is a good boy")

# who_is_who = dec1(who_is_who)

who_is_who()
