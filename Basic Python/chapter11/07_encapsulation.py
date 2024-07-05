class Car:
    def __init__(self, make, model, year):
        
        # The recommended approach is to use getter and setter methods to access and modify the 
        # protected and private members.
        # a convention indicating that the member should not be accessed outside the class
        # but still possible
        self._make = make      # Protected member
        self._model = model    # Protected member
        
        # cannot be accessed directly outside class.
        # possible only throgh public method
        self.__year = year     # Private member
    
    # also a valid approach to make getter and setter methods
    # but has different method names.
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        if year > 1885:  # The first car was made in 1886
            self.__year = year
        else:
            print("Invalid year")

car = Car("Toyota", "Camry", 2020)

# use getter and setter instead of _make(protected attribute)
print(car._make)      # Accessing protected member

print(car.get_year()) # Accessing private member via public method

car.set_year(1990)    
print(car.get_year()) # Updated year

car.set_year(1800)    # Trying to set an invalid year
print(car.get_year()) # Year remains unchanged

print(car.__year) # error as it is private
