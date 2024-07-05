# Type hints are added using the colon (:) syntax for variables and the -> syntax for
# function return types.

# you can explicitly declare the expected type

# They are not enforced at runtime but can be checked using static analysis tools, 
# making them a valuable addition to the Python programmer's toolkit. (wont raise error and works)
n: int = 5

name: str = 'saayam'

def sum(a: int, b: int) -> int:
    return a + b

print(sum(2.5, 3.5))

# eg 2

from typing import List, Tuple, Dict, Union
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

result = add(3, 4.5)
print(result)  # Output: 7.5

# eg 3

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid


