class Dealer:
    """
    Dealer of the game
    """

    hand = []

    def getVisibleCard(self):
        """
        :return: the top card of the dealer
        """
        return self.hand[1]


    def __init__(self):
        """
        constructor
        """
        pass