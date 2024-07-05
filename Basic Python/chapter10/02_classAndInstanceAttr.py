class Employee:
    # class attributes
    language = 'python'
    salary = '100000'

saayam = Employee()

# instance attribute
saayam.name = 'saayam'
saayam.language = 'JS'
# instance attribute has high priority than class attribute
# class attribute acts as default and can be overwritten
print(saayam.name, saayam.language, saayam.salary) # output: saayam JS 100000
print(Employee.language)

