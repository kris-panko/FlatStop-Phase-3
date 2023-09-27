from models.__init__ import CURSOR, CONN 

class Game:
    # all = {}
    RATINGS = ["E", "T", "M"]
    #adds owner_id here
    def __init__(self, name, price, rating, id=None, game_owner_id=None):
        self.name = name
        self.price = price
        self.rating = rating
        self.id = id
        self.game_owner_id = game_owner_id
        # Game.all.append(self)
    def __repr__(self):
        return f"<{self.id}: {self.name}, price: {self.price}, rating: {self.rating}>"
    
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
        game = cls(name, price, rating, None, game_owner_id)
        # game.save()
        #passes owner_id into the create so we can easily create a game with a specified owner
        sql = """
            INSERT INTO games (name, price, rating, game_owner_id)
            VALUES (?, ?, ?, ?)
        """
        # manager_id = 1
        #game_owner_id = 1
        #got rid of these because passing them in at init
        CURSOR.execute(sql, (game.name, game.price, game.rating, game.game_owner_id))
        CONN.commit()

        game.id = CURSOR.lastrowid
        # type(game).all[game.id] = self no more all plz!
        return game
    
    # def save(self): (create now saves so we don't need this)
    #changing name to be more descriptive here:
    @classmethod
    def db_to_object(cls, row):
        id, name, price, rating, game_owner_id = row
        return cls(name, price, rating, id, game_owner_id)
        # game = cls.all.get(row[0])
        # if game:
        #     game.name = row[1]
        #     game.price = row[2]
        #     game.rating = row[3]
        # else:
        #     game = cls(row[1], row[2], row[3])
        #     game.id = row[0]
        #     Game.all[game.id] = game
        # return game

    #changing names to be more descriptive here and match shopper 
    # also changed in rest of codebase for consistency   
    @classmethod
    def find_by_name(cls, name, game_owner_id=1):
        sql = """
            SELECT *
            FROM games
            WHERE name IS ? AND game_owner_id IS ?
        """
        rows = CURSOR.execute(sql, (name, game_owner_id)).fetchall()
        # row = CURSOR.execute(sql, (name, id)).fetchall()
        return [cls.db_to_object(row) for row in rows] 
        # return cls.db_to_object(row) if row else None
    
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
#added list comp here to ensure consistency