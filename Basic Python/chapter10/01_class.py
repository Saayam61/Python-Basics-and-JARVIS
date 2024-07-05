# class creation
class Employee:
    # class attributes
    language = 'python'
    salary = '100000'

# object instantiation (Instance)
saayam = Employee()
# adding attribute in class for specific object (instance attribute)
saayam.name = 'saayam'
# accessing object (instance of class) values
# 'name' is instance attribute, 'salary' and 'language' are class attributes
print(saayam.name, saayam.language, saayam.salary)

sam = Employee()
sam.name = 'sam'
print(sam.name, sam.salary, sam.language)



