def hello():
    print('Hello this is a function')
    print('Good Day to you sir!!')

hello()
print('\nLets use the function again \n ')
hello()

def greeting(name):
    print('Hello '+name)
    
userName = input('Enter a Name :- ')    
greeting(userName)

def addition(a, b):
    c = a + b
    print(str(a)+' pluss '+str(b)+' is '+str(c))

num1 = int(input('Enter Number one :- '))
num2 = int(input('Enter Number two :- '))
addition(num1, num2)