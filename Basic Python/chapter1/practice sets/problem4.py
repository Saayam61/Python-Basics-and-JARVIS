# 4. Write a python program to print the contents of a directory using the os module.
# os module is a built in module of Python

import os

# path for folder
directory_path = '/users/lenovo/desktop/code'

# list all files and directories in path
contents = os.listdir(directory_path)

# print contents of path
# simple way: print(contents)
for item in contents:
    print(item)