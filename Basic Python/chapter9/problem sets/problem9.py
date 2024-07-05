# 9. Write a program to find out whether a file is identical & matches the content of
# another file.

with open('this.txt') as f:
    data = f.read()

with open('this(1).txt') as f:
    data2 = f.read()

if data == data2:
    print('They are identical')
else:
    print('They are not identical')