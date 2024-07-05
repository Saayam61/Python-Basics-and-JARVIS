# by default open is in read mode so it is not necessary to specify mode for read
# f = open('file.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# read lines
f = open('file.txt')

# gives all lines in a list
# lines = f.readlines()
# print(lines, type(lines))

# one readline gives a first line. next gives second line and so on as a string.
# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))

# this can be done in short using loop
line = f.readline()
while line != '':
    print(line)
    line = f.readline()

f.close()