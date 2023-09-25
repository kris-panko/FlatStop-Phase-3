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