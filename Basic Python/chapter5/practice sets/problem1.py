# 1. Write a program to create a dictionary of English words with values as their Nepali
# translation. Provide user with an option to look it up!

d = {
    'name':'naam',
    'surname':'thar',
    'address':'thegana',
    'place':'thau',
    'things':'saman'
}
key = input('Which word would you like to translate into Nepali? ')
print(d[key])