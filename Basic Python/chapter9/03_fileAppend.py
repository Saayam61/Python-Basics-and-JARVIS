s = '\nThis is appending in file'

# opens file in append mode, adds content to the end of file
f = open('myfile.txt', 'a')
f.write(s)
f.close()