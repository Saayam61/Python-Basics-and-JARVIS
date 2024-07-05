# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# No the list cannot be inside set
# if there was no list:
# No the current values cannot be changed directly
# yes but by removing one element and adding another

s = {8, 7, 12, "Harry"}
s.remove(8)
s.add(3)
print(s)
