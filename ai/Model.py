from abc import ABC, abstractmethod

from ai.Types import Action


class Model(ABC):

    @abstractmethod
    def __init__(self, size):
        self.size_x, self.size_y = size

    @abstractmethod
    def train(self, __train_position , __train_correct_move):
        pass

    @abstractmethod
    def predict(self, game_state) -> Action:
        pass
