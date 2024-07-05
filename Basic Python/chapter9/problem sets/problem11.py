# 11. Write a python program to rename a file to “renamed_by_python.txt.

# copy the content of old file and move it to a new file with required name
with open('replaceable.txt') as f:
    data = f.read()

with open('renamed_by_python.txt','w') as f:
    f.write(data)



    
# using os module. directly rename
import os

# Specify the current file name and the new file name
current_filename = 'replaceable.txt'
new_filename = 'renamed_by_python.txt'

# Rename the file
os.rename(current_filename, new_filename)

print(f'File has been renamed to {new_filename}')




# using shutil module. moves the content to a new file and deletes the old file.
# can be used even to move them to a different directory or file systems.
# for 'rename' and 'move' both purposes
import shutil

# Specify the current file name and the new file name
current_filename = 'your_current_file.txt'
new_filename = 'renamed_by_python.txt'

# Rename the file
shutil.move(current_filename, new_filename)

print(f'File has been renamed to {new_filename}')


    
