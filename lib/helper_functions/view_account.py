from models.shopper import Shopper
from helper_functions.helpers import *

def get_account(shopper):
    print("PRINTING FROM GET ACCOUNT")
    print(shopper)
    curr_shopper = Shopper.find_by_username(shopper.user_name)
    print(curr_shopper)
    print("\nHere are your account details:\n")
    print("Username: " + curr_shopper.user_name)
    print("Password: " + curr_shopper.password)
    print("Age: ", curr_shopper.age)
    while True:
        print(shopper)
        print("\n1. Would you like to update your account?")
        print("2. Would you like to delete your account?")
        print("3. Go back to main menu")
        choice = input("> ")
        if choice == "1":
            while True:
                print("\n1. Update username")
                print("2. Update password")
                print("3. Update age")
                print("4. Return to Account Options")
                choice = input("> ")
                if choice == "1":
                    while True:
                        print("Please enter your new username: ")
                        new_username = input("> ")
                        if Shopper.does_username_exist(new_username):
                            print("This username is already taken, please enter a different one.")
                        else:
                            curr_shopper.user_name = new_username
                            if curr_shopper.user_name == new_username:
                                Shopper.update_username(curr_shopper.id, curr_shopper.user_name)
                                print("You're username has been successfully updated.")
                                break
                elif choice == "2":
                    break
                elif choice == "3":
                    break
                elif choice == "4":
                    break
                else:
                    print("Invalid input, please enter a number 1-3")
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


            
