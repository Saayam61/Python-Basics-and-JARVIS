l = ['Apple', 'Orange', 5, 36.17, True, 'ram', 'hari']

# insert at the end of list
l.append('Saayam')
print(l)

# insert at required index
l.insert(1, 'banana')
print(l)

# remove at required index and returns deleted value
print(l.pop(2))
print(l)

# remove specified value
l.remove('ram')
print(l)

# sorts string or numbers in ascending order
l1 = [2, 43, 23, 11, 1, 2.3]
l2 = ['ram', 'hari', 'gopal']
l1.sort()
l2.sort()
print(l1)

# reverse the list
l.reverse()
l1.reverse()
l2.reverse()
print(l)