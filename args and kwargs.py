                                                     ####### *args and **kwargs #######

# single star for args (*args) and double star for kwargs (**kwargs)

# normal function
'''
def function_name(a,b,c,d):
    print(a,b,c,d)
function_name("Ashwin",'Rabindra','Aayush','Prasmit')           # we cannot add elements exceeding its argument values
'''


# *args
'''
def funargs(normal,*args):                              # we can write anything after *x, it becomes args syntax
    print(normal)
    # print(type(args))
    # print(args[0:12])                                           # prints as a tuple
# even if we define as a list, its going to print in the form a tuple
    for i in args:
        print(i)
normal =  'This is a normal Argument and these are the name of some guys:'
lst = ["Ashwin",'Rabindra','Aayush','Prasmit','Amrit','Gaurav','Aadarsha']

funargs(normal,*lst)                            # always normal argument is at 1st place then *args and **kwargs
'''

# **kwargs
def funkwargs(normal,*args,**kwargs):                              # we can write anything after *x and **x, it becomes args and kwargs syntax
    print(normal)
    for i in args:
        print(i)
    print("What is what")
    for key,value in kwargs.items():
        print(f"{key} is {value}")

normal =  'This is a normal Argument and these are the name of some guys:'
lst = ["Ashwin",'Rabindra','Aayush','Prasmit','Amrit','Gaurav','Aadarsha']

kw = {'School':'study','Hosptal':'treatment','Bank':'Money'}

funkwargs(normal,*lst,**kw)

# unlike normal functions we dont need to add arguments to print n number of items, which is a hectic job. we can just update list or dictionary using *args and **kwargs