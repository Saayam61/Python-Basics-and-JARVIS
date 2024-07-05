# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
n = 3
for i in range (1, 4):
        print(' '*(n-i), end = '') #end = ' ' adds no new line after print statement
        print('*'*(2*i-1))
