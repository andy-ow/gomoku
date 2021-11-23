import sys
from typing import List, Tuple

from Game import Game
from ai.Types import GameState, Action
from gomoku_game.Board import Board
from gomoku_game.Check_win import CheckWin
from gomoku_game.Types import Position
from gomoku_game.common import Player, WINNING_NUMBER


class GomokuGame(Game):

    def __init__(self, size):
        self.size = size
        self._board = Board(size)
        self._is_playing = True
        self.winner = None
        self._current_player = Player.X
        self._history_x: List[Tuple[GameState, Action]] = []
        self._history_o: List[Tuple[GameState, Action]] = []

    def make_move(self, pos: Position):
        if not self._is_playing:
            sys.exit("Game already over. Not possible to make moves. Current state: " + str(self._is_playing))
        self._add_to_history(pos)
        stone = self._current_player.stone()
        if not self._board.is_move_legal(pos, stone):
            self.winner = self._current_player.opponent()
            self._is_playing = False
        else:
            self._board.make_move(pos, stone)
            if CheckWin.is_winning(board=self._board, last_move=pos, last_stone=self._current_player.stone(),
                                   winning_number=WINNING_NUMBER):
                self._is_playing = False
                self.winner = self._current_player
                self._current_player = None
            elif self._board.board_is_full():
                self._is_playing = False
                self.winner = None
                self._current_player = None
            else:
                self._next_player()

    def _next_player(self):
        self._current_player = self._current_player.opponent()

    def _add_to_history(self, pos: Position):
        if self._current_player is Player.X:
            self._history_x.append((self._board.get_board(), Action(pos)))
        elif self._current_player is Player.O:
            self._history_o.append((self._board.get_board_with_switched_xo(), Action(pos)))
        else:
            sys.exit("Wrong player.")

    def get_history_of_winning_moves(self) -> List[Tuple[GameState, Action]]:
        if self.winner is None:
            sys.exit("No history of winning moves. Game still in progress.")
        if self.winner == Player.X:
            return self._history_x
        if self.winner == Player.O:
            return self._history_o
        return list()

    def print_game(self):
        self.print_board()

    def print_board(self):
        print(self._board)

    def print_switched_board(self):
        Board.print_board(self._board.get_board_with_switched_xo(), self.size)

    @property
    def is_playing(self) -> bool:
        return self._is_playing

    @staticmethod
    def print_history(history, size):
        for (board, move) in history:
            Board.print_board(board, size)
            print("Move: " + str(move) + "\n")

    @property
    def current_player(self):
        return self._current_player

