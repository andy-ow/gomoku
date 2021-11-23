
import numpy as np

from Agent import Agent
from ai.Model import Model
from ai.Types import GameState, Action


class AiPlayer(Agent):

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def is_human(self) -> bool:
        return False

    def choose_action(self, game_state: GameState) -> Action:
        return self.model.predict(game_state)

    def __init__(self, name, shape, after_how_many_positions_to_train: int):
        self._name = name
        self.shape = shape
        self.after_how_many_positions_to_train: int = after_how_many_positions_to_train
        self.__train_position = []
        self.__train_correct_move = []
        self.model = self.__load_model()

    def learn(self, list_of_positions__correct_moves: list[np.ndarray, (int, int)]):
        assert list_of_positions__correct_moves[0].shape == self.shape
        self.__train_position.extend([data[0] for data in list_of_positions__correct_moves])
        self.__train_correct_move.extend([data[1] for data in list_of_positions__correct_moves])
        self.__train()

    def __train(self):
        if len(self.__train_position) > self.after_how_many_positions_to_train:
            self.model.train(self.__train_position, self.__train_correct_move)
            self.__train_correct_move = []
            self.__train_position = []

    def __load_model(self):
        return Model(self.shape)
