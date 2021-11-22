from gomoku_game import GomokuGame

if __name__ == '__main__':
    game = GomokuGame(size=(9,9))
    print("Input x and y, seperated by space. For example\n 1 2\n\n")
    while game.state == game.state.PLAYING:
        game.print_board()
        print("It is player's " + game.current_player.name() + " turn.")
        x, y = map(int, input().strip().split(" "))
        game.make_move((x,y))
    print("Game over. The winner is player: " + game.winner.name())

