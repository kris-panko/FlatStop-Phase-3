#!/usr/bin/env python3 

from models.shopper import Shopper
from models.game import Game

def fill_database():
    # May have to delete drop_table later if we want information in database to persist
    Shopper.drop_table()
    Shopper.create_table()
    Game.drop_table()
    Game.create_table()


    Shopper.create("Sergio", "password1", 27,)
    Game.create("Call of Duty", 20.00, "M")
    Game.create("Call of Duty", 20.00, "M")
    Game.create("Call of Duty", 20.00, "M")
    Game.create("Call of Duty", 20.00, "M")
    Game.create("Call of Duty", 20.00, "M")
    Game.create("Elden Ring", 60.00, "M")
    Game.create("Elden Ring", 60.00, "M")
    Game.create("Ratchet and Clank", 30.00, "T")

fill_database()