import random
from Card import Card
import helpers

class CardBank:
    """
    Defines a card bank containing of single or multiple decks
    """

    cards = []
    currentCardLocation = 0
    redCardLocation = None
    __numberOfDecks = 6

    def shuffle(self):
        """
        initialize the card bank by shuffling the cards
        """

        cards = [(x + 1) % 52 for x in range(1, self.__numberOfDecks * 52 + 1)]
        random.shuffle(cards)
        for i in cards:
            card = helpers.translateCardFromNumber(i)
            self.cards.append(card)


    def nextCard(self):
        """
        deal the next card
        :return: Card
        """
        card = self.cards[self.currentCardLocation]
        self.currentCardLocation += 1
        return card

    def cardsAvailable(self):
        return self.redCardLocation > self.currentCardLocation

    def __init__(self, numberOfDecks):
        """
        Constructor
        """

        self.__numberOfDecks = numberOfDecks
        self.redCardLocation = ((numberOfDecks * 52) + 1) - random.randint(20, 30)
        self.shuffle()

