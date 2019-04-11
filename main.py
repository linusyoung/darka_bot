from client_twitter import TwitterClient
from gsheet_data import GSheet

# 1116273666042421100 two invalids


def main():
    wks = GSheet()
    tc = TwitterClient()

    last_seen_id = wks.get_last_seen_id()
    api = tc.api

    mentions = api.mentions_timeline(since_id=last_seen_id)

    for mention in reversed(mentions):
        user = mention.user
        if user.screen_name not in wks.skip_users:
            row_id = wks.user_exists(user.screen_name)
            if row_id > 1:
                bot = wks.log_mention(mention)
                invalid_cmds = []
                action_responses = []
                response_text = ""
                for action in bot.actions:
                    if action.get('cmd').lower() in bot.VALID_CMDS:
                        action_responses.append(bot.take_action(action))
                    else:
                        invalid_cmds.append(action.get('cmd'))
                response_text = ".".join(action_responses)
                if len(invalid_cmds) > 0:
                    invalid_cmd_str = ",#".join(invalid_cmds)
                    response_text += \
                        '#{0} not invalid cmd(s).#help to see all valid cmds.' \
                        .format(invalid_cmd_str)

                print("@{0} {1}".format(
                    user.screen_name, response_text))
                print(len(response_text))
                # api.update_status("@{0} {1}".format(
                #     user.screen_name, response_text), mention.id)
            else:
                wks.skip_users.append(user.screen_name)

        wks.update_last_seen_id(mention.id_str)


if __name__ == "__main__":
    main()
