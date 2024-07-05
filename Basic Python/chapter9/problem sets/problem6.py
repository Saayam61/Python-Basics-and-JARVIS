# 6. Write a program to mine a log file and find out whether it contains ‘python’.

str = 'python'

with open('log.txt') as f:
    data = f.read()

if str in data:
    print('exists')
else:
    print(' does not exist')