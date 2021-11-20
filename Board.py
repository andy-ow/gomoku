import sys

import numpy as np

X_BOARD = 0
O_BOARD = 1
EMPTY = 0
TAKEN = 1


class Board:

    def __init__(self, size=(5, 5)):
        self.board = np.zeros((size[0], size[1], 3))
        self.size_x = size[0]
        self.size_y = size[1]
        self.number_of_moves = 0
        self.max_number_of_moves = self.size_x * self.size_y

    def get_xy_position(self, x, y):
        if not self.xy_is_within_limits(x, y) or self.__xy_is_empty(x, y): return EMPTY
        if self.board[x, y, X_BOARD] == TAKEN: return 'X'
        if self.board[x, y, O_BOARD] == TAKEN: return 'O'
        sys.exit('Board position not empty, not X, and not O: ' + self.board[x, y, X_BOARD] + ' ' + self.board[
            x, y, O_BOARD] + '\n')

    def is_move_legal(self, x, y, stone):
        return (stone == 'X' or stone == 'O') and self.xy_is_within_limits(x, y) and self.__xy_is_empty(x, y)

    def xy_is_within_limits(self, x, y):
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def board_is_full(self):
        return self.number_of_moves == self.max_number_of_moves

    def __xy_is_empty(self, x, y):
        return self.board[x, y, X_BOARD] == EMPTY and self.board[x, y, O_BOARD] == EMPTY

    def __set_x(self, x, y):
        self.number_of_moves += 1
        self.board[x, y, X_BOARD] = TAKEN

    def __set_y(self, x, y):
        self.number_of_moves += 1
        self.board[x, y, O_BOARD] = TAKEN