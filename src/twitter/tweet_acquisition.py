import settings

from tweepy import OAuthHandler
from tweepy import Stream
from stream_listener import StreamListener

if __name__ == '__main__':
    stream_listener = StreamListener()
    auth = OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, stream_listener)
    stream.filter(track=settings.TRACKED_TOPICS, languages=["pt"], filter_level="medium")

