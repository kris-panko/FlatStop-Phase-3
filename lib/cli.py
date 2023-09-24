#!/usr/bin/env python3 

from helpers import *

def main():
    #cur_user = login_or_create_account() - if we want to use name of user
    
    # print("Welcome to FlatStop!")
    # login_or_create_account()
    # buy_sell_menu()
    while True:
        show_store()
        prompt1()
        choice = input("> ")
        if choice == "1":
            show_inside()
            greeting()
            login_or_create_account()
            prompt2()
            choice_2 = input("> ")
            if choice_2 == "0":
                exit_program()
            elif choice_2 == "1":
                print("Wil show next prompt asking what they would like to view")
            elif choice_2 == "2":
                print("Will bring them to cashier and allow shopper to buy items in cart?")
            elif choice_2 == "3":
                print("Will bring them cashiet and allow shopper to sell items they own?")
            elif choice_2 == "4":
                print("Will show chatting prompt and will prompt questions for store attendee?")
        else:
            exit_program()



def greeting():
    print("Hi there welcome to FlatShop our online Interactive Store")
    print("Before getting started, please verify your account with us...\n")
def prompt1():
    print("Enter FlatStop?")
    print("0. Don't Enter the store")
    print("1. Enter the store")
def prompt2():
    print("What are you looking to do?")
    print("0. Leave Store")
    print("1. Browse Items")
    print("2. Buy Items")
    print("3. Sell Items")
    print("4. Chat")


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