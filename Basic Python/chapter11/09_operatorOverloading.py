# we dont have method and constructor overloading in python
# Constructor overriding is implicitly done when you define constructor for child class

# operator overloading and operator overriding is same thing

# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
class Number:
    def __init__(self, n) -> None:
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

# unsupported operand type(s) for +: 'Number' and 'Number' if __add__ is not defined
print(n + m)

# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)
# Other dunder/magic methods in Python:
# __str__() # used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling.__len__() or len(obj)
    
