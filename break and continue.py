# break : it exits the loop when the loop encounters break statement
# continue: When continue is encountered, it exits current loop where it is and gets back to the next iteration

# eg
"""
i = 0
while(True):

    if i+1<5:
        i+=1
        continue
   
    print(i+1, end=" ")                  # (end=" ") : it prints all the elements together in a same line
    if (i==44):
        i += 1
        break                           # stops the loop where it is 
    i += 1
"""
print("To check if the number is greater than 100 or not.")
while(True):
    inp = int(input('Enter the number: '))
    if (inp>100):
        print("The number you entered is greater than 100.")
        break
    else:
        print("Try Again!\n")
        continue
    exit() 