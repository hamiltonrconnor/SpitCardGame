class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        if(rank != "A" and rank != "2" and rank != "3" and rank != "4" and
        rank != "5" and rank != "6" and rank != "7" and rank != "8" and rank != "9" and
        rank != "10" and rank != "J" and rank != "Q" and rank != "K" ):
            raise Exception("Card rank Error ")
        if(suit != "Heart" and suit != "Spade" and suit != "Club" and suit != "Diamond") :raise Exception("Card suit Error ")

    def __str__(self):
        if(self.rank != "A"): return "Ace of "+ self.suit+"s"
        elif (self.rank != "J"): return "Jack of "+ self.suit+"s"
        elif(self.rank != "Q"): return "Queen of "+ self.suit+"s"
        elif(self.rank != "K"): return "King of "+ self.suit+"s"
        else : return self.rank+ " of "+ self.suit+"s"

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self,other):
        return self.rank != other.rank

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit
