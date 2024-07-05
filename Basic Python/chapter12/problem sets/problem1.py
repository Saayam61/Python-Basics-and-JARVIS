# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

fileList = ['file1.txt', 'file2.txt', 'file3.txt']
for fileName in fileList:
    try:
        with open(fileName) as file: 
            print(f'{fileName} opened successfully')
    except FileNotFoundError as e:
        print('file not found:', e)

print('Program not crashed')

# or use try-expect with individual files opening one by one