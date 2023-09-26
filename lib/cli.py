import argparse

games_database = [
    {"id": 1, "title": "Game 1", "price": 19.99},
    {"id": 2, "title": "Game 2", "price": 29.99},
    {"id": 3, "title": "Game 3", "price": 39.99},
]

user_credits = 0

shopping_cart = []

my_games = []

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
    else:
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                helper_1()
            else:
                print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")

def exit_program():
    print("Exiting the program...")
    # Add any necessary exit cleanup here
    exit()

def helper_1():
    print("This is helper function 1.")

def list_games():
    print("Available games:")
    for game in games_database:
        print(f"ID: {game['id']}, Title: {game['title']}, Price: ${game['price']}")

def add_to_cart(game_id):
    for game in games_database:
        if game["id"] == game_id:
            shopping_cart.append(game)
            print(f"{game['title']} added to cart.")

def view_cart():
    total_price = sum(game["price"] for game in shopping_cart)
    print("Shopping Cart:")
    for game in shopping_cart:
        print(f"Title: {game['title']}, Price: ${game['price']}")
    print(f"Total Price: ${total_price}")

def buy_games():
    view_cart()
    checkout()

def sell_game(game_id):
    for game in games_database:
        if game["id"] == game_id:
            my_games.append(game)
            print(f"{game['title']} added to your games.")
            # Add credits to the user when a game is sold
            global user_credits
            user_credits += game["price"]

def list_my_games():
    print("My Games:")
    for game in my_games:
        print(f"ID: {game['id']}, Title: {game['title']}, Price: ${game['price']}")

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

def check_credits():
    print(f"Your current credits: ${user_credits}")

if __name__ == "__main__":
    main()
