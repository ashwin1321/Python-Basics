#######  FOR LOOPS #######

list = [['a',1],['b',2],['c',3],['d',4]]

dict1 = dict (list)                          # converting list into dict 
print(dict1)

for i in dict1:                             # This prints only key in the dictionary
    print(i)

for it,number in dict1.items():              # .items() helps to print key and value both in dictionary, as normal looping gives error in dict
    if number >=3:
        print(it,number)

for i,j in list:
    print(i,j)


num = [int, float,'ashwin',2,34,56,47,63,1,5,7,4,3,24,63,7,3,252]
for n in num:
    if str(n).isalpha():            # .isalpha() is for alphabet and .isnumeric() is forn number
        print(n)
