from EndlessModeAgent import EndlessModeAgent
from TetrisAttackEnv import TetrisAttackEnv


def main():
    env = TetrisAttackEnv()
    agent = EndlessModeAgent(env)
    agent.fit_n_steps(3000)


if __name__ == '__main__':
    main()
