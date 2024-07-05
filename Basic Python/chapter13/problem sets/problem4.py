# 4. Write a program to filter a list of numbers which are divisible by 5.

numList = [i for i in range(1, 11)]
ans = list(filter(lambda x: x % 5 == 0, numList))
print(ans)