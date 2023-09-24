# lib/helpers.py
from models.shopper import Shopper
from models.game import Game
import time


def login_or_create_account():
    print("Do you have an account?")
    choice = input("[y/N]> ").lower()
    if choice == "y":
        # name = login() - if we want to use name of user
        print("\nPlease go ahead and login to your account")
        login()
    elif choice == "n":
        # name = create_account() - if we want to use name of user
        create_account()
    else:
        print("Invalid choice, please enter y for YES or N for no.")
        login_or_create_account()
    
    # return name - if we want to use name of user

def create_account():
    print("Would you like to create an account?")
    choice = input("[y/N]> ").lower()
    if choice == "y":
        username = input("Please create a username: ")
        exists = Shopper.does_username_exist(username)

        if exists == True:
            print("This username is already taken, please enter a different one.")
            create_account()

        age = input("Please enter age: ")
        print("Please create your password, must contain at least 5 characters including 1 number.")
        password = input("Please enter a password: ")

        try:
            shopper = Shopper.create(username, password, int(age))
            print(f"Hi {shopper.user_name}, your account was created successfully!")
            # return shopper.user_name - if we want to use shopper name later
        except Exception as exc:
            print("There was an error creating your account. Please try again.")
            print("Error:", exc)
            create_account()

    else:
        print("Okay maybe next time!")
        exit_program()

def login():
    login_attempts = 0
    max_attempts = 3

    username = input("Please enter your username: ")
    shopper = Shopper.find_by_username(username)

    if shopper:
        while login_attempts < max_attempts:
            password = input("Enter password: ")
            if shopper.password == password:
                print("\nLogging in....\n")
                time.sleep(2)
                #changed shopper function name here
                shopper = Shopper.find_by_username(username)
                print("Login was successful!")
                print(f"Hi {shopper.user_name}, welcome back!\n")
                break
                # return shopper.user_name - if we want to use shopper name later
            else:
                login_attempts += 1
                print(f"Login failed, incorrect password. Please try again. attempt: {login_attempts}. Max attempts: {max_attempts}.")
        if login_attempts == max_attempts:        
            print("Maximum login attempts reached. Your account has been locked.")
            exit_program()
    else:
        print("Sorry no such username exists!")
        print("Would you like to try to login in again or create a new account?")
        print("0. Exit program")
        print("1. Login again")
        print("2. Create an account")
        login_menu()

def login_menu():
    choice = input("> ")
    if choice == "0":
        print("Okay please come back soon!")
        exit_program()
    elif choice == "1":
        login()
    elif choice =="2":
        create_account()
    else:
        print("Invalid choice, please enter a valid number: 0, 1, 2")
        login_menu()

def show_store():

    figure = '''
__________________________________________________________________
           |                       |                              |
           |    F L A T S T O P    |______________________________|
|__________|_______________________|_________||_|_|_|_|_|_|_|_|_|_|
|__||  ||___||  |_|___|___|__|  ||___||  ||__||_|_|_|_|_|_|_|_|_|_|
||__|  |__|__|  |___|___|___||  |__|__|  |__|||_|_|_|_|_|_|_|_|_|_|
|__||  ||___||  |_|___|___|__|  ||___||  ||__||_|_|_|_|_|_|_|_|_|_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|     Games     |_|
|__||  ||___|| |     || |     | ||___||  ||__||_|.   Consoles   |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|*`.            |_|
|__||  ||___|| |     || |     | ||___||  ||__||_| S `.          |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|`. A `.        |_|
|__||  ||___|| |    [|| |]    | ||___||  ||__||_|  `. L `.      |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|    `. E `.    |_|
|__||  ||___|| |_____|| |     | ||___||  ||__||_|______`__*_`___|_|
||__|  |__|__|_| ____||_|____ | |__|__|  |__|||_|_|_|_|_|_|_|_|_|_|
|***|  |LLLLL|_______________|| |LLLLL|  |LLL|  |LLLLL|LLLLL|LLLLL|
|***|  |LLL|________________| | |LLLLL|  |LLL|  |LLLLL|LLLLL|LLLLL|
|***|__|L|_________________|__|_|LLLLL|__|LLL|  |LLLLL|LLLLL|LLLLL|
'''

    print(figure)
def show_inside():
    entrance = """

|.'',                                        ,''.|
|.'.'',                                    ,''.'.|
|.'.'.'',                                ,''.'.'.|
|.'.'.'.'',                            ,''.'.'.'.|
|.'.'.'.'.|                            |.'.'.'.'.|
|.'.'.'.'.|===;                    ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',        __      ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, ____|__|    |.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|       |====|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|       |    |,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|       |    |.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\      ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\       ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\          ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\           ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\            ','.'.|
|.','          /%%%%%%%%%%%%%%%\             ','.|
|;____________/%%%%%%%%%%%%%%%%%\   ____________;|

"""
    print("ENTERING STORE...\n\n")
    time.sleep(2)
    print(entrance)



# BUY/SELL + MENU FUNCTIONS
def prompt2():
    print("What are you looking to do?")
    print("1. List all available items")
    print("2. Buy Items")
    print("3. Sell Items")
    print("4. Chat")
    print("5. Leave Store")

games_database = [
    {"id": 1, "title": "Game 1", "price": 19.99},
    {"id": 2, "title": "Game 2", "price": 29.99},
    {"id": 3, "title": "Game 3", "price": 39.99},
]
user_credits = 0

shopping_cart = []

my_games = []

def list_games():
    print("\nAvailable games:")
    games = Game.get_all_available_games()

    for game in games:
        print(game)

def add_to_cart(game_id):
    for game in games_database:
        if game["id"] == game_id:
            shopping_cart.append(game)
            print(f"{game['title']} added to cart.")

def view_cart():
    total_price = sum(game.price for game in shopping_cart)
    print("Shopping Cart:")
    for game in shopping_cart:
        print(f"Title: {game.name}, Price: ${game.price}")
    print(f"Total Price: ${total_price}")

def buy_games():
    view_cart()
    # checkout()
    leave = input("press 1 to escape all")
    if leave == "1":
        exit_program()

def sell_game(game_id):
    for game in games_database:
        if game["game_id"] == game_id:
            my_games.append(game)
            print(f"{game['title']} added to your games.")
            # Add credits to the user when a game is sold
            global user_credits
            user_credits += game["price"]
            #*** THIS IS NOT WORKING, ID ISSUE***

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


def exit_program():
    print("Goodbye!")
    exit()

def show_game_display():
    game_display = '''

    ||-------------------------------------------------------||
    ||.--.    .-._                                           ||
    |||==|____| |H|___                                __ ___ ||
    |||  |====| | |xxx|_                             |G |---|||
    |||==|    | | |   | \                            |E | C |||
    |||  |    | | |   |\ \   .--.                    |A | O |||
    |||  |    | | |   |_\ \_( oo )                   |R | D |||
    |||==|====| |H|xxx|  \ \ |''|                    |S |---|||
    ||`--^----'-^-^---'   `-' ""  -------------------^--^---^||
    ||-------------------------------------------------------||
    ||-------------------------------------------------------||
    ||               ___                   .-.__.-----. .---.||
    ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
    ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
    ||      _a'{ / (|===|+|   |++|  |==|   | |  |Illum| | R |||
    ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |inati| | Y |||
    ||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
    ||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
    ||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
    ||-------------------------------------------------------||
    ||_______________________________________________________||
'''
    print(game_display)

def browse_store():
    show_game_display()
    print("Feel free to browse as long as you want...if you need anything just let us know")
    Browsing = True
    while Browsing:
        prompt3()
        choice_3 = input("> ")
        if choice_3 == "1":
            list_games()
        if choice_3 == "4":
            print("Which game are you grabbing?")
            selected_game = input("Enter Game name: ")
            all_games = Game.get_available_game(selected_game)
            cart_game_ids = [game.id for game in shopping_cart]
            if len(all_games) == 1:
                curr_game = all_games[0]
            else:
                for game in all_games:
                    if game.id not in cart_game_ids:
                        index = all_games.index(game)
                        curr_game = all_games[index]

            
            print("These are all the instances in Game.all")
            print(Game.all)
            if curr_game.id in cart_game_ids:
                print("You already placed this in your cart")
            else:
                shopping_cart.append(curr_game)
                print(shopping_cart)
                print(f"{curr_game} is now in your cart")
        if choice_3 == "5":
            break

def prompt3():
    print("1. List all available games")
    print("2. List all games by rating")
    print("3. Look at game")
    print("4. Add game to cart")
    print("5. Go back to main menu")


