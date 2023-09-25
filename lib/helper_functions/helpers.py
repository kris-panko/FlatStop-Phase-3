# lib/helpers.py
from models.shopper import Shopper

def become_member(id):
    print("In order to become a flatstop member you'll need to complete a quick survey: ")
    while True:
        choice = input("Complete survey?[y/N]> ").lower()
        if choice == "y":
            choice1 = input("What genre of game do you usually play? ")
            choice2 = input("We want to recommend you games that you'll like. What is your preferred game rating? ")
            choice3 = input("What is your favorite game that you currently own? ")
            Shopper.update_member_status(id)
            print("\nThank you for completing our short survey!\n Membership has its perks!\n")
            break
        elif choice == "n":
            print("Okay, maybe next time!")
            break
        else:
            print("\nInvalid input, please enter a y or N")

def exit_program():
    print("Goodbye!")
    exit()
