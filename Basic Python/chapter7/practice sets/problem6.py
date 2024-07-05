# 6. Write a program to calculate the factorial of a given number using for loop.

num = int(input('Enter a number to find factorial: '))
fact = 1
for i in range (1, num+1):
    fact *= i
else:
    print(fact)
