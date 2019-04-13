from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient import errors
from api_key import Keys
from robot import Robot


class GSheet():

    LAST_SEEN_RANGE = 'history!A2'
    TWEETS_LOG_RANGE = 'logs!A1:B1'
    CHECK_USER_RANGE = 'users!B1'
    USER_NAME_RANGE = 'users!A1:A'

    def __init__(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']

        creds = service_account.Credentials.from_service_account_file(
            'client_secret.json', scopes=scope)
        self.sheet = build('sheets', 'v4', credentials=creds).spreadsheets()
        self.skip_users = []

    def get_last_seen_id(self):
        request = self.sheet.values().get(spreadsheetId=Keys.SPREADSHEET_ID,
                                          range=self.LAST_SEEN_RANGE)
        try:
            response = request.execute()
            return int(response.get('values')[0][0])
        except errors.Error as err:
            print(err)

    def log_mention(self, mention):
        robot = Robot()
        hashtags = mention.entities.get('hashtags')
        for hashtag in hashtags:
            action = {
                'cmd': hashtag.get('text'),
                'arg': mention.text[hashtag.get('indices')[1] + 1:]
            }
            robot.actions.append(action)
        robot.clean_up_actions()
        value_input_option = 'RAW'
        insert_data_option = 'OVERWRITE'
        value_range_body = {
            "range": self.TWEETS_LOG_RANGE,
            "majorDimension": "ROWS",
            "values": [[mention.user.screen_name, mention.text.replace(robot.robot_name, '')]]
        }
        request = self.sheet.values().append(
            spreadsheetId=Keys.SPREADSHEET_ID, range=self.TWEETS_LOG_RANGE,
            valueInputOption=value_input_option, insertDataOption=insert_data_option,
            body=value_range_body)
        try:
            request.execute()
            return robot
        except errors.Error as err:
            print(err)

    def update_last_seen_id(self, id):
        value_input_option = 'RAW'
        value_range_body = {
            "range": self.LAST_SEEN_RANGE,
            "values": [[id]]
        }
        request = self.sheet.values().update(
            spreadsheetId=Keys.SPREADSHEET_ID, range=self.LAST_SEEN_RANGE,
            valueInputOption=value_input_option, body=value_range_body)
        try:
            request.execute()
        except errors.Error as err:
            print(err)

    def user_exists(self, screen_name):
        value_input_option = 'USER_ENTERED'
        value_range_body = {
            "range": self.CHECK_USER_RANGE,
            "values": [["=MATCH(\"{screen_name}\",{name_range},0)"
                        .format(screen_name=screen_name, name_range=self.USER_NAME_RANGE)]]
        }
        request = self.sheet.values().update(
            spreadsheetId=Keys.SPREADSHEET_ID, range=self.CHECK_USER_RANGE,
            valueInputOption=value_input_option, includeValuesInResponse=True,
            body=value_range_body)
        try:
            response = request.execute()
            matches = response.get('updatedData').get('values')[0][0]
            return int(matches) if matches != '#N/A' else 1
        except errors.Error as err:
            print(err)

    def signup_user(self, screen_name):
        value_input_option = 'RAW'
        insert_data_option = 'OVERWRITE'
        value_range_body = {
            "range": self.USER_NAME_RANGE,
            "majorDimension": "COLUMNS",
            "values": [[screen_name]]
        }
        request = self.sheet.values().append(
            spreadsheetId=Keys.SPREADSHEET_ID, range=self.USER_NAME_RANGE,
            valueInputOption=value_input_option, insertDataOption=insert_data_option,
            body=value_range_body)
        try:
            request.execute()
        except errors.Error as err:
            print(err)
