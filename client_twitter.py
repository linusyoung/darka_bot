import tweepy
from configs import Configures


class TwitterClient():

    def __init__(self):
        auth = tweepy.OAuthHandler(
            Configures.CONSUMER_KEY, Configures.CONSUMER_SECRET)
        auth.set_access_token(Configures.ACCESS_KEY, Configures.ACCESS_SECRET)
        self.api = tweepy.API(auth)
