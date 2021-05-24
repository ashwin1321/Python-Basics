# LAMDA FUNCTIONS or ANONYMOUS FUNCTIONS
# --> Used for convienence


'''
minus = lambda x,y: x+y                     # Its like making functions, nothing else
print(minus(9,5))

# Here, The functions above and below does the same work

def minus(x,y):
    return x+y
print(minus(9,5))

'''


'''

# def a_first(a):
#     return a[1]
# a = [[1,14], [0,6], [8,13]]
# a.sort(key = a_first)
# print(a)
'''
# here these two functions does the same thing

a = [[1,14], [0,6], [18,13]]
a.sort(key = lambda x:x[1])
print(a)

