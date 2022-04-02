import numpy as np

from src.Board.Blocks.Block import Block


class StarBlock(Block):

    def color(self):
        return np.array([255, 255, 0])

    def array(self):
        return np.array([0, 1, 0, 0, 0, 0, 0])
