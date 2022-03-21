from dataclasses import dataclass
from typing import List

import numpy as np
from PIL import Image
from numpy import ndarray


@dataclass
class KeyPoint:

    x_coord: int
    y_coord: int


class StateExtractor:

    def __init__(self):
        self.__block_pixel_radius = 8
        self.__n_block_rows = 12
        self.__n_block_cols = 6

    def extract_cursor_corner_position(self, image) -> ndarray:
        cursor_position = np.zeros((1, 1))
        cursor_position[0] = np.argmax(image)
        return cursor_position

    def extract_pixel_distances_to_top(self, image_arr) -> ndarray:
        pixel_distances = np.zeros((6, 1))
        for col in range(self.__n_block_cols):
            x_coord = 2 * col * self.__block_pixel_radius + self.__block_pixel_radius
            pixels_of_col = image_arr[:, x_coord]
            print(pixels_of_col)

    def extract_key_point_values(self, image_arr) -> ndarray:
        key_point_values = np.zeros((self.__n_block_rows * self.__n_block_cols, 1))

        for i, key_point in enumerate(self.extract_key_points()):
            key_point_values[i] = image_arr[key_point.y_coord, key_point.x_coord]

        return key_point_values

    def extract_key_points(self) -> List[KeyPoint]:
        key_points = []
        for row in range(self.__n_block_rows):
            for col in range(self.__n_block_cols):
                key_points.append(self.__get_key_point(row, col))

        return key_points

    def __get_key_point(self, row: int, col: int):
        x_coord = 2 * col * self.__block_pixel_radius + self.__block_pixel_radius
        y_coord = 2 * row * self.__block_pixel_radius + self.__block_pixel_radius

        return KeyPoint(x_coord, y_coord)

