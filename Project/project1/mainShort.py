import random

# Mapping inputs to their respective values
youDict = {'r': 1, 'p': 0, 's': -1}
reverseDict = {1: 'rock', 0: 'paper', -1: 'scissors'}

# Randomly choose for the computer
computer = random.choice(list(reverseDict.keys()))

# Get the user's choice
youChoice = input(
    '''Enter your choice: 
r for Rock
p for Paper
s for Scissors
''')
you = youDict[youChoice]

# Display choices
print(f'Computer chose {reverseDict[computer]}')
print(f'You chose {reverseDict[you]}')

# Determine the outcome
if computer == you:
    print('It\'s a draw!')
    
# We can take advantage of the fact that Rock-Paper-Scissors has a cyclical pattern 
# where each element beats the next one in a cyclic order. 
elif (you - computer) % 3 == 1:
    print('You win!')
else:
    print('You lose!')
