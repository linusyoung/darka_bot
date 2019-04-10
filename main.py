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
        wks.update_last_seen_id(mention.id_str)


if __name__ == "__main__":
    main()
