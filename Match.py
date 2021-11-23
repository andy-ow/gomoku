from typing import Type, Optional

from Agent import Agent
from Game import Game


class Match:

    def __init__(self, player1: Agent, player2: Agent, game_class: Type[Game], config):
        self.player1 = player1
        self.player2 = player2
        self.human_is_playing = any([player1.is_human, player2.is_human])
        self.game_class = game_class
        self.config = config
        self.game = game_class([player1, player2], config)

    def restart(self):
        self.game = self.game_class([self.player1, self.player2], self.config)

    def play(self, visible: Optional[bool] = None):
        if not self.game.is_playing:
            raise Exception("Error: Trying to play a finished game.")
        show_game = visible or (self.human_is_playing and visible is None)
        while self.game.is_playing:
            current_player: Agent = self.game.get_current_player()
            if show_game:
                self.game.print_game()
            gamestate = self.game.get_current_gamestate()
            action = current_player.choose_action(gamestate)
            if show_game:
                print("Playing action: " + str(action))
            self.game.make_move(action)
        winner = self.game.get_winner()
        winner.learn(self.game.get_history_of_winning_moves())
        if show_game:
            self.game.print_game()
            print("Game over. The winner is: " + winner.get_name)
