import os

import numpy as np
from keras import Model
from sklearn.model_selection import train_test_split

from ai.AiModel import AiModel
from ai.Types import Action
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class SimpleSequentialModel(AiModel):

    @staticmethod
    def model_name():
        return "A"

    def __init__(self, size, epochs, layers_no, filters_no, kernel_size):
        # os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        self.size_x, self.size_y = size
        self.translate_move_xy_to_onehot, self.translate_move_xy1D_to_xy = self.create_move_xy_onehot_translation(self.size_x, self.size_y)
        self.epochs = epochs
        self.layers_no = layers_no
        self.filers_no = filters_no
        self.kernel_size = kernel_size
        self.model = self.create_model()
        self.model.summary()

    def train(self, _train_position: np.ndarray, _train_correct_move_xy: np.ndarray):
        # _train_correct_move = np.array(list(map(lambda z: tf.keras.utils.to_categorical(int(z[0]*self.size_y+z[1]), num_classes=81), _train_correct_move_xy)))
        _train_correct_move = np.array(list(map(lambda z: self.translate_move_xy_to_onehot[z], _train_correct_move_xy)))
        _train_position = np.array(_train_position)
        # print("Fit model on training data")
        # print(len(_train_position))
        history = self.model.fit(
            _train_position,
            _train_correct_move,
            batch_size=256,
            epochs=self.epochs,
            # We pass some validation for
            # monitoring validation loss and metrics
            # at the end of each epoch
            # validation_data=(x_test, y_test),
        )

    def predict(self, game_state) -> Action:
        predictions_matrix = self.model.predict(game_state)
        # original_shape = predictions_matrix.shape
        flat_matrix = predictions_matrix.reshape((1, self.size_x*self.size_y))/(predictions_matrix.sum()+0.00000001)
        randomly_chosen_number = tf.random.categorical(tf.math.log(flat_matrix), 1).numpy()[0][0]
        # print(randomly_chosen_number, flat_matrix[[0],randomly_chosen_number])
        # x = randomly_chosen_number // self.size_y
        # y = randomly_chosen_number % self.size_y
        (x,y) = self.translate_move_xy1D_to_xy[randomly_chosen_number]
        return Action((x,y))

    def create_model(self) -> Model:
        model = keras.Sequential()
        model.add(keras.Input(shape=[self.size_x, self.size_y, 2]))
        for i in range(self.layers_no):
            model.add(layers.Conv2D(filters=self.filers_no, kernel_size=self.kernel_size, padding='same', activation="relu"))
        model.add(layers.Conv2D(filters=1, kernel_size=1, padding='same'))
        model.add(layers.Flatten())
        # model.add(layers.Dense(361))
        model.add(layers.Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        """model.compile(
            optimizer=keras.optimizers.RMSprop(),  # Optimizer
            # Loss function to minimize
            loss=keras.losses.SparseCategoricalCrossentropy(),
            # List of metrics to monitor
            metrics=[keras.metrics.SparseCategoricalCrossentropy()],
        )"""
        return model


