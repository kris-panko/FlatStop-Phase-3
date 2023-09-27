from models.game import Game
from helper_functions.figures import show_game_display

shopping_cart = []

def browse_store():
    show_game_display()
    print("Feel free to browse as long as you want...if you need anything just let us know")
    Browsing = True
    while Browsing:
        prompt3()
        choice_3 = input("> ")
        if choice_3 == "1":
            list_games()
        elif choice_3 == "2":
            while True:
                print("\nWhat rated games would you like to search for?")
                rating = input("Please enter M, T, E: ").upper()
                if rating not in Game.RATINGS:
                    print(f"{rating} is not a vaild rating. Please enter a vaild rating.")
                else:
                    games = Game.find_by_rating(rating)
    
                    if games == []:
                        print(f"Sorry, doesn't seem like we have any {rating} rated games in stock right now.")
                        break
                    else:
                        print(f"\nThese are the games we have that are rated {rating}:")
                        game_names = list({game.name for game in games})
                        for name in game_names:
                            print(name)
                        break
        elif choice_3 == "4":
            print("\nWhich game are you grabbing?")
            selected_game = input("Enter Game name: ")

            all_games = Game.find_by_name(selected_game)
            cart_game_ids = [game.id for game in shopping_cart]

            if len(all_games) == 0:
                print(f"Sorry we did not find {selected_game} in our store. Please check your spelling and try again.")
            elif len(all_games) == 1:
                curr_game = all_games[0]
                if curr_game.id in cart_game_ids:
                    print("You already placed this in your cart")
                else:
                    shopping_cart.append(curr_game)
                    print(shopping_cart)
                    print(f"{curr_game.name} is now in your cart")
            else:
                for game in all_games:
                    if game.id not in cart_game_ids:
                        index = all_games.index(game)
                        curr_game = all_games[index]
   
                if curr_game.id in cart_game_ids:
                    print("You already placed this in your cart")
                else:
                    shopping_cart.append(curr_game)
                    print(shopping_cart)
                    print(f"{curr_game.name} is now in your cart")
        elif choice_3 == "5":
            break
        else:
            print(f"{choice_3} is not a valid input, please enter a number 1-5.")

def list_games():
    print("\nAvailable games:")
    games = Game.get_all()

    for game in games:
        print(game)
    print("")

def prompt3():
    print("\nWhat would you like to do next?")
    print("1. List all available games")
    print("2. List all games by rating")
    print("3. Look at game")
    print("4. Add game to cart")
    print("5. Go back to main menu")