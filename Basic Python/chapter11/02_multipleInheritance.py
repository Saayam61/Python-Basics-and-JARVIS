# base class or parent class
class Employee:
    company = 'ITC'
    name = 'Default name'
    salary = 736171
    def show(self):
        print(f'The name is {self.name} and the salary is {self.salary}')

# base class or parent class
class Coder:
    language = 'Python'
    def printLanguages(self):
        print(f'Here is your language: {self.language}')

# Programmer class is being inherited from Employee and Coder
# multiple inheritance
# child class or derived class
class Programmer(Employee, Coder):
    # company = 'ITC Infotech'
    def showLanguage(self):
       print(f'The company is {self.company} and the language is {self.language}')

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()