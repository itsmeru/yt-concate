from pipeline.steps.preflight import Preflight
from pipeline.steps.get_vedio_list import GetVedioList
from pipeline.steps.initialize_yt import InitializeYt
from pipeline.steps.download_caption import DownloadCaptions
from pipeline.steps.read_caption import ReadCaption
from pipeline.steps.search import Search
from pipeline.steps.postflight import Postflight
from pipeline.pipeline import Pipeline
from utils import Utils

CHANNEL_ID = "UCsnZXdLOGBnezK--CiG7FZQ"

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'always exploring'
    }

    steps = [
        Preflight(),
        GetVedioList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)
    

if __name__ == '__main__':
    main()

