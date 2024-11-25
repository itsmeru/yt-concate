from moviepy import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

from .step import Step

class EditVedio(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            video_path = found.yt.video_filepath
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(video_path).subclipped(start, end)        
            clips.append(video)
            if len(clips) > inputs['limit']:
                break
        output_filepath = utils.get_output_filepath(inputs['channel_id'],inputs['search_word'])   
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start, end =  caption_time.split(' --> ')
        return self.parse_time_string(start), self.parse_time_string(end)
    
    def parse_time_string(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000