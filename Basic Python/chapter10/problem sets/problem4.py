# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n) -> None:
        self.n = n
        self.square()
        self.cube()
        self.squareRoot()
        Calculator.greet()
        self.greet()
        
    def square(self):
        print(f'The square of {self.n} is {self.n * self.n}')
        
    def cube(self):
        print(f'The cube of {self.n} is {self.n * self.n * self.n}')
        
    def squareRoot(self):
        print(f'The square root of {self.n} is {self.n ** 1/2}')
    
    @staticmethod
    def greet():
        print('Hello user')
    
a = Calculator(4)
# a.square()
# a.cube()
# a.squareRoot()
# Calculator.greet()
# a.greet()

