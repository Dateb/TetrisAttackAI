from keras import Sequential
from keras.layers import Activation, Flatten, Dense, Permute, Convolution2D
from keras.optimizer_v1 import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from tensorflow import keras

from Board.BoardConfiguration import BoardConfiguration
from TetrisAttackEnv import TetrisAttackEnv

WINDOW_LENGTH = 32


def get_model(env: TetrisAttackEnv, model_name: str = None):
    if model_name is None:
        return build_model(env)

    model = keras.models.load_model(f"models/{model_name}")

    return model


def build_model(env: TetrisAttackEnv) -> Sequential:
    model = Sequential()
    n_actions = env.action_space.shape[0]

    model.add(Permute((2, 1), input_shape=(WINDOW_LENGTH, BoardConfiguration.TOTAL_SIZE)))
    model.add(Flatten())
    model.add(Dense(1024, name="dense_a"))
    model.add(Activation('relu'))
    model.add(Dense(512, name="dense_b"))
    model.add(Activation('relu'))
    model.add(Dense(256, name="dense_c"))
    model.add(Activation('relu'))
    model.add(Dense(128, name="dense_d"))
    model.add(Activation('relu'))
    model.add(Dense(n_actions, name="dense_e"))
    model.add(Activation('linear'))

    return model


def fit_agent(env: TetrisAttackEnv, model: Sequential, save_interval=10000, model_name: str = "NoNameModel"):
    n_actions = env.action_space.shape[0]
    memory = SequentialMemory(limit=1000000, window_length=WINDOW_LENGTH)

    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
                                  nb_steps=1000000)

    dqn = DQNAgent(model=model, nb_actions=n_actions, policy=policy, memory=memory,
                   nb_steps_warmup=50000, gamma=.99, target_model_update=500,
                   enable_double_dqn=True, enable_dueling_network=True,
                   train_interval=4, delta_clip=1.)
    dqn.compile(Adam(lr=.00025), metrics=['mae'])
    print(model.summary())

    while True:
        dqn.fit(env, nb_steps=5000000, log_interval=save_interval / 10)
        model.save(f"models/{model_name}")


def build_environment():
    return TetrisAttackEnv()


def main():
    env = build_environment()
    model_name = "TetrisAttack_Agent_v0.01"
    model = get_model(env)
    fit_agent(env, model, save_interval=10000, model_name=model_name)


if __name__ == '__main__':
    main()
