import tensorflow as tf

class TetrisAttackMonitor:

    LOG_FOLDER: str = "log"

    def __init__(self):
        writer = tf.summary.create_file_writer(logdir=self.LOG_FOLDER)
        self.__total_steps = 0


    def on_step_end(self, step, logs={}):
        self.__total_steps += 1

        if step % 100 == 0:
            tf.summary.scalar(name="reward", data=reward, step=step)
            dqn_variable = model.trainable_variables
            tf.summary.histogram(name="dqn_variables", data=tf.convert_to_tensor(dqn_variable[0]), step=step)
            writer.flush()
