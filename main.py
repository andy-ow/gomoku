from HumanPlayer import HumanPlayer
from Match import Match
from ai.AiPlayer import AiPlayer
from ai.models.SimpleSequentialModel import SimpleSequentialModel
from gomoku_game import GomokuGame
import tensorflow as tf

if __name__ == '__main__':
    gpus = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])

    board_size = (19, 19)
    ai_player1 = AiPlayer(name="Player 1", model=SimpleSequentialModel(board_size, 100), shape=(19, 19, 2),
                          after_how_many_positions_to_train=1000)
    ai_player2 = AiPlayer(name="Player 2", model=SimpleSequentialModel(board_size, 20), shape=(19, 19, 2),
                          after_how_many_positions_to_train=200)
    human_player = HumanPlayer(name="Human")
    match_ai_vs_ai = Match(ai_player1, ai_player2, GomokuGame, board_size)
    match_ai_vs_ai2 = Match(ai_player2, ai_player1, GomokuGame, board_size)
    match_ai_vs_ai3 = Match(ai_player1, ai_player1, GomokuGame, board_size)
    match_ai_vs_ai4 = Match(ai_player2, ai_player2, GomokuGame, board_size)
    match_human_vs_ai = Match(human_player, ai_player2, GomokuGame, board_size)
    match_human_vs_ai2 = Match(ai_player1, human_player, GomokuGame, board_size)
    games = 0
    ai_matches = [match_ai_vs_ai, match_ai_vs_ai2, match_ai_vs_ai3, match_ai_vs_ai4]
    while True:
        print(len(ai_player1.train_position))
        match_human_vs_ai.play()
        match_human_vs_ai.restart()
        match_human_vs_ai2.play()
        match_human_vs_ai.restart()
        games += 1
        winner_stats = {ai_player1.get_name: 0, ai_player2.get_name: 0}
        for i in range(500):
            for ai_match in ai_matches:
                visible = True if i % 50 == 0 else False
                ai_match.play(visible=visible)
                if ai_match.player1 != ai_match.player2:
                    print("Winner: " + ai_match.winner.get_name)
                    winner_stats[ai_match.winner.get_name] += 1
                    print("Stats: ", winner_stats)
                ai_match.restart()
                games += 1
                print(games)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
