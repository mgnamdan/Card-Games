class Card:

    def __init__(self, rank="Two", suit="Clubs"):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        if self.rank != other.rank or self.suit != other.suit:
            return False
        else:
            return True
        