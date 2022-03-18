import numpy as np
from rl.core import Processor


#if self.processor is not None:
#    action = self.processor.process_action(action)
from StateExtractor import StateExtractor

import timeit

class TetrisAttackProcessor(Processor):

    def __init__(self, n_actions: int):
        super(TetrisAttackProcessor, self).__init__()
        self.__n_actions = n_actions
        self.__state_extractor = StateExtractor()

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

        features = np.concatenate((cursor_corner_position, key_points))

        return features

    def process_action(self, action):
        actions = np.zeros(self.__n_actions)
        actions[action] = 1
        return actions
