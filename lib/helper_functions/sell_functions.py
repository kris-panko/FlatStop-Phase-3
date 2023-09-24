from models.game import Game

def sell_game(shopper):
    print(shopper)
    game_name = input("Hi, what game were you looking to sell today? ")
    game_rating = input("What's the rating of this game?")
    game_price = input("What price did you pay for this game?")
    Game.create(game_name,int(game_price),game_rating,shopper.id)
    offer_price = 10.00
    print(f"Ok based, off that information we're willing to give you...{offer_price}")
    print("Are you okay with selling your game for this price? ")
    while True:
        choice = input("[y/N] ")
        if choice == "y":
            # transfer_ownership()
            # update_price()
            print("Here we would transfer ownership")
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