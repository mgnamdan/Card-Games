from deck import Deck


def main():
    testDeck = Deck()

    print("~~~~ Original Deck ~~~~")
    print(testDeck)
    print("")

    testDeck.deckShuffle()
    print("~~~~ Shuffled Deck ~~~~")
    print(testDeck)


if __name__ == "__main__":
    main()
