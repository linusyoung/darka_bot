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
        wks.log_mention(mention)
        print(mention.user.screen_name + ': ' + mention.text)
        # wks.update_last_seen_id(mention.id_str)
        # api.update_status('@' + test_mention.user.screen_name +
        #                   ' Roger that!', test_mention.id)
        break


if __name__ == "__main__":
    main()
