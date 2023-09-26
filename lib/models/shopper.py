from models.__init__ import CURSOR, CONN

class Shopper:
   #got rid of the all set because single source of truth could be database
    
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
        if (isinstance(password, str) and len(password) >= 8):
            self._password = password

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

#consolidates shopper and save actions, since they were doing the same thing,so create:
#instantiates, adds to database, and then returns it
#no all necessary becasue database is SSoT
    @classmethod
    def create(cls, user_name, password, age):
        #creates the table the first time, then won't do anything else once created
        cls.create_table()
        shopper = cls(user_name, password, age)
        sql = """
            INSERT INTO shoppers (user_name, password, age)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (shopper.user_name, shopper.password, shopper.age))
        CONN.commit()

        shopper.id = CURSOR.lastrowid
        cls.current_user = shopper 
        #adds a current_user so we can refer back to it later for efficiency
        return shopper
    
    #this uses a second source of truth, so we should streamline to use DB
    #renamed for greater clarity about what it's doing
    @classmethod
    def db_to_object(cls, row):
        #destructured tuple-rows into variables
        #id, user_name, age
        #for this row, make a shopper out of it
        id, user_name, password, age = row
        return cls(user_name, password, age, id)

        # shopper = cls.all.get(row[0])
        # if shopper:
        #     shopper.name = row[1]
        #     shopper.age = row[2]
        # else:
        #     shopper = cls(row[1], row[2])
        #     shopper.id = row[0]
        #     cls.all[shopper.id] = shopper
        # return shopper


    @classmethod 
    def get_all(cls):
        sql = "SELECT * FROM shoppers"
        rows = CURSOR.execute(sql).fetchall()
        #call a list comp on each row to convert it into an object
        return [cls.db_to_object(row) for row in rows]

    #changed name for clarity
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
    def does_username_exist(cls, user_name):
        sql = """
            SELECT * 
            FROM shoppers
            WHERE user_name = ?
        """
        row = CURSOR.execute(sql, (user_name,)).fetchone()

        if row == None:
            return False
        else:
            return True