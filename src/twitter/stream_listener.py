import csv
import unicodedata
import settings

from tweepy.streaming import StreamListener

csvfile = open('../../files/raw_stream_output.csv', 'a', encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow([
    'created_at',
    'tweet_content',
    'keyword',
    'user_location',
    'entities'
])
keywords = []

class StreamListener(StreamListener):  
    """
    Stream listener class to handle call functions to
    Tweepy stream methods
    """

    def on_status(self, status):
        """
        Method to handle streamed tweets content and save
        them into a csv file

        - If the stream contains "retweeted_status" or "quoted_status",
        status.text property does not return the tweet's full content.
        So the below validation was added to get the full content
        despite of being an original tweet, a retweet or a quoted tweet.

        - keywords.clear() is called at the beginning of each stream to
        remove previous tweet's keywords from the current row.
        """
        keywords.clear()

        if status["entities"]["urls"] == []:
            if hasattr(status, "retweeted_status"):
                try:
                    tweet_content = str(status.retweeted_status.extended_tweet["full_text"])
                except AttributeError:
                    tweet_content = str(status.retweeted_status.text)
            elif hasattr(status, "quoted_status"):
                try:
                    tweet_content = str(status.quoted_status.extended_tweet["full_text"])
                except AttributeError:
                    tweet_content = str(status.quoted_status.text)
            else:
                try:
                    tweet_content = str(status.extended_tweet["full_text"])
                except AttributeError:
                    tweet_content = str(status.text)

            for tracked_topic in settings.TRACKED_TOPICS:
                if tracked_topic.lower() in tweet_content.lower():
                    keywords.append(tracked_topic)
                    print(keywords)

            user_location = str(status.user.location)
            created_at = str(status.created_at)
            entities = str(status.entities)
            geo = status.geo
            coordinates = status.coordinates

            csvwriter.writerow(
                [
                    created_at,
                    tweet_content,
                    keywords,
                    user_location,
                    entities
                ]
            )
        
    def on_error(self, status_code):
        if status_code == 420:
            return False