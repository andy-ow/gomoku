from typing import List, Tuple

from Agent import Agent
from ai.Types import GameState, Action
from gomoku_game.Types import Position


class HumanPlayer(Agent):

    def __init__(self, name: str):
        self._name = name

    def user_input(self, message):
        try:
            x, y = map(int, input(message).strip().split(" "))
            return (x, y)
        except:
            return self.user_input(message)


    @property
    def get_name(self) -> str:
        return self._name

    def choose_action(self, game_state: GameState) -> Action:
        x, y = self.user_input("Input x and y, seperated by space. For example 1 2: ")
        return Action((x,y))

    def learn(self, game_states__actions: List[Tuple[GameState, Action]]):
        pass

    @property
    def is_human(self) -> bool:
        return True