from numpy import ndarray


class CursorFilter:

    HIGH_VALUE_THRESHOLD = 240

    def __init__(self, neighbor_x_offset: int, neighbor_y_offset: int,
                 check_neighbor_for_high_value: bool):
        self.__image_height = 0
        self.__image_width = 0
        self.__neighbor_x_offset = neighbor_x_offset
        self.__neighbor_y_offset = neighbor_y_offset
        self.__check_neighbor_for_high_value = check_neighbor_for_high_value

    def is_neighbor_filtered(self, image, x_position: int, y_position) -> bool:
        self.__image_height = image.shape[0]
        self.__image_width = image.shape[1]

        neighbor_x_position = x_position + self.__neighbor_x_offset
        neighbor_y_position = y_position + self.__neighbor_y_offset

        if self.__is_neighbor_out_of_bounds(neighbor_x_position, neighbor_y_position):
            return True

        if self.__check_neighbor_for_high_value:
            return not self.__has_neighbor_high_value(image, neighbor_x_position, neighbor_y_position)
        else:
            return not self.__has_neighbor_low_value(image, neighbor_x_position, neighbor_y_position)

    def __has_neighbor_high_value(self, image: ndarray, neighbor_x_position, neighbor_y_position):
        return self.HIGH_VALUE_THRESHOLD <= image[neighbor_y_position, neighbor_x_position]

    def __has_neighbor_low_value(self, image: ndarray, neighbor_x_position, neighbor_y_position):
        return image[neighbor_y_position, neighbor_x_position] < self.HIGH_VALUE_THRESHOLD

    def __is_neighbor_out_of_bounds(self, neighbor_x_position, neighbor_y_position):
        return (neighbor_x_position >= self.__image_width or neighbor_x_position < 0) or \
               (neighbor_y_position >= self.__image_height or neighbor_y_position < 0)
