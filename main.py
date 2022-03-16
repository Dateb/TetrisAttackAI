import retro
from PIL import Image
from keras import Sequential
from keras.layers import Convolution2D, Activation, Flatten, Dense, Permute
from keras.optimizer_v1 import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

#if self.processor is not None:
#    action = self.processor.process_action(action)

WINDOW_LENGTH = 4

def build_model(env):
    n_actions = env.action_space.shape[0]
    model = Sequential()

    model.add(Permute((4, 2, 3, 1), input_shape=(WINDOW_LENGTH, 224, 256, 3)))
    model.add(Convolution2D(2, (3, 3), strides=(1, 1)))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(n_actions))
    model.add(Activation('linear'))
    print(model.summary())

    memory = SequentialMemory(limit=1000000, window_length=WINDOW_LENGTH)

    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
                                  nb_steps=1000000)

    dqn = DQNAgent(model=model, nb_actions=n_actions, policy=policy, memory=memory,
                   nb_steps_warmup=50000, gamma=.99, target_model_update=10000,
                   train_interval=4, delta_clip=1.)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])

    dqn.fit(env, nb_steps=1750000, visualize=True, log_interval=10000)


def main():
    env = retro.make(game='TetrisAttack-Snes')
    obs = env.reset()

    obs, rew, done, info = env.step(env.action_space.sample())
    print(env.action_space.sample())

    img_arr = env.render(mode='rgb_array')
    print(img_arr.shape)
    build_model(env)
    if done:
        obs = env.reset()
    env.close()

    img_arr = img_arr[20:215, 86:186]
    im = Image.fromarray(img_arr)
    im = im.resize((20, 40))
    im.save("example.jpeg")


if __name__ == '__main__':
    print(retro.data.list_games())
    main()
