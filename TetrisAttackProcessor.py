import numpy as np
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
        img_arr = observation
        img_arr = img_arr[22:215, 88:185]

        start = timeit.default_timer()
        cursor_corner_position = self.__state_extractor.extract_cursor_corner_position(img_arr)
        stop = timeit.default_timer()

        #print('Time(cursor): ', stop - start)

        start = timeit.default_timer()
        key_points = self.__state_extractor.extract_board_state_key_points(img_arr)
        stop = timeit.default_timer()

        #print('Time(blocks): ', stop - start)

        speed_arr = np.zeros((1, 1))
        speed_arr[0] = self.__current_speed
        features = np.concatenate((cursor_corner_position, key_points, speed_arr))

        return features

    def process_action(self, action):
        actions = np.zeros(self.__n_actions)
        actions[action] = 1
        return actions

    def set_current_speed(self, speed: float):
        self.__current_speed = speed

    def set_n_actions(self, n_actions: int):
        self.__n_actions = n_actions
