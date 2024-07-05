# The join method in Python is used to concatenate elements of an iterable (such as a list) into a single 
# string. It's a string method and is particularly useful when you have a list (or any iterable) of 
# strings that you want to concatenate with a specific delimiter between them.

# If the iterable contains elements that are not strings, you will need to convert them to strings 
# before using join.

# syntax: delimiter_string.join(iterable)
# delimiter is a string that acts as separator in single string between words

# eg 1
words = ["Hello", "world", "in", "Python"]
joined_string = ' '.join(words)
print(joined_string)  # Output: Hello world in Python

# eg 2
numbers = [1, 2, 3, 4, 5]
joined_numbers = '-and-'.join(map(str, numbers))
print(joined_numbers)  # Output: 1-2-3-4-5

