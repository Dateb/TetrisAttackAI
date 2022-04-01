import timeit

import numpy as np
import retro

from Board.BoardConfiguration import BoardConfiguration
from Board.BoardImage import BoardImage
from Board.CursorLocation.CursorLocator import CursorLocator


class TetrisAttackEnv:

    def __init__(self):
        self.__cursor_locator = CursorLocator()
        self.__total_cursors = 0
        self.__failed_cursors = 0
        game = 'TetrisAttack-Snes'
        state = retro.State.DEFAULT

        self.__env = retro.make(game, state, record='./replays', scenario=None)
        self.__n_actions = self.__env.action_space.shape[0]

    def step(self, action):
        action = self.__process_action(action)
        game_image, rew, done, info = self.__env.step(action)

        rew = 1
        if done:
            rew = 0

        board_image = BoardImage(game_image)
        board_configuration = BoardConfiguration(board_image, self.__cursor_locator)

        return board_configuration.array, rew, done, info

    def __process_action(self, action):
        actions = np.zeros(self.__n_actions)

        actions[action] = 1
        return actions

    def reset(self):
        game_image = self.__env.reset()
        return BoardConfiguration(BoardImage(game_image), self.__cursor_locator).array

    def render(self, mode: str = "human", close: bool = "False"):
        return 0

    @property
    def action_space(self):
        return self.__env.action_space


