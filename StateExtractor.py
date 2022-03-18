from typing import List

import numpy as np
from numpy import ndarray

from BlockType import BlockType


class StateExtractor:

    def __init__(self):
        self.__block_pixel_radius = 8
        self.__n_block_rows = 12
        self.__n_block_cols = 6

    def extract_cursor_corner_position(self, image) -> ndarray:
        color_sum_image = np.sum(image, axis=2)
        cursor_position = np.zeros((1, 1))
        cursor_position[0] = np.argmax(color_sum_image)
        return cursor_position

    def extract_board_state_key_points(self, image) -> ndarray:
        key_points = np.zeros((self.__n_block_rows * self.__n_block_cols, 1))

        for row in range(self.__n_block_rows):
            for col in range(self.__n_block_cols):
                idx = (row * self.__n_block_cols) + col
                key_points[idx] = self.__get_block_value_of_key_point(image, row, col)

        return key_points

    def __get_block_value_of_key_point(self, image, row: int, col: int):
        x_coord = 2 * col * self.__block_pixel_radius + self.__block_pixel_radius
        y_coord = 2 * row * self.__block_pixel_radius + self.__block_pixel_radius

        return self.__get_block_type_of_rgb_values(image[y_coord, x_coord]).value

    def __get_block_type_of_rgb_values(self, rgb_values: List[int]) -> BlockType:
        red_value, green_value, blue_value = rgb_values
        color_threshold = 240
        if red_value > color_threshold and green_value > color_threshold:
            return BlockType.STAR
        if red_value > color_threshold and blue_value > color_threshold:
            return BlockType.DIAMOND
        if green_value > color_threshold and blue_value > color_threshold:
            return BlockType.TRIANGLE
        if red_value > color_threshold:
            return BlockType.HEART
        if green_value > color_threshold:
            return BlockType.CIRCLE
        return BlockType.BACKGROUND

