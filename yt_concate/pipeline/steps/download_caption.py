from yt_dlp import YoutubeDL
import os
import time
import yt_dlp


from pipeline.steps.step import Step, StepException

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            if utils.caption_file_exist(yt):
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
                    ydl.extract_info(yt.url, download=True)
                    subtitle_files = [f for f in os.listdir() if f.endswith('.vtt')]                    
                   
                    for vtt_file in subtitle_files:
                        srt_content = utils.convert_to_srt(vtt_file)
                        if srt_content:
                            srt_file = yt.caption_filepath
                            with open(srt_file, 'w', encoding='utf-8') as f:
                                f.write(srt_content)
                        os.remove(vtt_file)
             
            except (KeyError, AttributeError, yt_dlp.utils.DownloadError) as e:
                if "Sign in to confirm your age" in str(e):
                    print(f'Age restriction error for {yt.url}')
                else:
                    print('Error when download caption url for', yt.url)
                continue
            except Exception as e:  
                print(f"Error type: {type(e)}")  
                print(f"Error message: {str(e)}") 
                continue

            end = time.time()
            
            print('download time: ', end - start, 'sec')
        return data
                       
 