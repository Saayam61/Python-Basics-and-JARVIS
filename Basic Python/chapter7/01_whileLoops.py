i = 1
while i<6:
    print(i)
    i += 1

# while with list
j = 0
l = [2, 3.5, True, 'saayam']
while(j<len(l)):
    print(l[j])
    j += 1

# while else
j = 0
l = [2, 3.5, True, 'saayam']
while(j<len(l)):
    print(l[j])
    j += 1
else:
    print('The value of j has reached ',len(l))