import random, sys
import os

userName = "sauravDutt"
password = "sauravd069"

def clear(): 
    os.system('clear') 

 
while True :
    
    name = input("Enter a User Name : \n")
    clear()
    if name != userName:
        continue
    if name == userName:
        print("\n    *******************************************    ")
        print("                  Welcome back Saurav")
        print("    *******************************************    \n")
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
            print("                         quit - Exit                     " )
            print("                         doc  - Documentation                     " )
            print("                      MORE FUNCTIONS COMING SOON            ")
            print(" _____________________________________________________________________\n")
            break
        else:
            print("\n    *******************************************    ")
            print("    *********    _________________    *********    ")
            print("    *********    Access Denied !!     *********    ")
            print("    *********    _________________    *********    ")
            print("    *********         Retry           *********    ")
            print("    *******************************************    \n")
            print("\n ************************************************* ")
            input("            PRESS ANY KEY TO RESTART     :-  ")
            clear()
            continue

   
userInput = input("            Enter your option  :-    ")

quit = "quit"
documentation = "doc"
sauravDutt = "sd"
if userInput == quit :
    clear()
    print("\n ************************************************* ")
    print("               Good Day, to you sir!")
    print(" ************************************************* \n")
    sys.exit()
else:
    clear()
    print("\n ************************************************* ")
    print("             More features coming soon!!!")
    print(" ************************************************* \n")
