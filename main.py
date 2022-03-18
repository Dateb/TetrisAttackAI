from keras import Sequential
from keras.layers import Activation, Flatten, Dense, Permute
from keras.optimizer_v1 import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

from TetrisAttackEnv import TetrisAttackEnv
from TetrisAttackProcessor import TetrisAttackProcessor

WINDOW_LENGTH = 4


def build_model(env):
    n_actions = env.action_space.shape[0]
    model = Sequential()

    model.add(Permute((2, 3, 1),  input_shape=(WINDOW_LENGTH, 74, 1)))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dense(n_actions))
    model.add(Activation('linear'))
    print(model.summary())

    memory = SequentialMemory(limit=1000000, window_length=WINDOW_LENGTH)

    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.001, value_test=.05,
                                  nb_steps=800000)

    dqn = DQNAgent(model=model, nb_actions=n_actions, policy=policy, memory=memory, processor=env.processor,
                   nb_steps_warmup=10000, gamma=.99, target_model_update=10000,
                   train_interval=4, delta_clip=1.)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])

    dqn.fit(env, nb_steps=1750000, visualize=True, log_interval=10000)


def build_environment():
    processor = TetrisAttackProcessor()
    return TetrisAttackEnv(processor)


def main():
    env = build_environment()
    build_model(env)


if __name__ == '__main__':
    main()
