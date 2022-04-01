from enum import Enum

import numpy as np

from src.Board.BlockLocations.BlockPixel import BlockPixel


class BlockType(Enum):
    STAR = 0
    HEART = 1
    UPPER_TRIANGLE = 2
    LOWER_TRIANGLE = 3
    CIRCLE = 4
    DIAMOND = 5
    BACKGROUND = 6


class Block:

    def __init__(self, pixel: BlockPixel):
        self.__pixel = pixel
        self.__type = self.__map_color_to_type()

        self.__array = np.zeros(len(BlockType))
        self.__array[self.__type.value] = 1

    def __map_color_to_type(self):
        if self.__is_heart(): return BlockType.HEART
        if self.__is_diamond(): return BlockType.DIAMOND
        if self.__is_upper_triangle(): return BlockType.UPPER_TRIANGLE
        if self.__is_lower_triangle(): return BlockType.LOWER_TRIANGLE
        if self.__is_circle(): return BlockType.CIRCLE
        if self.__is_star(): return BlockType.STAR
        return BlockType.BACKGROUND

    def __is_heart(self):
        return self.__pixel.is_red_high and self.__pixel.is_green_low and self.__pixel.is_blue_low

    def __is_diamond(self):
        return self.__pixel.is_red_high and self.__pixel.is_green_low and self.__pixel.is_blue_high

    def __is_upper_triangle(self):
        return self.__pixel.is_red_low and self.__pixel.is_green_high and self.__pixel.is_blue_high

    def __is_lower_triangle(self):
        return self.__pixel.is_red_low and self.__pixel.is_green_low and self.__pixel.is_blue_high

    def __is_circle(self):
        return self.__pixel.is_red_low and self.__pixel.is_green_high and self.__pixel.is_blue_low

    def __is_star(self):
        return self.__pixel.is_red_high and self.__pixel.is_green_high and self.__pixel.is_blue_low

    @property
    def type(self):
        return self.__type

    @property
    def array(self):
        return self.__array




