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