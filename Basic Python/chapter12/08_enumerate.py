# The enumerate function in Python adds a counter to an iterable and returns it as an enumerate object. 
# This is often used in loops to obtain both the index and the value of the items in the iterable.
# syntax: enumerate(iterable, start=0)

# enumerate with 'list'
fruits = ["apple", "banana", "cherry"]

# default is start=0 so no need to write. need to specify if you want to change start.(fruits,start=1)
for index, fruit in enumerate(fruits): 
    print(index, fruit)
# Output:    
# 0 apple
# 1 banana
# 2 cherry

# enumerate with 'list comprehension'
fruits = ["apple", "banana", "cherry"]
indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
print(indexed_fruits)
# Output: [(0, "apple"), (1, "banana"), (2, "cherry")]

# enumerate with 'tuple'
animals = ("cat", "dog", "rabbit")
for index, animal in enumerate(animals):
    print(index, animal)
# output: 
# 0 cat
# 1 dog
# 2 rabbit

# enumerate with 'string'
word = "hello"
for index, letter in enumerate(word):
    print(index, letter)
# Output:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o


# Practical Example: Modifying a List
numbers = [1, 2, 3, 4, 5]

for index, number in enumerate(numbers):
    numbers[index] = number * 2

print(numbers)
# output: [2, 4, 6, 8, 10]