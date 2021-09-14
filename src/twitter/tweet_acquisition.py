from settings import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from tweepy import OAuthHandler
from tweepy import Stream
from stream_listener import StreamListener

class TweetAcquisition():

    def stream_tweets(self, keyword):
        stream_listener = StreamListener()
        auth = OAuthHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, stream_listener)
        stream.filter(track=keyword, languages=["pt"])
