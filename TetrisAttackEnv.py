import numpy as np
import retro

from StateExtractor import StateExtractor
from StateVisualizer import StateVisualizer


class TetrisAttackEnv:

    def __init__(self):
        game = 'TetrisAttack-Snes'
        state = retro.State.DEFAULT
        self.__env = retro.make(game, state, record='./replays', scenario=None)

        self.__state_extractor = StateExtractor()
        self.__state_visualizer = StateVisualizer(self.__state_extractor)
        self.__current_speed = 1.0
        self.__n_actions = self.__env.action_space.shape[0]

    def step(self, action):
        action = self.__process_action(action)
        obs, rew, done, info = self.__env.step(action)

        self.__state_extractor.create_state(obs, info)

        return self.__state_extractor.last_state, self.__process_reward(), done, info

    def __process_reward(self):
        free_board_amount = (len(np.argwhere(self.__state_extractor.last_processed_image == 0)) / 2)
        board_size = self.__state_extractor.last_processed_image.shape[0] * self.__state_extractor.last_processed_image.shape[1]
        free_board_proportion = free_board_amount / board_size

        return free_board_proportion

    def __process_action(self, action):
        actions = np.zeros(self.__n_actions)
        if self.__moved_blocks_up(action):
            action = 0

        actions[action] = 1
        return actions

    def __moved_blocks_up(self, action):
        return action in [self.__n_actions - 1, self.__n_actions - 2]

    def reset(self):
        self.__state_extractor.create_state(self.__env.reset(), {"speed": 1})
        self.__current_speed = 1
        return self.__state_extractor.last_state

    def render(self, mode: str = "human", close: bool = "False"):
        return 0

    @property
    def action_space(self):
        return self.__env.action_space

