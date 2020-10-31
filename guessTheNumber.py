# This is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 to 20')
for guessTaken in range(1, 7):
    guess = int(input('Take a guess :- '))
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber :
    print('Good job, you guessed my number in ' + str(guessTaken)+ ' attempts!')
else:
    print('Nope the number, I was thinking of was ' +str(secretNumber)+'.')