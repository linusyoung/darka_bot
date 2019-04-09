import tweepy
from api_key import Keys


class TwitterClient():

    def __init__(self):
        auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
        auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
        self.api = tweepy.API(auth)
