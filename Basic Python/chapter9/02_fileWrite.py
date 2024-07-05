s = 'This is writing in file'

# opens file in write mode if exists, else creates a new file
f = open('myfile.txt', 'w')
f.write(s)
f.close()