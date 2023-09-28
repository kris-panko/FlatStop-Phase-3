from models.game import Game
from helper_functions.figures import show_cashier
import random

def sell_game(shopper):
    break_out_of_sell_game = False
    break_out_of_while = False

    while True:
        if break_out_of_sell_game == True:
            break
        elif break_out_of_sell_game == False:
                show_cashier()
                game_name = input("Hi, what game were you looking to sell today? ")
                while True:
                    game_rating = input("What's the rating of this game? ")
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
                            print(f"\n{game_price} is not a vaild number. Please enter a vaild number for the price.")
                            continue
                        if float(game_price) > 150:
                            print("\nSorry that game is too expensive for us.")
                            print("Are you willing to give us a lower original price?")
                            choice = input("[y/N]> ")
                            if choice == "y":
                                print("\nGreat! Please enter a lower price.")
                            elif choice == "N":
                                print("\nOkay now worries, come back and sell to us again soon!") 
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
                    new_Game = Game.create(game_name,float(game_price),game_rating,shopper.id)

                    offer_price = float(game_price) * .6
                    print(f"\nOk, based off that information we're willing to give you... ${round(offer_price, 2)}0 for the game.")
                    print("Are you okay with selling your game for this price? ")
                    choice = input("[y/N]> ")
                    while True:
                        if choice == "y":
                            # float(offer_price)
                            store_price = round(offer_price * 1.75, 2)
                            Game.update_price_and_owner(new_Game.id, store_price)
                            print("\nThank you for the sale!")
                            print("Pleasure doing business with you....sucker")
                            break_out_of_sell_game = True
                            break                        
                        elif choice == "N":
                            print("\nHmmm..... okay then....")
                            count = 0
                            max_count = random.randint(1,3)
                            cur_haggle_price = offer_price
                            while count < max_count:
                                cur_haggle_price *= 1.2
                                print(f"\nAre you willing to sell for ${round(cur_haggle_price,2)}?")
                                choice = input("[y/N]> ")
                                
                                if choice == "y":
                                    store_price = round(offer_price * 1.75, 2)
                                    Game.update_price_and_owner(new_Game.id, store_price)
                                    print("\nThank you for the sale!")
                                    print("Pleasure doing business with you....sucker")
                                    break_out_of_sell_game = True
                                    break
                                elif choice == "N":
                                    print("\nHmmm..... okay then....")
                                    count +=1
                                else:
                                    print(f"{choice} is an invalid option. Please enter y for yes or N for no.")
                            
                            if break_out_of_sell_game == True:
                                break
                            else:
                                print("\nWell that was our best offer, better luck next time!")
                                Game.remove_game_from_db(new_Game.id)
                                break_out_of_sell_game = True
                                break
                        else:
                            print(f"{choice} is an invalid option. Please enter y for yes or N for no.")
