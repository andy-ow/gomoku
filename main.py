from HumanPlayer import HumanPlayer
from Match import Match
from ai.AiPlayer import AiPlayer
from ai.models.SimpleSequentialModel import SimpleSequentialModel
from gomoku_game import GomokuGame

if __name__ == '__main__':
    board_size = (19, 19)
    ai_player1 = AiPlayer(name="Player 1", model=SimpleSequentialModel(board_size), shape=(19, 19, 2), after_how_many_positions_to_train=100)
    ai_player2 = AiPlayer(name="Player 2", model=SimpleSequentialModel(board_size), shape=(19, 19, 2), after_how_many_positions_to_train=100)
    human_player = HumanPlayer(name="Human")
    match_ai_vs_ai = Match(ai_player1, ai_player2, GomokuGame, board_size)
    match_human_vs_ai = Match(human_player, ai_player1, GomokuGame, board_size)

    while True:
        match_human_vs_ai.play()
        match_human_vs_ai.restart()
        for i in range(100):
            match_ai_vs_ai.play(visible=True)
            match_ai_vs_ai.restart()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
