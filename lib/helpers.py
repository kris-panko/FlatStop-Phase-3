# lib/helpers.py
from models.shopper import Shopper

def create_account():
    print("Would you like to create an account?")
    choice = input("[y/N]> ").lower()
    if choice == "y":
        username = input("Please create a username: ")
        age = input("Please enter age: ")

        try:
            shopper = Shopper.create(username, int(age))
            print(f"Hi {shopper.user_name}, your account was created successfully!")
        except Exception as exc:
            print("Sorry there was an error creating your account. Please try again later: ", exc)

    else:
        print("Okay maybe next time!")
        exit_program()
def login():
    username = input("Please enter your username: ")
    try:
        print("Logging in....")
        #changed shopper function name here
        shopper = Shopper.find_by_username(username)
        print(f"Hi {shopper.user_name} welcome back! ")
    except Exception as exc:
        print("Sorry no such account exists, please try again")

def exit_program():
    print("Goodbye!")
    exit()