class Player:
    """
    defines a player
    """

    hands = [[]]
    balance = 0
    id = 0
    bet = 10
    def decide(self, dealer_card):
        """
        decide from the playbook
        :param dealer_card: top card of the dealer
        """

        pass

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

    def __init__(self, balance, id):
        self.balance = balance
        self.id = id

    def __str__(self):
        handString = "Player " + str(self.id) + " has cards: \n"
        for hand in self.hands:
            for card in hand:
                handString += card.__str__() + " \n"
        return handString


