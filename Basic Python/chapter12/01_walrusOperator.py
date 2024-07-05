# The walrus operator (:=) in Python is an assignment expression introduced in Python 3.8. 
# It allows you to assign a value to a variable as part of an expression.
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)

# example 2 (condtionals)
# Expression: True
# y = 3, if y > 5 ... else ...

# No matter if the expression is true or false, the value is always assigned to the variable
if (y := 3) > 5:
    print(f'y is {y} and the expression is True')
# Expression: False
else:
    print(f'y is {y} and the expression is False')
# Output: y is 3 and the expression is False

# example 3 (loops)
# Without walrus operator
# while True:
#     data = input("Enter something (or 'quit' to stop): ")
#     if data == 'quit':
#         break
#     print(f'You entered: {data}')

# the loop stops if false but the value is always assigned
# With walrus operator
# while (data := input("Enter something (or 'quit' to stop): ")) != 'quit':
#     print(f'You entered: {data}')
    
# example 4 (loops):
# n = 2
# while (m := n - 1) > 0:
#     print(f'n is {n}, m is {m}')
#     n -= 1

# print(f'Loop ended. Final values: n is {n}, m is {m}')

# example 5 list comprehension:
# list comprehension synatx: [expression for item in iterable if condition]
import math
numbers = [4, 9, -5, 16, 25, -1, 36]
positive_squares = [sqrt for num in numbers if num > 0 and (sqrt := math.sqrt(num)) >= 0]
print(positive_squares)


    


