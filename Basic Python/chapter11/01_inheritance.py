# base class or parent class
class Employee:
    company = 'ITC'
    def show(self):
        print(f'The name is {self.name} and the salary is {self.salary}')

# class Programmer:
#     company = 'ITC Infotech'
#     def show(self):
#         print(f'The name is {self.name} and the salary is {self.salary}')

#     def showLanguage(self):
#         print(f'The name is {self.name} and the language is {self.language}')

# Programmer class is being inherited from Employee
# single inheritance
# child class or derived class
class Programmer(Employee):
    # company = 'ITC Infotech'
    def showLanguage(self):
       print(f'The name is {self.name} and the language is {self.language}')

a = Employee()
b = Programmer()

# variables and methods of base class are accessed from child class
print(b.company)
b.name = 'saayam'
b.salary = 72183
b.show()
# b.showLanguage()


# 'Hierarchical' inheritance is same as single but there are more than one child of one parent class