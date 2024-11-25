import yt_dlp

from .step import Step
from settings import VEDIOS_DIR 

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('vedios to download= ', len(yt_set))
        for yt in yt_set:
            url = yt.url
            output_path = f'{VEDIOS_DIR}/{yt.id}.%(ext)s'
            ydl_opts = {
                'format': 'best',  
                'outtmpl': output_path,  
                'quiet': False, 
                'no_warnings': False,
                'nooverwrites': True,  
                }
            if utils.video_file_exist(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print(f"Successfully downloaded: {url}")
            except yt_dlp.utils.DownloadError as e:
                print(f"Error downloading {url}: {str(e)}")
        return data