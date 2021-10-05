case = int(input('password : '))

if case==3102: 
    print("Password Correct")
    select = int(input('Enter the number : '))
    
    if select == 1: print("You Enter the 1")
    elif select == 2: print("You Enter the 2")
    elif select == 1023: print("New Password Detected")

    new_password = int(input('Enter the Number : '))
    if new_password == 456 : print("□") 

elif case==4001:
    print("Welcome Owner")
    select = int(input('Enter the number : '))

    if select == 1 : print("You Enter the 391")

else : print("Failed")