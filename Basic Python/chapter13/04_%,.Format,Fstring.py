name = "Bob"
age = 25

# fString:
print(f"Hello, my name is {name} and I am {age} years old.")

# str.format:
print("Hello, my name is {} and I am {} years old.".format(name, age))
print("Hello, my name is {0} and I am {1} years old.".format(name, age))
print("Hello, my name is {1} and I am {0} years old.".format(name, age))

# %:
print("Hello, my name is %s and I am %d years old." % (name, age))