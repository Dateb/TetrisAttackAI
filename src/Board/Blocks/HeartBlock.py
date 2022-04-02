import numpy as np

from src.Board.Blocks.Block import Block


class HeartBlock(Block):

    def color(self):
        return np.array([255, 0, 0])

    def array(self):
        return np.array([1, 0, 0, 0, 0, 0, 0])
