# you can also install other external modules --> go to *(command prompt / terminal) -> type: pip install module_name


import random                               # to generate random varaibles,select random element from list, suffle elements randomly

'''
random_num = random.randint(0,5)            # randint(x,y) : used for selecting random integer between x and y  
print(random_num)                           # Prints the random number between x and y


rand = random.random()                      # this selects a random number from 0 and 1
rand1 = random.random()*100                  # this selects a random number from 0 to * x(some number)
print(rand)
print(rand1)
'''

lst = ['ntv','kantipur','ap1','image']
choise = random.choice(lst)                     # random.choise() picks the random item in the list
print(choise)
