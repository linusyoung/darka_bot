import copy


class Robot():
    VALID_CMDS = [
        'signup'
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

    def take_action(self, action):
        return "Roger that!"
