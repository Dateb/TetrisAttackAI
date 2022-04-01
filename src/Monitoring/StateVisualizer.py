from copy import copy

from PIL import Image


class StateVisualizer:

    def __init__(self, state_extractor: StateExtractor):
        self.__state_extractor = state_extractor

    def visualize_key_points(self, image_arr):
        image_arr = copy(image_arr)
        for i, key_point in enumerate(self.__state_extractor.key_points):
            image_arr[key_point.y_coord, key_point.x_coord] = 255

        im = Image.fromarray(image_arr)
        im.save("board_marked_key_points.jpeg")

    def visualize_cursor_position(self, image_arr):
        image_arr = copy(image_arr)
        cursor_position = self.__state_extractor.extract_cursor_position(image_arr)

        image_arr[:, :] = 0
        image_arr[int(cursor_position[1]), int(cursor_position[0])] = 255

        im = Image.fromarray(image_arr)
        im.save("board_marked_cursor_position.jpeg")
