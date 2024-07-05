# you can open and work with multiple files using various approaches, depending on your specific 
# requirements. Here are a few common methods:

# 1. Simply using Multiple open() Statements
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

# 2. Using Context Managers (with Statement) 
# with now allows multiple file, it did not used to previously
# (New way in python from latest update to allow multiple file opening using 'with')
with (
    open('file1.txt', 'r') as file1, 
    open('file2.txt', 'r') as file2
): 
    print('file opened')

# 3. Using a Loop for Dynamic File Handling
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# Open and process each file in a loop
for file_name in file_names:
    with open(file_name, 'r') as file: pass