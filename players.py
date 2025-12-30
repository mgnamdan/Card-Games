class Player:
    
    def __init__(self, name="Bob"):
        self.name = name
        self.hand = []
        self.bank = 0


    def __str__(self):
        return f"{self.name}"
    
    
    def __eq__(self, other):
        if isinstance(other, Player):
            if self.name != other.name:
                return False
            if len(self.hand) != len(other.hand):
                return False
            for idx in range(len(self.hand)):
                if self.hand[idx] != other.hand[idx]:
                    return False
            return True
        else:
            return False
    

    def draw(self, card):
        self.hand.append(card)


    def play_card(self, card_idx):
        return self.hand.pop(card_idx)
    

    def calc_hand_value(self):
        total = 0
        for card in self.hand:
            total = total + card.VALUES[card.rank]
        return total
    

    def show_hand(self):
        for idx in range(len(self.hand)):
            print(f"{idx + 1}. {self.hand[idx]}\n")



class HumBJPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name)


    def request_action(self):
        self.show_hand()
        action = input("Would you like to hit or stay? --> ").lower()
        return action



class CmpBJPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name)


    def request_action(self):
        if self.calc_hand_value() > 16:
            return "s"
        return "h"