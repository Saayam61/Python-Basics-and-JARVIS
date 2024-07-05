# 5. Write a program to find the sum of first n natural numbers using while loop.

num = int(input('Enter a number to find sum of first n natural numbers: '))
sum = 0
i = 1
while(i<=num):
    sum += i
    i += 1
else: 
    print(sum)
