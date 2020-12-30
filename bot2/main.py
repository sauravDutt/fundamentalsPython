import random, sys
import os

userName = "sauravDutt"
password = "sauravd069"

while True :

    def clear(): 
        os.system('clear') 
    name = input("Enter a User Name : \n")
    clear()
    if name != userName:
        continue
    if name == userName:
        print("\n    *******************************************    ")
        print("                  Welcome back Saurav")
        print("    *******************************************    ")
        passwordUser = input("Enter your password : \n")
        clear()
        if passwordUser == password:
            print("\n    *******************************************    ")
            print("    *********    _________________    *********    ")
            print("    *********    Access Granted !!    *********    ")
            print("    *********    _________________    *********    ")
            print("    *********       sauravDutt        *********    ")
            print("    *******************************************    \n")
            print("\n ************************************************* ")
            input("            PRESS ANY KEY TO CONTINU     :-  ")
            
            clear()
            
            print(" _____________________________________________________________________\n")
            print("             Type the following for different functions     ")
            print(" _____________________________________________________________________\n")
            print("             quit - Exit                     " )
            print("        Rockpaper - To play Rock Paper Sissors        " )
            print("  ideaProbability - To get accurate pridiction on your next big Idea " )
            print(" _____________________________________________________________________\n")
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

def getAnswer(answerNumber):
    if answerNumber == 1 :
        return " __________________________________________________________________________________________\nOkay Okay we can concider this plan !!\n ______________________________________________________________________________________"
    elif answerNumber == 2 :
        return " __________________________________________________________________________________________\nWe should think over this plan !!!\n __________________________________________________________________________________________" 
    elif answerNumber == 3 :
        return " __________________________________________________________________________________________\nNot interested, might concider it as plan B but definitly not plan A !!\n _____________________________________________________"
    elif answerNumber == 4 :
        return "What plan, you are calling this bullshit a plan"
 
    
userInput = input("            Enter your option  :-    ")

quit = "quit"
rockPaperScissors = "Rockpaper"
pridiction = 'ideaProbability'
if userInput == quit :
    print("\n ************************************************* ")
    print("               Good day, to you sir!")
    print(" ************************************************* \n")
    sys.exit()
elif userInput == rockPaperScissors :
    rockPaperSc()
elif userInput == pridiction :
    r = random.randint(1, 4)
    pridict = getAnswer(r)
    print(pridict)
