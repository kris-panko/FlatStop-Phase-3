from models.__init__ import CURSOR, CONN

class Shopper:
    all = {}
    def __init__(self, user_name, password, age, id=None):
        self.user_name = user_name
        self.age = age
        self.id = id
        self.password = password
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
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if isinstance(password, str) and len(password) >= 5 and True in [type(int(char)) == int for char in password if char in numbers]:
            self._password = password
        else:
            print("Invalid Entry, please try again. Passwords must be at least 5 characters long and contain at least 1 number. ")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shoppers (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            password TEXT,
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
    def create(cls, user_name, password, age):
        shopper = cls(user_name, password, age)
        shopper.save()
        return shopper
    
    def save(self):
        sql = """
            INSERT INTO shoppers (user_name, password, age)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.user_name, self.password, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    @classmethod
    def instance_from_db(cls, row):
        shopper = cls.all.get(row[0])
        if shopper:
            shopper.user_name = row[1]
            shopper.password = row[2]
            shopper.age = row[3]
        else:
            shopper = cls(row[1], row[2], row[3])
            shopper.id = row[0]
            cls.all[shopper.id] = shopper
        return shopper
        
    @classmethod
    def get_shopper_account(cls, user_name, password):
        sql = """
            SELECT *
            FROM shoppers
            WHERE user_name IS ? AND password IS ?
        """
        row = CURSOR.execute(sql, (user_name, password)).fetchone()
        return cls.instance_from_db(row) if row else None