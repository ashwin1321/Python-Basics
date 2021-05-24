# Create a dictionary and take input form the user and return the meaning of the word form the dictionary

dict = { 'rice': 'carbohydrates', 'pulses': 'proteins', 'vegetable oil': ' fat', 'mustard':'vitamins'}
name = str(input("Enter the Keyword: "))
n = str(name)
if name in dict:
    print(" The meaning is", dict[n])
else:
    print("Meaning not found, Enter a valid keyword")


