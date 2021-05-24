#######  DICTIONARY  #######

# dictionary is nothing but key value pairs
# we can have both string and number inside a dictionary

d1 = {}
print(type(d1))

d3 = {"Ashwin":'Khatiwada', "Gaurav":'Khanal', 'Aayush':'Raut', 'vegetables': {'a':'potato','b':'carrot'} }   
# we can use another dictionary for a key inside a dictionary
print(d3['vegetables']['a'])            # in this way we can access the value of a key of the key 

'''

d2 = {"Ashwin":'Khatiwada', "Gaurav":'Khanal', 'Aayush':'Raut', }            # {'key':'value'}

d2[" Prasmit"] = 'Neupane'          # we can add item in a dictionay in this way 
d2.update({'abcd':'defg'})          # we can add item in dictionary in this way as well

d2[12] = "hello"
print(d2)

print(d2.items())                   # it prints the key and values in a pair


print(d2.keys())                    # it prints all the keys present in the dictionary
print(d2.values())                  # it prints all the values in the dictionary

del d2[12]                          # we can delete item from a dictionary using del function
print(d2)

print(d2['Ashwin'])                 # using key we can find its value
print(d2.get('Gaurav'))             # we can also find the value of the key using .get() finction

# print(d2['Khatiwada'])              # we cannot find key using its value

d4 = d2.copy()                      # .copy() doesnt change the values in a dict even the d4 has changes
del d4["Ashwin"]
print(d2)

'''

# for additional functions go to google noobs, sabai comment garera haat dukhdaina ra mero

