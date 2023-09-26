from models.__init__ import CURSOR, CONN 

class Game:
    all = {}
    RATINGS = ["E", "T", "M"]

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
        # Game.all.append(self)
    def __repr__(self):
        return f"<{self.name}, price: {self.price}, rating: {self.rating}>"
    
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
    def create(cls, name, price, rating):
        game = cls(name, price, rating)
        game.save()
        return game
    
    def save(self):
        sql = """
            INSERT INTO games (name, price, rating, game_owner_id)
            VALUES (?, ?, ?, ?)
        """
        manager_id = 1
        game_owner_id = manager_id
        CURSOR.execute(sql, (self.name, self.price, self.rating, game_owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    @classmethod
    def instance_from_db(cls, row):
        game = cls.all.get(row[0])
        if game:
            game.name = row[1]
            game.price = row[2]
            game.rating = row[3]
        else:
            game = cls(row[1], row[2], row[3])
            game.id = row[0]
            game.all[game.id] = game
        return game
        
    @classmethod
    def get_available_game(cls, name, id=1):
        sql = """
            SELECT *
            FROM games
            WHERE name IS ? AND game_owner_id IS ?
        """
        row = CURSOR.execute(sql, (name, id)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all_available_games(cls, id=1):
        sql = """
            SELECT *
            FROM games
            WHERE game_owner_id IS ?
        """
        rows = CURSOR.execute(sql, (id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]