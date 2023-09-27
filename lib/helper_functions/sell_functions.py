def sell_game(game_id):
    for game in games_database:
        if game["game_id"] == game_id:
            my_games.append(game)
            print(f"{game['title']} added to your games.")
            # Add credits to the user when a game is sold
            global user_credits
            user_credits += game["price"]
            #*** THIS IS NOT WORKING, ID ISSUE***