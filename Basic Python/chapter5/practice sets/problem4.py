# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
print(len(s))
s.add(20)
print(len(s))
s.add(20.0)
print(len(s))
s.add('20')
print(len(s))

# 20 and 20.0 are considered equal in python as, if values are equal,
# data type doesnt matter. thus len is 2 annd only one 20 is inserted