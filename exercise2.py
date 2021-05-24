##### FAULTY CALCULATOR #####

def calculetor():
    print("\nWellcome to Calc:")
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    
    Enter Your Choise:
    ''')

    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter second Number: "))



    if operation == '+':
        if num1 == 56 and num2 ==9:
            print("56 + 9 = 77")
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        if num1 == 45 and num2 == 3:
            print("45 * 3 = 555")
        else:
            print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num1 == 56 and num2 == 4:
            print("56/6 = 4")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif operation == '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")
    elif operation == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("You Press a Invalid Key")
    again()

def again():
    cal_again = input('''
    Do you want to calculate again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        calculetor()
    elif cal_again == 'n':
        print("See You Later")
    else:
        again()

calculetor()