#!/usr/bin/python
from apiclient.discovery import build
from apiclient.errors import HttpError
import settings

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = settings.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Client(object):
    def search(self, query, order_by):
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        videos = []

        try:
            search_response = youtube.search().list(
                q=query,
                part='id,snippet',
                type='video',
                maxResults=25,
                order=order_by
            ).execute()

            [videos.append(search_result) for search_result in search_response.get('items', [])]
        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
            raise e

        return videos
