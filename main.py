# import tweepy
# from api_key import Keys
from client_twitter import TwitterClient
from gsheet_data import GSheet
# from pprint import pprint


def main():
    wks = GSheet()
    tc = TwitterClient()

    last_seen_id = wks.get_last_seen_id()
    api = tc.api

    mentions = api.mentions_timeline(since_id=last_seen_id)

    for mention in reversed(mentions):
        print(str(mention.id) + ': ' + mention.text)
        # wks.update_last_seen_id(mention.id)
        # api.update_status('@' + test_mention.user.screen_name +
        #                   ' Roger that!', test_mention.id)


if __name__ == "__main__":
    main()
