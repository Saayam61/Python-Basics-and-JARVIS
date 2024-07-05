# rock paper scissors game
'''
rock = 1
paper = 0
scissors = -1
'''
import random

youDict = {'r': 1, 'p': 0, 's': -1}
reverseDict = {1: 'rock', 0: 'paper', -1: 'scissor'}

computer = random.choice(list(reverseDict.keys()))
youChoice = input(
'''Enter your choice: 
r for Rock
p for Paper
s for Scissors
''')
you = youDict[youChoice]

print(f'Computer chose {reverseDict[computer]}')
print(f'You chose {reverseDict[you]}')

if computer == you:
    print('Its a draw!')
else:
    if computer == -1 and you == 1:
        print('You win!')
    elif computer == -1 and you == 0:
        print('You lose!')
    elif computer == 1 and you == 0:
        print('You win!')
    elif computer == 1 and you == -1:
        print('You lose!')
    elif computer == 0 and you == -1:
        print('You win!')
    elif computer == 0 and you == 1:
        print('You lose!')
    else:
        print('Something went wrong')

