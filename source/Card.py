

class Card:
    """
    Define the card location
    """
    suit = None
    value = None

    def __init__(self, suit, value):
        """
        Constructor
        :param suit: suit of the card
        :param value: value of the card 1 - 13
        """
        self.suit = suit
        self.value = value


    def __str__(self):
        cardName = str(self.value)
        if cardName == "11":
            cardName = "Jack"
        elif cardName == "12":
            cardName = "Queen"
        elif cardName == "13":
            cardName = "King"
        return cardName + " of " + str(self.suit)
