from twitter.settings import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from twitter.stream_listener import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TweetAcquisition():

    keyword = []

    def __init__(self, keyword):
        self.keyword = [keyword]

    def stream_tweets(self):
        stream_listener = StreamListener()
        auth = OAuthHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, stream_listener)
        stream.filter(track=self.keyword, languages=["pt"])