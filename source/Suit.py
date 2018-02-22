from enum import Enum

class Suit(Enum):
    Hearts = 1
    Diamonds = 2
    Clubs = 3
    Spades = 4

    def __str__(self):
        return self.name
