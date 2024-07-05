# 7. Write a program to find out the line number where python is present from ques 6.

str = 'python'

with open('log.txt') as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if str in line:
        print('exists in line',lineno)
        break
    lineno += 1
else:    
    print('exists in line',lineno)
