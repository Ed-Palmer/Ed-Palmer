import random

x = True
while x is True:
    choice = random.randint(1, 3)
    if choice == 1:
        computerChoice = 'rock'

    elif choice == 2:
        computerChoice = 'paper'

    elif choice == 3:
        computerChoice = 'scissors'



    playerChoice = input('Rock, Paper or Scissors')
    playerChoice.lower()

    def compare():
        if playerChoice == 'rock' and computerChoice == 'scissors':
            print('Player Wins!')

        elif playerChoice == 'paper' and computerChoice == 'rock':
            print('Player Wins!')

        elif playerChoice == 'scissors' and computerChoice == 'paper':
            print('Player Wins!')

        elif playerChoice == computerChoice:
            print('Draw!')

        else:
            print('You Lose!')
        print('Computer chose', computerChoice, '!')


    compare()
    ok = input('Press c to continue, Press s to stop')
    if ok == 'c':
        pass
    elif ok == 's':
        x = False

