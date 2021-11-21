import sys

import numpy as np

from gomoku_game.common import Stone

X_BOARD = 0
O_BOARD = 1
EMPTY = 0
TAKEN = 1


class Board:

    def __init__(self, size=(19, 19)):
        self.size_x = size[0]
        self.size_y = size[1]
        self.__board = Board.__new_empty_board(self.size_x, self.size_y)
        self.__number_of_moves = 0
        self.__max_number_of_moves = self.size_x * self.size_y

    def get_xy_position(self, pos):
        x,y = pos
        if not self.__xy_is_within_limits(pos) or self.__xy_is_empty(pos): return EMPTY
        if self.__board[x, y, X_BOARD] == TAKEN: return Stone.X
        if self.__board[x, y, O_BOARD] == TAKEN: return Stone.O
        sys.exit('Board position not empty, not X, and not O: ' + self.__board[x, y, X_BOARD] + ' ' + self.__board[
            x, y, O_BOARD] + '\n')

    def is_move_legal(self, pos, stone):
        return (stone == Stone.X or stone == Stone.O) and self.__xy_is_within_limits(pos) and self.__xy_is_empty(pos)

    def board_is_full(self):
        return self.__number_of_moves >= self.__max_number_of_moves

    def make_move(self, pos, stone):
        if stone is Stone.X:
            self.__set_x(pos)
        elif stone is Stone.O:
            self.__set_o(pos)
        else:
            sys.exit("make move with wrong stone: " + stone)

    def __xy_is_within_limits(self, pos):
        x, y = pos
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def __xy_is_empty(self, pos):
        x, y = pos
        return self.__board[x, y, X_BOARD] == EMPTY and self.__board[x, y, O_BOARD] == EMPTY

    def __set_x(self, pos):
        x, y = pos
        self.__number_of_moves += 1
        self.__board[x, y, X_BOARD] = TAKEN

    def __set_o(self, pos):
        x, y = pos
        self.__number_of_moves += 1
        self.__board[x, y, O_BOARD] = TAKEN

    def get_board(self):
        return self.__board

    def get_board_with_switched_xo(self):
        switched_board = Board.__new_empty_board(self.size_x, self.size_y)
        board_x = self.__board[:,:,X_BOARD]
        board_o = self.__board[:, :, O_BOARD]
        switched_board[:,:,X_BOARD] = board_o
        switched_board[:,:,O_BOARD] = board_x
        return switched_board

    @staticmethod
    def __new_empty_board(size_x, size_y):
        return np.zeros((size_x, size_y, 2))