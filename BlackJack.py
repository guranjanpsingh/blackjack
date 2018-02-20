from .Player import Player


class BlackJack:

    """
    Defines the black jack game
    """

    players = []
    cardBank = None

    def deal(self):
        """
        Deal a card
        """

        pass

    def play(self):
        """
        single round of the game
        """

        pass


    def __init__(self, playerCount, deckCount):
        """
        constructor
        :param playerCount: number of players in the game
        :param deckCount: number of decks to use
        """
        players = [Player] * playerCount


    def __InitialDeal(self):
        """
        Deal the first round of cards to all players and the Dealer
        :return:
        """
        pass

    def __IntermediateCheck(self):
        """
        Check for payouts, blackjacks etc before continuing the play
        :return:
        """
        pass

    def __ContinuePlay(self):
        """
        continute the play for all players until the end of round
        :return:
        """
        pass
