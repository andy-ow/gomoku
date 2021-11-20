import sys


class Game_Controller:
    PLAYER_1 = 1
    PLAYER_2 = 2

    def __init__(self, game):
        self.turn = Game_Controller.PLAYER_1
        self.winner = None
        self.finish = False
        self.game = game
        self.data = game.data
        self.history = []

    def get_current_data(self):
        return self.game.data

    def make_move(self, move):
        if self.finish:
            sys.exit("Game already finished. No moves possible.")
        self.history.append([self.data, move])
        self.game.make_move(move)
        self.data = self.game.data
        if self.game.winner is not None:
            self.winner = self.game.winner
            self.finish = True
