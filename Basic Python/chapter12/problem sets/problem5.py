# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input('Enter a number: '))
mulTable = [f'{num} * {i} =  {i * num}' for i in range(1, 11)]
print(mulTable)
with open ('file.txt','w') as f:
    for item in mulTable:
        f.write(f'{item}\n')