# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
from functools import reduce
list1 = [12, 235, 45363, 4345, 45648, 4356, 7664]
ans = reduce(lambda x,y: x if x > y else y, list1)
print(ans)
