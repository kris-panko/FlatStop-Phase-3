from models.shopper import Shopper
from helper_functions.helpers import exit_program
import time
#RETURN POINT HERE
def login_or_create_account():
    while True:
        print("Do you have an account?")
        choice = input("[y/N]> ").lower()
        if choice == "y":
            # name = login() - if we want to use name of user
            print("\nPlease go ahead and login to your account")
            return login()
            # return curr_shopper
        elif choice == "n":
            # name = create_account() - if we want to use name of user
            return create_account()
            # return curr_shopper
        else:
            print(f"\n{choice} is not a vaild option, please enter y for YES or N for no.")
            # login_or_create_account()
    
    # return name - if we want to use name of user

def create_account():
    while True:
        print("Would you like to create an account?")
        choice = input("[y/N]> ").lower()
        if choice == "y":
            username = input("Please create a username: ")
            exists = Shopper.does_username_exist(username)

            if exists == True:
                print("This username is already taken, please enter a different one.")
                # create_account()

            age = input("Please enter age: ")
            print("Please create your password, must contain at least 5 characters including 1 number.")
            password = input("Please enter a password: ")

            try:
                shopper = Shopper.create(username, password, int(age))
                print(f"Hi {shopper.user_name}, your account was created successfully!")
                return shopper
                # return shopper.user_name - if we want to use shopper name later
            except Exception as exc:
                print("There was an error creating your account. Please try again.")
                print("Error:", exc)
                # create_account()
        elif choice == "n":
            print("Okay maybe next time!")
            exit_program()
        else:
            print("Invalid input, please enter y or n")

def login():
    login_attempts = 0
    max_attempts = 3
    while True:
        username = input("Please enter your username: ")
        shopper = Shopper.find_by_username(username)

        if shopper:
            while login_attempts < max_attempts:
                password = input("Enter password: ")
                if shopper.password == password:
                    print("\nLogging in....\n")
                    time.sleep(2)
                    #changed shopper function name here
                    print("Login was successful!")
                    print(f"Hi {shopper.user_name}, welcome back!\n")
                    print(shopper)
                    return shopper
                    # return shopper.user_name - if we want to use shopper name later
                else:
                    login_attempts += 1
                    print(f"Login failed, incorrect password. Please try again. attempt: {login_attempts}. Max attempts: {max_attempts}.")
            if login_attempts == max_attempts:        
                print("Maximum login attempts reached. Your account has been locked.")
                exit_program()
            
        else:
            print("Sorry no such username exists!")
            print("Try again:")
            # print("Would you like to try to login in again or create a new account?")
            # print("0. Exit program")
            # print("1. Login again")
            # print("2. Create an account")
            # login_menu()

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