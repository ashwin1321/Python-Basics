
########## LISTS #######
    # list is mutable, we can replace the items in the lists
'''
grocery = [ 'harpic', ' vim bar', 'deodrant', 'bhindi',54]          # we can include stirng and integer together in a list
print(grocery)
print(grocery[2])

'''
'''
numbers = [12,4,55,16,7]            # list can also be empty [], we can add items in it later

print(numbers)
print(numbers.sort())               # it gives none output

numbers.sort()                      # it sorts the numbers in ascending order in a list
print(numbers)     

numbers.reverse()                   # it sorts the numbers in reverse order
print(numbers)                      


numbers.append(17)                   # .append adds the item in the last of the list
print(numbers)

numbers.insert(1,123)                 # . insert(index,item), we can add item in the desired index
print(numbers)

numbers.remove(55)                     # .removes the items we want to remove
print(numbers)

numbers.pop()                       # .pop is used to remove the last items, Or it pops out the last item in the list
print(numbers)

numbers[1] = 45                     # we can replace the item in the list with desired item
print(numbers)
''' 

# MUTABLE = can change 
# IMMUTABLE = cannot change


####### TUPLES #######
    # tuples are immutable, as we cannot change the items in a tuple as of lists


tuple = (1,2,3,4,5)
print(tuple)

# tuple[1] = 6            # see, we cannot replace the items in tuple, as its immutable
# print(tuple)

'''
a=9
b=1
a,b = b,a               # in this we can swap the values in python. like in traditional programming we use (temp=a, a=b, b= temp)
print(a,b)
'''


