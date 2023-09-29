from models.shopper import Shopper
from helper_functions.helpers import *

def get_account(shopper):
    curr_shopper = Shopper.find_by_id(shopper.id)
    print("\nHere are your account details:\n")
    while True:
        curr_shopper = Shopper.find_by_id(shopper.id)
        member_status = "Member" if curr_shopper.member == 1 else "Not member"
        print(f"""
        ------------------------------------------
        * Username : {curr_shopper.user_name} 

        * Password: {curr_shopper.password} 

        * Age: {curr_shopper.age}

        * Membership Status: {member_status}
    
        -------------------------------------------            
        """)
        print("\n1. Would you like to update your account?")
        print("2. Would you like to delete your account?")
        print("3. Sign up to become a FlatStop member and receive discounts.")
        print("4. Go back to main menu")
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
                                print("Your username has been successfully updated.")
                                break
                elif choice == "2":
                    while True:
                        print("Please enter a new password: ")
                        new_password = input("> ")
                        if curr_shopper.password == new_password:
                            print("Your new password is the same as your old password.")
                        else:
                            curr_shopper.password = new_password
                            if curr_shopper.password == new_password:
                                Shopper.update_password(curr_shopper.id, curr_shopper.password)
                                print("Your password has been successfully updated.")
                                break
                elif choice == "3":
                    while True:
                        print("Please enter your age: ")
                        new_age = input("> ")
                        try:
                            new_age_int = int(new_age)
                        except:
                            print("Please enter a valid numerical age over 12")

                        if "new_age_int" in locals() and curr_shopper.age == new_age_int:
                            print("Looks like you didn't get any older- weird!")
                        elif "new_age_int" in locals():
                            curr_shopper.age = new_age_int
                            if curr_shopper.age == new_age_int:
                                Shopper.update_age(curr_shopper.id, curr_shopper.age)
                                print("Your age has been successfully updated.")
                                break
                    break
                elif choice == "4":
                    break
                else:
                    print("Invalid input, please enter a number 1-4")
        elif choice == "2":
            print("\nAre you sure you want to delete your account?")
            print("We'd hate to see you go....")
            choice1 = input("[y/N] ").lower()
            if choice1 == "y":
                print("\nFine, good riddance...")
                Shopper.delete_shopper_from_db(curr_shopper.id)
                print("\nYour account has been successfully deleted")
                exit_program()
            elif choice == "n":
                break
        elif choice == "3":
            if (curr_shopper.member) == 1:
                print("You're already a member. Can't become a double member...or can you? NO.")
            else:
                become_member(shopper.id)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please enter a number 1-4")

