from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
from PIL import Image
from numpy import ndarray


@dataclass
class KeyPoint:

    x_coord: int
    y_coord: int


class StateExtractor:

    def __init__(self):
        self.__last_state = None
        self.__last_processed_image = None
        self.__block_pixel_radius = 8
        self.__n_block_rows = 12
        self.__n_block_cols = 6

        self.__key_points = self.__extract_key_points()
        self.__successful_cursor_extractions = 0
        self.__n_extractions = 0

        self.__board_x_start = 88
        self.__board_x_end = 185
        self.__board_y_start = 22
        self.__board_y_end = 215

    def create_state(self, observation, info):
        board_image = self.__get_board_image(observation)
        board_image.save("board_prev.jpeg")

        board_image = self.__transform_board_rgb_to_grayscale(board_image)
        board_image.save("board.jpeg")

        self.__last_processed_image = np.asarray(board_image)

        #self.__state_visualizer.visualize_key_points(self.__im_arr)
        #self.__state_visualizer.visualize_cursor_position(self.__im_arr)

        # start = timeit.default_timer()
        cursor_corner_position = self.extract_cursor_position(self.__last_processed_image)
        # stop = timeit.default_timer()

        # print('Time(cursor): ', stop - start)

        # start = timeit.default_timer()
        key_points = self.extract_key_point_values(self.__last_processed_image)
        # stop = timeit.default_timer()

        # print('Time(blocks): ', stop - start)

        speed = np.array([[info["speed"]]])
        self.__last_state = np.concatenate((cursor_corner_position, key_points, speed))

    def __get_board_image(self, observation):
        return Image.fromarray(
            observation[self.__board_y_start:self.__board_y_end, self.__board_x_start:self.__board_x_end]
        )

    def __transform_board_rgb_to_grayscale(self, board_image):
        r, g, b = board_image.split()

        r = r.point(lambda i: int(i / 200) * 255)

        g = g.point(lambda i: int(i / 200) * 255)

        b = b.point(lambda i: int(i / 200) * 255)

        # Recombine back to RGB image
        board_image = Image.merge('RGB', (r, g, b))
        board_image = board_image.convert('L')

        return board_image

    def __extract_key_points(self) -> List[KeyPoint]:
        key_points = []
        for row in range(self.__n_block_rows):
            for col in range(self.__n_block_cols):
                key_points.append(self.__get_key_point(row, col))

        return key_points

    def __get_key_point(self, row: int, col: int):
        x_coord = 2 * col * self.__block_pixel_radius + self.__block_pixel_radius
        y_coord = 2 * row * self.__block_pixel_radius + self.__block_pixel_radius

        return KeyPoint(x_coord, y_coord)

    def extract_cursor_position(self, image) -> ndarray:
        cursor_value = np.zeros((2, 1))
        white_positions = np.argwhere(image == 255)
        image_width = image.shape[1]

        white_positions_idx = [i for i in range(white_positions.shape[0])]
        for i in range(white_positions.shape[0]):
            # Condition 1:
            x_coord_neighbor = white_positions[i][1] + 31
            y_coord_neighbor = white_positions[i][0]

            if x_coord_neighbor >= image_width:
                white_positions_idx.remove(i)
                continue
            if image[y_coord_neighbor, x_coord_neighbor] != 255:
                white_positions_idx.remove(i)
                continue

            # Condition 2:
            x_coord_neighbor = white_positions[i][1]
            y_coord_neighbor = white_positions[i][0] - 1

            if y_coord_neighbor < 0:
                white_positions_idx.remove(i)
                continue

            if image[y_coord_neighbor, x_coord_neighbor] == 255:
                white_positions_idx.remove(i)
                continue

            # Condition 3:
            x_coord_neighbor = white_positions[i][1]
            y_coord_neighbor = white_positions[i][0] - 14

            if y_coord_neighbor < 0:
                white_positions_idx.remove(i)
                continue

            if image[y_coord_neighbor, x_coord_neighbor] != 255:
                white_positions_idx.remove(i)
                continue

        if len(white_positions_idx) == 1:
            self.__successful_cursor_extractions += 1
            cursor_value[1] = white_positions[white_positions_idx[0]][0]
            cursor_value[0] = white_positions[white_positions_idx[0]][1]
        else:
            cursor_value[1] = -1
            cursor_value[0] = -1

        self.__n_extractions += 1

        return cursor_value

    def extract_pixel_distances_to_top(self, image_arr) -> ndarray:
        pixel_distances = np.zeros((6, 1))
        for col in range(self.__n_block_cols):
            x_coord = 2 * col * self.__block_pixel_radius + self.__block_pixel_radius
            pixels_of_col = image_arr[:, x_coord]
            print(pixels_of_col)

    def extract_key_point_values(self, image_arr) -> ndarray:
        key_point_values = np.zeros((self.__n_block_rows * self.__n_block_cols, 1))

        for i, key_point in enumerate(self.__key_points):
            key_point_values[i] = image_arr[key_point.y_coord, key_point.x_coord]

        return key_point_values

    @property
    def key_points(self) -> List[KeyPoint]:
        return self.__key_points

    @property
    def last_state(self):
        return self.__last_state

    @property
    def last_processed_image(self):
        return self.__last_processed_image

