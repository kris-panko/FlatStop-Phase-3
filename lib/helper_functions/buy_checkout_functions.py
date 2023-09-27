from helper_functions.helpers import exit_program
from helper_functions.browse_store_functions import shopping_cart

def buy_games():
    view_cart()
    # checkout()
    leave = input("press 1 to escape all")
    if leave == "1":
        exit_program()

def view_cart():
    total_price = sum(game.price for game in shopping_cart)
    print("Shopping Cart:")
    for game in shopping_cart:
        print(f"Title: {game.name}, Price: ${game.price}")
    print(f"Total Price: ${total_price}")

# need to update this checkout function
def checkout():
    total_price = sum(game["price"] for game in shopping_cart)
    print(f"Total Price: ${total_price}")
    choice = input("Enter 'yes' to confirm purchase, or 'no' to cancel: ")
    if choice.lower() == "yes":
        for game in shopping_cart:
            my_games.append(game)
        shopping_cart.clear()
        print("Thank you for your purchase!")
    else:
        print("Purchase canceled.")