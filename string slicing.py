mystr = "Thiss is a paragraph" 

print(len(mystr))                   # to check the length of the string we use len function

print (mystr[0:19])                 # slicing, we can print the elements in a string from one index to other                      

print (mystr[0:19:2])               # [source:desination:gap], here we can print string from one to other skipping characters or print elements from a gap

print (mystr[0:19:-1])              # string reverse ma print garxa 

print (mystr[0::4])                 # same as above, [s:d:g] , if any of its value not given it has default value as of string length in d and 1 in g, and s is 0

print (mystr[ -5: -1])               # it prints elements in  from backside [-d: -s]

print(mystr[::-1])                  # string reverse ma print garxa



#@ Some Functions

print (type(mystr))                  # it print what type of data type it is

print (mystr.isalnum())              # same as boolean (true if its number for .isalnum) (true if its alphanumeric for .isalpha)

print (mystr.endswith("paragraph"))         # endswith: it checks if the string ends with the entered word

print (mystr.count("O"))             # it counts how many times a word or a letter is repeated 

print(mystr.capitalize())           # first character capital hunxa

print(mystr.find("is"))             # it prints the number form which the searched index starts from

print(mystr.upper())                # it converts the string into UPPER case and .lower converts string in lowercase

print(mystr.replace("is","are"))    # it replaces the item

