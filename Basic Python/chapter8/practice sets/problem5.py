# 5. Write a python recursive function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def star(n):
    if n==0:
        return
    print('*' * n)
    star(n-1)

n = int(input('Enter number of lines: '))
star(n)