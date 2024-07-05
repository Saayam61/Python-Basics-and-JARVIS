# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    def __mul__(self, other):
        real_part = self.a * other.a - self.b * other.b
        imag_part = self.a * other.b + self.b * other.a
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f'{self.a} + {self.b}i'
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)
print(c1 * c2)