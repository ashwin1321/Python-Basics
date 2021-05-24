# Guess the number

n =18
count = 1
print("\n.......... Game Start ..........\n")
while(count<=5):

    num = int(input('Enter the number: '))
    if n == num:
        print(f"The number is {n}, you guessed it correct")
        break
    elif num >= 18:
        print("The number you guessed is bigger but not that big. Try Again!")
    
    else:
        print("The number you entered is  smaller than the correct number. Try again!")
    count += 1
if count >5:
    print("Game Over!")