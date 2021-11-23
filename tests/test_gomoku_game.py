from unittest import TestCase

from gomoku_game.GomokuGame import GomokuGame
from gomoku_game.common import Player


class TestGomokuGame(TestCase):
    size = (8,8)
    def test_make_move1(self):
        game = GomokuGame(players = ['test','test'], size = self.size)
        self.assertTrue(game._is_playing)
        for move in [(1,0), (0,1), (2,0), (0,2), (3,0), (0,3), (4,0), (0,4)]:
            game.make_move(move)
            self.assertTrue(game._is_playing)
            self.assertEqual(game.winner, None)
        game.make_move((5,0))
        self.assertFalse(game._is_playing)
        self.assertEqual(game.winner, Player.X)
        print("\nGame history from X viewpoint\n")
        game.print_history(game._history_x)
        print("\nGame history from O viewpoint for AI training (X and O switched)\n")
        game.print_history(game._history_o)
        print("\nEND of history.\n")
        print("Last position\n")
        game.print_board()
        print("\nLast position with switched X and O\n")
        game.print_switched_board()
        print("\nEND printing.")


    def test_make_move2(self):
        game = GomokuGame(players = ['test','test'], size = self.size)
        for move in [(1,0), (0,1), (2,0), (0,2), (3,0), (0,3), (4,0), (0,4)]:
            game.make_move(move)
            self.assertTrue(game._is_playing)
            self.assertEqual(game.winner, None)
        game.make_move((7,0))
        self.assertTrue(game._is_playing)
        self.assertEqual(game.winner, None)
        game.make_move((0,5))
        self.assertFalse(game._is_playing)
        self.assertEqual(game.winner, Player.O)
