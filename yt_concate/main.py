from pipeline.steps.preflight import Preflight
from pipeline.steps.get_vedio_list import GetVedioList
from pipeline.steps.initialize_yt import InitializeYt
from pipeline.steps.download_caption import DownloadCaptions
from pipeline.steps.read_caption import ReadCaption
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.edit_video import EditVedio
from pipeline.steps.postflight import Postflight
from pipeline.pipeline import Pipeline
from utils import Utils

CHANNEL_ID = "UCdTDC0hc3EPLOwwiPp6i6xw"

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'amazing',
        'limit' : 20
    }

    steps = [
        Preflight(),
        GetVedioList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVedio(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)
    

if __name__ == '__main__':
    main()

