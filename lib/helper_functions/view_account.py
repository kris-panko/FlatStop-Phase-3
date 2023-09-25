from models.shopper import Shopper
from helper_functions.helpers import *

def get_account(shopper):
    curr_shopper = Shopper.find_by_username(shopper.user_name)
    print("\nHere are your account details:\n")
    print("Username: " + curr_shopper.user_name)
    print("Password: " + curr_shopper.password)
    print("Age: ", curr_shopper.age)
    while True:
        print("\n1. Would you like to update your account?")
        print("2. Would you like to delete your account?")
        print("3. Go back to main menu")
        choice = input("> ")
        if choice == "1":
            print("\n1. Update username")
            print("2. Update password")
            print("3. Update age")
            get_account(shopper)
        elif choice == "2":
            print("\nAre you sure you want to delete your account?")
            print("We'd hate to see you go....")
            choice1 = input("[y/N] ")
            if choice1 == "y":
                print("\nFine, good riddance...")
                Shopper.delete_shopper_from_db(curr_shopper.id)
                print("\nYour account has been successfully deleted")
                exit_program()
            elif choice == "N":
                get_account(shopper)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please enter a number 1-3")


            
