from abc import ABC, abstractmethod

from ai.Types import Action
import tensorflow as tf

class AiModel(ABC):

    @abstractmethod
    def __init__(self, size):
        self.size_x, self.size_y = size

    @abstractmethod
    def train(self, __train_position , __train_correct_move):
        pass

    @abstractmethod
    def predict(self, game_state) -> Action:
        pass

    def create_move_xy_onehot_translation(self, size_x, size_y):
        translate_move_xy_to_onehot, translate_move_xy1D_to_xy = {}, {}
        for x in range(size_x):
            for y in range(size_y):
                onehot = tf.keras.utils.to_categorical(int(x*self.size_y+y), num_classes=size_x*size_y)
                translate_move_xy_to_onehot[(x,y)] = onehot
                number1D = onehot.argmax()
                # print((x, y), onehot, number1D)
                translate_move_xy1D_to_xy[number1D] = (x,y)
        return translate_move_xy_to_onehot, translate_move_xy1D_to_xy