import numpy as np

from Board.BlockLocations.Block import Block
from Board.BlockLocations.BlockPixel import BlockPixel
from Board.BoardImage import BoardImage
from Board.CursorLocation.CursorLocator import CursorLocator


class BoardConfiguration:

    BLOCKS_PER_ROW = 6
    BLOCKS_PER_COLUMN = 12
    N_BLOCK_TYPES = 5

    CURSOR_SIZE: int = BLOCKS_PER_ROW * BLOCKS_PER_COLUMN
    BLOCKS_SIZE: int = BLOCKS_PER_ROW * BLOCKS_PER_COLUMN * (N_BLOCK_TYPES + 1)
    TOTAL_SIZE: int = CURSOR_SIZE + BLOCKS_SIZE

    def __init__(self, board_image: BoardImage):
        self.__board_image = board_image

        self.__block_pixels = [
            BlockPixel(board_image, board_row, board_column)
            for board_row in range(self.BLOCKS_PER_COLUMN)
            for board_column in range(self.BLOCKS_PER_ROW)
        ]
        self.__blocks = [Block(pixel) for pixel in self.__block_pixels]
        self.__blocks_array = np.concatenate([block.array for block in self.__blocks])

        cursor_x_coordinate, cursor_y_coordinate = CursorLocator().get_coordinates(board_image.array)
        self.__map_cursor_coordinates(cursor_x_coordinate, cursor_y_coordinate)
        
        self.__configuration_array = np.concatenate((self.__blocks_array, self.__cursor_array))

    def __map_cursor_coordinates(self, cursor_x_coordinate: int, cursor_y_coordinate: int):
        self.__cursor_array = np.zeros((self.BLOCKS_PER_ROW, self.BLOCKS_PER_COLUMN))
        if cursor_x_coordinate == -1 or cursor_y_coordinate == -1:
            self.__cursor_array = self.__cursor_array.flatten()
            return

        block_width = self.__board_image.width / self.BLOCKS_PER_ROW
        block_height = self.__board_image.height / self.BLOCKS_PER_COLUMN

        cursor_x_block_position = int(cursor_x_coordinate / block_width)
        cursor_y_block_position = int(cursor_y_coordinate / block_height)

        self.__cursor_array[cursor_x_block_position, cursor_y_block_position] = 1
        self.__cursor_array = self.__cursor_array.flatten()

    @property
    def array(self):
        return self.__configuration_array

