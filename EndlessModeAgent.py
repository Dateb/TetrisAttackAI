from keras.optimizer_v1 import Adam
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

import AgentPersistence
from TetrisAttackEnv import TetrisAttackEnv
from ValueNetwork import ValueNetwork


class EndlessModeAgent:

    DISCOUNT_FACTOR = .99
    N_WARMUP_STEPS = 100
    N_STEPS_UNTIL_TARGET_UPDATE = 500
    WINDOW_LENGTH = 4
    MEMORY_LIMIT = 1000000
    OPTIMIZER_LR = .00025
    METRICS = ['mae']

    LOG_INTERVAL = 1000

    def __init__(self, env: TetrisAttackEnv, name: str = "DefaultAgent"):
        self.__env = env

        self.__n_actions = env.action_space.shape[0]

        self.__value_network = ValueNetwork(n_actions=self.__n_actions, n_input_frames=self.WINDOW_LENGTH)
        self.__memory = SequentialMemory(limit=self.MEMORY_LIMIT, window_length=self.WINDOW_LENGTH)
        self.__policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
                                             nb_steps=1000000)
        self.__optimizer = Adam(lr=self.OPTIMIZER_LR)
        self.__dqn = self.__build_dqn()
        self.__dqn.compile(self.__optimizer, self.METRICS)

        AgentPersistence.load_weights_if_trained(self.__dqn, name)
        self.__callbacks = [AgentPersistence.get_save_checkpoints_callback(name)]

    def __build_dqn(self):
        return DQNAgent(model=self.__value_network.model, nb_actions=self.__n_actions, policy=self.__policy,
                        memory=self.__memory, nb_steps_warmup=self.N_WARMUP_STEPS, gamma=self.DISCOUNT_FACTOR,
                        target_model_update=self.N_STEPS_UNTIL_TARGET_UPDATE,
                        enable_double_dqn=True, enable_dueling_network=True,
                        train_interval=4, delta_clip=1.)

    def fit_n_steps(self, n_steps: int = 5000000):
        self.__dqn.fit(self.__env, callbacks=self.__callbacks, nb_steps=n_steps, log_interval=self.LOG_INTERVAL)
