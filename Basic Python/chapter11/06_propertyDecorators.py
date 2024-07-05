class Employee:

    # Property: method acts as an attribute
    # method acts as a getter for the name attribute, cannot be modified only access
    # To be a getter method, must be decorated with property.
    @property
    def name(self):
        return f'{self.fname} {self.lname}'
    
    # equivalent setter method is 'property_name.setter'
    # can be modified, acts as a setter, can be modified
    @name.setter
    def name(self, value):
        self.fname = value.split(' ')[0]
        self.lname = value.split(' ')[1]
    
e = Employee()

e.name = 'saayam gautam'
print(e.name)

print(e.fname, e.lname)
