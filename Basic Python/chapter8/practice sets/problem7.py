# 7. Write a python function to remove a given word from a list and strip it at the same
# time.

l = ['ram', 'ramayan', 'saayam', 'am', 'hari']

def rem(i, word):
    n = []
    for item in i:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(rem(l, 'am'))