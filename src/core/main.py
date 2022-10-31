from EndlessModeAgent import EndlessModeAgent
from TetrisAttackEnv import TetrisAttackEnv


def main():
    env = TetrisAttackEnv()
    agent = EndlessModeAgent(env)
    agent.learn_n_steps(300000)


if __name__ == '__main__':
    main()
