from unittest import TestCase

from gomoku_game import GomokuGame, State, Player


class TestGomokuGame(TestCase):
    def test_make_move1(self):
        game = GomokuGame((19,19))
        for move in [(1,0), (0,1), (2,0), (0,2), (3,0), (0,3), (4,0), (0,4)]:
            game.make_move(move)
            self.assertEqual(State.PLAYING, game.state)
            self.assertEqual(game.winner, None)
        game.make_move((5,0))
        self.assertEqual(State.END, game.state)
        self.assertEqual(game.winner, Player.X)

    def test_make_move2(self):
        game = GomokuGame((19,19))
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