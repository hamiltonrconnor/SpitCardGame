from StockPile import StockPile
class Event:
    def blank():
        pass


class Spit(Event):
    """Event that occurs if a player runs out of cards """
    def __init__(self,player):
        self.player = player

    def __str__(self):
        return self.__class__.__name__

    def getPlayer(self)-> int:
        return self.player

class Move(Event):
    """ Event that occurs if a player makes a move """
    def __init__(self,stockPile: StockPile,stockPileNum,spitPile):
        self.stockPile = stockPile
        self.stockPileNum = stockPile
        self.spitPile = spitPile
    def __str__(self):
        return self.__class__.__name__

    def getStockPile(self):
        return self.stockPile

    def getSpitPile(self):
        return self.spitPile

    def getStockPileNum(self):
        return self.stockPileNum


class Bored(Event):
    """ Event that occurs if both players cannot move """
    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__
