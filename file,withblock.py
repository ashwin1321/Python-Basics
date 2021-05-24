with open('qwerty.txt') as f:              # works same as the file pointer below f, here we dont need to close the file
    print(f.read(4))








# f = open("qwerty.txt",'rt')                 # "rt" mode is default, doesnot matter if we write or not
# # print(f.readlines())
# print(f.read(10))

# f.close()