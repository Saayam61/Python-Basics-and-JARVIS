# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open('poems.txt') as f:
    data = f.read()
    if 'twinkle' in data:
    # if data.find('twinkle') != -1:
        print('found')
    else:
        print('not found')
        