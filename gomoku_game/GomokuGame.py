import sys
from typing import List, Tuple, Optional

from Agent import Agent
from Game import Game
from ai.Types import GameState, Action
from gomoku_game.Board import Board
from gomoku_game.Check_win import CheckWin
from gomoku_game.Types import Position
from gomoku_game.common import Player, WINNING_NUMBER


class GomokuGame(Game):

    def get_winner(self) -> Optional[Agent]:
        return self._players[self._winner]

    def get_current_gamestate(self) -> GameState:
        return self._board.get_board()

    def get_current_player(self) -> Agent:
        return self._players[self._current_player]

    def __init__(self, players: List[Agent], size: Tuple[int, int]):
        if not len(players) == 2: sys.exit(
            "Gumoku is a game for exactly 2 players. Current number of players: " + str(len(players)))
        # first player plays X, second player is O
        self._players = {Player.X: players[0], Player.O: players[1]}
        self.size = size
        self._board = Board(size)
        self._is_playing = True
        self._winner = None
        self._current_player = Player.X
        self._history_x: List[Tuple[GameState, Action]] = []
        self._history_o: List[Tuple[GameState, Action]] = []

    def make_move(self, pos: Position):
        if not self._is_playing:
            sys.exit("Game already over. Not possible to make moves. Current state: " + str(self._is_playing))
        self._add_to_history(pos)
        stone = self._current_player.stone()
        if not self._board.is_move_legal(pos, stone):
            self._winner = self._current_player.opponent()
            self._is_playing = False
        else:
            self._board.make_move(pos, stone)
            if CheckWin.is_winning(board=self._board, last_move=pos, last_stone=self._current_player.stone(),
                                   winning_number=WINNING_NUMBER):
                self._is_playing = False
                self._winner = self._current_player
                self._current_player = None
            elif self._board.board_is_full():
                self._is_playing = False
                self._winner = None
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
        if self._winner is None:
            sys.exit("No history of winning moves. Game still in progress.")
        if self._winner == Player.X:
            return self._history_x
        if self._winner == Player.O:
            return self._history_o
        return list()

    def print_game(self):
        self.print_board()

    def print_board(self):
        print(self._board)

    def print_switched_board(self):
        Board.print_board(self._board.get_board_with_switched_xo())

    @property
    def is_playing(self) -> bool:
        return self._is_playing

    @staticmethod
    def print_history(history):
        for (board, move) in history:
            Board.print_board(board)
            print("Move: " + str(move) + "\n")

    @property
    def current_player(self):
        return self._current_player
