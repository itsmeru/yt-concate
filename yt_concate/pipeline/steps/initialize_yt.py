from .step import Step
from model.yt import YT
class InitializeYt(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]