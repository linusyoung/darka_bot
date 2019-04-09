import tweepy
from api_key import Keys

from gsheet_data import GSheet
# from pprint import pprint

wks = GSheet()
last_seen_id = wks.get_last_seen_id()

print(last_seen_id)

# get data from twitter
auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)

api = tweepy.API(auth)

mentions = api.mentions_timeline(since_id=last_seen_id)

for mention in reversed(mentions):
    print(str(mention.id) + ': ' + mention.text)
    wks.update_last_seen_id(mention.id)
    # api.update_status('@' + test_mention.user.screen_name +
    #                   ' Roger that!', test_mention.id)
