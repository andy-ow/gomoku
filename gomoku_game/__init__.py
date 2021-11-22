import sys

import gomoku_game.Board
from gomoku_game.Check_win import CheckWin
from gomoku_game.common import Player, State


class GomokuGame:
    WINNING_NUMBER = 5

    def __init__(self, size):
        self.__board = gomoku_game.Board.Board(size)
        self.state = State.PLAYING
        self.winner = None
        self.current_player = Player.X
        self.history_x = []
        self.history_o = []

    def make_move(self, pos):
        if self.state != State.PLAYING:
            sys.exit("Game already over. Not possible to make moves. Current state: " + str(self.state))
        self.__add_to_history(pos)
        stone = self.current_player.stone()
        if not self.__board.is_move_legal(pos, stone):
            self.winner = self.current_player.opponent()
            self.state = State.END
        else:
            self.__board.make_move(pos, stone)
            if CheckWin.is_winning(board=self.__board, last_move=pos, last_stone=self.current_player.stone(),
                                   winning_number=self.WINNING_NUMBER):
                self.state = State.END
                self.winner = self.current_player
                self.current_player = None
            elif self.__board.board_is_full():
                self.state = State.END
                self.winner = None
                self.current_player = None
            else:
                self.__next_player()

    def __next_player(self):
        self.current_player = self.current_player.opponent()

    def __add_to_history(self, pos):
        if self.current_player is Player.X:
            self.history_x.append([self.__board.get_board(), pos])
        elif self.current_player is Player.O:
            self.history_o.append([self.__board.get_board_with_switched_xo(), pos])
        else:
            sys.exit("Wrong player.")

    def print_board(self):
        print(self.__board)

    @staticmethod
    def __enemy(player):
        if player == State.TURN_PLAYER_X: return State.TURN_PLAYER_O
        if player == State.TURN_PLAYER_O: return State.TURN_PLAYER_X
        sys.exit("Invalid player parameter: " + player)
