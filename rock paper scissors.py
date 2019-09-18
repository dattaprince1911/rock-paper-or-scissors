from random import randint

player = input('rock(r), paper(p) or scissors(s)?')

if player == 'r':
    print('O vs', end=' ')
elif player == 'p':
    print('__ vs', end=' ')
elif player == 's':
    print('>8 vs', end=' ')
else:
    print('enter a valid choice')
choose = randint(1, 3)

if choose == 1:
    computer = 'r'
    print('O')
elif choose == 2:
    computer = 'p'
    print('__')
else:
    computer = 's'
    print('>8')

if player == computer:
    print('DRAW')
elif player == 'r' and computer == 'p':
    print('COMPUTER WINS')
elif player == 'r' and computer == 's':
    print('PLAYER WINS')
elif player == 'p' and computer == 'r':
    print('PLAYER WINS')
elif player == 'p' and computer == 's':
    print('COMPUTER WINS')
elif player == 's' and computer == 'r':
    print('COMPUTER WINS')
elif player == 's' and computer == 'p':
    print('PLAYER WINS')
