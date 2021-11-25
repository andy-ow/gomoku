from typing import List, Tuple

import tensorflow as tf
import numpy as np

from Agent import Agent
from ai.AiModel import AiModel
from ai.Types import GameState, Action


class AiPlayer(Agent):

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def is_human(self) -> bool:
        return False

    def choose_action(self, game_state: GameState) -> Action:
        return self.model.predict(game_state.reshape(1, *game_state.shape))

    def __init__(self, name: str, model: AiModel, shape, after_how_many_games_to_train: int, max_positions_to_train):
        self._name = name
        self.shape = shape
        self.after_how_many_games_to_train: int = after_how_many_games_to_train
        self.train_position = []
        self.train_correct_move = []
        self.model = model
        self.games_played = 0
        self.max_positions_to_train = max_positions_to_train

    def learn(self, list_of_positions__correct_moves: List[Tuple[np.ndarray, Action]]):
        if len(list_of_positions__correct_moves)>0:
            assert list_of_positions__correct_moves[0][0].shape == self.shape
            print(self._name + ": Adding positions: " + str(len(list_of_positions__correct_moves)))
            self.train_position.extend(tf.convert_to_tensor([data[0] for data in list_of_positions__correct_moves]))
            self.train_correct_move.extend(data[1] for data in list_of_positions__correct_moves)
            if self.games_played % self.after_how_many_games_to_train == 0: self.__train()

    def __train(self):
        print(self._name + ": Learn: current list of positions: " + str(len(self.train_position)))
        if self.games_played % self.after_how_many_games_to_train == 0:
            self.model.train(self.train_position, self.train_correct_move)
            if len(self.train_position) > self.max_positions_to_train:
                self.train_correct_move = self.train_correct_move[len(self.train_position)//2:]
                self.train_position = self.train_position[len(self.train_position)//2:]

