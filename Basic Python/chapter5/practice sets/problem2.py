# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s = set()

a = input('Enter your number: ')
b = input('Enter your number: ')
c = input('Enter your number: ')
d = input('Enter your number: ')
e = input('Enter your number: ')
f = input('Enter your number: ')
g = input('Enter your number: ')
h = input('Enter your number: ')
s.add(int(a))
s.add(int(b))
s.add(int(c))
s.add(int(d))
s.add(int(e))
s.add(int(f))
s.add(int(g))
s.add(int(h))
print(s)