from mycroft import MycroftSkill, intent_file_handler


class Basicmath(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('basicmath.intent')
    def handle_basicmath(self, message):
        self.speak_dialog('basicmath')


def create_skill():
    return Basicmath()

