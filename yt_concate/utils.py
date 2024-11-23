import os
import webvtt

from settings import CAPTIONS_DIR, DOWNLOADS_DIR, VEDIOS_DIR

class Utils:
    def __init__(self):
        pass
    
    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VEDIOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + ".txt")
    
    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0
    
    @staticmethod
    def convert_to_srt(vtt_file):
        """Download VTT and turn into SRT content"""
        try:
            vtt = webvtt.read(vtt_file)
            srt_lines = []
            srt_index = 1
            last_text = ""
            
            for caption in vtt.captions:
                start = caption.start.replace('.', ',')
                end = caption.end.replace('.', ',')
                
                texts = caption.text.split('\n')
                current_text = texts[-1] if texts else ""
                
                if current_text != last_text and current_text.strip():
                    srt_lines.append(f"{srt_index}")
                    srt_lines.append(f"{start} --> {end}")
                    srt_lines.append(current_text)
                    srt_lines.append("")
                    srt_index += 1
                    last_text = current_text
            
            return "\n".join(srt_lines)
        except Exception as e:
            print(f"when turn file: {vtt_file} error: {str(e)}")
            return None
    
    @staticmethod
    def get_vedio_id_from_url(url):
        return url.split("watch?v=")[-1]
    
    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_vedio_id_from_url(url) + '.txt')
    
    def caption_file_exist(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0
    
