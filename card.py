class Card:

    VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
              "Six": 6, "Seven": 7, "Eight": 8, "nine": 9, "Ten": 10,
              "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            if self.rank != other.rank or self.suit != other.suit:
                return False
            else:
                return True
        else:
            return False
        