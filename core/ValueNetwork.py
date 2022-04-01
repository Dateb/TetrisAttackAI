from keras import Sequential
from keras.layers import Permute, Flatten, Dense, Activation

from Board.BoardConfiguration import BoardConfiguration


class ValueNetwork:

    def __init__(self, n_actions: int, n_input_frames: int):
        self.__n_actions = n_actions
        self.__n_input_frames = n_input_frames
        self.__init_model()

    def __init_model(self) -> None:
        self.__model = Sequential()

        self.__model.add(Permute((2, 1), input_shape=(self.__n_input_frames, BoardConfiguration.TOTAL_SIZE)))
        self.__model.add(Flatten())
        self.__model.add(Dense(1024, name="dense_a"))
        self.__model.add(Activation('relu'))
        self.__model.add(Dense(512, name="dense_b"))
        self.__model.add(Activation('relu'))
        self.__model.add(Dense(256, name="dense_c"))
        self.__model.add(Activation('relu'))
        self.__model.add(Dense(128, name="dense_d"))
        self.__model.add(Activation('relu'))
        self.__model.add(Dense(self.__n_actions, name="dense_e"))
        self.__model.add(Activation('linear'))

    @property
    def model(self):
        return self.__model
