# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print('Infinite (Not allowed),', e)