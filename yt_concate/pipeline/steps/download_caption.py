from yt_dlp import YoutubeDL
import os
import time

from pipeline.steps.step import Step, StepException

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for video_url in data:
            if utils.caption_file_exist(video_url):
                print('found exits caption file')
                continue
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitleslangs': inputs.get('languages',['en']),
                'skip_download': True,
                'format': 'best',
            }
        
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.extract_info(video_url, download=True)
                    subtitle_files = [f for f in os.listdir() if f.endswith('.vtt')]                    
                   
                    for vtt_file in subtitle_files:
                        srt_content = utils.convert_to_srt(vtt_file)
                        if srt_content:
                            srt_file = utils.get_caption_path(video_url)
                            with open(srt_file, 'w', encoding='utf-8') as f:
                                f.write(srt_content)
                        os.remove(vtt_file)
             
            except (KeyError, AttributeError): # AttributeError cuz has no caption
                print('Error when download caption url for', video_url)
                continue

            end = time.time()
            
            print('download time: ', end - start, 'sec')
                       
 