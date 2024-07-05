# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:
    def __init__(self, n) -> None:
        self.n = n
        self.square()
        self.cube()
        self.squareRoot()
        
    def square(self):
        print(f'The square of {self.n} is {self.n * self.n}')
        
    def cube(self):
        print(f'The cube of {self.n} is {self.n * self.n * self.n}')
        
    def squareRoot(self):
        print(f'The square root of {self.n} is {self.n ** 1/2}')
    
a = Calculator(4)
# a.square()
# a.cube()
# a.squareRoot()