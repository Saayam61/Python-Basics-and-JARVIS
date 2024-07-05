# f = open('file.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# same can be done using 'with' statement and you dont have to close the file explicitly
with open('file.txt') as f:
    data = f.read()
    print(data)
