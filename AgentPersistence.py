import os

from rl.callbacks import ModelIntervalCheckpoint


def is_already_trained(name: str):
    return os.path.exists(f"models/{name}.h5f.index")


def load_weights(dqn, name):
    dqn.load_weights(f"models/{name}.h5f")


def load_weights_if_trained(dqn, name):
    if is_already_trained(name):
        load_weights(dqn, name)


def get_save_checkpoints_callback(name):
    return ModelIntervalCheckpoint(f"models/{name}.h5f", interval=1000)
