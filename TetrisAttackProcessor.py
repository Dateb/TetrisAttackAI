from math import floor

import numpy as np
from PIL import Image
from rl.core import Processor
from StateExtractor import StateExtractor

import timeit


class TetrisAttackProcessor(Processor):

    def __init__(self):
        super(TetrisAttackProcessor, self).__init__()
        self.__state_extractor = StateExtractor()
        self.__current_speed = 1.0
        self.__n_actions = 0

    def process_observation(self, observation):
        im_arr = observation
        im_arr = im_arr[22:215, 88:185]
        im = Image.fromarray(im_arr)
        im.save("board_prev.jpeg")

        r, g, b = im.split()

        r = r.point(lambda i: int(i / 200) * 255)

        g = g.point(lambda i: int(i / 200) * 255)

        b = b.point(lambda i: int(i / 200) * 255)

        # Recombine back to RGB image
        result = Image.merge('RGB', (r, g, b))
        result = result.convert('L')
        result.save("board.jpeg")
        im_arr = np.asarray(result)

        #start = timeit.default_timer()
        cursor_corner_position = self.__state_extractor.extract_cursor_corner_position(im_arr)
        #stop = timeit.default_timer()

        #print('Time(cursor): ', stop - start)

        #start = timeit.default_timer()
        key_points = self.__state_extractor.extract_key_point_values(im_arr)
        #stop = timeit.default_timer()

        #print('Time(blocks): ', stop - start)

        speed_arr = np.zeros((1, 1))
        speed_arr[0] = self.__current_speed
        features = np.concatenate((cursor_corner_position, key_points, speed_arr))

        return features

    def process_action(self, action):
        actions = np.zeros(self.__n_actions)
        if self.__moved_blocks_up(action):
            action = 0

        actions[action] = 1
        return actions

    def set_current_speed(self, speed: float):
        self.__current_speed = speed

    def set_n_actions(self, n_actions: int):
        self.__n_actions = n_actions

    @property
    def current_speed(self):
        return self.__current_speed

    def __moved_blocks_up(self, action):
        return action in [self.__n_actions - 1, self.__n_actions - 2]
