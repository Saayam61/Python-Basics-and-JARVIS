# a = int(input('Enter your number: '))
# b = int(input('Enter your number: '))
# c = int(input('Enter your number: '))

# avg = (a + b + c)/3
# print(avg)

# function definition
def avg():
    a = int(input('Enter your number: '))
    b = int(input('Enter your number: '))
    c = int(input('Enter your number: '))

    avg = (a + b + c)/3
    print(avg)

# function call
# avg()
# avg()
# avg()
# avg()
# avg()

# with arguments
# here edning is a default parameter/argument; used if value is not passed throgh call
def greet(name, ending = 'Thank you'):
    print('Good day, ' + name)
    # print('Good day,',name)
    print(ending)
    return 'done'

a = greet('Saayam')
print(a) # return value
greet('ram','thanks')
    