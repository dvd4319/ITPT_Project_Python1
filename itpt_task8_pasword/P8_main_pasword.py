"""

Implement and test a program to enter and validate a password. The program should do the following:
 - Prompt the user to enter their password that can contain letters and numbers and be at least six characters long.
 - If the password is correct, it should display a welcome message.
 - If not, it should notify the user that their password was entered wrongly, 
    they should be warned that they will be locked out of the system 
    after three attempts and let them try again, but only allow three tries.
 - If the user makes three incorrect attempts they should receive a suitable message.

"""

def password_validate(password):
    SpecialSymbol =['!', '£', '$', '@', '#', '%'] 
    val = True
      
    if len(password) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(password) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in password): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in password): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in password): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if any(char in SpecialSymbol for char in password): 
        print('Password should not have one of the symbols $@#!£') 
        val = False
    if val: 
        return val 

    
def main(): 
    password = input("Enter the Password: ")
    if (password_validate(password)):
        print("Welcome. Password is valid")
        break
    else:
        print("Sorry. Password is invalid!!") 

count =3
while count >= 0:
    if count != 0:
        print("You have " + str(count) + " try left")
        main()
    else:
        print("Sorry, the account is blocked, no more try left.")
    count = count -1;