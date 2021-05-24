##### FILE WRITING #####

# -> If the file mentioned already exists, it replaces the content when we write something f.write("")

# -> If the file doesnot exist it creates a new file and add the content to that file
'''

f = open('qwertyy.txt', 'w')                     # open the file xyz.txt and enable writing mode
f.write("Nepal is a landlock country. ")          # To add content to the file we use f.write(" "), where f is just a pointer, can be named anything
f.close()                                        # always close the opeaned file, Its a good practice.


f = open('qwertyy.txt', 'a')                     # open the file xyz.txt and enable append mode
# -> when we enable "a" (append), it keeps on adding the same content at last as many time as we run the program
f.write("Nepal is a landlock country. ")          # To add content to the file we use f.write(" "), where f is just a pointer, can be named anything
f.close()                                        # always close the opeaned file, Its a good practice.


f = open('qwertyy.txt', 'w')                     # open the file xyz.txt and enable writing mode
a = f.write("Nepal is a landlock country. ")          # To add content to the file we use f.write(" "), where f is just a pointer, can be named anything
# -> a = f.write(" "), if we print a then it will print total number of characters in the file
print(a)
f.close()                                        # always close the opeaned file, Its a good practice.

'''

####### HANDLE READ AND WRITE #######

f= open('qwertyy.txt','r+')                     # 'r' enables both reading and writing mode
print(f.read())
f.write("Thank You.")
f.close()

