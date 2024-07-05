class Employee:
    language = 'python'
    salary = '100000'
    
    # if a method is created inside class, 'self' parameter is must.
    # saayam.greet is treated as Employee.greet(saayam).
    # here an argument is passed through method call, so 'self' parameter is a must.
    # and variables should also be accessed as 'self.var_name'.
    # 'self' is same as 'this' keyword in Java.
    
    # 'self' is a convention name, so any other name can be used.
    def getInfo(self):
        print(f'The language is {self.language}. {self.name}\nThe salary is {self.salary}')
    
    def greet1(self):
        print('Good morning')
    
    
    # if a method is created with '@classmethod', 'cls' parameter is must.
    # same as instance method but is mainly for dealing with class level attributes or operation
    
    # 'cls' is a convention name, so any other name can be used.
    # variables are accessed through 'cls.var_name'. cls cannot access instance variable.
    @classmethod
    def greet2(cls):
        print(f'Good afternoon {saayam.name}. language is {cls.language}')
        
    # if you dont want to pass the object (self) to a method, declare it as static
    # The '@staticmethod' decorator in Python is used to define a method that belongs to a class
    # but does not access or modify the class state or instance state. Static methods do not 
    # require a reference to an instance (self) or a class (cls) and can be called on the class 
    # itself rather than on instances of the class.
    
    # variables are accessed through class or instance name
    @staticmethod
    def greetLast():
        print(f'Good night {saayam.name}. salary is {Employee.salary}')
        

saayam = Employee()

saayam.name = 'saayam'
saayam.language = 'JS'

# instance method
saayam.greet1()
# treated as Employee.greet1(saayam)

#saayam.greet2()
# class method
Employee.greet2() # mainly this as it is class method
# both above are valid

# for static method
# saayam.greetLast()
Employee.greetLast() # mainly this for static method


# both below lines are valid and are exactly the same.
saayam.getInfo() # mainly this as it is instance method
# Employee.getInfo(saayam)

