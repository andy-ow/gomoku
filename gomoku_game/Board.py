import sys

import numpy as np

from ai.Types import GameState
from gomoku_game.Types import Position
from gomoku_game.common import Stone

X_BOARD = 0
O_BOARD = 1
_EMPTY = 0
TAKEN = 1


class Board:

    def __init__(self, size=(19, 19)):
        self.size_x, self.size_y = size
        self.__board: GameState = Board.__new_empty_board(self.size_x, self.size_y)
        self.__number_of_moves = 0
        self.__max_number_of_moves = self.size_x * self.size_y

    def get_xy_position(self, pos: Position):
        x, y = pos
        if not self.__xy_is_within_limits(pos) or self.__xy_is_empty(pos): return Stone.EMPTY
        if self.__board[x, y, X_BOARD] == TAKEN: return Stone.X
        if self.__board[x, y, O_BOARD] == TAKEN: return Stone.O
        sys.exit('Board position not empty, not X, and not O: ' + self.__board[x, y, X_BOARD] + ' ' + self.__board[
            x, y, O_BOARD] + '\n')

    def is_move_legal(self, pos: Position, stone: Stone):
        return (stone == Stone.X or stone == Stone.O) and self.__xy_is_within_limits(pos) and self.__xy_is_empty(pos)

    def board_is_full(self):
        return self.__number_of_moves >= self.__max_number_of_moves

    def make_move(self, pos: Position, stone: Stone):
        if stone is Stone.X:
            self.__set_x(pos)
        elif stone is Stone.O:
            self.__set_o(pos)
        else:
            sys.exit("make move with wrong stone: " + str(stone))

    def __xy_is_within_limits(self, pos: Position):
        x, y = pos
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def __xy_is_empty(self, pos: Position):
        x, y = pos
        return self.__board[x, y, X_BOARD] == _EMPTY and self.__board[x, y, O_BOARD] == _EMPTY

    def __set_x(self, pos: Position):
        x, y = pos
        self.__number_of_moves += 1
        self.__board[x, y, X_BOARD] = TAKEN

    def __set_o(self, pos: Position):
        x, y = pos
        self.__number_of_moves += 1
        self.__board[x, y, O_BOARD] = TAKEN

    def get_board(self) -> GameState:
        return self.__board.__copy__()

    def get_board_with_switched_xo(self) -> GameState:
        switched_board = Board.__new_empty_board(self.size_x, self.size_y)
        board_x = self.__board[:, :, X_BOARD]
        board_o = self.__board[:, :, O_BOARD]
        switched_board[:, :, X_BOARD] = board_o
        switched_board[:, :, O_BOARD] = board_x
        return switched_board

    def __str__(self) -> str:
        board_string = ''
        for y in range(self.size_y):
            for x in range(self.size_x):
                board_string = board_string + str(self.get_xy_position(Position((x,y))))
            board_string += '\n'
        return board_string

    @staticmethod
    def print_board(board: GameState):
        size_x, size_y, _ = board.shape
        board_string = ''
        for y in range(size_y):
            for x in range(size_x):
                stone = Stone.EMPTY
                position_value = board[x,y,:]
                if position_value[X_BOARD]==TAKEN: stone = Stone.X
                if position_value[O_BOARD]==TAKEN: stone = Stone.O
                board_string = board_string + str(stone)
            board_string += '\n'
        print(board_string)


    @staticmethod
    def __new_empty_board(size_x: int, size_y: int) -> GameState:
        return GameState(np.zeros((size_x, size_y, 2)))
