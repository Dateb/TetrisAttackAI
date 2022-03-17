import PIL
import numpy as np
from PIL import Image
from rl.core import Processor


#if self.processor is not None:
#    action = self.processor.process_action(action)

class TetrisAttackProcessor(Processor):

    def __init__(self, n_actions: int):
        super(TetrisAttackProcessor, self).__init__()
        self.__n_actions = n_actions

    def process_observation(self, observation):
        img_arr = observation
        img_arr = img_arr[20:215, 86:286]
        im = Image.fromarray(img_arr)
        im = im.resize((80, 80))
        im.save("example.jpeg")
        return np.asarray(PIL.Image.open("example.jpeg"))

    def process_action(self, action):
        actions = np.zeros(self.__n_actions)
        actions[action] = 1
        return actions
