from enum import Enum, auto


class State(Enum):
    PLAYING = auto()
    END = auto()

class Stone(Enum):
    X = 'X'
    O = 'O'

class Player(Enum):
    X = auto()
    O = auto()

    def stone(self):
        return Stone.X if self == Player.X else Stone.O

    def opponent(self):
        return Player.O if self == Player.X else Player.X
