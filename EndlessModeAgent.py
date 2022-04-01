from keras.optimizer_v1 import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

from TetrisAttackEnv import TetrisAttackEnv
from ValueNetwork import ValueNetwork


class EndlessModeAgent:

    DISCOUNT_FACTOR = .99
    N_WARMUP_STEPS = 50000
    N_STEPS_UNTIL_TARGET_UPDATE = 500
    WINDOW_LENGTH = 4
    MEMORY_LIMIT = 1000000
    OPTIMIZER_LR = .00025
    METRICS = ['mae']

    LOG_INTERVAL = 1000

    def __init__(self, env: TetrisAttackEnv):
        self.__env = env

        n_actions = env.action_space.shape[0]

        self.__value_network = ValueNetwork(n_actions=n_actions, n_input_frames=self.WINDOW_LENGTH)
        self.__memory = SequentialMemory(limit=self.MEMORY_LIMIT, window_length=self.WINDOW_LENGTH)
        self.__policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
                                             nb_steps=1000000)
        self.__optimizer = Adam(lr=self.OPTIMIZER_LR)

        self.__dqn = DQNAgent(model=self.__value_network.model, nb_actions=n_actions, policy=self.__policy,
                              memory=self.__memory, nb_steps_warmup=self.N_WARMUP_STEPS, gamma=self.DISCOUNT_FACTOR,
                              target_model_update=self.N_STEPS_UNTIL_TARGET_UPDATE,
                              enable_double_dqn=True, enable_dueling_network=True,
                              train_interval=4, delta_clip=1.)
        self.__dqn.compile(self.__optimizer, self.METRICS)

    def fit(self):
        self.__dqn.fit(self.__env, nb_steps=5000000, log_interval=self.LOG_INTERVAL)
