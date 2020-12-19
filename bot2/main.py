import random, sys

userName = "sauravDutt"
password = "sauravd069"

while True :
    name = input("Enter a User Name : \n")
    if name != userName:
        continue
    if name == userName:
        print("Welcome back Saurav")
        passwordUser = input("Enter your password : \n")
        if passwordUser == password:
            print("\n    *******************************************    ")
            print("    *********    _________________    *********    ")
            print("    *********    Access Granted !!    *********    ")
            print("    *********    _________________    *********    ")
            print("    *********       sauravDutt        *********    ")
            print("    *******************************************    \n")
            print("\n ************************************************* ")
            print("      Type the following for different functions     ")
            print(" ___________________________________________________ \n")
            print("                     quit - Exit                     ")
            print("       Rockpaper - To play Rock Paper Sissors        ")
            print(" ___________________________________________________\n")
            break


def rockPaperSc ():
        
        print("\n    *********    Strart With some      *********    ")
        print("    *********  Rock Paper and Scissors *********    \n")

        # These variables are to store wins, losses and ties.
        wins = 0
        losses = 0
        ties = 0
        computerMove = ''

        while True : # The main game loop
            print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
            while True: # The player input loop
                print('Enter your move :- (r)ock, (p)aper, (s)cissors and (q)uit')
                playerMove = input()
                if playerMove == 'q':
                    sys.exit() #Quit the program
                if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                    break # Break out of the player loop
                print('Type one of r, p, s or q')
                
            # Diplay what the player chose:
            if playerMove == 'r':
                print('ROCK versus .....')
            elif playerMove == 'p':
                print('PAPER versus .....')
            elif playerMove == 's':
                print('SCISSORS versus .....')
            
            # Display what the computer chose
            randomNumber = random.randint(1,3)
            if randomNumber == 1:
                computerMove = 'r'
                print('ROCK')
            elif randomNumber == 2:
                computerMove = 'p'
                print('PAPER')
            elif randomNumber == 3:
                computerMove = 's'
                print('SCISSORS')
            
            # Display and record the wins, losses and ties
            if playerMove == computerMove:
                print('Its a Tie')
                ties = ties + 1
            elif playerMove == 'r' and computerMove == 's':
                print('You won this round :) !!')
                wins = wins + 1
            elif playerMove == 's' and computerMove == 'r':
                print('You lost this round :( ')
                losses = losses + 1
            elif playerMove == 'p' and computerMove == 'r':
                print('You won this round :) !!')
                wins = wins + 1
            elif playerMove == 'r' and computerMove == 'p':
                print('You lost this round :( ')
                losses = losses + 1
            elif playerMove == 's' and computerMove == 'p':
                print('You won this round :) !!')
                wins = wins + 1
            elif playerMove == 'p' and computerMove == 's':
                print('You lost this round :( ')
                losses = losses + 1


    
userInput = input("            Enter your option  :-    ")

quit = "quit"
rockPaperScissors = "Rockpaper"
if userInput == quit :
    sys.exit()
elif userInput == rockPaperScissors :
    rockPaperSc()

