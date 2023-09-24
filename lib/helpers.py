# lib/helpers.py
from models.shopper import Shopper
import time



def login_or_create_account():
    print("Do you have an account?")
    choice = input("[y/N]> ").lower()
    if choice == "y":
        # name = login() - if we want to use name of user
        print("\nPlease go ahead and login to your account")
        login()
    elif choice == "n":
        # name = create_account() - if we want to use name of user
        create_account()
    else:
        print("Invalid choice, please enter y for YES or N for no.")
        login_or_create_account()
    
    # return name - if we want to use name of user

def create_account():
    print("Would you like to create an account?")
    choice = input("[y/N]> ").lower()
    if choice == "y":
        username = input("Please create a username: ")
        exists = Shopper.does_username_exist(username)

        if exists == True:
            print("This username is already taken, please enter a different one.")
            create_account()

        age = input("Please enter age: ")
        print("Please create your password, must contain at least 5 characters including 1 number.")
        password = input("Please enter a password: ")

        try:
            shopper = Shopper.create(username, password, int(age))
            print(f"Hi {shopper.user_name}, your account was created successfully!")
            # return shopper.user_name - if we want to use shopper name later
        except Exception as exc:
            print("There was an error creating your account. Please try again.")
            print("Error:", exc)
            create_account()

    else:
        print("Okay maybe next time!")
        exit_program()

def login():
    login_attempts = 0
    max_attempts = 3

    username = input("Please enter your username: ")
    shopper = Shopper.find_by_username(username)

    if shopper:
        while login_attempts < max_attempts:
            password = input("Enter password: ")
            if shopper.password == password:
                print("\nLogging in....\n")
                time.sleep(2)
                #changed shopper function name here
                shopper = Shopper.find_by_username(username)
                print("Login was successful!")
                print(f"Hi {shopper.user_name}, welcome back!\n")
                break
                # return shopper.user_name - if we want to use shopper name later
            else:
                login_attempts += 1
                print(f"Login failed, incorrect password. Please try again. attempt: {login_attempts}. Max attempts: {max_attempts}.")
        if login_attempts == max_attempts:        
            print("Maximum login attempts reached. Your account has been locked.")
            exit_program()
    else:
        print("Sorry no such username exists!")
        print("Would you like to try to login in again or create a new account?")
        print("0. Exit program")
        print("1. Login again")
        print("2. Create an account")
        login_menu()

def login_menu():
    choice = input("> ")
    if choice == "0":
        print("Okay please come back soon!")
        exit_program()
    elif choice == "1":
        login()
    elif choice =="2":
        create_account()
    else:
        print("Invalid choice, please enter a valid number: 0, 1, 2")
        login_menu()

def show_store():

    figure = '''
__________________________________________________________________
           |                       |                              |
           |    F L A T S T O P    |______________________________|
|__________|_______________________|_________||_|_|_|_|_|_|_|_|_|_|
|__||  ||___||  |_|___|___|__|  ||___||  ||__||_|_|_|_|_|_|_|_|_|_|
||__|  |__|__|  |___|___|___||  |__|__|  |__|||_|_|_|_|_|_|_|_|_|_|
|__||  ||___||  |_|___|___|__|  ||___||  ||__||_|_|_|_|_|_|_|_|_|_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|     Games     |_|
|__||  ||___|| |     || |     | ||___||  ||__||_|.   Consoles   |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|*`.            |_|
|__||  ||___|| |     || |     | ||___||  ||__||_| S `.          |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|`. A `.        |_|
|__||  ||___|| |    [|| |]    | ||___||  ||__||_|  `. L `.      |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|    `. E `.    |_|
|__||  ||___|| |_____|| |     | ||___||  ||__||_|______`__*_`___|_|
||__|  |__|__|_| ____||_|____ | |__|__|  |__|||_|_|_|_|_|_|_|_|_|_|
|***|  |LLLLL|_______________|| |LLLLL|  |LLL|  |LLLLL|LLLLL|LLLLL|
|***|  |LLL|________________| | |LLLLL|  |LLL|  |LLLLL|LLLLL|LLLLL|
|***|__|L|_________________|__|_|LLLLL|__|LLL|  |LLLLL|LLLLL|LLLLL|
'''

    print(figure)
def show_inside():
    entrance = """

|.'',                                        ,''.|
|.'.'',                                    ,''.'.|
|.'.'.'',                                ,''.'.'.|
|.'.'.'.'',                            ,''.'.'.'.|
|.'.'.'.'.|                            |.'.'.'.'.|
|.'.'.'.'.|===;                    ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',        __      ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, ____|__|    |.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|       |====|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|       |    |,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|       |    |.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\      ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\       ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\          ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\           ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\            ','.'.|
|.','          /%%%%%%%%%%%%%%%\             ','.|
|;____________/%%%%%%%%%%%%%%%%%\   ____________;|

"""
    print("ENTERING STORE...\n\n")
    time.sleep(2)
    print(entrance)








def exit_program():
    print("Goodbye!")
    exit()