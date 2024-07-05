s1 = {1, 3, 43, 26}
s2 = {2, 26, 4, 90}

# union
print(s1.union(s2))

# intersection
print(s1.intersection(s2))

# difference
print(s1.difference(s2))

# subset
print({1, 26}.issubset(s1))

#superset
print(s1.issuperset({1,2}))

# disjoint
print(s1.isdisjoint(s2))