# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = 'Microsoft'
    def __init__(self, department, name, salary) -> None:
        self.department = department
        self.name = name
        self.salary = salary
        print(f'''
Hi, I am a {self.company} employee in {self.department} department
My name is {self.name}
My salary is {self.salary}
''')

p = Programmer('Machine Learning', 'Saayam', '1500000')
print(p.company, p.department, p.name, p.salary)
q = Programmer('R & D', 'Saayam2', '150000')
print(q.company, q.department, q.name, q.salary)