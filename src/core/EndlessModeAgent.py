from stable_baselines3 import A2C
from src.core.TetrisAttackEnv import TetrisAttackEnv


class EndlessModeAgent:

    def __init__(self, env: TetrisAttackEnv, name: str = "DefaultAgent"):
        self.env = env
        self.model = A2C("MlpPolicy", env, verbose=1)

    def learn_n_steps(self, total_timesteps: int = 5000000):
        self.model.learn(total_timesteps=total_timesteps)
