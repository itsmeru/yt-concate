from pipeline.pipeline import Pipeline
from pipeline.steps.get_vedio_list import GetVedioList
from pipeline.steps.download_caption import DownloadCaptions
from utilities import Utils
from pipeline.steps.preflight import Preflight
from pipeline.steps.postflight import Postflight


CHANNEL_ID = "UCb-ikMqe9iS8GjG7WgGwCrQ"

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
        Preflight(),
        GetVedioList(),
        DownloadCaptions(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)
    

if __name__ == '__main__':
    main()

