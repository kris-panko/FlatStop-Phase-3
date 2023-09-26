from models.__init__ import CURSOR, CONN 

class Game:
    RATINGS = ["E", "T", "M"]
    def __init__(self, name, price, rating, id=None, game_owner_id=None):
        self.name = name
        self.price = price
        self.rating = rating
        self.id = id
        self.game_owner_id = game_owner_id
    def __repr__(self):
        return f"[{self.id}: {self.name}, price: ${self.price}, rating: {self.rating} ###### ]"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1:
            self._name = name
        else:
            print("Please input a valid game name")
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self._price = price
        else:
            print("Please enter a valid price for game")

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, str) and rating in Game.RATINGS:
            self._rating = rating
        else:
            print("Try again")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            rating TEXT,
            game_owner_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS games;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, price, rating, game_owner_id=None):
        game = cls(name.title(), price, rating, None, game_owner_id)
        sql = """
            INSERT INTO games (name, price, rating, game_owner_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (game.name, game.price, game.rating, game.game_owner_id))
        CONN.commit()

        game.id = CURSOR.lastrowid
        return game
    
    @classmethod
    def db_to_object(cls, row):
        id, name, price, rating, game_owner_id = row
        return cls(name, price, rating, id, game_owner_id)

    @classmethod
    def find_by_name(cls, name, game_owner_id=1):
        sql = """
            SELECT *
            FROM games
            WHERE name IS ? AND game_owner_id IS ?
        """
        rows = CURSOR.execute(sql, (name, game_owner_id)).fetchall()
        return [cls.db_to_object(row) for row in rows] 
    
    @classmethod
    def get_all(cls, game_owner_id=1):
        sql = """
            SELECT *
            FROM games
            WHERE game_owner_id IS ?
        """
        rows = CURSOR.execute(sql, (game_owner_id,)).fetchall()
        return [cls.db_to_object(row) for row in rows]
    
    @classmethod
    def find_by_rating(cls, rating, game_owner_id=1):
        sql = """
            SELECT *
            FROM games
            WHERE rating IS ? AND game_owner_id IS ?
        """
        rows = CURSOR.execute(sql, (rating, game_owner_id)).fetchall()
        return [cls.db_to_object(row) for row in rows]
    
    @classmethod
    def remove_game_from_db(cls, game_id):
        sql = """
            DELETE FROM games WHERE id = ?
        """
        CURSOR.execute(sql, (game_id,))
        CONN.commit()
    @classmethod
    def update_price_and_owner(cls, game_id, store_price):
        sql = """
            UPDATE games
            SET game_owner_id = 1,
            price = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (store_price, game_id))
        CONN.commit()
    @classmethod
    def get_games_by_lowest_price(cls, game_owner_id=1):
        sql = """
            SELECT * FROM games
            ORDER by price ASC        
        """
        rows = CURSOR.execute(sql)
        return [cls.db_to_object(row) for row in rows]
    
