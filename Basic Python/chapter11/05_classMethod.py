class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f'The class attribute of a is {cls.a}')

e = Employee()

# since it is a class method, its value remains 1 and does not change due to its instance.
e.a = 5
e.show() # 1