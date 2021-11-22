from unittest import TestCase

from gomoku_game.Board import Board
from gomoku_game.common import Stone


class TestBoard(TestCase):
    def test_get_xy_position(self):
        board = Board()
        board.make_move((0, 0), Stone.X)
        self.assertEqual(Stone.X, board.get_xy_position((0, 0)))
        board.make_move((3, 3), Stone.O)
        self.assertEqual(Stone.O, board.get_xy_position((3, 3)))

    def test_is_move_legal(self):
        board = Board()
        self.assertEqual(True, board.is_move_legal((5, 5), Stone.X))
        self.assertEqual(True, board.is_move_legal((0, 0), Stone.O))
        board.make_move((0, 0), Stone.X)
        self.assertEqual(False, board.is_move_legal((0, 0), Stone.X))
        board.make_move((5, 5), Stone.O)
        self.assertEqual(False, board.is_move_legal((5, 5), Stone.X))
        board.make_move((9, 9), Stone.X)
        self.assertEqual(False, board.is_move_legal((9, 9), Stone.O))
        board.make_move((9, 8), Stone.O)
        self.assertEqual(False, board.is_move_legal((9, 8), Stone.O))

    def test_xy_is_within_limits(self):
        board = Board()
        self.assertEqual(False, board.is_move_legal((20, 20), Stone.X))
        self.assertEqual(False, board.is_move_legal((-1, 2), Stone.X))

    def test_board_is_full(self):
        board = Board()
        for x in range(19):
            for y in range(19):
                self.assertEqual(False, board.board_is_full())
                board.make_move((x, y), Stone.X)
        self.assertEqual(True, board.board_is_full())

