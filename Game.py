from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from Agent import Agent
from ai.Types import Action, GameState


class Game(ABC):

    @abstractmethod
    def __init__(self, players: List[Agent], config):
        raise TypeError("TypeError: This is an Abstract Class and it cannot be instantiated")

    @abstractmethod
    def get_current_gamestate(self) -> GameState:
        pass

    @abstractmethod
    def make_move(self, action: Action):
        pass

    @abstractmethod
    def is_playing(self) -> bool:
        pass

    @abstractmethod
    def get_current_player(self) -> Agent:
        pass

    @abstractmethod
    def get_winner(self) -> Optional[Agent]:
        pass

    @abstractmethod
    def get_history_of_winning_moves(self) -> List[Tuple[GameState, Action]]:
        pass

    @abstractmethod
    def print_game(self):
        pass

