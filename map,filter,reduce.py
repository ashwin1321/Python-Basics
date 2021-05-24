#############################################      MAP FUNCTION      ###############################################

# -->  applys one function in the whole list
'''
numbers = ['2','3','4']

# normal loop 
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])                # Typecasting
numbers[2] = numbers[2] +1
print(numbers[2])

#using map function

numbers = list(map(int,numbers))                   # converting the elements in number in integer 
numbers[2] = numbers[2] +1
print(numbers[2])



def sq(a):
    return a*a
num = [1,2,3,4,5,6,6,7]
square = list(map( sq ,num))                        # using the elements in a list into a function
print(square)


num = [1,2,3,4,5,6,6,7]
square1 = list(map(lambda x: x*x  ,num))                        # using the elements in a list into a lambda function
print(square1)



def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square,cube]

for i in range(5):
    val = list(map(lambda x: x(i),func))
    print(val)
'''


#######################################      FILTER FUNCTION    #########################################

# --> filters and prints the items if its True 
'''
lst = [1,32,4,5,7,8,9,90,13]

def greater(num):
    return num>5                                        # it only returns either True or False

bigger_than_5 = list(filter(greater,lst))               # prints the elements in lst if the condition in the function greater is true         
print(bigger_than_5)    
'''



##############################              REDUCE FUNCTION             ##############################

from functools import reduce

lst1 = [1,2,3,4,5]
num = reduce(lambda x,y:x+y,lst1)
print(num)

#normal
# num = 0
# for i in lst1:
#     num += i
# print(num)