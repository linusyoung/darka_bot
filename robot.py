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
            res_text = self.print_help(action)
        elif cmd == "signup":
            res_text = self.signup(gsheet, user)
        elif cmd == "follow":
            res_text = self.follow(api, action)
        elif cmd == "signout":
            res_text = self.signout(gsheet, user)
        elif cmd == "mention":
            res_text = self.mention(api, action)
        else:
            res_text = "unknown action"
        return res_text

    def print_help(self, action):
        arg = action.get('arg')
        if arg != '':
            if arg in self.VALID_CMDS:
                if arg == "signup":
                    res_text = "#signup"
                elif arg == "signout":
                    res_text = "#signout"
                elif arg == "follow":
                    res_text = "#follow screen_name"
                elif arg == "mention":
                    res_text = "#mention screen_name text"
                else:
                    res_text = "#help [valid commands]"
            else:
                res_text = "{} is not a valid cmd.".format(arg)
        else:
            res_text = "valid cmds:" + ",".join(self.VALID_CMDS)
        return res_text

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
        # TODO: check if user exists
        to_follow = action.get('arg')
        api.create_friendship(to_follow)
        return "follow {}".format(to_follow)

    def mention(self, api, action):
        # TODO: check if user exists
        mention_arg = action.get('arg')
        first_space_index = mention_arg.find(' ')
        mention_user = mention_arg[:first_space_index]
        mention_text = mention_arg[first_space_index + 1:]
        status_text = "@{0} {1}".format(mention_user, mention_text)
        api.update_status(status_text)
        return "mention {0}".format(mention_user)
