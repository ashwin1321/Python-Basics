# Recursions and Iterations
'''
def print2(str1):
    print2(str1)                         #Calling a function inside a same function :- This gives recursion error: Maximum recrusion depth reached
    print( "this is " + str1)

print2("Ashwin")
'''

# # factorial using iterative method
# def factorial_iterative (n):                
#     """
#     :param n:                           # it takes a parameter integer
#     :return:                            # it returns n*n-1*n-2*......1
#     """

#     fact = 1
#     for i in range(n):
#         fact = fact *(i+1)
#     return fact

# number = int(input("Enter the number: "))
# print(factorial_iterative(number))



# # factorial using recursion
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)               #recursion

# number = int(input("Enter the number: "))
# print(factorial_recursive(number))

 


# fibonacci Series
# 0 1 1 2 3 5 8 13 .....

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)                          # returns the value in the nth position

number = int(input("Enter the number: "))
print(fib(number))
 