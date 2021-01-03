import random, sys
import os

userName = "sauravDutt"
password = "sauravd069"
quit = "quit"
documentation = "doc"
sauravDutt = "sd"

def clear(): 
    os.system('clear') 

def authentication(name):
    
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
def menu(userInput):
    if userInput == quit :
        clear()
        print("\n ************************************************* ")
        print("               Good Day, to you sir!")
        print(" ************************************************* \n")
        sys.exit()
    elif userInput == documentation:
        clear()
        print("\n ***************************************************** \n")
        print("              Documentation - SDtools")
        print("   This Program provides you with Exclusive tools ")
        print("  This is just a practice of python just tried to ")
        print("  Make a switch case kind of applicatyion (or menu)\n")
        print(" ****************************************************** \n")
    else:
        clear()
        print("\n ************************************************* ")
        print("             More features coming soon!!!")
        print(" ************************************************* \n")

while True :
    
    name = input("Enter a User Name : \n")
    clear()
    if name != userName:
        continue
    authentication(name)
    userInput = input("            Enter your option  :-    ")
    menu(userInput)
   




