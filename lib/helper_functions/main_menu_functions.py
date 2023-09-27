from helper_functions.browse_store_functions import *
from helper_functions.buy_checkout_functions import *

def main_menu():
    def prompt2():
        print("What can we help you with today?")
        print("1. Browse Store")
        print("2. Buy Items")
        print("3. Sell Items")
        print("4. Chat")
        print("5. Leave Store")

    while True:
        prompt2()
        choice_2 = input("> ")
        if choice_2 == "5":
            exit_program()
        elif choice_2 == "1":
            browse_store()
        elif choice_2 == "2":
            buy_games()
        elif choice_2 == "3":
            sell_game() #PASS IN A GAME ID**
        elif choice_2 == "4":
            print("Will show chatting prompt and will prompt questions for store attendee?")
        else:
            print(f"{choice_2} is not a valid input. Please enter a number 1-5.\n")