# A lambda function in Python is a small, anonymous function defined using the lambda keyword. It can 
# take any number of arguments, but it has only one expression. The expression is evaluated and returned. 
# Lambda functions are often used for short, simple operations where defining a full function using def 
# would be overkill.
# same as arrow/anonymous functions ()=> in JavaScript

# syntax: lambda arguments: expression

# without lambda
# def square(n):
#     return n * n

# with lambda
square = lambda n: n * n
print(square(5))