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
        if isinstance(user_name, str) and len(user_name) > 3:
            self._user_name = user_name
        else:
            print("Please try entering username again: Must be a string and greater than 3 characters long")



class Game:
    all = []
    RATINGS = ["E", "T", "M"]

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
        Game.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(str) >= 1:
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



class Console:
    TYPES = ["PlayStation", "Xbox", "Nintendo", "PC", "VR"]
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name in Console.TYPES:
            self._name = name
        else:
            print("Please try again")



class Sale:
    def __init__(self, sale_amount, console = None, game = None):
            self.sale_amount = sale_amount
            self.console = console
            self.game = game
    @property
    def sale_amount(self):
        return self._sale_amount
    @sale_amount.setter
    def sale_amount(self, sale_amount):
        if isinstance(sale_amount, (int,float)) and sale_amount > 0:
            self._sale_amount = sale_amount
        else:
            print("Please enter a valid sale amount")
    @property
    def console(self):
        return self._console
    @console.setter
    def console(self, console):
        if isinstance(console, Console):
            self._console = console
        else:
            print("Try again")
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            print("Try again")



    