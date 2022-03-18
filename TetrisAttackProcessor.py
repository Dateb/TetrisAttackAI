import PIL
import numpy as np
from PIL import Image
from rl.core import Processor


#if self.processor is not None:
#    action = self.processor.process_action(action)
from StateExtractor import StateExtractor


class TetrisAttackProcessor(Processor):

    def __init__(self, n_actions: int):
        super(TetrisAttackProcessor, self).__init__()
        self.__n_actions = n_actions
        self.__state_extractor = StateExtractor()

    def process_observation(self, observation):
        img_arr = observation
        img_arr = img_arr[22:215, 88:185]

        key_points = self.__state_extractor.extract_board_state_key_points(img_arr)
        print(key_points)

        im = Image.fromarray(img_arr)
        #im = im.resize((80, 80))
        im.save("example.jpeg")
        return np.asarray(PIL.Image.open("example.jpeg"))

    def process_action(self, action):
        actions = np.zeros(self.__n_actions)
        actions[action] = 1
        return actions
