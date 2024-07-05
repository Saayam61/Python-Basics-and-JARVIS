# The global keyword in Python is used to indicate that a variable inside a function is a global 
# variable. It allows you to modify the variable outside of the current scope. Without the global 
# keyword, you cannot assign a new value to a global variable inside a function; it would be treated 
# as a local variable.

# Using 'global variables' breaks the principle of encapsulation in object-oriented programming.

# without 'global' keyword
y = 10  # Global variable

def modify_local():
    y = 20  # This creates a local variable y, does not affect the global y

print(f"Before calling modify_local: {y}")  # Output: 10
modify_local()
print(f"After calling modify_local: {y}")   # Output: 10

# with 'global' keyword
x = 10  # Global variable

def modify_global():
    global x  # Declare that we want to use the global variable x
    x = 20    # Modify the global variable

print(f"Before calling modify_global: {x}")  # Output: 10
modify_global()
print(f"After calling modify_global: {x}")   # Output: 20
