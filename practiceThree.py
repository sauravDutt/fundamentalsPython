import random
import sys

while True:
    response = input('Enter Exit for exit or type anything to continu :- ')
    if response == 'Exit':
        sys.exit()
    else:
        print('You typed '+response+' you asshole')
for i in range(5):
    print(random.randint(1,10))
print('\n Done \n')