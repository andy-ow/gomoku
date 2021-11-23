from typing import Type

from Agent import Agent
from Game import Game


class Match:

    def __init__(self, player1: Agent, player2: Agent, game_class: Type[Game]):
        self.player1 = player1
        self.player2 = player2
        self.game = game_class([player1, player2])

    def play(self, visible: bool = False):
        if visible: self.game.print_game()


