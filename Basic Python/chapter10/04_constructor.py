class Employee:
    language = 'python'
    salary = '100000'
    
    # __init__(self) is a constructor, constructor is invoked when an object is created.
    # its purpose is to initialize the instance attributes of a class
    # -> none means it does not return anything, 
    # writing it is optional as it always returns none anyways
    # dunder (methods enclosed with __) method 
    # dunder methods are automatically called in appropriate contexts
    def __init__(self, name, language, salary) -> None: 
        self.name = name
        self.language = language
        self.salary = salary
        print('I am creating an object')
    
    def getInfo(self):
        print(f'The language is {self.language}.\nThe salary is {self.salary}')
    
    @staticmethod
    def greet1():
        print(f'Good morning')


# attributes are passed to constructor
saayam = Employee('saayam','JS','1200000')
# saayam.name = 'saayam'

print(saayam.name, saayam.language, saayam.salary)
