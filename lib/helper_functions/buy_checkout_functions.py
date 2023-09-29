from helper_functions.helpers import exit_program
from helper_functions.browse_store_functions import shopping_cart
from helper_functions.figures import show_cashier
from helper_functions.helpers import become_member
from models.game import Game
import time

def buy_from_store(curr_shopper):
    view_cart(curr_shopper)
    checkout()

def view_cart(curr_shopper):
    print("\nApproaching register...\n\n")
    time.sleep(2)
    total_price = sum(game.price for game in shopping_cart)
    show_cashier(total_price)
    if curr_shopper.member == 1:
        print("\nShopping Cart:")
        for game in shopping_cart:
            print(f"Title: {game.name}, Price: ${game.price}")
        print(f"Total Price: ${total_price}")
        print(f"I do see that you're flatstop store member so you get a 40% discount")
        total_price = total_price - int(total_price *.4)
        print(f"New Total Price is ${total_price}")
    elif curr_shopper.member == 0:
        print("We noticed you're not currently a member, would sign up to become one?")
        print("Members are elligible for discounts on games")
        choice = input("[y/N]> ").lower()
        if choice == "y":
            become_member(curr_shopper.id)
            original_price = total_price
            total_price -= int(total_price *.4)
            show_cashier(total_price)
            print("\nShopping Cart:")
            for game in shopping_cart:
                print(f"Title: {game.name}, Price: ${game.price}")
            print(f"\nOk your Total Price would have been: ${original_price}")
            print(f"But after applying your 40% discount")
            print(f"Your new total is ${total_price}")
        else:
            print("\nShopping Cart:")
            for game in shopping_cart:
                print(f"Title: {game.name}, Price: ${game.price}")
            print(f"Total Price: ${total_price}")


def checkout():
    if len(shopping_cart) == 0:
        print("Hey you haven't picked up anything to buy...come back when you're ready to make a purchase.\n")
        time.sleep(5)
        return None
    while True:
        choice = input("\nEnter 'yes' to confirm purchase, or 'no' to cancel: ").lower()
        if choice == "yes":
            for game in shopping_cart:
                Game.remove_game_from_db(game.id)
            shopping_cart.clear()
            print("Thank you for your purchase!\n")
            time.sleep(3)
            break
        elif choice == "no":
            print("Purchase cancelled\n")
            break
        else:
            print("hmmm...not quite sure what you meant there...")