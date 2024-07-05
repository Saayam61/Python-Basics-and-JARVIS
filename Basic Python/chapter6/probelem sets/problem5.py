# 5. Write a program which finds out whether a given name is present in a list or not.

names = ['hari', 'ram', 'saayam', 'ashish', 'bibek']
name = input('Enter name you want to search: ')
if(name in names):
    print(f'{name} is in a list')
else:
    print(f'{name} is not in a list')