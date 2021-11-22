from ai.Model import Model


class ai_player:

    def __init__(self, size: (int, int), after_how_many_positions_to_train: int):
        self.after_how_many_positions_to_train: int = after_how_many_positions_to_train
        self.size: (int,int) = size
        self.__train_position = []
        self.__train_correct_move = []
        self.model = self.__load_model()

    def add_train_position(self, position__correct_move):
        self.__train_position.append(position__correct_move[0])
        self.__train_correct_move.append(position__correct_move[1])

    def add_train_positions(self, list_of_positions__correct_moves):
        self.__train_position.extend([data[0] for data in list_of_positions__correct_moves])
        self.__train_correct_move.extend([data[1] for data in list_of_positions__correct_moves])

    def __load_model(self):
        return Model(self.size)
