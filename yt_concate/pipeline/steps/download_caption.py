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
                    # 找出 VTT 文件
                    subtitle_files = [f for f in os.listdir() if f.endswith('.vtt')]                    
                    
                    # 讀取和轉換字幕
                    for vtt_file in subtitle_files:
                        # 轉換為 SRT 格式
                        srt_content = utils.convert_to_srt(vtt_file)
                        if srt_content:
                            # 保存 SRT 文件
                            srt_file = utils.get_caption_path(video_url)
                            with open(srt_file, 'w', encoding='utf-8') as f:
                                f.write(srt_content)
                            os.remove(vtt_file)
                end = time.time()
             
            except Exception as e:
                print(f'下載失敗: {str(e)}')
            
            print('download time: ', end - start)
                       
 