from pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('In prflight')
        utils.create_dir()