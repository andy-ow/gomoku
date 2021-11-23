from gomoku_game.Board import Board
from gomoku_game.Types import Position


class CheckWin:

    @staticmethod
    def is_winning(board: Board, last_move, last_stone, winning_number):
        last_move_x, last_move_y = last_move
        for (_step_x, _step_y) in [(0,1),(1,0),(1,1),(1,-1)]:
            count = 1
            for direction in [-1,1]:
                x, y = last_move_x, last_move_y
                step_x, step_y = direction * _step_x, direction * _step_y
                while True:
                    x += step_x
                    y += step_y
                    if board.get_xy_position(Position((x, y))) == last_stone:
                        count += 1
                    else:
                        break
            if count >= winning_number:
                return True
        return False
