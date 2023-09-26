#!/usr/bin/env python3 
from helpers import *


def main():
    #cur_user = login_or_create_account() - if we want to use name of user
    print("Welcome to FlatStop!")
    login_or_create_account()
    buy_sell_menu()


def login_or_create_account():
    print("Do you have an account?")
    choice = input("[y/N]> ")
    if choice == "y":
        # name = login() - if we want to use name of user
        login()
    elif choice == "N":
        # name = create_account() - if we want to use name of user
        create_account()
    else:
        print("Invalid choice, please enter y for YES or N for no.")
        login_or_create_account()
    
    # return name - if we want to use name of user

def buy_sell_menu():
    print("How can we help you today?")
    print("Please select one of the following options: ")
    print("0. Log out")
    print("1. Buy a video game or console.")
    print("2. Sell a video game or console.")
    
    choice = input("> ")
    if choice == "0":
        print("Okay please come back soon!")
        print("Logging out....")
        exit_program()
    elif choice == "1":
        buy_game_or_console()
    elif choice =="2":
        sell_game_or_console()
    else:
        print("Invalid choice, please enter a valid number: 0, 1, 2")
        buy_sell_menu()


if __name__ == "__main__":
    main()
