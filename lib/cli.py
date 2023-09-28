#!/usr/bin/env python3 
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
            curr_shopper = login_or_create_account()
            main_menu(curr_shopper)
        elif choice == "2":
            exit_program()
        else:
            print(f"{choice} is not a valid input. Please enter either 1 or 2.\n")
    

if __name__ == "__main__":
    main()
