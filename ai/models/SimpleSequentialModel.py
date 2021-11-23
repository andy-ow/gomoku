from keras import Model
from sklearn.model_selection import train_test_split

from ai.AiModel import AiModel
from ai.Types import Action
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class SimpleSequentialModel(AiModel):
    def __init__(self, size):
        self.size_x, self.size_y = size
        self.model = self.create_model()
        print(self.model.summary())

    def train(self, _train_position, _train_correct_move):
        x_train, x_test, y_train, y_test = train_test_split(_train_position, _train_correct_move, test_size = 0.2)
        for data in [x_train, x_test, y_train, y_test]:
            data = data.astype("float32")
        print("Fit model on training data")
        history = self.model.fit(
            x_train,
            y_train,
            batch_size=64,
            epochs=20,
            # We pass some validation for
            # monitoring validation loss and metrics
            # at the end of each epoch
            validation_data=(x_test, y_test),
        )

    def predict(self, game_state) -> Action:
        predictions_matrix = self.model.predict(game_state)
        
        return Action((1,1))

    def create_model(self) -> Model:
        model = keras.Sequential()
        model.add(keras.Input(shape=(self.size_x, self.size_y, 2)))  # 250x250 RGB images
        model.add(layers.Conv2D(filters=10, kernel_size=5, padding='same', activation="relu"))
        model.add(layers.Conv2D(filters=10, kernel_size=5, padding='same', activation="relu"))
        model.add(layers.Conv2D(filters=10, kernel_size=5, padding='same', activation="relu"))
        model.compile(
            optimizer=keras.optimizers.RMSprop(),  # Optimizer
            # Loss function to minimize
            loss=keras.losses.SparseCategoricalCrossentropy(),
            # List of metrics to monitor
            metrics=[keras.metrics.SparseCategoricalAccuracy()],
        )
        return model
