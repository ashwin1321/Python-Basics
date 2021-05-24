####### SETS #######

# It stores only unique values. no repetation of the items is done

'''
# if we store list in set(LIST), it becomes a set

num = set([1,2,3,4])            #we can define set as set([]) in the form of lists  or directly by {}
print(num)

sett = {3,4,5,6}                # we can define set in this way as well
print(sett)
print(type(sett))

'''

s = set() 
s.add(1)
s.add(2)                    # here it doesnt add 1 two times, it only stores the unique values
'''
s1 = s.union({1,2,3})       # s.union() alone doesnt works so we assign another varaiable. .union() makes a new set

s2 = s1.intersection({2,3,4,5})     # .intersection() gives out the intersection values in two sets
print(s2)
'''
s1 = {3,4}
print(s.isdisjoint(s1))         # to check if two sets is disjoint. If disjoint it prints true else false

s.remove(2)                 # it delets the desired item form the set
print(s)



# len(), max(), type() are some common functions

