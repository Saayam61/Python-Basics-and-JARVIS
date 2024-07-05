# slicing
name = 'saayam'
sl = name[0:3]
print(sl)
char = name[0]
print(char)

# negative slicing
sl2 = name[-6:-3]
print(sl2)
char2 = name[-6]
print(char2)

# empty 1st starts with 0
sl3 = name[:3]
print(sl3)

# empty end is length-1
sl4 = name[0:]
print(sl4)

# 0 to length-1
sl5 = name[:]
print(sl5)
