#!/usr/bin/env python3 

from models.shopper import Shopper
from models.game import Game

def fill_database():
    # May have to delete drop_table later if we want information in database to persist
    Shopper.drop_table()
    Shopper.create_table()
    Game.drop_table()
    Game.create_table()

    Shopper.create("Store", "password1", 27)
    Game.create("Call of Duty", 30.00, "M")
    Game.create("Zelda", 60.00, "T")
    Game.create("Halo", 70.00, "M")
    Game.create("Gears of War", 85.00, "M")

fill_database()