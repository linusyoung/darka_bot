# import tweepy
# from api_key import Keys

from google.oauth2 import service_account
from googleapiclient.discovery import build


# get data from twitter
# auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
# auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)

# api = tweepy.API(auth)

# mentions = api.mentions_timeline()

# # for mention in mentions:


# test_mention = mentions[0]

# api.update_status('@' + test_mention.user.screen_name +
#                   ' Roger that!', test_mention.id)

# print(str(test_mention.id) + ': ' + test_mention.text)

spreadsheet_id = '1uwjJCXNgXBzf_IaBj1hwl_y5pJ54XW5FKtKecrgHM58'
data_range = 'logs!A1:B2'

# interactive with gspread
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = service_account.Credentials.from_service_account_file(
    'client_secret.json', scopes=scope)

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id, range=data_range).execute()

values = result.get('values', [])

if not values:
    print('No data found.')
else:
    for row in values:
        print(row)
