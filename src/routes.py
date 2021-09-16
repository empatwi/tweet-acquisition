import werkzeug
from werkzeug.utils import cached_property
werkzeug.cached_property = cached_property
from flask_restplus import Resource, fields, Namespace
from flask import request
from api import api

from twitter.tweet_acquisition import TweetAcquisition

search_ns = Namespace('search', description='Search related operations')
#tweet_acquisition = TweetAcquisition()

# Model required by flask_restplus for expected data
search_fields = api.model('Search', {
    'keyword': fields.String(required=True)
})

@search_ns.route('/')
@search_ns.expect(search_fields, validate=True)
class Search(Resource):
    @search_ns.doc(responses={
        200: 'OK',
        400: 'Bad request',
        500: 'Internal server error'
    })
    @search_ns.doc(description='Searches for keyword on Twitter through Twitter API')
    def post(self):
        payload = request.get_json()
        keyword = payload['keyword']
        #tweet_acquisition.stream_tweets(keyword)
        TweetAcquisition(keyword).stream_tweets()
        return 200
