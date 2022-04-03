from copy import copy

from PIL import Image

from src.Board.Blocks.BlockPixel import BlockPixel
from src.Board.BoardConfiguration import BoardConfiguration
from src.Board.BoardImage import BoardImage


class StateImage:

    def __init__(self, board_image: BoardImage, board_configuration: BoardConfiguration):
        self.__array = copy(board_image.array)
        self.__board_configuration = board_configuration
        self.__build_state_image()
        self.__image = Image.fromarray(self.__array)

    def __build_state_image(self):
        radius = BlockPixel.RADIUS
        for pixel in self.__board_configuration.block_pixels:
            x_position = pixel.x_position
            y_position = pixel.y_position

            for i in range(-radius, radius):
                for j in range(-radius, radius):
                    self.__array[y_position + i, x_position + j] = pixel.block.color()

        print(self.__board_configuration.cursor_x_coordinate)
        self.__array[self.__board_configuration.cursor_y_coordinate, self.__board_configuration.cursor_x_coordinate] \
            = [255, 255, 255]

    @property
    def image(self):
        return self.__image

    @property
    def array(self):
        return self.__image

