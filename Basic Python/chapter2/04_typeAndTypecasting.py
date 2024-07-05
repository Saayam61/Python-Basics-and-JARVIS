# Integer
num = 10
print(type(num))  # Output: <class 'int'>

# Float
pi = 3.14
print(type(pi))  # Output: <class 'float'>

# String
name = "Alice"
print(type(name))  # Output: <class 'str'>

# Boolean
is_valid = True
print(type(is_valid))  # Output: <class 'bool'>

# List
my_list = [1, 2, 3, 4, 5]
print(type(my_list))  # Output: <class 'list'>

# Tuple
my_tuple = (10, 20, 30)
print(type(my_tuple))  # Output: <class 'tuple'>

# Dictionary
my_dict = {'name': 'Alice', 'age': 30}
print(type(my_dict))  # Output: <class 'dict'>

# Set
my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>

# Define a class
class MyClass:
    pass

# Create an instance of the class
obj = MyClass()

# Check the type of the class and the instance
print(type(MyClass))  # Output: <class 'type'>
print(type(obj))      # Output: <class '__main__.MyClass'>

# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Check the type of the function
print(type(greet))  # Output: <class 'function'>

# Check type of built-in function
print(type(len))  # Output: <class 'builtin_function_or_method'>

# Check type of method
lst = [1, 2, 3]
print(type(lst.append))  # Output: <class 'builtin_function_or_method'>
