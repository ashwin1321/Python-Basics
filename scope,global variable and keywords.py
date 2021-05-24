# Scope, Global Variable and Global Keyword

'''
l = 10                           # this is a global variable
a =5

def function1(n):
    l = 5                        # local variable
    m = 2

    # a += 4                     # this throws an error, as we cannot change the value of global variable

    m +=1                       # we can change the value in of a local variable
    print(m)
    print(l)                    # this print local value of l as local variable is given, else it prints the declared golbal variable l

    print(n,"hello")

function1("Ashwin")

print(l)                        # this print global value of l
'''



def first():
    x = 20
    def second():
        a =2
        global x                # it makes x a global variable, but it doesnot exixt if there is already a local variable named x
        x =32
        print('after calling second()',a)

    print('before second()',x)              # it prints the local variable defined in the first function
    second()
    
first()

print(x)                                    # this prints the global variable of x
