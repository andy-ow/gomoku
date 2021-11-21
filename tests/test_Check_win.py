from unittest import TestCase

from gomoku_game.Board import Board
from gomoku_game.Check_win import CheckWin
from gomoku_game.common import Stone


class TestCheckWin(TestCase):
    def test_is_winning1(self):
        board = Board(size=(19, 19))
        winning_number = 5
        for (x, y) in [(0, 0), (0, 1), (0, 3), (0, 4)]:
            board.make_move((x, y), Stone.X)
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
            win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
            win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
            self.assertEqual(False, win_x, msg="x: " + str(x) + " y: " + str(y))  # add assertion here
            self.assertEqual(False, win_o)  # add assertion here
        for (x, y) in [(0, 0), (0, 1), (0, 3), (0, 4)]:
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
        x, y = 0, 2
        board.make_move((x, y), Stone.X)
        win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
        win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
        self.assertEqual(True, win_x, board)
        self.assertEqual(False, win_o)

    def test_is_winning2(self):
        board = Board(size=(19, 19))
        winning_number = 5
        for (x, y) in [(1, 1), (2, 2), (3, 3), (4, 4)]:
            board.make_move((x, y), Stone.X)
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
            win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
            win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
            self.assertEqual(False, win_x, msg="x: " + str(x) + " y: " + str(y))  # add assertion here
            self.assertEqual(False, win_o)  # add assertion here
        for (x, y) in [(1, 1), (2, 2), (3, 3), (4, 4)]:
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
        x, y = 0, 0
        board.make_move((x, y), Stone.X)
        win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
        win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
        self.assertEqual(True, win_x, board)
        self.assertEqual(False, win_o)

    def test_is_winning3(self):
        board = Board(size=(19, 19))
        winning_number = 5
        for (x, y) in [(18, 18), (17, 18), (15, 18), (14, 18)]:
            board.make_move((x, y), Stone.O)
            self.assertEqual(Stone.O, board.get_xy_position((x, y)))
            win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
            win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
            self.assertEqual(False, win_x, msg="x: " + str(x) + " y: " + str(y))  # add assertion here
            self.assertEqual(False, win_o)  # add assertion here
        for (x, y) in [(18, 18), (17, 18), (15, 18), (14, 18)]:
            self.assertEqual(Stone.O, board.get_xy_position((x, y)))
        x, y = 16, 18
        board.make_move((x, y), Stone.O)
        win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
        win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
        self.assertEqual(False, win_x)
        self.assertEqual(True, win_o)

    def test_is_winning4(self):
        board = Board(size=(19, 19))
        winning_number = 5
        for (x, y) in [(6, 6), (7, 5), (10, 2), (9, 3)]:
            board.make_move((x, y), Stone.X)
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
            win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
            win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
            self.assertEqual(False, win_x, msg="x: " + str(x) + " y: " + str(y))  # add assertion here
            self.assertEqual(False, win_o)  # add assertion here
        for (x, y) in [(6, 6), (7, 5), (10, 2), (9, 3)]:
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
        x, y = 8, 4
        board.make_move((x, y), Stone.X)
        win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
        win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
        self.assertEqual(True, win_x, board)
        self.assertEqual(False, win_o)

    def test_is_winning5(self):
        board = Board(size=(19, 19))
        winning_number = 5
        for (x, y) in [(0, 0), (0, 1), (0, 2), (0, 3)]:
            board.make_move((x, y), Stone.X)
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
            win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
            win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
            self.assertEqual(False, win_x, msg="x: " + str(x) + " y: " + str(y))  # add assertion here
            self.assertEqual(False, win_o)  # add assertion here
        for (x, y) in [(0, 0), (0, 1), (0, 2), (0, 3)]:
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
        x, y = 0, 4
        board.make_move((x, y), Stone.X)
        win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
        win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
        self.assertEqual(True, win_x, board)
        self.assertEqual(False, win_o)

    def test_is_winning6(self):
        board = Board(size=(19, 19))
        winning_number = 5
        for (x, y) in [(0, 0), (0, 1), (0, 2)]:
            board.make_move((x, y), Stone.X)
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
            win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
            win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
            self.assertEqual(False, win_x, msg="x: " + str(x) + " y: " + str(y))  # add assertion here
            self.assertEqual(False, win_o)  # add assertion here
        for (x, y) in [(0, 0), (0, 1), (0, 2)]:
            self.assertEqual(Stone.X, board.get_xy_position((x, y)))
        x, y = (0, 3)
        board.make_move((x, y), Stone.O)
        x, y = 0, 4
        board.make_move((x, y), Stone.X)
        win_x = CheckWin.is_winning(board, (x, y), Stone.X, winning_number)
        win_o = CheckWin.is_winning(board, (x, y), Stone.O, winning_number)
        self.assertEqual(False, win_x)
        self.assertEqual(False, win_o)
