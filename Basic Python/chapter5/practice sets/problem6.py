# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# d = {} # or d = dict()
# d.update({input('Enter your name: '): input('Enter your favorite language: ')})
# d.update({input('Enter your name: '): input('Enter your favorite language: ')})
# d.update({input('Enter your name: '): input('Enter your favorite language: ')})
# d.update({input('Enter your name: '): input('Enter your favorite language: ')})
# # d[input('Enter your name: ')] = input('Enter your favorite language: ')
# # d[input('Enter your name: ')] = input('Enter your favorite language: ')
# # d[input('Enter your name: ')] = input('Enter your favorite language: ')
# print(d)

# The behavior of input() can vary depending on the execution environment (e.g., IDE, terminal). 
# Sometimes, unexpected behavior arises due to how inputs are managed by the environment or how 
# the script handles input buffering.
# This can lead to inputs being concatenated or misinterpreted, resulting in unexpected keys or 
# values being stored in the dictionary.

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

