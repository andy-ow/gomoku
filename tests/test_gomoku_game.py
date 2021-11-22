from unittest import TestCase

from gomoku_game.GomokuGame import GomokuGame
from gomoku_game.common import State, Player


class TestGomokuGame(TestCase):
    size = (8,8)
    def test_make_move1(self):
        game = GomokuGame(self.size)
        self.assertEqual(State.PLAYING, game.state)
        for move in [(1,0), (0,1), (2,0), (0,2), (3,0), (0,3), (4,0), (0,4)]:
            game.make_move(move)
            self.assertEqual(State.PLAYING, game.state)
            self.assertEqual(game.winner, None)
        game.make_move((5,0))
        self.assertEqual(State.END, game.state)
        self.assertEqual(game.winner, Player.X)
        print("\nGame history from X viewpoint\n")
        game.print_history(game.history_x, self.size)
        print("\nGame history from O viewpoint for AI training (X and O switched)\n")
        game.print_history(game.history_o, self.size)
        print("\nEND of history.\n")
        print("Last position\n")
        game.print_board()
        print("\nLast position with switched X and O\n")
        game.print_switched_board()
        print("\nEND printing.")


    def test_make_move2(self):
        game = GomokuGame(self.size)
        for move in [(1,0), (0,1), (2,0), (0,2), (3,0), (0,3), (4,0), (0,4)]:
            game.make_move(move)
            self.assertEqual(State.PLAYING, game.state)
            self.assertEqual(game.winner, None)
        game.make_move((7,0))
        self.assertEqual(State.PLAYING, game.state)
        self.assertEqual(game.winner, None)
        game.make_move((0,5))
        self.assertEqual(State.END, game.state)
        self.assertEqual(game.winner, Player.O)
