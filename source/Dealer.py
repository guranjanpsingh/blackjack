class Dealer:
    """
    Dealer of the game
    """

    __hand = []

    def getVisibleCard(self):
        """
        :return: the top card of the dealer
        """
        return self.__hand[1]

    def __init__(self):
        """
        constructor
        """
        pass