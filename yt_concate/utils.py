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
    
    def caption_file_exist(self, yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0
    
    def video_file_exist(self, yt):
        filepath = yt.vedio_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0
    
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
    
