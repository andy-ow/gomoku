from typing import List, Tuple

from Agent import Agent
from ai.Types import GameState, Action
from gomoku_game import GomokuGame
from gomoku_game.Types import Position
class DummyAgent(Agent):

    def choose_action(self, game_state: GameState) -> Action:
        pass

    def learn(self, game_states__actions: List[Tuple[GameState, Action]]):
        pass

    @property
    def is_human(self) -> bool:
        return True


if __name__ == '__main__':
    game = GomokuGame(size=(9,9), players=[DummyAgent(), DummyAgent()])
    print("Input x and y, seperated by space. For example\n 1 2\n\n")
    while game.is_playing:
        game.print_board()
        print("It is player's " + game.current_player.name() + " turn.")
        x, y = map(int, input().strip().split(" "))
        game.make_move(Position((x,y)))
    print("Game over. The winner is player: " + game.winner.name())

