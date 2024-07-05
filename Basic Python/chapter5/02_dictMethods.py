marks = {
    'saayam':98,
    'ram':76,
    'hari':80,
    0:'hehehe'
}
#length
print(len(marks))

# gives all key value pairs in list
print(marks.items())

# gives all keys in list
print(marks.keys())

# gives all values in list
print(marks.values())

# gives value of key in list
print(marks.get('ram')) # gives none if not found
print(marks['ram']) # gives error if not found

# update values or insert if key is new
marks.update({'hari': 82})
print(marks)