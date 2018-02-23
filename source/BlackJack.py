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

        self.dealer.hand.append(self.cardBank.nextCard())
        for player in self.players:
            card = self.cardBank.nextCard()
            player.hands[0].append(card)

        self.dealer.hand.append(self.cardBank.nextCard())

    def __IntermediateCheck(self):
        """
        Check for payouts, blackjacks etc before continuing the play
        :return:
        """
        #TODO: payout the side bet of lucky lucky
        self.__payoutSideBet()

        # payout black jacks
        for player in self.players:
            hand = player.hands[0]
            if helpers.isBlackJack(hand):
                player.balance += player.bet * 1.5
                print("Player " + str(player.id) + " got a black jack.")
                print("Balance: " + str(player.balance))





    def __ContinuePlay(self):
        """
        continute the play for all players until the end of round
        :return:
        """
        for player in self.players:
            for hand in player.hands:
                while True and not helpers.isBlackJack(hand):
                    decision = player.decide(self.dealer.hand[1], hand) # 1 is the top card of dealer
                    print("Player " + str(player.id))
                    helpers.printHand(hand)
                    print("Dealer card: " + str(self.dealer.hand[1]))
                    print("Player decided to: " + str(decision))
                    print("")
                    if not self.validDecision(player, decision):
                        print("Not a valid choice.")
                        continue
                    if decision == decision.Stand:
                        break
                    elif decision == decision.Hit:
                        hand.append(self.cardBank.nextCard())
                        break
                    elif decision == decision.Double:
                        hand.append(self.cardBank.nextCard())
                        break  # only one card given for double
                    else:
                        break


    def __cleanUp(self):
        """
        Clean up the board after each play
        :return:
        """

        for player in self.players:
            player.resetHand()
        self.dealer.hand = []


    def __payoutSideBet(self):
        """
        Pay out side bet of lucky lucky
        Using the players 2 cards and dealers top card
        Payouts:
        18 or less loss
        19, 20: 2 to 1
        21: 3 to 1
        21 (Suited): 15 to 1
        6,7,8: 30 to 1
        7,7,7: 50 to 1
        6,7,8 (Suited): 100 to 1
        7,7,7 (Suited): 200 to 1
        :return:
        """
        pass

    def validDecision(self, player, decision):
        """
        Make sure the player can make they decision
        :param player:
        :param decision:
        :return:
        """

        return True


