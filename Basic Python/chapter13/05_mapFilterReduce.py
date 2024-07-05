# map(): Applies a function to all items in an input iterable (list, tuple, etc.) and 
# returns a new iterable with the results.
numbers = [1, 2, 3, 4, 5]
squared = lambda x: x**2 # or just do: squared = list(map(lambda x: x**2, numbers))
sList = list(map(squared, numbers))
print(sList)

# filter(): Constructs an iterator from elements of an iterable for which a function returns True.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# reduce(): Applies a rolling computation to sequential pairs of values in an iterable, reducing them 
# to a single value. In Python 3, it has been moved to the functools module.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)
