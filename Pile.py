
class Pile:

    def __init__(self,pile):
        self.pile = pile

    def addCard(self,card) :
        temp = []
        temp.extend(self.pile)
        temp.append(card)

        return Pile(temp)

    def removeCard(self):
        if(len(self.pile) == 0 ):return None
        pile = self.pile.pop()
        return Pile(pile)

    def getCard(self) :
        if(len(self.pile) == 0 ):return None
        temp = []
        temp.extend(self.pile)
        return temp[len(temp)-1]

    def getSize(self):
        return size(self.pile)

    def getPile(self):
        return self.pile
