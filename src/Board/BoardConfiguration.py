import numpy as np

from src.Board.BlockLocations.Block import Block, BlockType
from src.Board.BlockLocations.BlockPixel import BlockPixel
from src.Board.BoardImage import BoardImage
from src.Board.CursorLocation.CursorLocator import CursorLocator


class BoardConfiguration:

    BLOCKS_PER_ROW = 6
    BLOCKS_PER_COLUMN = 12
    N_BLOCK_TYPES = len(BlockType)

    CURSOR_SIZE: int = BLOCKS_PER_ROW * BLOCKS_PER_COLUMN
    BLOCKS_SIZE: int = BLOCKS_PER_ROW * BLOCKS_PER_COLUMN * N_BLOCK_TYPES
    TOTAL_SIZE: int = CURSOR_SIZE + BLOCKS_SIZE

    def __init__(self, board_image: BoardImage, cursor_locator: CursorLocator):
        self.__board_image = board_image
        self.__cursor_locator = cursor_locator

        self.__build_blocks_array()
        self.__build_cursor_array()
        
        self.__configuration_array = np.concatenate((self.__blocks_array, self.__cursor_array))

    def __build_blocks_array(self):
        blocks = [[0 for _ in range(self.BLOCKS_PER_COLUMN)] for _ in range(self.BLOCKS_PER_ROW)]
        self.__blocks_array = np.zeros((self.BLOCKS_PER_ROW, self.BLOCKS_PER_COLUMN, len(BlockType)))
        for i in range(self.BLOCKS_PER_ROW):
            for j in range(self.BLOCKS_PER_COLUMN):
                block = Block(BlockPixel(self.__board_image, j, i))
                blocks[i][j] = block
                self.__blocks_array[i, j, :] = block.array
        self.__blocks_array = self.__blocks_array.flatten()

    def __build_cursor_array(self):
        self.__cursor_array = np.zeros((self.BLOCKS_PER_ROW, self.BLOCKS_PER_COLUMN))

        cursor_x_coordinate, cursor_y_coordinate = self.__cursor_locator.get_coordinates(self.__board_image.array)
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

