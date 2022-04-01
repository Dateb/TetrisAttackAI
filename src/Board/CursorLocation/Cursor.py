import numpy as np


class Cursor:

    SIZE: int = 2

    def __init__(self, x_position: int, y_position: int):
        self.__x_position = x_position
        self.__y_position = y_position

    @property
    def array(self):
        return np.array([self.__x_position, self.__y_position])
