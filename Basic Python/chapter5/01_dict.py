# values can be any data type but keys must be immutable
# allowed keys: string, int, float, tuple, frozenset

marks = {
    'saayam':98,
    'ram':76,
    'hari':80,
    0:'hehehe'
}

# insert
marks['sam'] = 20

# update
marks['sam'] = 30

# access
marks['saayam'] = 99
print(marks['saayam'])

# delete
print(marks.pop('sam')) # returns value of deleted key
print(marks.popitem()) # removes last inserted and returns key value pair

print(marks, type(marks))