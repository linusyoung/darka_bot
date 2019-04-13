import copy


class Robot():
    VALID_CMDS = [
        'signup',
        'signout',
        'follow',
        'mention',
        'help'
    ]

    def __init__(self):
        # action is a list of tag values.
        self.actions = []
        # TODO: may need to move robot name to a better place not hardcoded.
        self.robot_name = '@darka_bot '

    def clean_up_actions(self):
        self.actions.reverse()
        o_actions = copy.deepcopy(self.actions)
        [self.actions[i + 1].update(
            {'arg': o_actions[i + 1].get('arg').replace("#{0} {1}".format(
                o_actions[i].get('cmd'), o_actions[i].get('arg')), '').strip()})
         for i in range(len(self.actions) - 1)]

    def take_action(self, action, gsheet, user):
        cmd = action.get('cmd').lower()
        if cmd == "help":
            res_text = self.print_help()
        elif cmd == "signup":
            res_text = self.signup(gsheet, user)
        else:
            pass
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
