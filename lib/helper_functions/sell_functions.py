from models.game import Game
from helper_functions.figures import show_cashier

def sell_game(shopper):
    print(shopper)
    show_cashier()
    game_name = input("Hi, what game were you looking to sell today? ")
    game_rating = input("What's the rating of this game? ")
    game_price = input("What price did you pay for this game? ")
    new_Game = Game.create(game_name,float(game_price),game_rating,shopper.id)
    offer_price = 10.00
    print(f'''Ok based, off that information we're willing to give you... ${offer_price}0''')
    print("Are you okay with selling your game for this price? ")
    while True:
        choice = input("[y/N] ")
        if choice == "y":
            float(offer_price)
            store_price = offer_price * 4
            Game.update_price_and_owner(new_Game.id, store_price)
            print("Pleasure doing business with you....sucker")
            break
        elif choice == "N":
            #Come back here to add haggle functionality
            print("Well get out of here then!")
            print("Walk away from offer?")
            choice = input("[y/N]")
            if choice == "y":
                break
            elif choice == "N":
                print("Well that was our offer, are you going to accept it this time?")


        


        



    # for game in games_database:
    #     if game["game_id"] == game_id:
    #         my_games.append(game)
    #         print(f"{game['title']} added to your games.")
    #         # Add credits to the user when a game is sold
    #         global user_credits
    #         user_credits += game["price"]
    #         #*** THIS IS NOT WORKING, ID ISSUE***