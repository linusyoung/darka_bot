from google.oauth2 import service_account
from googleapiclient.discovery import build
from api_key import Keys


class GSheet():

    LAST_SEEN_RANGE = 'history!A2'
    TWEETS_LOG_RANGE = 'logs!A1:B1'

    def __init__(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']

        creds = service_account.Credentials.from_service_account_file(
            'client_secret.json', scopes=scope)
        self.sheet = build('sheets', 'v4', credentials=creds).spreadsheets()

    def get_last_seen_id(self):
        request = self.sheet.values().get(spreadsheetId=Keys.SPREADSHEET_ID,
                                          range=self.LAST_SEEN_RANGE)
        response = request.execute()
        return int(response.get('values')[0][0])

    def update_last_seen_id(self, id):
        value_input_option = 'RAW'
        value_range_body = {
            "range": self.LAST_SEEN_RANGE,
            "values": [[str(id)]]
        }
        request = self.sheet.values().update(
            spreadsheetId=Keys.SPREADSHEET_ID, range=self.LAST_SEEN_RANGE, valueInputOption=value_input_option, body=value_range_body)
        request.execute()
