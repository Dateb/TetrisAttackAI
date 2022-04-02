from abc import ABC, abstractmethod


class Block(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def array(self):
        pass




