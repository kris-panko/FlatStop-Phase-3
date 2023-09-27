#!/usr/bin/env python3 
import argparse
from helper_functions.helpers import exit_program
from helper_functions.login_create_account_functions import *
from helper_functions.figures import show_store, show_inside
from helper_functions.main_menu_functions import *

def greeting():
    print("Hi there welcome to FlatShop our online Interactive Store")
    print("Before getting started, please verify your account with us...\n")
def prompt1():
    print("Enter FlatStop?")
    print("1. Enter the store")
    print("2. Don't Enter the store")

def main():

    show_store()
    while True:
        prompt1()
        choice = input("> ")
        if choice == "1":
            show_inside()
            greeting()
            login_or_create_account()
            main_menu()
        elif choice == "2":
            exit_program()
        else:
            print("Input invalid, please try again.\n")
    

if __name__ == "__main__":
    main()


# parser = argparse.ArgumentParser(description="FlatStop")
# parser.add_argument("--list", action="store_true", help="List available games")
# parser.add_argument("--add", type=int, help="Add a game to the cart by specifying its ID")
# parser.add_argument("--cart", action="store_true", help="View shopping cart")
# parser.add_argument("--buy", action="store_true", help="Buy games in the cart")
# parser.add_argument("--sell", type=int, help="Sell a game by specifying its ID")
# parser.add_argument("--mygames", action="store_true", help="List your games")
# parser.add_argument("--credits", action="store_true", help="Check your credits")

# args = parser.parse_args()

# if args.list:
#     list_games()
# elif args.add:
#     add_to_cart(args.add)
# elif args.cart:
#     view_cart()
# elif args.buy:
#     buy_games()
# elif args.sell:
#     sell_game(args.sell)
# elif args.mygames:
#     list_my_games()
# elif args.credits:
#     check_credits()
#cur_user = login_or_create_account() - if we want to use name of user

# print("Welcome to FlatStop!")
# login_or_create_account()
# buy_sell_menu()