 # try and except: If a code throws an error then we can use try and except exceptions. if code is correct it works, if it throws an error it escapes that and go to the except and executes what's inside

num1  = (input("Enter num 1: "))
num2  = (input("Enter num 2: "))

try:
    print('The sum of the two number is: ' ,
    int(num1)+int(num2))


# except:                                         # this prints what is inside it
#     print("Enter a valid number!")
    
except Exception as e:                      # this prints what error is there 
    print(e)
