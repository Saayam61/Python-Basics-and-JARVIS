# List comprehensions provide a concise way to create lists based on existing list in Python.
# more readable and expressive way to create lists compared to traditional loops. 
# They consist of brackets containing an expression followed by a for clause, and they can also 
# include zero or more if clauses. basic syntax: [expression for item in iterable]

# normal list creation from existing list
myList = [1, 2, 9, 5, 3, 5]
squaredList = []
for item in myList:
    squaredList.append(item * item)
print(squaredList)

# list comprehensions from existing list
squaredList = [i ** 2 for i in myList] # range(10) such can also be done in place of myList
print(squaredList)

# list comprehensions With an if Clause
even_squares = [x ** 2 for x in range(10) if x % 2 == 0] #myList can be used in place of range
print(even_squares)

# list comprehensions Using Nested Loops
combinations = [(x, y) for x in range(3) for y in range(3)]
print(combinations)

# list comprehensions for Flattening a Nested List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)

# List Comprehensions with Functions
def square(x):
    return x ** 2

squares = [square(x) for x in range(10)]
print(squares)

# List Comprehensions with Strings
letters = [letter for letter in "hello"]
print(letters)

# Combining Multiple Conditions
filtered = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(filtered)

# Creating a Dictionary with List Comprehension
squares_dict = {x: x ** 2 for x in range(10)}
print(squares_dict)

# Creating a Set with List Comprehension
unique_squares = {x ** 2 for x in range(10)}
print(unique_squares)
