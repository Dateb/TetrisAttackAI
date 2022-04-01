from enum import Enum

import numpy as np

from Board.BlockLocations.BlockPixel import BlockPixel


class BlockType(Enum):
    STAR = 0
    HEART = 1
    TRIANGLE = 2
    CIRCLE = 3
    DIAMOND = 4
    BACKGROUND = 5


class Block:

    HEART_LOW = 62
    HEART_HIGH = 89

    DIAMOND_LOW = 95
    DIAMOND_HIGH = 109

    TRIANGLE_LOW = 170
    TRIANGLE_HIGH = 190

    CIRCLE_LOW = 128
    CIRCLE_HIGH = 162

    STAR_LOW = 211
    STAR_HIGH = 254

    def __init__(self, pixel: BlockPixel):
        self.__pixel = pixel
        self.__type = self.__map_color_to_type()

        self.__array = np.zeros(6)
        self.__array[self.__type.value] = 1

    def __map_color_to_type(self):
        color = self.__pixel.color
        if self.HEART_LOW    <= color <= self.HEART_HIGH:    return BlockType.HEART
        if self.DIAMOND_LOW  <= color <= self.DIAMOND_HIGH:  return BlockType.DIAMOND
        if self.TRIANGLE_LOW <= color <= self.TRIANGLE_HIGH: return BlockType.TRIANGLE
        if self.CIRCLE_LOW   <= color <= self.CIRCLE_HIGH:   return BlockType.CIRCLE
        if self.STAR_LOW     <= color <= self.STAR_HIGH:     return BlockType.STAR
        return BlockType.BACKGROUND

    @property
    def array(self):
        return self.__array




