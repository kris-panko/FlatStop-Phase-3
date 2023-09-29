#!/usr/bin/env python3 

from models.shopper import Shopper
from models.game import Game

def fill_database():
    Shopper.drop_table()
    Shopper.create_table()
    Game.drop_table()
    Game.create_table()

    store = Shopper.create("Manager", "password1", 55)
    Shopper.create("Sergio", "password1", 27)
    Shopper.create("Kim", "password1", 29)
    Shopper.create("Charlotte", "password1", 33)
    Shopper.create("Kris", "password1", 33)
    Game.create("Call of Duty", 30.00, "M", store.id)
    Game.create("Zelda", 60.00, "T", store.id)
    Game.create("Zelda", 60.00, "T", store.id)
    Game.create("Halo", 70.00, "M", store.id)
    Game.create("Gears of War", 85.00, "M", store.id)
    Game.create("Call of Duty", 30.00, "M", store.id)
    Game.create("Zelda", 60.00, "T", store.id)
    Game.create("Zelda", 60.00, "T", store.id)
    Game.create("Halo", 70.00, "M", store.id)
    Game.create("Gears of War", 85.00, "M", store.id)
    Game.create("Animal Crossing", 59.00, "E", store.id)
    Game.create("The Sims4", 39.99, "E", store.id)
    Game.create("Mario Kart", 59.99, "E", store.id)
    Game.create("Overwatch 2", 59.99, "T", store.id)

fill_database()