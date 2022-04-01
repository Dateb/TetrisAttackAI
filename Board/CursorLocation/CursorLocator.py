from typing import Tuple

import numpy as np
from PIL import Image
from numpy import ndarray

from Board.CursorLocation.CursorFilter import CursorFilter


class CursorLocator:

    def __init__(self):
        self.__cursor_filters = []

        self.__cursor_filters.append(CursorFilter(-1, -1, check_neighbor_for_high_value=False))
        self.__cursor_filters.append(CursorFilter(0, -1, check_neighbor_for_high_value=True))
        self.__cursor_filters.append(CursorFilter(1, -1, check_neighbor_for_high_value=True))

        self.__cursor_filters.append(CursorFilter(-1, 0, check_neighbor_for_high_value=False))
        self.__cursor_filters.append(CursorFilter(1, 0, check_neighbor_for_high_value=True))

        self.__cursor_filters.append(CursorFilter(-1, 1, check_neighbor_for_high_value=False))
        self.__cursor_filters.append(CursorFilter(0, 1, check_neighbor_for_high_value=False))
        self.__cursor_filters.append(CursorFilter(1, 1, check_neighbor_for_high_value=False))

        self.__cursor_filters.append(CursorFilter(9, 0, check_neighbor_for_high_value=True))
        self.__cursor_filters.append(CursorFilter(10, 0, check_neighbor_for_high_value=False))

        self.__cursor_filters.append(CursorFilter(5, 4, check_neighbor_for_high_value=True))
        self.__cursor_filters.append(CursorFilter(5, 5, check_neighbor_for_high_value=False))

    def get_coordinates(self, image: ndarray) -> Tuple[int, int]:
        potential_positions = np.argwhere((240 <= image) & (image <= 255))

        potential_positions_idx = [i for i in range(potential_positions.shape[0])]
        for i in range(potential_positions.shape[0]):
            x_position = potential_positions[i][1]
            y_position = potential_positions[i][0]
            for cursor_filter in self.__cursor_filters:
                if cursor_filter.is_neighbor_filtered(image, x_position, y_position):
                    potential_positions_idx.remove(i)
                    break

        if len(potential_positions_idx) == 1:
            cursor_y_coordinate = potential_positions[potential_positions_idx[0]][0]
            cursor_x_coordinate = potential_positions[potential_positions_idx[0]][1]
        else:
            Image.fromarray(image).save(f"failed_{len(potential_positions_idx)}.jpeg")
            cursor_y_coordinate = -1
            cursor_x_coordinate = -1

        return cursor_x_coordinate, cursor_y_coordinate
