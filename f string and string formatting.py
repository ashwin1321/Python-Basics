##### F STRINGS AND STRING FORMATTING #####


# simple string formatting

'''
name = "Ashwin"
a1 = 2 
a = "this is %s."%name                      # easy to use for small number of variables, but for large number chak dukhxa k ko %s ho bhanera khojdai 
aa = "this is %s %s."%(name,a1)    
print(a)


a2 = "this is {} {}"                        # we can format string in this way as well.  here the value of 1st {} is 0 and increase according to the number of {}
a2 = "this is {1} {0}"                      # we can change the value and it prints the item accordingly             
b = a2.format(name,a1)  
print(b)

'''

# F STRINGS
# --> F stands for fast

import math

name = "Ashwin"
a1 = 2 

a = f"This is {name} {a1} { 4*2} {math.cos(60)}"        # we can use anything, functions, functions inside a module in {}
print(a)
