#!/usr/bin/env python3 
import argparse
from helpers import *

def main():
    parser = argparse.ArgumentParser(description="FlatStop")
    parser.add_argument("--list", action="store_true", help="List available games")
    parser.add_argument("--add", type=int, help="Add a game to the cart by specifying its ID")
    parser.add_argument("--cart", action="store_true", help="View shopping cart")
    parser.add_argument("--buy", action="store_true", help="Buy games in the cart")
    parser.add_argument("--sell", type=int, help="Sell a game by specifying its ID")
    parser.add_argument("--mygames", action="store_true", help="List your games")
    parser.add_argument("--credits", action="store_true", help="Check your credits")

    args = parser.parse_args()

    if args.list:
        list_games()
    elif args.add:
        add_to_cart(args.add)
    elif args.cart:
        view_cart()
    elif args.buy:
        buy_games()
    elif args.sell:
        sell_game(args.sell)
    elif args.mygames:
        list_my_games()
    elif args.credits:
        check_credits()
    #cur_user = login_or_create_account() - if we want to use name of user
    
    # print("Welcome to FlatStop!")
    # login_or_create_account()
    # buy_sell_menu()

    show_store()
    prompt1()
    choice = input("> ")
    if choice == "1":
        show_inside()
        greeting()
        login_or_create_account()
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
        exit_program()


def greeting():
    print("Hi there welcome to FlatShop our online Interactive Store")
    print("Before getting started, please verify your account with us...\n")
def prompt1():
    print("Enter FlatStop?")
    print("1. Enter the store")
    print("2. Don't Enter the store")
def prompt2():
    print("\nWhat are you looking to do?")
    print("1. Browse Store")
    print("2. Buy Items")
    print("3. Sell Items")
    print("4. Chat")
    print("5. Leave Store")
    #PRINT
def prompt3():
    print("Feel free to browse as long as you want...if you need anything just let us know")
    print("1. List all available games")
    print("2. List all games by rating")
    print("3. Look at game")
    print("4. Add game to cart")
    print("5. Go back to main menu")

# def buy_sell_menu():
#     print("How can we help you today?")
#     print("Please select one of the following options: ")
#     print("0. Log out")
#     print("1. Buy a video game or console.")
#     print("2. Sell a video game or console.")
    
    # choice = input("> ")
    # if choice == "0":
    #     print("Okay please come back soon!")
    #     print("Logging out....")
    #     exit_program()
    # elif choice == "1":
    #     buy_game_or_console()
    # elif choice =="2":
    #     sell_game_or_console()
    # else:
    #     print("Invalid choice, please enter a valid number: 0, 1, 2")
    #     buy_sell_menu()


if __name__ == "__main__":
    main()