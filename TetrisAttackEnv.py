import retro


class TetrisAttackEnv:

    def __init__(self):
        game = 'TetrisAttack-Snes'
        state = retro.State.DEFAULT
        self.__env = retro.make(game, state, scenario=None)

    def step(self, action):
        obs, rew, done, info = self.__env.step(action)
        return obs, rew, done, info

    def reset(self):
        return self.__env.reset()

    def render(self, mode: str = "human", close: bool = "False"):
        return 0

    @property
    def action_space(self):
        return self.__env.action_space
