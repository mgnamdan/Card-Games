from random import shuffle
from card import Card

class Deck:

    ranks = ["Two", "Three", "Four", "Five",
             "Six", "Seven", "Eight", "Nine",
             "Ten", "Jack", "Queen", "King", "Ace"]
    
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]


    def __init__(self):
        self.drawPile = []
        self.discardPile = []
        self.outPile = []
        self.setupDrawPile()


    def setupDrawPile(self):
        for suit in self.suits:
            for rank in self.ranks:
                newCard = Card(rank, suit)
                self.drawPile.append(newCard)


    def deckShuffle(self):
        shuffle(self.drawPile)


    def drawCard(self):
        drawnCard = self.drawPile.pop(0)
        self.outPile.append(drawnCard)
        return drawnCard

    
    def __str__(self):
        return "\n".join(str(card) for card in self.drawPile)
    

    def __eq__(self, other):
        if isinstance(other, Deck):
            selfTotal = len(self.drawPile) + len(self.discardPile) + len(self.outPile)
            otherTotal = len(other.drawPile) + len(other.discardPile) + len(other.outPile)

            if selfTotal == otherTotal:
                return True
            else:
                return False
        else:
            return False
