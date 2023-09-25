from helper_functions.helpers import exit_program
from helper_functions.browse_store_functions import shopping_cart
from helper_functions.figures import show_cashier
from models.game import Game

def buy_from_store():
    show_cashier()
    view_cart()
    checkout()
    # leave = input("press 1 to escape all")
    # if leave == "1":
    #     exit_program()

def view_cart():
    total_price = sum(game.price for game in shopping_cart)
    print("\nShopping Cart:")
    for game in shopping_cart:
        print(f"Title: {game.name}, Price: ${game.price}")
    print(f"Total Price: ${total_price}")

# need to update this checkout function
def checkout():
    choice = input("\nEnter 'yes' to confirm purchase, or 'no' to cancel: ")
    if choice.lower() == "yes":
        # Delete from database
        for game in shopping_cart:
            Game.remove_game_from_db(game.id)
        shopping_cart.clear()
        print("Thank you for your purchase!\n")
    else:
        print("Purchase canceled.\n")