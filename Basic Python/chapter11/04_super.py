# base class
class Employee:
    def __init__(self) -> None:
        print('Constructor of Employee')
    a = 1

# 'child' class for Employee and 'parent' class for Manager
class Programmer(Employee):
    def __init__(self) -> None:
        print('Constructor of Programmer')
    b = 2

# child class for Programmer
class Manager(Programmer):
    def __init__(self) -> None:
        # calls parent constructor when the instance of Manager is created
        # 'super' keyword is used to access parent class attribute or methods
        super().__init__()
        print('Constructor of Manager')
    c = 3

# o = Employee()

# o = Programmer()

o = Manager()
