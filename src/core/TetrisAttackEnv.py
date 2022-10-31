import numpy as np
import retro
from gym import Env
from gym.vector.utils import spaces

from src.Board.BoardConfiguration import BoardConfiguration
from src.Board.BoardImage import BoardImage
from src.Board.CursorLocation.CursorLocator import CursorLocator
from src.Monitoring.BoardStateMonitorImage import BoardStateMonitorImage
from src.Monitoring.StateImage import StateImage


class TetrisAttackEnv(Env):

    def __init__(self):
        self.cursor_locator = CursorLocator()
        self.total_cursors = 0
        self.failed_cursors = 0
        game = 'TetrisAttack-Snes'
        state = retro.State.DEFAULT

        self.env = retro.make(game, state, record='./replays', scenario=None)
        self.observation_space = spaces.Box(low=0, high=1, shape=(BoardConfiguration.TOTAL_SIZE,), dtype=np.uint8)
        self.action_space = self.env.action_space
        self.n_actions = self.env.action_space.shape[0]

    def step(self, action):
        game_image, rew, done, info = self.env.step(action)

        board_image = BoardImage(game_image)
        board_configuration = BoardConfiguration(board_image, self.cursor_locator)
        state_image = StateImage(board_image, board_configuration)
        BoardStateMonitorImage(board_image, state_image).image.save("state.jpeg")

        return board_configuration.array, rew, done, info

    def reset(self):
        game_image = self.env.reset()
        return BoardConfiguration(BoardImage(game_image), self.cursor_locator).array

    def render(self, mode: str = "human", close: bool = "False"):
        return 0
