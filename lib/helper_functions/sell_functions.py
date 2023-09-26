from models.game import Game
from helper_functions.figures import show_cashier
import random
import time

def sell_game(shopper):
    break_out_of_sell_game = False
    break_out_of_while = False
    print("\nApproaching register...\n\n")
    time.sleep(2)

    while True:
        if break_out_of_sell_game == True:
            break
        elif break_out_of_sell_game == False:
                show_cashier()
                game_name = input("Hi, what game were you looking to sell today? ")
                while True:
                    print("What's the rating of this game? ")
                    game_rating = input("Rated E, T, or M?> ")
                    if game_rating.upper() in Game.RATINGS:
                        game_rating = game_rating.upper()
                        break
                    else:
                        print(f"\n{game_rating} is not a vaild rating.")
                        print("Please enter a vaild game rating: E, T, M")
                print("\nWhat price did you pay for the game?")
                while True:
                    if break_out_of_while == True:
                        break
                    elif break_out_of_while == False:
                        game_price = input("Enter price: ")
                        try:
                            float(game_price)
                        except:
                            print(f"\n{game_price} is not a valid number. Please enter a valid number for the price.")
                            continue
                        if float(game_price) > 150:
                            print("\nSorry that game is too expensive for us.")
                            print("Are you willing to give us a lower original price?")
                            choice = input("[y/N]> ").lower()
                            if choice == "y":
                                print("\nGreat! Please enter a lower price.")
                            elif choice == "n":
                                print("\nOkay, no worries, come back and sell to us again soon!") 
                                break_out_of_sell_game = True
                                break_out_of_while = True
                                break
                            else:
                                print(f"{choice} is an invalid option. Please enter y for yes or N for no.")
                        else:
                            break

                if break_out_of_sell_game == True:
                    break
                else:
                    game_name = game_name.lower().title()
                    our_same_game = Game.find_by_name(game_name)
                    if our_same_game:
                        our_same_game = our_same_game[0]
                        new_Game = Game.create(game_name,float(game_price),our_same_game.rating,shopper.id)
                    else:
                        new_Game = Game.create(game_name,float(game_price),game_rating,shopper.id)
                    offer_price = our_same_game.price * .6 if our_same_game else float(game_price) * .6
                    offer_price = round(offer_price, 0)
                    print(f"\nOk, based on the information we have on this game we're willing to give you... ${offer_price}0 for the game.")
                    print("Are you okay with selling your game for this price? ")
                    choice = input("[y/N]> ").lower()
                    while True:
                        if choice == "y":
                            store_price = our_same_game.price if our_same_game else round(offer_price * 1.75, 0)
                            
                            Game.update_price_and_owner(new_Game.id, store_price)
                            print("\nThank you for the sale!")
                            print("Pleasure doing business with you....we appreciate your money!")
                            time.sleep(2)
                            break_out_of_sell_game = True
                            break                        
                        elif choice == "n":
                            print("\nHmmm..... okay then....")
                            count = 0
                            max_count = random.randint(1,3)
                            cur_haggle_price = offer_price
                            while count < max_count:
                                cur_haggle_price *= 1.2
                                print(f"\nAre you willing to sell for ${round(cur_haggle_price,0)}0?")
                                choice = input("[y/N]> ").lower()
                                
                                if choice == "y":
                                    store_price = our_same_game.price if our_same_game else round(cur_haggle_price * 1.75, 0)

                                    Game.update_price_and_owner(new_Game.id, store_price)
                                    print("\nThank you for the sale!")
                                    print("Pleasure doing business with you....we appreciate your money!")
                                    time.sleep(2)
                                    break_out_of_sell_game = True
                                    break
                                elif choice == "n":
                                    print("\nHmmm..... okay then....")
                                    count +=1
                                else:
                                    print(f"{choice} is an invalid option. Please enter y for yes or N for no.")
                            
                            if break_out_of_sell_game == True:
                                break
                            else:
                                print("\nWell that was our best offer, better luck next time!")
                                time.sleep(2)
                                Game.remove_game_from_db(new_Game.id)
                                break_out_of_sell_game = True
                                break
                        else:
                            print(f"{choice} is an invalid option. Please try again.")
                            break
