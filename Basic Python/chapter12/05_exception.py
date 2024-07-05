# Exception handling in Python allows you to manage and respond to errors that occur during the 
# execution of your program. This ensures that your program can gracefully recover from unexpected 
# situations, rather than crashing abruptly. 
# try, except, else, and finally
# 'except' is same as 'catch' in java

# An exception is an event that occurs during the execution of a program that disrupts 
# the normal flow of instructions.
# An error, in the context of programming, refers to any unexpected condition that prevents 
# the program from executing as intended. 

# The try block is used to wrap code that might raise an exception. If an exception occurs within 
# this block, the control is immediately transferred to the except block(s).
try:
    a = int(input('enter a number: '))   
    print(a)
# The except block catches and handles exceptions that occur in the try block. You can specify 
# different except blocks for different types of exceptions.
# if exception does not occur the 'except' will be ignored

# exception can be specified as such: (there are many specified errors like 'valueError')
except ValueError as v:
    print('Value error occured:',v)
    
# Handling multiple exceptions in one block
except (TypeError, FileNotFoundError) as e:
    pass

# handles exception those that are not directly specified in the code above
except Exception as e:
    print(e)

# The else block executes if no exceptions were raised in the try block. This block is useful for 
# code that should run only if the try block succeeds.
# ignored if exception occurs
else:
    print("No exceptions occurred.")
    
# The finally block executes whether an exception occurred or not. It is typically used for cleanup 
# actions, like closing files or releasing resources.
# we could achieve the same purpose even without the 'finally' keyword except if there was 'return' 
# in function. even if there is 'return' keyword in 'try and except' both, 'finally' will still run.
finally:
    print("Cleanup code here.")
    
# if exception occurs the code below will not execute if exception handling is not done (crash program)
# but if exception handling is done, the code below will be executed even if exception occurs.
print('Thank you')


# raising exception
# Raising exceptions is the process of explicitly triggering an exception in your code.
# You might want to raise an exception when your code encounters an error condition or some 
# unexpected situation that it cannot handle.

# Raise is used to crash program if you are making modules or library, 
# during initial Development and for Unrecoverable Errors

# try-except is not necessary to 'raise' error but better to do it
# raise will crash program
# wont crash if used with try except
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

print('Thank you')

# Output: Error: Division by zero is not allowed
