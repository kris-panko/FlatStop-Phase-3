from game import Game
from console import Console

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