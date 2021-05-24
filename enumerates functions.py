# makes things easy

# normal function
lst = [ 'apple','banana','guava','grapes']
# i =1
# for item in lst:
#     if i%2 is not 0:
#         print(f"The fruits is {item}")
#     i +=1


# enumerates
for index,item in enumerate(lst):
    if index%2 == 0:
        print(f"The fruits is {item}")

