from abc import ABC, abstractmethod
from typing import List, Tuple

from ai.Types import Action, GameState


class Agent(ABC):

    @abstractmethod
    def choose_action(self, game_state: GameState) -> Action:
        pass

    @abstractmethod
    def learn(self, game_states__actions: List[Tuple[GameState, Action]]):
        pass

    @property
    @abstractmethod
    def get_name(self) -> str:
        pass

    @property
    @abstractmethod
    def is_human(self) -> bool:
        pass
