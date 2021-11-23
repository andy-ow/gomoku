from abc import ABC, abstractmethod

from ai.Types import Action, GameState


class Agent(ABC):

    @abstractmethod
    def choose_action(self, game_state: GameState) -> Action:
        pass

    @abstractmethod
    def learn(self, game_states__actions: list[(GameState, Action)]):
        pass
