from random import randint
from deck import Deck
from players import HumBJPlayer, CmpBJPlayer


class BJM:

    COMPNAMES = ["Angela", "Chelsea", "Daryl", "Elizabeth", "Fred", "Gabby",
                 "Harold", "Ike", "Julie", "Katie", "Lindsey", "Mike",
                 "Nancy", "Oliver", "Pat", "Richard", "Samantha", "Terrence",
                 "Ursula", "Vic", "Wendy", "Xavier", "Yasmeen", "Zach"]

    def __init__(self):
        self.deck = Deck()
        self.dealer = CmpBJPlayer(name="Bob")
        self.players = []
        self.scores = {}
        self.winners = []


    def starter_deal(self):
        for _ in range(2):
            for player in self.players:
                player.draw(self.deck.drawCard())
            self.dealer.draw(self.deck.drawCard())


    def manage_turn(self, player):
        play = True
        while play:
            if player.calc_hand_value() > 21:
                player.show_hand()
                print(f"{player.name} busts!\n")
                play = False
            elif len(player.hand) > 5:
                play = False
            else:
                choice = player.request_action()
                if choice == "hit" or choice == "h":
                    player.draw(self.deck.drawCard())
                else:
                    play = False
        self.calculate_score(player)


    def calculate_score(self, player):
        self.scores[player.name] = player.calc_hand_value()


    def prompt_nxt_game(self):
        choice = input("Would you like to play another game? (y/n) --> ").lower()
        if choice == 'y':
            return True
        return False


    def play_game(self):
        gameOn = True
        while gameOn:
            print("Welcome to Blackjack!")
            hum_name = input("What is your name or nickname? --> ")
            self.players.append(HumBJPlayer(hum_name))

            opps = int(input("How many computers would you like to play against? --> "))
            for _ in range(opps):
                new_player = CmpBJPlayer(name=self.COMPNAMES[randint(0, len(self.COMPNAMES) - 1)])
                self.players.append(new_player)

            for _ in range(3, 7):
                self.deck.deckShuffle()

            self.starter_deal()

            for player in self.players:
                self.manage_turn(player)
            self.manage_turn(self.dealer)

            if self.scores["Bob"] == 21:
                print("The dealer wins! Better luck next time!")
            else:
                high_score = -1
                for player in self.scores:
                    # This needs to be fixed, adds any player to winners as long as they have higher score than last checked
                    if self.scores[player] >= high_score and self.scores[player] < 22:
                        high_score = self.scores[player]
                        self.winners.append(player)

                if len(self.winners) == 0:
                    print("Everyone busted! Nobody wins!")
                elif len(self.winners) > 1:
                    winners = " ".join([str(player) for player in self.winners])
                    print(f"{winners} win!")
                else:
                    print(f"{self.winners[0]} wins!")

            gameOn = self.prompt_nxt_game()
        return False
