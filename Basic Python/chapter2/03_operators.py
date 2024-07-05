# f or F means formatted string literal or we can use % or str.format
# name = "Alice"
# age = 30

# f:
# print(f"Hello, my name is {name} and I am {age} years old.")

# %:
# print("Hello, my name is %s and I am %d years old." % (name, age))

# str.format:
# print("Hello, my name is {} and I am {} years old.".format(name, age))

# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition: 10 + 3 = 13
# print("a + b = %d" % (a + b))  # Addition: 10 + 3 = 13
# print("a + b = {}" .format(a + b))  # Addition: 10 + 3 = 13

print(f"a - b = {a - b}")  # Subtraction: 10 - 3 = 7
print(f"a * b = {a * b}")  # Multiplication: 10 * 3 = 30
print(f"a / b = {a / b}")  # Division: 10 / 3 = 3.333...
print(f"a % b = {a % b}")  # Modulus: 10 % 3 = 1
print(f"a ** b = {a ** b}")  # Exponentiation: 10 ** 3 = 1000
print(f"a // b = {a // b}")  # Floor Division: 10 // 3 = 3

# Assignment Operators
c = 5
print("\nAssignment Operators:")
c += 2  # Equivalent to: c = c + 2
print(f"c += 2 -> c = {c}")  # c is now 7
c -= 2  # Equivalent to: c = c - 2
print(f"c -= 2 -> c = {c}")  # c is now 5
c *= 2  # Equivalent to: c = c * 2
print(f"c *= 2 -> c = {c}")  # c is now 10
c /= 2  # Equivalent to: c = c / 2
print(f"c /= 2 -> c = {c}")  # c is now 5.0
c %= 2  # Equivalent to: c = c % 2
print(f"c %= 2 -> c = {c}")  # c is now 1.0
c **= 3  # Equivalent to: c = c ** 3
print(f"c **= 3 -> c = {c}")  # c is now 1.0
c //= 2  # Equivalent to: c = c // 2
print(f"c //= 2 -> c = {c}")  # c is now 0.0

# Comparison Operators
print("\nComparison Operators:")
print(f"a == b -> {a == b}")  # Equal to: 10 == 3 is False
print(f"a != b -> {a != b}")  # Not equal to: 10 != 3 is True
print(f"a > b -> {a > b}")  # Greater than: 10 > 3 is True
print(f"a < b -> {a < b}")  # Less than: 10 < 3 is False
print(f"a >= b -> {a >= b}")  # Greater than or equal to: 10 >= 3 is True
print(f"a <= b -> {a <= b}")  # Less than or equal to: 10 <= 3 is False

# Logical Operators
x = True
y = False
print("\nLogical Operators:")
print(f"x and y -> {x and y}")  # Logical AND: True and False is False
print(f"x or y -> {x or y}")  # Logical OR: True or False is True
print(f"not x -> {not x}")  # Logical NOT: not True is False

# Bitwise Operators
print("\nBitwise Operators:")
print(f"a & b -> {a & b}")  # Bitwise AND: 10 & 3 = 2 (1010 & 0011 = 0010)
print(f"a | b -> {a | b}")  # Bitwise OR: 10 | 3 = 11 (1010 | 0011 = 1011)
print(f"a ^ b -> {a ^ b}")  # Bitwise XOR: 10 ^ 3 = 9 (1010 ^ 0011 = 1001)
print(f"~a -> {~a}")  # Bitwise NOT: ~10 = -11 (inverts all bits)
print(f"a << 2 -> {a << 2}")  # Bitwise left shift: 10 << 2 = 40 (1010 << 2 = 101000)
print(f"a >> 2 -> {a >> 2}")  # Bitwise right shift: 10 >> 2 = 2 (1010 >> 2 = 10)

# Membership Operators
lst = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print(f"3 in lst -> {3 in lst}")  # in: True if 3 is in lst
print(f"6 not in lst -> {6 not in lst}")  # not in: True if 6 is not in lst

# Identity Operators
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("\nIdentity Operators:")
print(f"m is n -> {m is n}")  # is: True if m and n are the same object
print(f"m is o -> {m is o}")  # is: True if m and o are the same object
print(f"m is not o -> {m is not o}")  # is not: True if m and o are not the same object
