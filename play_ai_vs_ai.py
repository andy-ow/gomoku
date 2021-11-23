from Match import Match
from ai.AiPlayer import AiPlayer
from ai.models.RandomModel import RandomModel
from gomoku_game import GomokuGame

if __name__ == '__main__':
    board_size = (8, 8)
    match = Match(AiPlayer(name="Player 1", model=RandomModel(board_size), shape=(8, 8, 2), after_how_many_positions_to_train=1),
                  AiPlayer(name="Player 2", model=RandomModel(board_size), shape=(8, 8, 2), after_how_many_positions_to_train=1),
                  GomokuGame, board_size)
    for i in range(12):
        match.play(visible=True)
        match.restart()