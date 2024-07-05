# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

num = int(input('Multiplication table of '))
for i in range(-10, 0):
    print(f'{num} * {-i} = {num * -i}')
    
# or

num = int(input('Multiplication table of '))
for i in range(1, 11):
    print(f'{num} * {11-i} = {num * (11-i)}')

