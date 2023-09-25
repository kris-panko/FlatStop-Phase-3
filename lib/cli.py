#!/usr/bin/env python3 

from helpers import *


def main():
    while True:
        login_or_create_account()


def login_or_create_account():
    print("Do you have an account?")
    choice = input("[y/N] ")
    if choice == "y":
        login()
    elif choice == "N":
        create_account()
    else:
        print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
