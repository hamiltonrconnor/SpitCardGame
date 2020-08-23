import random
from Card import Card
class Deck:

    def __init__(self,deck) :
        self.deck =deck

    def __eq__(self,other):
        if(len(self.deck)!=len(other.deck)):return False
        for i in range(len(self.deck)):
            if(self.deck[i] != other.deck[i]): return False


    def createDeck(self):
        ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        suits = ["Heart","Spade","Club","Diamond"]
        deck = []
        for rank in ranks:
            for suit in suits:
                deck.append(Card(rank,suit))
        return Deck(deck)

    def shuffleDeck(self):
        temp = self.deck
        random.shuffle(temp)
        
        return Deck(temp)

    def pop(self):
        return self.deck.pop()

    def size(self):
        return len(self.deck)

    def getDeck(self):
        return self.deck
