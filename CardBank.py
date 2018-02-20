class CardBank:
    """
    Defines a card bank containing of single or multiple decks
    """

    cards = []
    currentCardLocation = 0
    redCardLocation = None

    def shuffle(self):
        """
        initialize the card bank by shuffling the cards
        """
        pass

    def nextCard(self):
        """
        deal the next card
        :return: Card
        """
        pass

    def __init__(self):
        """
        Constructor
        """
