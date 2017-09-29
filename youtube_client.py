#!/usr/bin/python
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import settings

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = settings.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Client(object):
    def youtube_search(self, options):
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        videos = []

        search_response = youtube.search().list(
            q=options.q,
            part='id,snippet',
            type='video',
            maxResults=options.max_results,
            order='date'
        ).execute()

        for search_result in search_response.get('items', []):
            videos.append(search_result)

        return videos


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="耳かき")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  client = Client()

  try:
    videos = client.youtube_search(args)
    import pdb; pdb.set_trace()
    # print(client.youtube_search(args))
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
