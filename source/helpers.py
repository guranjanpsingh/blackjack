from Card import Card
from Suit import Suit

def translateCardFromNumber(number):
    cardNumber = (number % 13) + 1
    suit = None
    if 0 < number <= 13:
        suit = Suit.Hearts
    elif 13 < number <= 26:
        suit = Suit.Diamonds
    elif 26 < number <= 39:
        suit = Suit.Clubs
    else:
        suit = Suit.Spades

    return Card(suit, cardNumber)


def translateNumberFromCard(card):
    number = 0
    suit = card.suit
    if suit == Suit.Hearts:
        number = number * 1
    elif suit == Suit.Diamonds:
        number = number * 2
    elif suit == Suit.Clubs:
        number = number * 3
    else:
        number = number * 4

    number = number + card.value
    return number

def handSum(hand):
    sum = 0
    for card in hand:
        sum += min(10, card.value)
    return sum

def isBlackJack(hand):
    sum = handSum(hand)
    if sum == 11:
        print(sum)
        for card in hand:
            if card.value == 1:
                return True

    return False

