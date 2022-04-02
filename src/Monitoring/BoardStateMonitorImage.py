import numpy as np
from PIL import Image

from src.Board.BoardImage import BoardImage
from src.Monitoring.StateImage import StateImage


class BoardStateMonitorImage:

    def __init__(self, board_image: BoardImage, state_image: StateImage):
        board_array = board_image.array
        state_array = state_image.array

        board_state_monitor_array = np.hstack((board_array, state_array))
        self.__image = Image.fromarray(board_state_monitor_array)

    @property
    def image(self):
        return self.__image
