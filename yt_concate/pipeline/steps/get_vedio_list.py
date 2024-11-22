import urllib.request
import json
import ssl

from pipeline.steps.step import Step, StepException
from setting import API_KEY

ssl._create_default_https_context = ssl._create_unverified_context

class GetVedioList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
       
        return video_links
