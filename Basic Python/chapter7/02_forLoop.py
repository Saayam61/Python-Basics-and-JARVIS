# 5 in range is (0, 4)

# (1, 6) gives 1 to 5

# step size can also be used; same as in slicing previously
for i in range(1, 6, 2):
    print(i)

# for loop in list; same can be done with string and tuple
l = [2, 3.5, True, 'saayam']
for item in l:
    print(item)

# for else: else is executed after condition reaches false
l = [2, 3.5, True, 'saayam']
for item in l:
    print(item)
else:
    print('The list is over')