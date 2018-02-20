

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

