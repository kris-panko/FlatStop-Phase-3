#!/usr/bin/env python3 

from models.shopper import Shopper

def fill_database():
    # May have to delete drop_table later if we want information in database to persist
    Shopper.drop_table()
    Shopper.create_table()

    Shopper.create("Sergio", "Password", 27)

fill_database()