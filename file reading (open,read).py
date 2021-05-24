# here i have created a .txt file and lets see what can be done
'''
f = open("qwerty.txt")                  # to open the file
# f = open("qwerty.txt", 'rb')          # to read the file in binary mode we use rb

content = f.read()                      # read the file contained in a file. After the file is read, this variable has all the content and the file pointer 'f' in this program is empty
print(content)

# content = f.read(x)                   # reads only first x no. of characters mentioned in the argument

"""
content = f.read(1233113)
print("1",content)

content = f.read(1233113)
print("2",content)                      # as all the content is printed already in the file in previous statement, it doesnot print anything even the content function is called
"""

f.close()                               # to close the opened file

'''
#### To print the lines in a file

f = open("qwerty.txt")                  # to open the file

print(f.read())                         # sabai kura print garxa, j j xa sab file bhitra ko

print(f.readlines())                    # sabai line print garxa eauta list banayaera

print(f.readline())                     # reads the  first line in the file
print(f.readline())                     # reads the  next line in the file as 1st line is already printed

# for line in f:
#     print(line, end="")                 # prints every line sepetately in a new line