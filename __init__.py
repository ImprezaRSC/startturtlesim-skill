from mycroft import MycroftSkill, intent_file_handler


class Startturtlesim(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('startturtlesim.intent')
    def handle_startturtlesim(self, message):
        self.speak_dialog('startturtlesim')


def create_skill():
    return Startturtlesim()

