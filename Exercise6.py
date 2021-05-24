                                            ########## SNAKE WATER GUN GAME ##########

import random

choices = ["s", 'w', 'g']
cho = random.choice(choices)            # its for computer to choose a random item fromt the list above
you = 0
computer = 0
count = 10
n = 1
while (n <= 10):
    user_choise = input("""Plese choose:                   
    s for snake
    g for gun
    w for water:  """)                                 # take input from the user

    user = str(user_choise)                            # making the input a string
    count -= 1
    n += 1
    if user == cho:
        print("draw, you and computer both choosed same thing.")
        print(f"{count} round remaining out of 10.\n")
        continue

    elif user == 's' and cho == 'g':
        print(f"Computer Wins!, Computer choosed Gun.")
        print(f"{count} round remaining out of 10.\n")
        computer += 1

        continue

    elif user == 's' and cho == 'w':
        print(f"You Win!, Computer choosed Water.")
        print(f"{count} round remaining out of 10.\n")
        you += 1
        continue

    elif user == 'g' and cho == 's':
        print(f"You Win!, Computer choosed Snake.")
        print(f"{count} round remaining out of 10.\n")
        you += 1
        continue

    elif user == 'g' and cho == 'w':
        print(f"Computer Wins!, Computer choosed Water.")
        print(f"{count} round remaining out of 10.\n")
        computer += 1
        continue

    elif user == 'w' and cho == 's':
        print(f"Computer Wins!, Computer choosed Snake.")
        print(f"{count} round remaining out of 10.\n")
        computer += 1
        continue

    elif user == 'w' and cho == 'g':
        print(f"You Win!, Computer choosed Gun.")
        print(f"{count} round remaining out of 10.\n")
        you += 1
        continue
    else:
        print("Enter a valid input!")
        print(f"{count} round remaining out of 10.\n")
        continue

print("Game Over!")
if (you > computer):
    print(f"""
You Win!
You scored {you} points.""")

elif (computer > you):
    print(f"""
You Lose!
You scored {you} points.""")
elif(computer == you):
    print("Draw")