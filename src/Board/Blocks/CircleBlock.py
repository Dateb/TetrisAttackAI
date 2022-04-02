import numpy as np

from src.Board.Blocks.Block import Block


class CircleBlock(Block):

    def color(self):
        return np.array([0, 255, 0])

    def array(self):
        return np.array([0, 0, 0, 0, 0, 1, 0])
