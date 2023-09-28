from models.shopper import Shopper
from helper_functions.helpers import exit_program, become_member
import time

def login_or_create_account():
    while True:
        print("Do you have an account?")
        choice = input("[y/N]> ").lower()
        if choice == "y":
            print("\nPlease go ahead and login to your account")
            curr_shopper = login()
            if curr_shopper:
                return curr_shopper
        elif choice == "n":
            return create_account()
        else:
            print(f"\n{choice} is not a vaild option, please enter y for YES or N for no.")


def create_account():
    while True:
        print("Would you like to create an account?")
        choice = input("[y/N]> ").lower()
        if choice == "y":
            username = input("Please create a username: ")
            exists = Shopper.does_username_exist(username)

            if exists == True:
                print("This username is already taken, please enter a different one.")
            else:
                age = input("Please enter age: ")
                print("Please create your password, must contain at least 5 characters including 1 number.")
                password = input("Please enter a password: ")
                try:
                    shopper = Shopper.create(username, password, int(age))
                    print(f"\nHi {shopper.user_name}, your account was created successfully!")
                    choice = input("\nWould you like to upgrade your account status to flatstop member?[y/N]> ").lower()
                    if choice == "y":
                        become_member(shopper.id)
                    elif choice == "n":
                        print("Ok, maybe next time!")
                    else:
                        print("Ok, maybe next time!")
                    return shopper
                except Exception as exc:
                    print("There was an error creating your account. Please try again. \n")
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
                    print("Login was successful!")
                    print(f"Hi {shopper.user_name}, welcome back!\n")
                    return shopper
                else:
                    login_attempts += 1
                    print(f"Login failed, incorrect password. Please try again. attempt: {login_attempts}. Max attempts: {max_attempts}.")
            if login_attempts == max_attempts:        
                print("Maximum login attempts reached. Your account has been locked.")
                exit_program()
            
        else:
            print("Sorry no such username exists!")
            print("Would you like to go back or try again? ")
            print("1. Try Again ")
            print("2. Go Back")
            choice = input("> ")
            if choice == "1":
                pass
            elif choice == "2":
                return None