from HumanPlayer import HumanPlayer
from Match import Match
from ai.AiPlayer import AiPlayer
from ai.models.SimpleSequentialModel import SimpleSequentialModel
from ai.models.SimpleSequentialModel2 import SimpleSequentialModel2
from gomoku_game import GomokuGame
import tensorflow as tf


def print_stats(stats: dict):
    for player, score in sorted(list(stats.items()), key=lambda z: z[1] / z[0].games_played, reverse=True):
        print(player.get_name, '   ' + str(score) + '/' + str(player.games_played) + '   ', score / player.games_played)


if __name__ == '__main__':
    gpus = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])

    board_size = (9, 9)
    ai_players = []
    for layers_no in [3, 4, 7]:
        for epochs in [30]:
            for max_positions_to_train in [10000]:
                for model in [SimpleSequentialModel, SimpleSequentialModel2]:
                    for after_how_many_to_train in [100]:
                        # ai_player = AiPlayer(name="AI__layers_"+str(layers_no)+"__epochs_"+str(epochs)+"__max_positions_"+str(how_many_games_remember)+"__model_"+str(model.model_name()),
                        ai_player = AiPlayer(name="La" + str(layers_no) + "__e" + str(epochs) + "__max" + str(
                            max_positions_to_train) + "__a" + str(after_how_many_to_train) + "__" + str(
                            model.model_name()),
                                             model=model(board_size, epochs=epochs, layers_no=layers_no),
                                             shape=(9, 9, 2),
                                             after_how_many_games_to_train=after_how_many_to_train,
                                             max_positions_to_train=max_positions_to_train)
                        ai_players.append(ai_player)
    human_player = HumanPlayer(name="Human")
    matches = []
    for player1 in ai_players:
        for player2 in ai_players:
            match = Match(player1, player2, GomokuGame, board_size)
            matches.append(match)

    rounds = 0
    games = 0
    winner_stats = {}
    for player in ai_players:
        winner_stats[player] = 0
    while True:
        for ai_match in matches:
            visible = True if rounds != 0 and rounds % 10 == 0 else False
            ai_match.play(visible=visible)
            games += 1
            print("", end=".")
            if games % 100 == 0:
                print()
                print("Games: " + str(games))
                print_stats(winner_stats)
            if ai_match.player1 != ai_match.player2:
                winner_stats[ai_match.winner] += 1
            ai_match.restart()
        rounds += 1
        print()
        print("Games: " + str(games))
        print_stats(winner_stats)
        print("\nRound: " + str(rounds))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
