from src.Board.Blocks.BackGroundBlock import BackGroundBlock
from src.Board.Blocks.Block import Block
from src.Board.Blocks.CircleBlock import CircleBlock
from src.Board.Blocks.DiamondBlock import DiamondBlock
from src.Board.Blocks.HeartBlock import HeartBlock
from src.Board.Blocks.LowerTriangleBlock import LowerTriangleBlock
from src.Board.Blocks.StarBlock import StarBlock
from src.Board.Blocks.UpperTriangleBlock import UpperTriangleBlock
from src.Board.BoardImage import BoardImage


class BlockPixel:

    RADIUS: int = 8
    LOW_THRESHOLD = 100
    HIGH_THRESHOLD = 100

    def __init__(self, board_image: BoardImage, board_row: int, board_column: int):
        self.x_position = 2 * board_column * self.RADIUS + self.RADIUS
        self.y_position = 2 * board_row * self.RADIUS + self.RADIUS

        self.color = board_image.array[self.y_position, self.x_position]

        self.red_color = self.color[0]
        self.blue_color = self.color[1]
        self.green_color = self.color[2]

        self.__block = self.__get_block_from_color()

    def __get_block_from_color(self) -> Block:
        if self.__is_heart(): return HeartBlock()
        if self.__is_diamond(): return DiamondBlock()
        if self.__is_upper_triangle(): return UpperTriangleBlock()
        if self.__is_lower_triangle(): return LowerTriangleBlock()
        if self.__is_circle(): return CircleBlock()
        if self.__is_star(): return StarBlock()
        return BackGroundBlock()

    def __is_heart(self):
        return self.is_red_high and self.is_green_low and self.is_blue_low

    def __is_diamond(self):
        return self.is_red_high and self.is_green_low and self.is_blue_high

    def __is_upper_triangle(self):
        return self.is_red_low and self.is_green_high and self.is_blue_high

    def __is_lower_triangle(self):
        return self.is_red_low and self.is_green_low and self.is_blue_high

    def __is_circle(self):
        return self.is_red_low and self.is_green_high and self.is_blue_low

    def __is_star(self):
        return self.is_red_high and self.is_green_high and self.is_blue_low

    @property
    def is_red_low(self):
        return self.red_color <= self.LOW_THRESHOLD

    @property
    def is_red_high(self):
        return self.red_color >= self.HIGH_THRESHOLD

    @property
    def is_blue_low(self):
        return self.blue_color <= self.LOW_THRESHOLD

    @property
    def is_blue_high(self):
        return self.blue_color >= self.HIGH_THRESHOLD

    @property
    def is_green_low(self):
        return self.green_color <= self.LOW_THRESHOLD

    @property
    def is_green_high(self):
        return self.green_color >= self.HIGH_THRESHOLD

    @property
    def block(self):
        return self.__block
