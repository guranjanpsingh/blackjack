from enum import Enum

class Decision(Enum):
    Hit = 1
    Stand = 2
    Split = 3
    Double = 4

    def __str__(self):
        return self.name
