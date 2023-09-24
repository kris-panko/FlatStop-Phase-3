# lib/helpers.py
from models.shopper import Shopper
import time



def login_or_create_account():
    print("Do you have an account?\n")
    choice = input("[y/N] ")
    if choice == "y":
        print("Please go ahead and login to your account\n")
        login()
    elif choice == "N":
        create_account()
    else:
        print("Invalid choice")

def create_account():
    print("Would you like to create an account?")
    choice = input("[y/N]> ")
    if choice == "y":
        username = input("Please create a username: ")
        password =  input("Please create your password, must contain at least 5 characters including 1 number")
        age = input("Please enter age: ")

        try:
            shopper = Shopper.create(username, password, int(age))
            print(f"Hi {shopper.user_name}, your account was created successfully!")
        except Exception as exc:
            print("Sorry there was an error creating your account. Please try again later: ", exc)

    else:
        print("Okay maybe next time!")
        exit_program()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    try:
        print("\nLogging in....\n")
        time.sleep(2)
        shopper = Shopper.get_shopper_account(username, password)
        print("Login was successful!")
        print(f"Hi {shopper.user_name} welcome back!\n")
    except Exception as exc:
        print("Invalid username or password, please try again")

def exit_program():
    print("Goodbye!")
    exit()

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