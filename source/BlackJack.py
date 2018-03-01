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
    roundsPlayed = 0
    def deal(self):
        """
        Deal a card
        """

        pass

    def play(self):
        """
        single round of the game
        """
        helpers.disabledPrint()
        while self.cardBank.cardsAvailable():
            self.roundsPlayed += 1
            print("Round " + str(round))
            self.__InitialDeal()
            print("")
            helpers.disabledPrint()
            helpers.enablePrint()
            self.__payoutSideBet()
            helpers.disabledPrint()
            self.__IntermediateCheck()
            print("")
            self.__ContinuePlay()
            print("")
            self.__cleanUp()
            print("")
            print("")




    def __init__(self, players, deckCount):
        """
        constructor
        :param playerCount: number of players in the game
        :param deckCount: number of decks to use
        """
        self.players = players
        self.cardBank = CardBank.CardBank(deckCount)


    def __InitialDeal(self):
        """
        Deal the first round of cards to all players and the Dealer
        :return:
        """

        for player in self.players:
            if player.balance > 0:
                card = self.cardBank.nextCard()
                player.hands[0].append(card)
                print("Player " + str(player.id) + " got " + str(card))

        dealer_card = self.cardBank.nextCard()
        self.dealer.hand.append(dealer_card)
        for player in self.players:
            if player.balance > 0:
                card = self.cardBank.nextCard()
                player.hands[0].append(card)
                print("Player " + str(player.id) + " got " + str(card))

        dealer_card = self.cardBank.nextCard()
        self.dealer.hand.append(dealer_card)
        print("Dealer top card " + str(dealer_card))

    def __IntermediateCheck(self):
        """
        Check for payouts, blackjacks etc before continuing the play
        :return:
        """
        #TODO: payout the side bet of lucky lucky
        #self.__payoutSideBet()

        # payout black jacks
        for player in self.players:
            if player.balance > 0:
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
            if player.balance > 0:
                for hand in player.hands:
                    doubled = False
                    print("Dealer top card: " + str(self.dealer.getVisibleCard()))
                    while True and not helpers.isBlackJack(hand):
                        decision = player.decide(self.dealer.hand[1], hand) # 1 is the top card of dealer
                        print("Player " + str(player.id) + " hand total: " + str(helpers.handSum(hand)))

                        print("Player " + str(player.id) + " decided to " + str(decision))

                        if not self.validDecision(player, decision):
                            print("Not a valid choice.")
                            continue
                        if decision == decision.Stand:
                            break
                        elif decision == decision.Hit:
                            card = self.cardBank.nextCard()
                            print("Player " + str(player.id) + " got " + str(card))
                            hand.append(card)
                            if helpers.handSum(hand) > 21:
                                print("Player " + str(player.id) + " busyed with hand total: " + str(helpers.handSum(hand)))
                                player.balance -= player.bet
                                print(player.balance)
                                player.resetHand()
                            continue
                        elif decision == decision.Double:
                            card = self.cardBank.nextCard()
                            print("Player " + str(player.id) + " got " + str(decision))
                            hand.append(card)
                            break  # only one card given for double
                        else:
                            helpers.printHand(hand)
                            print("Dealer card: " + str(self.dealer.hand[1]))
                            print("Player decided to: " + str(decision))
                            print("")
                            player.splitHands()
                            hand = player.hands[0]
        #handle dealer hits
        while helpers.handSum(self.dealer.hand) < 17:
            card = self.cardBank.nextCard()
            print("Dealer got " + str(card))
            self.dealer.hand.append(card)

        for player in self.players:
            if player.balance > 0:
                for hand in player.hands:
                    if len(hand) == 0:
                        print(hand)
                        continue
                    print("Player hand: ")
                    print(helpers.printHand(hand))
                    print("Dealer hand: ")
                    print(helpers.printHand(self.dealer.hand))
                    if helpers.handSum(self.dealer.hand) > 21:
                        player.winCount += 1
                        print("Player 1 won")
                        print(player.balance)
                        player.balance += player.bet
                        print(player.balance)
                        print("")
                        break
                    if len(hand) != 0:
                        if helpers.handSum(hand) > helpers.handSum(self.dealer.hand):
                            player.winCount += 1
                            print(helpers.handSum(hand))
                            print(helpers.handSum(self.dealer.hand))
                            print("Player 1 won")
                            print(player.balance)
                            player.balance += player.bet
                            print(player.balance)
                            print("")
                            break
                        else:
                            print("Player 1 lost")
                            print(player.balance)
                            player.balance -= player.bet
                            print(player.balance)
                            print("")
                            break


    def __cleanUp(self):
        """
        Clean up the board after each play
        :return:
        """

        for player in self.players:
            if player.balance > 0:
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
        dealer_card = self.dealer.getVisibleCard()
        for player in self.players:
            if player.balance > 0:
                player_first_card = player.hands[0][0]
                player_second_card = player.hands[0][1]
                suited = False
                if player_first_card.suit == player_second_card.suit == dealer_card.suit:
                    suited = True

                if player_first_card.value == player_second_card.value == dealer_card.value == 7:
                    if suited:
                        player.sideBetWinCount += 1
                        print("Player " + str(player.id) + " got a suited 777")
                        player.balance += player.sideBet * 200
                    else:
                        player.sideBetWinCount += 1
                        print("Player " + str(player.id) + " got an unsuited 777")
                        player.balance += player.sideBet * 50

                elif player_first_card in [6, 7, 8] and player_second_card in [6, 7, 8] and dealer_card in [6, 7, 8] \
                        and (player_first_card.value + player_second_card.value + dealer_card.value) == 21:
                    if suited:
                        player.sideBetWinCount += 1
                        print("Player " + str(player.id) + " got a suited 678")
                        player.balance += player.sideBet * 100
                    else:
                        player.sideBetWinCount += 1
                        print("Player " + str(player.id) + " got an unsuited 678")
                        player.balance += player.sideBet * 30
                elif (player_first_card.value + player_second_card.value + dealer_card.value) == 21:
                    if suited:
                        player.sideBetWinCount += 1
                        print("Player " + str(player.id) + " got a suited 21")
                        player.balance += player.sideBet * 15
                    else:
                        player.sideBetWinCount += 1
                        print("Player " + str(player.id) + " got an unsuited 21")
                        player.balance += player.sideBet * 3
                elif (player_first_card.value + player_second_card.value + dealer_card.value) in [19, 20]:
                    player.sideBetWinCount += 1
                    print("Player got crap")
                    player.balance += player.sideBet * 2

    def validDecision(self, player, decision):
        """
        Make sure the player can make they decision
        :param player:
        :param decision:
        :return:
        """

        return True


