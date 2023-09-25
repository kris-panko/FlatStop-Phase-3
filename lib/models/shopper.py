from models.__init__ import CURSOR, CONN

class Shopper:
    def __init__(self, user_name, age):
        self.user_name = user_name
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 12:
            self._age = age
        else:
            print("Sorry, age needs to be a valid number and greater than 12")
    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, user_name):
        if isinstance(user_name, str) and len(user_name) >= 3:
            self._user_name = user_name
        else:
            print("Please try entering username again: Must be a string and greater than 3 characters long")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shoppers (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            age INTEGER);
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS shoppers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, user_name, age):
        shopper = cls(user_name, age)
        shopper.save()
        return shopper
    
    def save(self):
        sql = """
            INSERT INTO shoppers (user_name, age)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.user_name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid