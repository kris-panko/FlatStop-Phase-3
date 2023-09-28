from models.__init__ import CURSOR, CONN

class Shopper:
    
<<<<<<< HEAD
    def __init__(shopper, user_name, password, age, id=None):
        shopper.user_name = user_name
        shopper.age = age
        shopper.id = id
        shopper.password = password
=======
    def __init__(self, user_name, password, age, member=0, id=None):
        self.user_name = user_name
        self.age = age
        self.id = id
        self.member = member
        self.password = password
>>>>>>> main
    @property
    def age(shopper):
        return shopper._age
    @age.setter
    def age(shopper, age):
        if isinstance(age, int) and age > 12:
            shopper._age = age
        else:
            print("Sorry, age needs to be a valid number and greater than 12")
    @property
    def user_name(shopper):
        return shopper._user_name
    @user_name.setter
    def user_name(shopper, user_name):
        if isinstance(user_name, str) and len(user_name) >= 3:
            shopper._user_name = user_name
        else:
            print("Please try entering username again: Must be a string and greater than 3 characters long")
    @property
    def password(shopper):
        return shopper._password
    @password.setter
    def password(shopper, password):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if isinstance(password, str) and len(password) >= 5 and True in [type(int(char)) == int for char in password if char in numbers]:
            shopper._password = password
        else:
            print("Invalid Entry, please try again. Passwords must be at least 5 characters long and contain at least 1 number. ")


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shoppers (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            password TEXT,
            age INTEGER,
            member INTEGER);
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
        sql = """
            INSERT INTO shoppers (user_name, password, age, member)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (shopper.user_name, shopper.password, shopper.age, shopper.member))
        CONN.commit()

        shopper.id = CURSOR.lastrowid
        return shopper
    
    @classmethod
    def db_to_object(cls, row):
        id, user_name, password, age, member = row
        return cls(user_name, password, age, member, id,)


    @classmethod 
    def get_all(cls):
        sql = "SELECT * FROM shoppers"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.db_to_object(row) for row in rows]

    @classmethod
    def find_by_username(cls, user_name):
        sql = """
            SELECT *
            FROM shoppers
            WHERE user_name IS ?
        """
        row = CURSOR.execute(sql, (user_name,)).fetchone()
        return cls.db_to_object(row) if row else None
    @classmethod
    def find_by_id(cls, user_id):
        sql = """
            SELECT *
            FROM shoppers
            WHERE id IS ?
        """
        row = CURSOR.execute(sql, (user_id,)).fetchone()
        return cls.db_to_object(row) if row else None
    
    @classmethod
    def does_username_exist(cls, user_name):
        user = cls.find_by_username(user_name)
        if user == None:
            return False
        else:
            return True
    @classmethod
    def delete_shopper_from_db(cls, shopper_id):
        sql = """
            DELETE FROM shoppers
            WHERE id = ?
        """
        CURSOR.execute(sql,(shopper_id,))
        CONN.commit()
    @classmethod
    def update_username(cls, shopper_id, username):
        sql = """
            UPDATE shoppers    
            SET user_name = ?
            WHERE id = ?
    """
        CURSOR.execute(sql, (username, shopper_id))
        CONN.commit()
    @classmethod
    def update_password(cls, shopper_id, password):
        sql = """
            UPDATE shoppers    
            SET password = ?
            WHERE id = ?
    """
        CURSOR.execute(sql, (password, shopper_id))
        CONN.commit()
    @classmethod
    def update_member_status(cls, shopper_id):
        sql = """
            UPDATE shoppers    
            SET member = ?
            WHERE id = ?
    """
        CURSOR.execute(sql, (1, shopper_id))
        CONN.commit()
    

            