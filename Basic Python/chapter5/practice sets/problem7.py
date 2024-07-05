# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

# it works as update. First key value pair is stored and the second value is updated as new value.
d = {}

# Allow each friend to enter their information individually
name1 = input('Enter your name: ')
lang1 = input('Enter your favorite language: ')
d[name1] = lang1

name2 = input('Enter your name: ')
lang2 = input('Enter your favorite language: ')
d[name2] = lang2

name3 = input('Enter your name: ')
lang3 = input('Enter your favorite language: ')
d[name3] = lang3

name4 = input('Enter your name: ')
lang4 = input('Enter your favorite language: ')
d[name4] = lang4

print(d)