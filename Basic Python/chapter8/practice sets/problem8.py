# 8. Write a python function to print multiplication table of a given number.

def mulTable(n):
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')
n = int(input('Enter number for multiplication table: '))
mulTable(n)