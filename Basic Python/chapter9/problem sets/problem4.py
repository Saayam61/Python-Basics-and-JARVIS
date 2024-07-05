# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.

str = 'Donkey'

with open('donkey.txt') as f:
    data = f.read()

if str in data:
    newdata = data.replace(str, '######')
    with open('donkey.txt','w') as f:
        f.write(newdata)

        
    
