def func(a,b):
    # print( a+b)
    sum = a+b
    return sum
s = func(2,5)
print(s)


def func1(a,b):
    """ This is called a docstring, basically a comment. It can be accessed by calling function_name.__doc__ """
    print( a+b)
func1(5, 7)                  # until a function is not called it doesnt executes

print(func1.__doc__)         # To access the docstring in a function
