from helper_functions.browse_store_functions import *
from helper_functions.buy_checkout_functions import *
from helper_functions.sell_functions import *
from helper_functions.view_account import *
from helper_functions.figures import show_good_employee


def main_menu(shopper):
    def prompt2():
        print("\nWhat can we help you with today?")
        print("1. Browse Games")
        print("2. Buy/Checkout Items")
        print("3. Sell Items")
        print("4. View your account")
        print("5. Leave Store")

    while True:
        #Place some figure here...
        show_good_employee()
        prompt2()
        curr_shopper = Shopper.find_by_id(shopper.id)
        choice_2 = input("> ")
        if choice_2 == "1":
            browse_store()
        elif choice_2 == "2":
            buy_from_store(curr_shopper)
        elif choice_2 == "3":
            sell_game(curr_shopper) 
        elif choice_2 == "4":
            get_account(curr_shopper)
        elif choice_2 == "5":
            exit_program()
        else:
            print(f"{choice_2} is not a valid input. Please enter a number 1-5.\n")