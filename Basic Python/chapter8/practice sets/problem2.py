# 2. Write a python program using function to convert Celsius to Fahrenheit.
# c/5 = f-32/9

def celciusToFahrenheit(c):
    return ((c*9)/5)+32

c = float(input('Enter temperature in celcius: '))
ans = round(celciusToFahrenheit(c), 2)
print(f'{c} degrees celcius is {ans} degree fahrenheit')