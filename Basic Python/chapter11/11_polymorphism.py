# Using method overriding (Inheritance)
class Animal:
    def make_sound(self):
        pass
    
class Dog(Animal):
    # here make_sound() method of Animal class is overridden for Dog class
    def make_sound(self):
        return "Woof"

d = Dog()
print(d.make_sound())

# Using method overriding without Inheritance
class MathOpr:
    def operate(self, a, b):
        return a + b

class StringOpr(MathOpr):
    def operate(self, a, b):
        return str(a) + str(b)

math_ops = MathOpr()
string_ops = StringOpr()

print(math_ops.operate(10, 5))  # Output: 15
print(string_ops.operate(10, 5))  # Output: 105

# Method overloading using default arguments
# Actual method overloading is not available in python 
# so we use default argument to acheive the same purpose
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(1, 2))      # Output: 3
print(calc.add(1, 2, 3))   # Output: 6
