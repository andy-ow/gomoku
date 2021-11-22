from abc import ABC, abstractmethod

from ai.GameState import GameState
from ai.Action import Action


class Agent(ABC):

    @abstractmethod
    def choose_action(self, game_state: GameState) -> Action:
        pass

    @abstractmethod
    def learn(self, game_states__actions: list[GameState, Action]):
        pass

