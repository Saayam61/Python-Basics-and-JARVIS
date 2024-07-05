# 6. Write a python function which converts inches to cms.
# cm = 2.54 inch

def inchesToCm(inch):
    return 2.54 * inch

inch = float(input('Enter inches: '))
print(f'{inch} inches is {inchesToCm(inch)} cm')