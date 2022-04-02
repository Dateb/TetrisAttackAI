import numpy as np

from src.Board.Blocks.Block import Block


class DiamondBlock(Block):

    def color(self):
        return np.array([255, 0, 255])

    def array(self):
        return np.array([0, 0, 1, 0, 0, 0, 0])
