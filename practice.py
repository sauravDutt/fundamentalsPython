# this program is for the authentication the following is an infinite while loop with two if conditions.
# break and continue can only be used with while and for loop.
while True :
    userName = input("Enter userName :- ")
    if userName != 'sauravDutt':
        continue
    print('Welcome Back !!')
    password = input('Enter your password :- ')
    if password == 'sauravd069':
        break
    else:
        print('\n   ******** Access Denied ********   \n')
print('\n   ******** Access Granted ********   \n         www.sauravdutt.tech            \n')
