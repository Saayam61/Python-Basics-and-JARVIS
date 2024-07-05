# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.

myList = [2, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(myList):
    if index == 2 or index == 4 or index == 6:
        print(item)
