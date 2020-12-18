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
            print("Access Granted !!")
            break
    
