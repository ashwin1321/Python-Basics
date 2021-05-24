f = open("qwerty.txt")

'''
print(f.tell())                     # prints where the index is, gives out its value

print(f.readline())                 # prints the first line in the file

print(f.tell())                    
print(f.readline())                 
'''

f.seek(0)                          # f.seek(x): using this function we can bring back index to the x position
print(f.readline())

f.close()

