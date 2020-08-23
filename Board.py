
from Card import Card
from Deck import Deck
from StockPile import StockPile
class Board:
    def __init__(self,stockPile1: StockPile,stockPile2: StockPile,spitPile1,spitPile2,spitStack1,spitStack2):
        self.stockPile1: StockPile= stockPile1
        self.stockPile2 : StockPile= stockPile2
        self.spitPile1 = spitPile1
        self.spitPile2 = spitPile2
        self.spitStack1 = spitStack1
        self.spitStack2 = spitStack2


    def setup(self):
        deck = Deck([]).createDeck().shuffleDeck()


        for i in range(5):
            for j in range(i):
                self.stockPile1.getPile(i).addCard(deck.pop())
        for i in range(5):
            for j in range(i):
                self.stockPile2.getPile(j).addCard(deck.pop())
        while(deck.size()>0):
            self.spitStack1.addCard(deck.pop())
            self.spitStack2.addCard(deck.pop())
        return Board(self.stockPile1,self.stockPile2,self.spitPile1,self.spitPile2,self.spitStack1,self.spitStack2)

    def move(self,stockPile,stockPileNum,spitPile):
        if(stockPile == 1 ):
            x = self.stockPile1
            t1 =x.getPile(stockPileNum)
            temp = t1.getCard()
            t1.removeCard()
            x.removePile(stockPileNum)
            x.addPile(t1)
            if(spitPile == 1):
                self.spitPile1.addCard(temp)

            if(spitPile ==2):
                self.spitPile2.addCard(temp)
            return Board(x,self.stockPile2,self.spitPile1,self.spitPile2,self.spitStack1,self.spitStack2)

        elif(stockPile == 2):
            x = self.stockPile2
            t1 =x.getPile(stockPileNum)
            temp = t1.getCard()
            t1.removeCard()
            x.removePile(stockPileNum)
            x.addPile(t1)
            if(spitPile == 1):
                self.spitPile1.addCard(temp)
            if(spitPile ==2):
                self.spitPile2.addCard(temp)
            return Board(self.stockPile1,x,self.spitPile1,self.spitPile2,self.spitStack1,self.spitStack2)
        return None


    def bored(self):
        p1 = self.spitStack1
        temp = self.spitStack1.getCard()
        s1 = self.spitPile1.addCard(temp)
        p1.removeCard()

        p2 = self.spitStack2
        temp = p1.getCard()
        s2 = self.spitPile2.addCard(temp)
        p2.removeCard()

        return Board(self.stockPile1,self.stockPile2,s1,s2,p1,p2)
