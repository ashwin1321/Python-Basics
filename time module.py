                                                                           ##### TIME MODULE #####
# --> to find the time of execution of a program


# time.time()

import time

initial = time.time()                       # .time() gives number of ticks. (1 sec = 1 tick)
print(initial)
k = 0 

while (k<4):
    print("Hello")
    time.sleep(2)                           #  time.sleep(x): it prints the output after every x seconds
    k +=1
print("The time taken by while loop to execute the program is : ",time.time()-initial,"seconds")

# initial2 = time.time()                    # reseting time
# for i in range(45):
#     print("Hello")
# print("The time taken by for loop to execute the program is : ",time.time()-initial2,"seconds")


# localtime = time.asctime(time.localtime(time.time()))           # Prints the local time and day
# print(localtime)
