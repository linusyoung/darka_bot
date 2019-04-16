import copy


class Robot():
    VALID_CMDS = [
        'signup',
        'signout',
        'follow',
        'mention',
        'help'
    ]

    def __init__(self, api):
        # action is a list of tag values.
        self.actions = []
        # TODO: may need to move robot name to a better place not hardcoded.
        self.robot_name = '@darka_bot '
        self.api = api

    def clean_up_actions(self):
        self.actions.reverse()
        o_actions = copy.deepcopy(self.actions)
        [self.actions[i + 1].update(
            {'arg': o_actions[i + 1].get('arg').replace("#{0} {1}".format(
                o_actions[i].get('cmd'), o_actions[i].get('arg')), '').strip()})
         for i in range(len(self.actions) - 1)]

    def take_action(self, action, gsheet, api, user):
        cmd = action.get('cmd').lower()
        if cmd == "help":
            res_text = self.print_help()
        elif cmd == "signup":
            res_text = self.signup(gsheet, user)
        elif cmd == "follow":
            res_text = self.follow(api, action)
        elif cmd == "signout":
            res_text = self.signout(gsheet, user)
        else:
            res_text = "unknown action"
            # gsheet.signup_user(user.screen_name)
        return res_text

    def print_help(self):
        return ",".join(self.VALID_CMDS)

    def signup(self, gsheet, user):
        row_id = gsheet.user_exists(user.screen_name)
        if row_id > 1:
            return "already signed up."
        else:
            gsheet.signup_user(user.screen_name)
            return "you're all set."

    def signout(self, gsheet, user):
        row_id = gsheet.user_exists(user.screen_name)
        if row_id > 1:
            gsheet.signout_user(row_id)
            return "sad to say good bye."
        else:
            return "please sign up first."

    def follow(self, api, action):
        to_follow = action.get('arg')
        api.create_friendship(to_follow)
        return "follow {}".format(to_follow)
