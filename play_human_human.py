
from HumanPlayer import HumanPlayer
from Match import Match
from gomoku_game import GomokuGame

if __name__ == '__main__':
    board_size = (8, 8)
    match = Match(HumanPlayer("Player 1"), HumanPlayer("Player 2"), GomokuGame, board_size)
    match.play()



"""
class DummyAgent(Agent):
    def choose_action(self, game_state: GameState) -> Action:
        pass

    def learn(self, game_states__actions: List[Tuple[GameState, Action]]):
        pass

    @property
    def is_human(self) -> bool:
        return True


if __name__ == '__main__':
    game = GomokuGame(size=(9, 9), players=[DummyAgent(), DummyAgent()])
    print("Input x and y, seperated by space. For example\n 1 2\n\n")
    while game.is_playing:
        game.print_board()
        print("It is player's " + game.current_player.name() + " turn.")
        x, y = map(int, input().strip().split(" "))
        game.make_move(Position((x, y)))
    print("Game over. The winner is player: " + game.winner.name())
"""