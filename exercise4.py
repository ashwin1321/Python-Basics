# PATTERN PRINT
'''

--> Take a integer input 
--> Take a boolean variable (if true print the pattern, if false print pattern from opposite)

output:
True                            False
*                               ****
**                              ***
***                             **
****                            *    

'''

# print("Enter the number of rows: ")
# inp = int(input())
# print("Type 1 for ascending order, 0 for descending order")
# order = int(input())
# check = bool(order)

# if check == True:
#     for i in range(1,inp+1):
#         for j in range(1,i+1):
#             print("*",end=(""))
#         print()

# elif check == False:
#     for i in range(inp,0,-1):               # if we insert range in reverse and -1 at the end it prints in reverse order
#         for j in range(1,i+1):
#             print("*",end=(""))
#         print()   



inp = int(input("Enter the number of rows: "))
order = int(input("Type 1 for ascending order, 0 for descending order: "))

if order == 1:
    for i in range(0,inp+1):
        print("*"*int(i))

elif order == 0 :
    for i in range(inp,0,-1):
        print("*"*int(i))