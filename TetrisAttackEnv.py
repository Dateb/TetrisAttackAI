import numpy as np
import retro

from TetrisAttackProcessor import TetrisAttackProcessor


class TetrisAttackEnv:

    def __init__(self, processor: TetrisAttackProcessor):
        game = 'TetrisAttack-Snes'
        state = retro.State.DEFAULT
        self.__env = retro.make(game, state, record='./replays', scenario=None)
        self.__processor = processor
        self.__processor.set_n_actions(self.__env.action_space.shape[0])

    def step(self, action):
        obs, rew, done, info = self.__env.step(action)
        self.__processor.set_current_speed(info["speed"])
        if done:
            rew = -100
        return obs, rew, done, info

    def reset(self):
        init_obs = self.__env.reset()
        self.__processor.set_current_speed(1)
        return init_obs

    def render(self, mode: str = "human", close: bool = "False"):
        return 0

    @property
    def action_space(self):
        return self.__env.action_space

    @property
    def processor(self):
        return self.__processor
