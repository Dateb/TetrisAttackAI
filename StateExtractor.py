import numpy as np
from PIL import Image
from numpy import ndarray


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

    def extract_board_state_key_points(self, image_arr) -> ndarray:
        key_points = np.zeros((self.__n_block_rows * self.__n_block_cols, 1))

        image = Image.fromarray(image_arr)
        image_hsv = image.convert("HSV")
        image_arr = np.asarray(image_hsv)

        for row in range(self.__n_block_rows):
            for col in range(self.__n_block_cols):
                idx = (row * self.__n_block_cols) + col
                key_points[idx] = self.__get_block_value_of_key_point(image_arr, row, col)

        return key_points

    def __get_block_value_of_key_point(self, image_arr, row: int, col: int):
        x_coord = 2 * col * self.__block_pixel_radius + self.__block_pixel_radius
        y_coord = 2 * row * self.__block_pixel_radius + self.__block_pixel_radius

        return image_arr[y_coord, x_coord][0]

