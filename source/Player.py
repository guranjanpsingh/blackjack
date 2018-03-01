import helpers
from decision import Decision

class Player:
    """
    defines a player
    """

    hands = [[]]
    balance = 0
    id = 0
    bet = 10
    sideBet = 5
    winCount = 0
    sideBetWinCount = 0

    def decide(self, dealer_card, hand):
        """
        decide from the playbook
        :param dealer_card: top card of the dealer
        """
        hand_total = helpers.handSum(hand)
        is_soft = helpers.hand_contains_ace(hand)
        dealer_card_number = min(dealer_card.value, 10)
        if len(hand) == 1:
            return Decision.Hit
        if (hand[0].value == 1 and hand[1].value == 1 and len(hand) == 2) or (hand[0].value == 8 and hand[1].value == 8 and len(hand) == 2):
            return Decision.Split
        if hand[0].value > 9 and hand[1].value > 9 and len(hand) == 2:
            return Decision.Stand
        if hand[0].value == hand[1].value == 9 and len(hand) == 2:
            if dealer_card_number in [2, 3, 4, 5, 6, 7, 9]:
                return Decision.Split
            else:
                return Decision.Stand

        if hand[0].value == hand[1].value == 7 and len(hand) == 2:
            if dealer_card_number in [2, 3, 4, 5, 6, 7]:
                return Decision.Split
            else:
                return Decision.Stand

        if hand[0].value == hand[1].value == 6 and len(hand) == 2:
            if dealer_card_number in [2, 3, 4, 5, 6]:
                return Decision.Split
            else:
                return Decision.Hit
        if hand[0].value == hand[1].value == 5 and len(hand) == 2:
            if dealer_card_number in [2, 3, 4, 5, 6, 7, 8, 9]:
                return Decision.Double
            else:
                return Decision.Hit
        if hand[0].value == hand[1].value == 4 and len(hand) == 2:
            if dealer_card_number in [5, 6]:
                return Decision.Split
            else:
                return Decision.Hit
        if hand[0].value == hand[1].value == 3 and len(hand) == 2:
            if dealer_card_number > 7:
                return Decision.Hit
            else:
                return Decision.Split
        if hand[0].value == hand[1].value == 2 and len(hand) == 2:
            if dealer_card_number > 7:
                return Decision.Hit
            else:
                return Decision.Split
        return self.__decisionHelper(hand_total, dealer_card, is_soft)



    def resetHand(self):
        """
        Reset hands
        :return:
        """
        self.hands = [[]]

    def printHand(self, index):
        hand = self.hands[index]
        for card in hand:
            print(card)

    def splitHands(self):
        cards = self.hands[0]
        print(cards)
        self.hands[0] = [cards[0]]
        self.hands.append([cards[1]])

    def __decisionHelper(self, player_total, dealer_card, is_soft):

        if not is_soft:
            if player_total > 16:
                return Decision.Stand
            else:
                return Decision.Hit
            if  12 < player_total < 17 and 2 <= dealer_card <= 6:
                return Decision.Stand
            if 12 < player_total < 17 and dealer_card > 6:
                return Decision.Hit
            if player_total == 12:
                if dealer_card in [2, 3, 7, 8, 9, 1]:
                    return Decision.Hit
                else:
                    return Decision.Stand
            if player_total == 11:
                if dealer_card != 1:
                    return Decision.Double
                else:
                    return Decision.Hit
            if player_total == 10:
                if dealer_card not in [1, 10]:
                    return Decision.Double
                else:
                    return Decision.Hit
            if player_total == 9:
                if dealer_card in [3, 4, 5, 6]:
                    return Decision.Double
                else:
                    return Decision.Hit
            return Decision.Hit
        else:
            if player_total > 8:
                return Decision.Stand
            if player_total == 8:
                if dealer_card in [1, 9, 10]:
                    return Decision.Hit
                elif dealer_card in [3, 4, 5, 6]:
                    return Decision.Double
                else:
                    return Decision.Stand
            if player_total == 7:
                if dealer_card in [1, 2, 7, 8, 9, 10]:
                    return Decision.Hit
                else:
                    return Decision.Double
            if player_total in [5, 6]:
                if dealer_card in [4, 5, 6]:
                    return Decision.Double
                else:
                    return Decision.Hit
            if player_total in [2, 3]:
                if dealer_card in [5, 6]:
                    return Decision.Double
                else:
                    return Decision.Hit
            return Decision.Stand






    def __init__(self, balance, id):
        self.balance = balance
        self.id = id

    def __str__(self):
        handString = "Player " + str(self.id) + " has cards: \n"
        for hand in self.hands:
            for card in hand:
                handString += card.__str__() + " \n"
        return handString
