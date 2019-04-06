import tweepy

from api_key import Keys


auth = tweepy.OAuthHandler(Keys().CONSUMER_KEY, Keys().CONSUMER_SECRET)
auth.set_access_token(Keys().ACCESS_KEY, Keys().ACCESS_SECRET)

api = tweepy.API(auth)

mentions = api.mentions_timeline()

# for mention in mentions:

test_mention = mentions[0]

api.update_status('@' + test_mention.user.screen_name +
                  ' Roger that!', test_mention.id)

print(str(test_mention.id) + ': ' + test_mention.text)
