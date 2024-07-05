# base class
class Employee:
    a = 1

# 'child' class for Employee and 'parent' class for Manager
class Programmer(Employee):
    b = 2

# child class for Programmer
class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)
# print(o.b) # error
# print(o.c) # error

o = Programmer()
print(o.a,o.b)
# print(o.c) # error

o = Manager()
print(o.a,o.b,o.c)