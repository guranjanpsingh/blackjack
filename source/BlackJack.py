import Player
import CardBank
import Dealer
import Suit
import Card
import helpers

class BlackJack:

    """
    Defines the black jack game
    """

    players = []
    cardBank = None
    dealer = Dealer.Dealer()

    def deal(self):
        """
        Deal a card
        """

        pass

    def play(self):
        """
        single round of the game
        """
        while self.cardBank.cardsAvailable():
            self.__InitialDeal()
            self.__IntermediateCheck()
            self.__ContinuePlay()
            self.__cleanUp()




    def __init__(self, playerCount, deckCount):
        """
        constructor
        :param playerCount: number of players in the game
        :param deckCount: number of decks to use
        """
        for i in range(playerCount):
            player = Player.Player(100, i + 1)
            self.players.append(player)
        self.cardBank = CardBank.CardBank(deckCount)


    def __InitialDeal(self):
        """
        Deal the first round of cards to all players and the Dealer
        :return:
        """

        for player in self.players:
            card = self.cardBank.nextCard()
            player.hands[0].append(card)

        dealerCard = self.cardBank.nextCard()
        self.dealer.hand.append(dealerCard)
        for player in self.players:
            card = self.cardBank.nextCard()
            player.hands[0].append(card)

    def __IntermediateCheck(self):
        """
        Check for payouts, blackjacks etc before continuing the play
        :return:
        """
        for player in self.players:
            hand = player.hands[0]
            if helpers.isBlackJack(hand):
                player.balance += player.bet * 1.5



    def __ContinuePlay(self):
        """
        continute the play for all players until the end of round
        :return:
        """
        pass


    def __cleanUp(self):
        """
        Clean up the board after each play
        :return:
        """

        for player in self.players:
            player.resetHand()

