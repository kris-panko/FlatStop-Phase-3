# lib/helpers.py
from models.shopper import Shopper

def create_account():
    print("Would you like to create an account?")
    choice = input("[y/N]> ")
    if choice == "y":
        username = input("Please create a username: ")
        exists = Shopper.does_username_exist(username)

        if exists == True:
            print("This username is already take, please enter a different one.")
            create_account()

        age = input("Please enter age: ")
        print("Password must be 8 characters or longer.")
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
    shopper = Shopper.get_shopper_account(username)

    if shopper:
        while login_attempts < max_attempts:
            password = input("Enter password: ")
            if shopper.password == password:
                print("Logging in....")
                print(f"Hi {shopper.user_name}, welcome back! ")
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
        print("Would you like to try to login in again or create a new accout?")
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




def exit_program():
    print("Goodbye!")
    exit()