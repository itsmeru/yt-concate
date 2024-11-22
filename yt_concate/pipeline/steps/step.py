from abc import ABC, abstractmethod

class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass

class StepException(Exception):
    pass
